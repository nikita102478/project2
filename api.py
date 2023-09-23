import requests

a = dict[str, dict[str, list]]


class RequestsManager:
    """
    катугориу фыавф фыафваыв
    """

    BASE_URL = "https://fakestoreapi.com"

    def get(self, endpoint: str):
        response = requests.get(self.BASE_URL + endpoint)
        return response.json()


