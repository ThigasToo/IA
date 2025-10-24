# 📧 Automação de E-mails de Suporte

Este projeto implementa uma automação de atendimento a e-mails de suporte utilizando **n8n**.  
A automação é responsável por **filtrar, classificar e responder automaticamente** a mensagens recebidas no e-mail de suporte, além de registrar os dados em uma planilha.

---

## 🚀 Funcionalidades

- **Captura automática de e-mails** via **Gmail Trigger**.  
- **Classificação de texto** para identificar o tipo de mensagem (reclamação, agradecimento, contato, dúvidas sobre serviços/produtos etc.).  
- **Agente IA (OpenAI)** para auxiliar na classificação do conteúdo.  
- **Registro em planilha do Google Sheets**, salvando:
  - E-mail de contato  
  - Conteúdo da mensagem  
- **Envio automático de resposta** após um **delay configurável**, garantindo mais naturalidade no atendimento.  
- **Mensagem de confirmação de recebimento**, informando ao cliente que a solicitação foi recebida e que a equipe de suporte entrará em contato.  

---

## 🛠️ Tecnologias Utilizadas

- [n8n](https://n8n.io/) – Orquestração e automação de workflows  
- [Gmail API](https://developers.google.com/gmail/api) – Captura e envio de e-mails  
- [Google Sheets API](https://developers.google.com/sheets/api) – Registro e armazenamento de dados  
- [OpenAI](https://openai.com/) – Classificação de mensagens com IA  

---

## 📂 Estrutura do Workflow

1. **Gmail Trigger** → Dispara ao receber um novo e-mail.  
2. **Text Classifier (OpenAI)** → Classifica o conteúdo do e-mail.  
3. **Registro no Google Sheets** → Salva e-mail e mensagem recebida.  
4. **Envio de E-mail Automático** → Retorno imediato de confirmação.  

---

## 📝 Exemplo de Fluxo

1. Cliente envia um e-mail para o suporte.  
2. A automação captura o e-mail automaticamente.  
3. O texto é classificado pela IA.  
4. O e-mail e sua mensagem são armazenados em uma planilha do Google Sheets.  
5. O cliente recebe uma mensagem como:  
```
Assunto: Confirmação de Recebimento - Suporte Automação

Boa tarde,

Recebemos seu e-mail relatando problemas na automação. Gostaríamos de confirmar que sua mensagem foi recebida e que nossa equipe entrará em contato em breve para ajudar a resolver a situação.

Agradecemos pela paciência e compreensão.

Atenciosamente,
Equipe de Suporte
```

## 🔮 Possíveis Melhorias
- Adicionar múltiplas respostas personalizadas de acordo com a classificação.
- Integração com CRM para histórico de atendimentos.
- Dashboard de métricas de tickets recebidos.


<img width="1919" height="989" alt="Captura de tela 2025-09-18 222507" src="https://github.com/user-attachments/assets/7ecfbe0b-7ea1-430e-9bb5-da5d474b9453" />
