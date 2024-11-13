import logging
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
    print(f"Attempting to send prompt to OpenAI API...")
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-4o-mini",
        )
        print(f"Response generated successfully.")
        return response
    except openai.AuthenticationError as e:
        logging.error(f"Authentication failed. {e}.")
        return None
    except openai.APIConnectionError as e:
        logging.error(f"Failed to connect to OpenAI API: {e}")
        return None
    except openai.APIError as e:
        logging.error(f"OpenAI API returned error: {e}.")
        return None


def read_content_from_file(file_name):
    print(f"Attempting to read file {file_name}...")
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"File read successfully.")
        return content
    except FileNotFoundError:
        logging.error(f"File {file_name} was not found.")
        return None
    except IOError:
        logging.error(f"An issue occurred while reading file {file_name}.")
        return None

def save_response_to_html_file(content_to_save, file_name):
    print(f"Attempting to save data to file {file_name}...")
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(content_to_save)
        print(f"File saved successfully.")
    except IOError:
        logging.error(f"An issue occurred while saving data to file {file_name}")
        return None


if __name__ == '__main__':
    content = read_content_from_file("Zadanie dla JJunior AI Developera - tresc artykulu.txt")

    if content is not None:
        prompt = ("Create plain HTML code for a body tag based on this criteria: \n"
                  f"1.Content of website: {content} \n"
                  "2.Don't generate <body> tag \n"
                  "3.Don't use css or java scripts code \n"
                  "4.Add placeholder images in places where its needed in your opinion with attribute src=\"image_placeholder.jpg\" \n"
                  "5.Add attribute alt for each image based on what should it represents as well as caption under image \n"
                  "6.Don't generate ``` tag before and after code \n"
                  )
        response = ai_response(prompt)
        if response is not None and hasattr(response, 'choices') and response.choices:
            content_to_save = response.choices[0].message.content
            print(content_to_save)
            save_response_to_html_file(content_to_save, "artykul.html")
        else:
            logging.error(f"Something went wrong while communicating with OpenAI API.")
    else:
        logging.error(f"Somthing went wrong while reading file.")


