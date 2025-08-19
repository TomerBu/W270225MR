import requests

url = 'https://opentdb.com/api.php?amount=10&category=27&difficulty=easy&type=multiple'

response = requests.get(url)

if response.status_code != 200:
    print("Server error")
    print(response.status_code)
    print(response.text)
    exit(0)

json = response.json()

questions = json['results']

for q in questions:
    print("QUESTION", q['question'])
    print("ANSWER", q['correct_answer'])
    print("ANSWER", q['incorrect_answers'])
