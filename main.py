
def read_content():
    file = open("Zadanie dla JJunior AI Developera - tresc artykulu.txt", "r")
    content = file.read()
    file.close()
    return content


if __name__ == '__main__':
    content = read_content()
    print(content)