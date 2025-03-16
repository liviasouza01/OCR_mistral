import os
from mistralai import Mistral
import re

api_key = os.environ["MISTRAL_API_KEY"]  # insira sua API key do Mistral

client = Mistral(api_key=api_key)

# URL de um documento PDF de fatura (exemplo público)
document_url = "https://www.wmaccess.com/downloads/sample-invoice.pdf"

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={"type": "document_url", "document_url": document_url}
)

# Extraindo o texto em Markdown da primeira página
page_text = ocr_response.pages[0].markdown
print(page_text[:500])  # imprime início do texto extraído para ver os campos
'''
ocr_text = ocr_response.pages[0].markdown
# máscara simples de padrão CPF (substitui dígitos por X)
masked_text = re.sub(r'\d{3}\.\d{3}\.\d{3}-\d{2}', '[CPF_MASCARADO]', ocr_text)
masked_text = re.sub(r'Nome:\s+[A-Za-zçãõâêéÁÉÍÓÚáéíóú ]+', 'Nome: [NOME]', masked_text)
masked_text = re.sub(r'Endereço:\s+.*', 'Endereço: [ENDERECO]', masked_text)

print(masked_text)
'''
# Supondo que page_text contenha algo como "Invoice No: 12345" e "Total: $ 987,65"
invoice_no_match = re.search(r'Invoice No[:\s]+(\S+)', page_text)
total_match = re.search(r'Total[:\s]+([\d\.,]+)', page_text)

invoice_no = invoice_no_match.group(1) if invoice_no_match else None
total_value = total_match.group(1) if total_match else None

print("Número da Fatura:", invoice_no)
print("Valor Total:", total_value)