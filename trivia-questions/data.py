import requests

params = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=params)
data = response.json()
question_data = data["results"]
