import requests
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage, AIMessage

import os

load_dotenv()


model = init_chat_model(
    model="meta-llama/llama-3-8b-instruct",
    model_provider="openai", 
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)



conversation = [
    SystemMessage(content="You are a helpful assistant for questions regarding programming."),
    HumanMessage(content="What is python?"),
    AIMessage('Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. Python syntax emphasizes code readability, making it an excellent choice for beginners and experienced developers alike'),
    HumanMessage(content="When was it released?"),
]

response = model.invoke(conversation)

print(response)
print(response.content)