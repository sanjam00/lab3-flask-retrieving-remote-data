import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # query endpoint
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # convert to json data
        response_body = self.get_response_body()
        data = json.loads(response_body)
        return data        

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

requester = GetRequester(url)

people = requester.load_json()

print(people)