# Prompt_engineering
Aprenda a fazer um prompt para seus agentes 

# 5 partes: 

<img width="200" height="300" alt="Captura de tela 2025-09-01 225001" src="https://github.com/user-attachments/assets/265c65d8-0488-4815-ac8a-0e85b35f0179" />

## 🧻 Papel

<img width="200" height="30" alt="image" src="https://github.com/user-attachments/assets/64a34f96-971b-4c12-8115-decd82eb6cbf" />

A atribuição de papel é uma técnica onde ao modelo de linguagem é atribuído um papel específico para desempenhar durante a interação. Isso ajuda a imergir o modelo no papel e pode melhorar o desempenho em tarefas subsequentes.

Exemplo:
   - "Você é um roteirista de conteúdo de formato curto altamente qualificado e criativo, com um talento para criar vídeos envolventes, informativos e concisos."

Neste exemplo, o papel (roteirista de conteúdo de formato curto altamente qualificado e criativo) é estabelecido, e qualidades-chave (envolvente, informativo, conciso) são destacadas para enfatizar a aptidão do modelo neste papel.

### Resultados da Pesquisa: 🚀
- Quando atribuído um papel vantajoso, a precisão aumentou em 10,3%
- Descrições elogiosas de suas habilidades aumentaram ainda mais a precisão (~15-25% de aumento total!)


## 📕 Tarefa
<img width="200" height="30" alt="image" src="https://github.com/user-attachments/assets/81ea8e76-e89e-4e80-b573-ebd89bcc3269" />

A tarefa é o que a maioria das pessoas normalmente fornece a um modelo esperando um resultado. É uma descrição direta do que elas querem alcançar.

Exemplo:
- "Gere mensagens de contato (outreach) casuais e envolventes para usuários que procuram promover seus serviços na indústria odontológica, focando especialmente na integração de ferramentas de IA para escalar negócios. Suas mensagens devem ser diretas, amigáveis e personalizadas para o destinatário, incentivando uma conversa sobre como a IA pode beneficiar o negócio dele."

Notas sobre Como Escrever Tarefas:
- Sempre comece com um verbo (ex: gere, escreva, analise)
- Seja descritivo e preciso, mantendo o texto breve.
- Dependendo do caso de uso, é aqui que você pode inserir suas variáveis (veja abaixo)

Exemplo com Variáveis:

"Gere mensagens de contato casuais e envolventes para usuários que procuram promover seus serviços ou produtos específicos de um nicho, focando especialmente na integração de ferramentas de IA para escalar negócios. Suas mensagens devem ser diretas, amigáveis e personalizadas para o destinatário, incentivando uma conversa sobre como a IA pode beneficiar o negócio dele. Abaixo estão os detalhes para os quais você deve gerar o conteúdo.
- Nicho: {{nicho}}
- Oferta: {{oferta}}"


## 📒 Específicos 
<img width="200" height="30" alt="image" src="https://github.com/user-attachments/assets/656ebe86-643f-4d53-84de-21b06e4a4c00" />

A seção de especificações é uma oportunidade para listar as notas mais importantes sobre a execução da tarefa descrita acima.

O formato de lista permite que você adicione facilmente novas instruções enquanto testa e melhora o prompt. Claro, tente não acumular informações desnecessárias aqui. Menos é mais.

Exemplo de Especificações:
- Cada mensagem deve ter uma introdução, corpo e conclusão, com um tom informal e envolvente.
- Use placeholders como (user.firstname) para personalizar as introduções.
- Etc.

## 📝 Contexto
<img width="200" height="40" alt="image" src="https://github.com/user-attachments/assets/5ff2f55f-914a-427e-81a3-c4caa1be9a24" />

Fornecer contexto sobre em qual ambiente o LLM está operando e por que ele está realizando essa tarefa específica pode ajudar a aumentar ainda mais o desempenho.

Isso combina técnicas anteriores como a Atribuição de Papel (Role Prompting), ao esclarecer ainda mais quem ele é, o que está fazendo e por que está fazendo. O Prompt Emocional (EmotionPrompt) também pode ser usado aqui ao explicar a importância do papel do LLM no sucesso do negócio e até mesmo da sociedade como um todo.

Exemplo Específico:
- "Nossa empresa fornece soluções baseadas em IA para negócios de diversas indústrias. Recebemos um alto volume de e-mails de potenciais clientes através do formulário de contato do nosso site. Seu papel na classificação desses e-mails é essencial para que nossa equipe de vendas priorize seus esforços e responda às solicitações em tempo hábil. Ao identificar com precisão as oportunidades e os e-mails que precisam de atenção, você contribui diretamente para o crescimento e sucesso de nossa empresa, portanto, valorizamos muito sua cuidadosa consideração e atenção à classificação."

Notas Gerais:
- Forneça contexto sobre o negócio, incluindo clientes, tipos de serviços ou produtos, valores da empresa, etc.
- Forneça contexto sobre o sistema do qual faz parte. Ex: quando clientes enviam nosso formulário no site, nós recebemos um e-mail, você então...
- Forneça contexto sobre a importância da tarefa e o impacto no negócio e/ou na sociedade como um todo.


## 📗 Exemplos
<img width="200" height="100" alt="image" src="https://github.com/user-attachments/assets/30a14bf7-667d-403f-b2bb-5e5f36099e91" />

Na seção de exemplos, usamos uma técnica conhecida como Few-Shot Prompting (Prompting com Poucos Exemplos) para aumentar o desempenho e ajustar finamente o tom, o formato e o comprimento da resposta.

Isso ocorre quando vários exemplos de entrada e saída são fornecidos ao modelo de linguagem como parte do prompt. Isso permite que o modelo execute novas tarefas sem a necessidade de ajuste fino (fine-tuning).

Resultados da Pesquisa: 🚀
- O GPT-3 175B alcançou uma melhora média de 14,4% sobre sua precisão de zero-shot (nenhum exemplo) de 57,4% ao usar 32 exemplos por tarefa.

Principais Conclusões:
- Fornecer apenas alguns exemplos melhora significativamente o desempenho em comparação com o prompting zero-shot (sem exemplos).
- A precisão escala com o número de exemplos, mas apresenta retornos decrescentes.
- A maior parte dos ganhos pode ser alcançada com 10 a 32 exemplos bem-elaborados.

## 📃 Notas
<img width="200" height="30" alt="image" src="https://github.com/user-attachments/assets/55506af1-354d-4540-b338-a8bf7da8f25b" />

A seção de notas é sua última chance de lembrar o LLM (Modelo de Linguagem Grande) dos aspectos-chave da tarefa e adicionar quaisquer detalhes finais para ajustar as saídas ao seu estilo desejado.

Suas notas formam uma lista que consiste em coisas como:
- Notas de formatação da saída, ex: “sua saída deve estar no formato x”
- Prompting negativo: “NÃO faça x”
- Ajustes de tom
- Lembretes de pontos-chave da tarefa ou das especificações

Esta lista de notas geralmente começa enxuta e acaba com algumas linhas de profundidade após algumas rodadas de testes e ajustes. É nesta lista que você pode adicionar coisas sem precisar refatorar o prompt inteiro.

A inclusão da seção de 'notas' nesta fórmula de prompt é baseada no efeito “Perdido no Meio” (Lost in the Middle), que destaca uma limitação significativa na forma como os modelos de linguagem lidam com grandes quantidades de tokens de entrada.
