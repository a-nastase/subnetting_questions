import json

with open('./db.json') as f:
    data = json.load(f)

pairs = list(data.items())

index = 0
while True:
    question, answer = pairs[index]

    print(question, end="\n")
    ans = input("answer: ")

    if ans == answer:
        print("correct!")
    else:
        print("nope...it was: ")
        print(answer)

    index+=1