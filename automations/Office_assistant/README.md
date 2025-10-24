# 🤖 Assistente Digital para Consultórios (WhatsApp + n8n)

Este projeto implementa uma **assistente digital para consultórios médicos e odontológicos** utilizando o [n8n](https://n8n.io/).  
A assistente é capaz de **atender pacientes pelo WhatsApp**, verificar **disponibilidade de horários no calendário**, agendar consultas e **enviar e-mails de confirmação automaticamente**.

---
<img width="1919" height="984" alt="Captura de tela 2025-09-17 152812" src="https://github.com/user-attachments/assets/d6ff866a-6ae0-4dd6-82d5-72b1f850c375" />

## 🚀 Funcionalidades

- 📌 **Atendimento automatizado no WhatsApp**  
  Responde dúvidas dos pacientes a partir de uma base de conhecimento usando **RAG (Retrieval-Augmented Generation)**.

- 📅 **Agendamento de consultas**  
  - Verifica disponibilidade no Google Calendar.  
  - Solicita dados do paciente (**nome, e-mail e motivo da consulta**).  
  - Cria o evento no calendário na data e horário disponíveis.  

- 📧 **Confirmação por e-mail**  
  - Após o agendamento, envia automaticamente uma mensagem de confirmação para o paciente via **Gmail**.  

---

## 🛠️ Tecnologias Utilizadas

- **n8n** – Orquestração e automação dos fluxos.  
- **OpenAI** – Geração de respostas inteligentes no atendimento.  
- **Postgres** – Memória de conversas para manter contexto.  
- **Google Calendar** – Checagem de disponibilidade e marcação de consultas.  
- **Gmail** – Envio de e-mails de confirmação para pacientes.  

---

## 📂 Estrutura do Fluxo no n8n

1. **When chat message received** → Captura a mensagem do WhatsApp.  
2. **AI Agent (OpenAI + Postgres Memory)** → Interpreta a solicitação do paciente.  
3. **Calendar Availability** → Verifica os horários disponíveis.  
4. **Calendar Appointment** → Agenda a consulta no Google Calendar.  
5. **Send a message in Gmail** → Envia e-mail de confirmação ao paciente.  

---

## 📸 Exemplos de Uso

### Verificação de disponibilidade
> Paciente: "Gostaria de marcar uma consulta dia 18/09/2025 às 14h"  
> Assistente: "O horário das 14h às 15h no dia 18/09/2025 está disponível. Por favor, forneça seu nome, e-mail e motivo da consulta para que eu possa agendar."

### Confirmação de consulta
> Paciente: "Thiago, aqueleeuapolo@gmail.com, gostaria de uma consulta ortodôntica"  
> Assistente: "Sua consulta ortodôntica foi agendada para o dia 18/09/2025, das 14h às 15h. Você receberá um e-mail de confirmação em breve."  

### 📩 O paciente então recebe no e-mail:  

```
Assunto: Confirmação de Consulta Odontológica
Mensagem: Prezado Thiago,
Sua consulta ortodôntica está confirmada para o dia 18 de setembro de 2025, das 14h às 15h.
Atenciosamente,
Clínica Odontológica
```
<img width="1919" height="984" alt="Captura de tela 2025-09-17 153208" src="https://github.com/user-attachments/assets/e6fd4fcc-fc04-460f-b58e-0f8ab9452c84" />

## 📌 Possíveis Melhorias
- Integração com outros sistemas de prontuário eletrônico.
- Envio de lembretes automáticos (WhatsApp/E-mail).
- Painel de gestão de pacientes e consultas.

