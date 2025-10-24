# Webchat de Atendimento Inteligente
Este projeto consiste em uma automação de webchat projetada para interagir com clientes, responder a perguntas comuns e encaminhar solicitações para a equipe de atendimento humano quando necessário. A solução é construída para ser integrada facilmente ao site de uma empresa, totalmente customizável para a identidade visual da companhia, proporcionando um ponto de contato inicial e eficiente para os visitantes.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/e211c9b4-f425-4e60-93ce-840428d73ae9" />

## 🚀 Funcionalidades
- Atendimento Automatizado: Responde a perguntas frequentes sobre serviços e produtos utilizando uma base de conhecimento.
- Interação Dinâmica: Mantém um histórico de conversa para oferecer respostas mais contextuais e personalizadas.
- Encaminhamento para Atendimento Humano: Captura informações do cliente (nome, e-mail, assunto) e notifica a equipe de atendimento via e-mail, garantindo que solicitações complexas sejam tratadas por um ser humano.
- Base de Conhecimento RAG: Utiliza a técnica de Retrieval-Augmented Generation (RAG) para buscar informações relevantes em uma base de dados e gerar respostas precisas.

## 🛠️ Tecnologias Utilizadas
- n8n: Ferramenta de automação que orquestra o fluxo de trabalho do chat.
- OpenAI: Utilizado para processar as mensagens do cliente e gerar respostas inteligentes.
- Supabase: Base de dados para armazenar o histórico de todas as conversas do chat.
- Pinecone: Base de dados vetorial que armazena a base de conhecimento (perguntas frequentes, informações de produtos, etc.) para o sistema RAG.
- Gmail: Usado como ferramenta para enviar e-mails de notificação para a equipe de atendimento, contendo os dados do cliente e a solicitação.

## 🧠 Como Funciona
O fluxo de trabalho é iniciado toda vez que uma nova mensagem é recebida no webchat:

1. Mensagem Recebida: O fluxo de trabalho é ativado pela entrada de uma nova mensagem do cliente.
2. Histórico da Conversa: A mensagem e o histórico de toda a conversa são enviados para um agente da OpenAI, que consulta o banco de dados do Supabase para manter o contexto.
3. Processamento da Mensagem:
- O agente da OpenAI avalia se a pergunta pode ser respondida com base na base de conhecimento.
- Se a resposta for encontrada na Pinecone, o agente a utiliza para formular uma resposta precisa e direta.
- Se o cliente solicitar falar com um ser humano ou se a pergunta for muito complexa, o agente solicita informações de contato (nome e e-mail).
4. Encaminhamento (se necessário):
- Após coletar as informações, o fluxo aciona o Gmail para enviar um e-mail à equipe de atendimento.
- O e-mail inclui o nome do cliente, e-mail de contato e o resumo da dúvida ou tópico, permitindo que a equipe entre em contato diretamente.
5. Resposta ao Cliente: O agente envia a resposta final ao cliente, seja uma resposta automática, ou uma confirmação de que sua solicitação foi encaminhada para a equipe.

## 📝 Showcase
- Foi utilizado um site html básico de "Hello word" para a apresentação da funcionalidade do chat, porém a configuração do webchat pode ser facilmente realizada em qualquer site

<img width="1919" height="1079" alt="Captura de tela 2025-09-16 134600" src="https://github.com/user-attachments/assets/bbc74e10-6172-4560-916e-a64b575f7409" />

