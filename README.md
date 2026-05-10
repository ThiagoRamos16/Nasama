# 🎙️ Nasama — Assistente Virtual com IA

Assistente virtual desenvolvida em Python com reconhecimento 
e síntese de voz, capaz de executar tarefas por comando de voz.

## 🚀 Funcionalidades
- ⏰ Informa hora atual por voz
- 📧 Envia e-mails por comando de voz
- 📰 Consulta Google News
- 🔊 Responde em português (gTTS)

## 🛠️ Tecnologias utilizadas
| Tecnologia | Finalidade |
|---|---|
| gTTS | Síntese de voz (Text-to-Speech) |
| SpeechRecognition | Reconhecimento de voz |
| smtplib / ssl | Envio de e-mails |
| Google Speech API | Transcrição de áudio |

## ▶️ Como executar
1. Clone o repositório
2. Instale as dependências:
   pip install -r requirements.txt
3. Adicione sua senha de app Gmail em files/senha
4. Execute: python nasama.py

## ⚠️ Segurança
O arquivo files/senha não está no repositório.
Utilize senha de app do Gmail (não a senha principal).

## 👨‍💻 Autor
Seu Nome — linkedin.com/in/seuperfil




## 📁 Estrutura do Projeto
nasama/
│
├── files/
│   ├── senha          # não incluso — senha de app do Gmail
│   └── contatos.json  # cadastro de contatos por voz
│
├── funcoes_email.py
├── funcoes_so.py
├── nasama.py
├── requirements.txt
├── .gitignore
└── README.md

## ⚙️ Configuração

### Senha do Gmail
Crie o arquivo `files/senha` com sua senha de app do Gmail.
Veja como gerar: [Senhas de app Google](https://myaccount.google.com/apppasswords)

### Contatos
Cadastre seus contatos em `files/contatos.json`:
```json
