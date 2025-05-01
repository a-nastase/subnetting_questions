import requests
from bs4 import BeautifulSoup

url="http://www.subnettingquestions.com/"

while True:
    response=requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    question_element = soup.find('p', class_='question')
    question = question_element.text.strip()

    answer_div = soup.find('div', id='answerLayer')
    answer_text = answer_div.find('p').text.split('Answer: ')[-1].strip()

    print(question)
    user = input("Answer: ")
    if(user == answer_text):
        print("correct!")
    else:
        print("this was the correct answer...")
        print(answer_text)  
