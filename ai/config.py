import os

from dotenv import load_dotenv

load_dotenv()

MODEL = "gemini-1.0-pro"
GEMINI_KEY = os.environ.get("GOOGLE_API_KEY")

GEN_CONFIG = {"temperature": 0.5}

SAFETY_SETTINGS = {
    "HATE": "BLOCK_NONE",
    "HARASSMENT": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

PROD_ID = "6f3b5b605d91b7439c5e3f5a8dffeea7"

PROMPT = "Por favor, analise as avaliações do meu produto. \
Seu resposta deve seguir esse modelo: \
**Pontos Positivos:** \
* Entrega rápida \
\
**Pontos Negativos:** \
* Produtos falsos ou com defeito \
\
**Recomendações\
* Verificar possiveis defeitos \
\
"
