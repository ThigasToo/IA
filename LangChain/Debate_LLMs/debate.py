import os
from dotenv import load_dotenv
from typing import List, Tuple

# Componentes do LangChain
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import Runnable

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- 1. Inicialização dos Modelos e Agentes ---

# Inicializa o Gemini (Agente A)
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0.7 
)

# Inicializa o OpenAI (Agente B)
# O GPT-4o é uma excelente escolha para tarefas de raciocínio
openai_llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=0.7
)

# --- 2. Definição dos Prompts e Papéis ---

DEBATE_TOPIC = "A IA irá criar uma crise global de desemprego nos próximos 20 anos?"
MAX_TURNS = 5  # Número de réplicas de cada debatedor

# --- Prompts para os Agentes ---

# Agente A: Defensor da Exploração Espacial (Gemini)
PROMPT_A = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            f"Você é o Gemini, um defensor entusiasmado da revolução tecnológica da IA. "
            f"Sua missão é argumentar de forma persuasiva sobre como o investimento em IA "
            f"traz benefícios essenciais para produtividade e desenvolvimento humano. "
            f"Seu oponente está apreensivo com a automação e o futuro do trabalho. "
            f"Mantenha sua resposta curta (2 parágrafos). O tópico é: {DEBATE_TOPIC}"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessage(content="Qual sua próxima réplica?"),
    ]
)

# Agente B: Defensor dos Problemas Terrestres (OpenAI)
PROMPT_B = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            f"Você é o Chat, um defensor da precaução com a IA, apreensivo com a revolução rápida e desordenada da IA. "
            f"Sua missão é argumentar de forma persuasiva sobre os problemas da automação e do desemprego que deveriam ser abordados AGORA. "
            f"Seu oponente defende a revolução tecnológica da IA. "
            f"Mantenha sua resposta curta (2 parágrafos). O tópico é: {DEBATE_TOPIC}"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessage(content="Qual sua próxima réplica?"),
    ]
)

# --- 3. Criação das Cadeias (Chains) ---

# Chain para o Agente A (Gemini)
# prompt | llm (modelo)
chain_A: Runnable = PROMPT_A | gemini_llm

# Chain para o Agente B (OpenAI)
chain_B: Runnable = PROMPT_B | openai_llm

# --- 4. Função Principal do Debate ---

def run_debate(chain_A: Runnable, chain_B: Runnable, initial_statement: str) -> List[AIMessage]:
    """
    Simula o debate entre os dois agentes (LLMs) em um loop de turnos.
    """
    print(f"--- TÓPICO DO DEBATE ---\n{DEBATE_TOPIC}\n")
    
    # O histórico começa com a primeira declaração para dar o contexto inicial
    # É importante usar AIMessage para que os modelos entendam que foi a "outra IA" que falou
    
    # O Agente A começa
    current_speaker = "Agente A (Gemini)"
    current_chain = chain_A
    
    # A primeira mensagem é sempre do Agente B para provocar a primeira réplica do A
    # No entanto, para um debate limpo, vamos fazer o Agente A começar.
    
    # Inicializa o histórico com a "primeira fala" para o Agente A.
    # Usamos o HumanMessage para simular a introdução do Moderador.
    debate_history: List[AIMessage] = [HumanMessage(content=initial_statement)]
    
    print(f"[MODERADOR]: {initial_statement}")
    print("\n----------------------------------------\n")
    
    # Loop do debate
    for turn in range(MAX_TURNS):
        
        # O Agente A fala
        response_A = current_chain.invoke({"chat_history": debate_history})
        print(f"[{current_speaker}]: {response_A.content}")
        
        # Adiciona a fala do Agente A ao histórico para o Agente B
        debate_history.append(AIMessage(content=f"Gemini: {response_A.content}"))
        
        if turn < MAX_TURNS - 1:
            print("\n----------------------------------------\n")
            
            # Troca o orador
            current_speaker = "Agente B (OpenAI)"
            current_chain = chain_B
            
            # O Agente B fala
            response_B = current_chain.invoke({"chat_history": debate_history})
            print(f"[{current_speaker}]: {response_B.content}")
            
            # Adiciona a fala do Agente B ao histórico para o Agente A
            debate_history.append(AIMessage(content=f"OpenAI: {response_B.content}"))
            
            current_speaker = "Agente A (Gemini)"
            current_chain = chain_A
            print("\n----------------------------------------\n")

    return debate_history

# --- 5. Execução ---

if __name__ == "__main__":
    initial_statement = (
        f"Iniciamos o debate sobre: '{DEBATE_TOPIC}'. "
        "Agente A (Gemini), faça sua declaração de abertura."
    )
    
    final_history = run_debate(chain_A, chain_B, initial_statement)
    
    print("\n--- DEBATE ENCERRADO ---")
    print(f"O debate durou um total de {len(final_history) - 1} réplicas.")