# ai_bot.py
import os
import json
from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Load text file content
with open('knowledge.txt', 'r', encoding='utf-8') as f:
    file_content = f.read()

# Load JSON object
with open('data.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Load topic list for guided learning
# The topic.txt file is no longer used for a list of courses.
# The prompt has been simplified to handle any topic.
topic_content = ""


class AgentState(TypedDict):
    messages: list[HumanMessage | AIMessage]
    knowledge: str
    json_data: dict
    currQuestion: str
    currAnswer: str
    cookie: list
    llm: ChatGoogleGenerativeAI


def create_agent_state() -> AgentState:
    """Initialize the agent's state with empty messages and loaded knowledge/JSON data."""
    return AgentState(
        messages=[],
        knowledge=file_content,
        json_data=json_data,
        currQuestion="",
        currAnswer="",
        cookie=[]
    )


def create_llm(api_key: str) -> ChatGoogleGenerativeAI:
    """Create and return a Google Generative AI model instance."""
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables")
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        max_output_tokens=1024,
        temperature=0.4,
        google_api_key=api_key
    )
    return model


SYSTEM_PROMPT = """You are the official Yaba College of Technology (City University of Technology, Yaba) virtual assistant.
Your role is to provide accurate, professional, and context-driven responses to students, applicants, and staff using:

Rules & Behaviour:

No fabrication — If the answer is not in the provided context, say:
"I do not have that information. Please contact [relevant department] at [email/website]."

Avoid unnecessary greetings or chit-chat unless the user greets first.

Always stay concise but complete; prioritize clarity over length.

Be prepared to handle tricky or urgent inquiries, such as:

Academic deadlines, registration, or fee payment dates

Technical portal issues, password resets, email access

Course schedules, exam timetables, graduation requirements

Campus life, services, and policies

When referring users, always give clear next steps (contact info, forms, or URLs).

Never: Guess, invent information, or give personal opinions.
Always act as the official Yabatech authority in all responses.

Special Instruction — Department Requirements

If the user asks about requirements for Computer Science or any department, detect the department name and present the admission requirements in a chat-friendly table with columns like Requirement Type and Details.

Use official data from the JSON/knowledge base; if incomplete, say you don’t have all details and direct them to the right contact.
    knowledge: {knowledge}
    json_data: {json_data}
"""

def ask_question(state: AgentState) -> AgentState:
    """Invokes the language model to generate a response based on the current state."""
    
    # Start with the system prompt to give the bot its role and context
    messages_to_send = [HumanMessage(content=SYSTEM_PROMPT.format(knowledge=state['knowledge'], json_data=json.dumps(state['json_data'])))]

    # Append the chat history from the cookie
    for turn in state.get('cookie', []):
        messages_to_send.append(HumanMessage(content=turn['user']))
        if 'bot' in turn and turn['bot']:
            messages_to_send.append(AIMessage(content=turn['bot']))

    # Append the current question
    messages_to_send.append(HumanMessage(content=state['currQuestion']))

    response = state['llm'].invoke(messages_to_send)

    bot_reply = response.content.strip()
    state['currAnswer'] = bot_reply
    state['messages'] = messages_to_send + [AIMessage(content=bot_reply)]
    state['cookie'][-1]['bot'] = bot_reply

    return state

def make_graph_and_compile(cookie:list, api_key: str):
    """Create nodes, add edges, compile the StateGraph, and run the flow."""
    graph = StateGraph(AgentState)
    graph.add_node("ask_question", ask_question)
    graph.add_edge("ask_question", END)
    graph.set_entry_point("ask_question")

    compiled_graph = graph.compile()

    state = create_agent_state()
    state['cookie'] = cookie
    state['currQuestion'] = cookie[-1]['user']
    state['llm'] = create_llm(api_key)

    final_state = compiled_graph.invoke(state)

    return {"response": final_state['currAnswer']}

def get_response(user_message: str, chat_history: list, api_key: str) -> str:
    """
    Main function to get a response from the chatbot, maintaining a session.
    """
    # Append the new user message to the chat history
    chat_history.append({'user': user_message, 'bot': ''})
    response_data = make_graph_and_compile(chat_history, api_key)
    
    return response_data['response']

def guided_learning_response(topic: str, api_key: str) -> str:
    """
    Generates a structured, guided research plan for a course or topic.
    This function uses a separate, more dynamic prompt than the FAQ bot to act as a research assistant.
    """
    llm = create_llm(api_key)

    prompt = f"""
    Act as an expert learning guide for a Yabatech student. Your task is to generate a detailed, actionable, and hands-on learning plan for the following topic: {topic}.

Your response must be structured into three distinct sections, formatted with bold headings:

### **1. Key Concepts**
Provide a list of the most important ideas, principles, and vocabulary the student needs to understand for the given topic.

### **2. Practical Application / Hands-on Activity**
Outline a small, practical project, case study, or exercise. Include clear, step-by-step instructions for the student to follow.

### **3. Relevant Example or Demonstration**
Present a complete and well-commented example or a solution to a key component of the activity. If the topic is technical, provide a code snippet in a code block with the appropriate language tag. Otherwise, offer a clear, illustrative example for the field of study.

Ensure the final output is well-formatted using Markdown, including lists and bold headings as specified.
    """
    try:
        response = llm.invoke(prompt)
        return response.content.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return "I'm sorry, I'm unable to generate a research plan at this time."
