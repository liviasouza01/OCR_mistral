# Extração de Texto com Mistral OCR

Este documento demonstra como utilizar a API Mistral OCR para extrair texto de faturas em PDF e notas manuscritas.

## Requisitos

- Python 3.6+
- Biblioteca `mistralai`
- Chave de API Mistral

## Configuração

1. Instale as dependências necessárias:
   ```
   pip install mistralai
   ```

2. Configure sua chave de API Mistral:
   - Crie um arquivo `.env` baseado no `.env-example`
   - Adicione sua chave de API Mistral ao arquivo

## Scripts Disponíveis

### 1. Extração de Texto de Faturas (nf_ingestion.py)

Este script demonstra como extrair informações específicas de uma fatura em PDF:
- Extrai o texto completo usando OCR
- Identifica o número da fatura e valor total usando expressões regulares
- Inclui código comentado para mascarar informações sensíveis (CPF, nome, endereço)

Uso: 
```
python nf_ingestion.py
```

### 2. Extração de Texto de Notas Manuscritas (handwritten_ingestion.py)

Este script demonstra como extrair texto de uma nota manuscrita:
- Extrai o texto completo usando OCR
- Inclui código comentado para mascarar informações sensíveis (CPF, nome, endereço)

Uso: 
```
python handwritten_ingestion.py
```  