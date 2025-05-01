import requests
import time
from bs4 import BeautifulSoup
import json

url="http://www.subnettingquestions.com/"
file="db.json"

with open(file, "r") as f:
    pairs=json.load(f)

while True:
    response=requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')

    question_element = soup.find('p', class_='question')
    question = question_element.text.strip().replace("\u00a0", " ")

    answer_div = soup.find('div', id='answerLayer')
    answer_text = answer_div.find('p').text.split('Answer: ')[-1].strip()

    if question not in pairs:
        pairs[question] = answer_text
        print(f"New entry added: {question} -> {answer_text}")
        
        with open(file, 'w') as f:
            json.dump(pairs, f, indent=4)

    else:
        print("Duplicate found, skipping...")

    time.sleep(0.5)