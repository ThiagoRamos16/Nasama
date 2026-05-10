from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import sys
import os
import funcoes_so , funcoes_email



def cria_audio(audio, mensagem):
    tts = gTTS(mensagem, lang = 'pt-br')
    tts.save(audio)
    playsound(audio)
    os.remove(audio)
    

def monitora_audio(executar_comando=True):
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source, duration=1)
        while True:
            print("Diga alguma coisa")
            audio = recon.listen(source, phrase_time_limit=10)
            try:
                mensagem = recon.recognize_google(audio, language= 'pt-br')
                mensagem = mensagem.lower()
                print("Você disse: ", mensagem)
            
                if executar_comando:
                    executa_comandos(mensagem)
                break
            except sr.WaitTimeoutError:
                cria_audio("erro.mp3", "Tempo esgotado. Tente novamente.")
            except sr.UnknownValueError:
                cria_audio("erro.mp3", "Não consegui entender. Tente novamente.")
            except sr.RequestError:
                cria_audio("erro.mp3", "Erro ao conectar ao serviço de reconhecimento.")
        return mensagem 
    

def executa_comandos(acao):
    if 'fechar assistente' in acao:
        sys.exit()
    elif 'horas' in acao:
        cria_audio('mensagem.mp3', funcoes_so.verifica_hora())
    elif 'enviar email' in acao or 'enviar e-mail' in acao:
        status_email = funcoes_email.enviar_email(cria_audio, monitora_audio)
        cria_audio('mensagem.mp3', status_email)
        

def main():
    cria_audio("wellcome.mp3", "Olá, sou a Nasama. Em que posso lhe ajudar?")
    while True:
        monitora_audio()    
main()