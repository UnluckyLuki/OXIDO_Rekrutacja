import os
from dotenv import load_dotenv
import openai
from openai import OpenAI

load_dotenv()

api_key = os.getenv("API_KEY")
org = os.getenv("ORG")
project_id = os.getenv("PROJECT_ID")

client = OpenAI(
    organization=org,
    project=project_id,
    api_key=api_key,
)

def ai_response(prompt):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
            ],
        model="gpt-4o-mini",
    )
    return response

def read_content():
    file = open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", "r")
    content = file.read()
    file.close()
    return content


if __name__ == '__main__':
    content = read_content()
    response = ai_response("print: this is test")
    print(response.choices[0].message.content)
