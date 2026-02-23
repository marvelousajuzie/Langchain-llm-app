from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
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


    prompt_template_name = PromptTemplate(
        input_variables=['animal_type'],
       template="I have a {animal_type} and I want a cool name for it, suggest 10 cool names."
    )

    chain = prompt_template_name | llm | StrOutputParser()

    response = chain.invoke({"animal_type": "cats"})
    return response


if __name__ == "__main__":
    print(generate_pet_name())