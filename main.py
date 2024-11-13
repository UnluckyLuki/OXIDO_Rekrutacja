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
    file = open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content


def save_response_to_html_file(content_to_save):
    with open("artykul.html", "w", encoding="utf-8") as file:
        file.write(content_to_save)


if __name__ == '__main__':
    content = read_content()
    prompt = (("Create ONLY plain HTML code for a body tag based on this criteria: \n"
               "1.Content of website:") + content + "\n"
                                                    "2.Don't generate <body> tag"
                                                    "3.Don't use css or java scripts code \n"
                                                    "4.Add placeholder images with attribute src=\"image_placeholder.jpg\" \n"
                                                    "5.Add attribute alt for each image based on what should it represents \n"
                                                    "6.Don't generate ``` tag before and after code \n")
    response = ai_response(prompt)
    content_to_save = response.choices[0].message.content
    print(content_to_save)
    save_response_to_html_file(content_to_save)
