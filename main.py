from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()


def generate_pet_name():
    llm = OpenAI(temperature=0.6)

    name = llm("I have a pet dog and i want a cool name for it, sugguest me 10 cool names for my dog")

    return name

if __name__ == "__main__":
    print(generate_pet_name())