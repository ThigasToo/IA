# Automatização de Resumo de E-mails com OpenAI

Esta automação foi criada para simplificar sua rotina de e-mails, resumindo automaticamente as mensagens recebidas e enviando o resumo para sua caixa de entrada. É a solução perfeita para quem lida com um alto volume de e-mails e precisa absorver o conteúdo principal de forma rápida, sem perder tempo lendo mensagens longas.

<img width="1919" height="986" alt="Captura de tela 2025-09-16 101200" src="https://github.com/user-attachments/assets/bd329951-721c-45c8-aa2f-598ceb0f6059" />

## Como a Automação Funciona
A automação é composta por uma sequência de três etapas:

- Monitoramento de E-mails: O primeiro módulo (Email: Watch Emails) monitora sua caixa de entrada. Você pode definir critérios específicos, como remetente, assunto ou palavras-chave, para selecionar quais e-mails serão processados.
- Geração de Resumo com OpenAI: O e-mail selecionado é enviado para a API da OpenAI. Usando um modelo de linguagem avançado (como o o4-mini da imagem), o conteúdo do e-mail é processado para criar um resumo conciso e preciso.
- Envio do E-mail Resumido: O último módulo (Email: Send an Email) recebe o resumo gerado pela OpenAI e o envia para um novo e-mail. Você pode configurar o destino para sua própria caixa de entrada, garantindo que o resumo esteja sempre acessível.

## Benefícios
- Economia de Tempo: Reduz drasticamente o tempo gasto na leitura de e-mails longos.
- Eficiência: Garante que você não perca informações cruciais, mesmo em mensagens complexas.
- Personalização: Os critérios de seleção de e-mails e as configurações da API podem ser totalmente adaptados às suas necessidades.

## Requisitos
Para replicar esta automação, você precisará de:

 - Uma plataforma de automação (como Make.com ou Zapier).
- Uma chave de API da OpenAI.
- Acesso à sua conta de e-mail.

Para que a automação funcione corretamente, o prompt de entrada do módulo da OpenAI deve ser configurado para receber o conteúdo do e-mail do primeiro módulo. O output do módulo da OpenAI, por sua vez, será o corpo do e-mail no terceiro módulo.

<img width="1919" height="986" alt="Captura de tela 2025-09-16 101242" src="https://github.com/user-attachments/assets/8fac2872-a662-4a71-8c67-62d1eaf3c22d" />
