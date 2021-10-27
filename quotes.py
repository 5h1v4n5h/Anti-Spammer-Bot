import requests
import json

def inspire_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']+" -"+json_data[0]['a']
  return quote




def get_quote():
  response = requests.get("https://api.quotable.io/random")
  if response.ok:
    data = json.loads(response.text)
    quote = data['content']
    author = data['author']
    return  (f' {quote} - {author}')
        

