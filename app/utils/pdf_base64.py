import base64
from io import BytesIO
from typing import Optional
import img2pdf
import requests
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfReader, PdfWriter

def encode_image_to_pdf_base64(image_url: str, filename: str, save_pdf_file: bool=False) -> Optional[str]:
    # Make a GET request to fetch the image
    response = requests.get(image_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the image content to PDF
        try:
            pdf_bytes = img2pdf.convert(BytesIO(response.content))
        except img2pdf.AlphaChannelError as ae:
            print(f"[ERROR] {ae}")
            return None
        
        # Read the PDF using PyPDF2
        pdf_buffer = BytesIO(pdf_bytes)
        pdf = PdfReader(pdf_buffer)
        
        # Create a PDF writer object
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf.pages[0])
        
        
        # Create a BytesIO object to capture the output PDF data
        output_pdf_buffer = BytesIO()
        pdf_writer.write(output_pdf_buffer)
        
        # Get the PDF data from the BytesIO object
        pdf_data = output_pdf_buffer.getvalue()
        
        # Encode the PDF data to base64
        base64_encoded_pdf = base64.b64encode(pdf_data).decode('utf-8')

        # write the PDF to a file
        if save_pdf_file:
            with open(filename, 'wb') as f:
                f.write(pdf_data)
        
        return base64_encoded_pdf
    else:
        raise Exception("Failed to fetch the image.")
        
        