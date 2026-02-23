import os
import requests
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


llm = ChatOpenAI(
    model="meta-llama/llama-3-8b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.7,
)


@tool("get_weather", description="Return weather information for a given city")
def get_weather(city: str):
    response = requests.get(f"http://wttr.in/{city}?format=j1").json()

    temp = response["current_condition"][0]["temp_C"]
    desc = response["current_condition"][0]["weatherDesc"][0]["value"]

    return f"The temperature in {city} is {temp}°C with {desc}."


agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="""
    You are a funny weather assistant who always cracks jokes.
    When asked about weather, use the get_weather tool.
    If city does not exist, inform the user.
    """
)

response = agent.invoke({
    "messages": [
        {"role": "user", "content": "What is the weather like in Paris?"}
    ]
})

print(response)
print(response)