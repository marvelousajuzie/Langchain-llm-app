from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def generate_pet_name():
    llm = ChatOpenAI(
        model="meta-llama/llama-3-8b-instruct",
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        temperature=0.7,
    )

    response = llm.invoke(
        "I have a pet dog and I want a cool name for it, suggest 10 cool names."
    )

    return response.content


if __name__ == "__main__":
    print(generate_pet_name())