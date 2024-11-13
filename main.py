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

def save_response_to_html_file(content_to_save):
    with open("artykul.html", "w", encoding="utf-8") as file:
        file.write(content_to_save)

if __name__ == '__main__':
    content = read_content()
    prompt = "Create ONLY plain HTML code without css or java scripts for a website based on this text: " + content
    response = ai_response(prompt)
    content_to_save = response.choices[0].message.content
    print(content_to_save)
    save_response_to_html_file(content_to_save)

