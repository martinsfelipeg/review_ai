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

PROMPT = "Por favor, analise as avaliações do meu produto. \
Forneça recomendações específicas em forma de bullet points para melhorar as vendas desse produto em específico.\
Faça também bullet points para pontos positivos e negativos das avaliações desse produto em específico:"
