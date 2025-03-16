from mistralai import Mistral
import base64
import os

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])

image_path = "nota_manuscrita.jpg"  # caminho da imagem local

# Leitura do arquivo de imagem e conversão para base64
with open(image_path, "rb") as img_file:
    base64_data = base64.b64encode(img_file.read()).decode('utf-8')

# Preparação do URI de dados base64
data_uri = f"data:image/jpeg;base64,{base64_data}"

# Processamento OCR da imagem manuscrita
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={"type": "image_url", "image_url": data_uri}
)

text_md = ocr_response.pages[0].markdown  # texto extraído em Markdown

print(text_md[:300])