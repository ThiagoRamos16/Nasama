# 🎙️ Nasama — Assistente Virtual com IA

Assistente virtual desenvolvida em Python com reconhecimento e síntese de voz,
capaz de executar tarefas por comando de voz.

> O nome **Nasama** é uma homenagem aos meus 3 pets: **Na**ni, **Sa**ndy e **Ma**ya. 🐾

> Projeto desenvolvido durante o curso **OneBitCode Python**, com funcionalidades extras adicionadas como envio de e-mails por voz, agenda de contatos e interface gráfica.
---

## 🚀 Funcionalidades
- ⏰ Informa a hora atual por voz
- 📧 Envia e-mails por comando de voz
- 🔊 Responde em português com síntese de voz
- 🖥️ Interface gráfica com tema dark/light
- 🎵 Animação no círculo ao falar
- 💬 Histórico de conversa na tela
---

## 🛠️ Tecnologias utilizadas
| Tecnologia | Finalidade |
|---|---|
| gTTS | Síntese de voz (Text-to-Speech) |
| SpeechRecognition | Reconhecimento de voz |
| Google Speech API | Transcrição de áudio em português |
| smtplib / ssl | Envio de e-mails |
| customtkinter | Interface gráfica moderna |
| pygame | Reprodução de áudio |
| Pillow | Manipulação de imagens |
---

## 📁 Estrutura do Projeto
```
nasama/
│
├── files/
│   ├── senha          # não incluso — senha de app do Gmail
│   └── contatos.json  # não incluso — agenda de contatos
│
├── funcoes_email.py   # funções de envio de e-mail por voz
├── funcoes_so.py      # funções do sistema operacional
├── interface.py       # interface gráfica
├── nasama.py          # arquivo principal
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/ThiagoRamos16/nasama.git
cd nasama
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```
> Bibliotecas instaladas: `gTTS`, `pygame`, `SpeechRecognition`, `customtkinter`, `Pillow`

### 3. Senha do Gmail
Crie o arquivo `files/senha` com sua senha de app do Gmail.
Veja como gerar: [Senhas de app Google](https://myaccount.google.com/apppasswords)

### 4. Agenda de contatos
Crie o arquivo `files/contatos.json` com seus contatos:
```json
{
    "exemplo": "exemplo@gmail.com",
    "exemplo2": "exemplo2@gmail.com"
}
```

### 5. Execute
> ⚠️ **Recomendado: Python 3.12** — versões mais recentes podem ter incompatibilidade com o PyAudio/playsound.

```bash
python nasama.py
```

---

## 🗣️ Comandos disponíveis
| Comando | Ação |
|---|---|
| *"horas"* | Informa a hora atual |
| *"enviar e-mail"* | Inicia o fluxo de envio de e-mail por voz |
| *"fechar assistente"* | Encerra a Nasama |

---

## ⚠️ Segurança
Os arquivos `files/senha` e `files/contatos.json` **não estão no repositório** por segurança.
Utilize sempre senha de app do Gmail, nunca a senha principal.

---

## 👨‍💻 Autor
**Thiago Ramos da Silva**
[linkedin.com/in/thiagoramosdasilva](https://www.linkedin.com/in/thiagoramosdasilva)
