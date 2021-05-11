import requests
import json
from config.config_management import SUBSCRIPTION_KEY, BASE_URL


def ms_luis_connect(input: str):
    """

    :param input: input for intent classification
    :return: intent and score
    """
    base_url = BASE_URL
    parameters = {"subscription-key": SUBSCRIPTION_KEY,
                  "verbose": False,
                  "show-all-intents": False,
                  "log": False,
                  "query": input}

    response = json.loads(requests.request("GET", base_url, params=parameters).text)
    return {
        "intent": response["prediction"]["topIntent"],
        "score": response["prediction"]['intents'][response["prediction"]["topIntent"]]["score"]
    }
