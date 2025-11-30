import requests

# r = requests.get("https://google.com")
# print(r.status_code)
# print(r.text)

with open('dogs.txt','a') as file:
    for _ in range(10):
        url = 'https://dog.ceo/api/breeds/image/random'
        r = requests.get(url)
        print(r.json())
        data =r.json()
        file.write(data["message"] + '\n')
    