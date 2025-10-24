# 🤖 LangChain Multi-Agente: Debate e Planejamento entre Gemini e GPT

Este projeto demonstra o poder do framework **LangChain** para orquestrar sistemas multiagentes (Multi-Agent Systems), colocando dois Large Language Models (LLMs) de provedores diferentes — **Google Gemini** e **OpenAI GPT-4o** — para interagir de forma estruturada.

O código foi estruturado para suportar dois modos principais de interação: **Debate** (conflito de ideias) e **Planejamento Cooperativo** (estruturação de soluções).

## 🚀 Funcionalidades

O script em Python (`debate.py` ou similar) permite que os dois modelos interajam com personas distintas, usando o histórico de mensagens para manter a coerência da conversação.

### 1. Modo Debate (Conflito de Ideias)

* **Agente A (Gemini):** Assume um papel de defensor, argumentando veementemente a favor de um tópico específico.
* **Agente B (OpenAI/GPT-4o):** Assume um papel de opositor, apresentando críticas pragmáticas e defendendo o ponto de vista contrário.
* **Mecanismo:** O output de um agente se torna o input (histórico) do outro, simulando um diálogo de réplicas e tréplicas.

### 2. Modo Planejamento Cooperativo (Estruturação de Soluções)

* **Agente A (Gemini - O Conceptualizador):** Focado em *brainstorming*, criatividade e expansão de recursos para uma ideia inicial.
* **Agente B (OpenAI/GPT-4o - O Planejador Crítico):** Focado em viabilidade, identificação de riscos e estruturação da ideia em um *roadmap* de implementação.
* **Resultado:** Uma estrutura de solução detalhada e criticada.

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **LangChain:** Framework de orquestração (utilizando o LangChain Expression Language - LCEL).
    * `ChatOpenAI`: Integração com os modelos GPT.
    * `ChatGoogleGenerativeAI`: Integração com os modelos Gemini (ex: `gemini-2.5-flash`).
    * `MessagesPlaceholder`: Essencial para gerenciar o histórico de conversação (memória) entre os agentes.
* **python-dotenv:** Para gerenciamento seguro das chaves de API.

## ⚙️ Configuração do Projeto

### Pré-requisitos

Você precisa de chaves de API para acessar os modelos:

1.  **OpenAI API Key**
2.  **Google AI API Key (para Gemini)**

### Passos para Execução

1.  **Clone o repositório:**
    ```bash
    git clone [LINK_DO_SEU_REPOSITORIO]
    cd [NOME_DO_SEU_REPOSITORIO]
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    # (ou use o comando direto: pip install langchain langchain-openai langchain-google-genai python-dotenv)
    ```

3.  **Configure as chaves de API:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione suas chaves:
    ```ini
    OPENAI_API_KEY="SUA_CHAVE_OPENAI"
    GOOGLE_API_KEY="SUA_CHAVE_GEMINI"
    ```

4.  **Execute o script:**
    ```bash
    python debate.py
    ```

## 📝 Como Adaptar

Para alterar o modo de operação:

1.  **Mudar o Tópico (Modo Debate):** Edite a variável `DEBATE_TOPIC` no arquivo.
2.  **Mudar a Ideia (Modo Planejamento):** Edite a variável `INITIAL_IDEA` no arquivo.
3.  **Ajustar Personas:** Edite os `SystemMessage` dentro das definições `PROMPT_A` e `PROMPT_B` para dar novas funções, regras e personalidades aos seus agentes.
