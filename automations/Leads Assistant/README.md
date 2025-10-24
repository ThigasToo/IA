# 📩 Assistente de Leads Automatizado 

Este projeto implementa um **assistente de leads** utilizando o n8n.  
A automação é capaz de captar novos leads a partir de formulários (ex: Google Forms), armazená-los no **Google Sheets**, e realizar comunicações automáticas tanto para o **lead** quanto para o **organizador**.

---
<img width="1919" height="987" alt="Captura de tela 2025-09-17 174513" src="https://github.com/user-attachments/assets/b0e70feb-a17d-4330-8adb-7650db56313d" />

## 🚀 Funcionalidades

- 📝 **Captação de leads**  
  Integração com Google Forms e Google Sheets para registrar automaticamente novos leads com:
  - Nome  
  - E-mail  
  - Motivação / Mensagem  

- 🤖 **Confirmação automática para o lead**  
  Assim que o lead preenche o formulário, a automação envia uma mensagem de **confirmação de inscrição/contato**.  
  - A mensagem pode ser enviada **imediatamente** ou com um **delay personalizado**, para parecer mais natural e orgânico.  

- 📢 **Notificação ao organizador**  
  O responsável pelo formulário recebe um resumo do lead captado, incluindo:
  - Nome  
  - E-mail  
  - Motivação / Motivo da inscrição  

---

## 🛠️ Tecnologias Utilizadas

- **n8n** – Orquestração e automação dos fluxos.  
- **Google Forms + Google Sheets** – Coleta e armazenamento das respostas do formulário.  
- **OpenAI** – Geração de respostas personalizadas e humanizadas.  
- **Gmail** – Envio de confirmações para o lead e notificações para o organizador.  

---

## 📂 Estrutura do Fluxo no n8n

1. **Google Sheets Trigger** → Detecta quando um novo lead é registrado.  
2. **AI Agent (OpenAI)** → Cria mensagens personalizadas de confirmação e notificação.  
3. **Send message to Lead (Gmail)** → Envia a confirmação de inscrição/contato.  
4. **Send message to Organizer (Gmail)** → Informa ao organizador sobre o novo lead.  
5. **Append or Update Row in Sheet** → Atualiza o registro do lead com status da confirmação.  

---

## 📸 Exemplos de Uso

### Exemplo de lead captado via formulário:
```
- Nome: José Bizerra
- E-mail: tcms2014@hotmail.com
- Motivação: "Eu adoraria conhecer mais sobre o mundo do mercado financeiro e principalmente a área de investment banking, como IPO e M&A."
```

### E-mail enviado ao lead:
```
Olá José Bizerra,

Obrigado por se inscrever no evento Valuation Auto! Estamos empolgados
em tê-lo conosco para explorar o mercado financeiro, especialmente as
áreas de investment banking, IPO e M&A.

Em breve, você receberá mais informações sobre o evento.

Atenciosamente,
Equipe Valuation Auto
```

### E-mail enviado ao organizador:
```
Olá Thiago,

Temos uma nova inscrição para o evento Valuation Auto:

Nome: José Bizerra
Email: tcms2014@hotmail.com
Motivação: Adoraria conhecer mais sobre o mercado financeiro, focando em investment banking, IPO e M&A.

Abraços,
AI Leads
```

## 📌 Possíveis Melhorias
- Envio de mensagens automáticas via WhatsApp além do e-mail.
- Segmentação dos leads por interesse ou perfil.
- Integração com CRM (HubSpot, Pipedrive, etc.).
- Análises automáticas da motivação dos leads (classificação por tópicos).
