import os
from datetime import datetime

def verifica_hora():
    hora = datetime.now().strftime("%H:%M")
    frase = f"Agora são {hora}"
    return frase