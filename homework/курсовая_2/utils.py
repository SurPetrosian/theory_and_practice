from clas import BasicWord, Player
import json
import requests
import random


def load_random_word():
    data = requests.get('https://jsonkeeper.com/b/XQ39', verify=False).text
    json_data = json.loads(data)
    random_word = random.choice(json_data)

    return BasicWord(random_word["word"], random_word["subwords"])

