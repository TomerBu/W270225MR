import requests


url = 'https://google.com'


response = requests.get(url)


print(response.status_code)
print(response.encoding)
print(response.headers)
print(response.headers['Content-Type']) #text/html; charset=ISO-8859-1

print(response.text)