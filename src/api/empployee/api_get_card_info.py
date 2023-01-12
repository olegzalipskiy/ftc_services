import requests

from config import BASE_URL


class GetCardInfo:
    def __init__(self, access_token: str):
        self.user_access_token = access_token
        self.card_data = {}
        self.headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {self.user_access_token}'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def api_get_card_info(self) -> dict[dict[str]]:
        url = BASE_URL + "/mobile/v1/Cards"

        response = self.session.get(url)

        if response.status_code != 200:
            raise AssertionError(f"Status code for {url} is {response.status_code}")

        else:
            for _ in response.json():
                self.card_data[_.get("brand")] = {"type": _.get("type"), "card_holder_name": _.get("cardHolderName"),
                                                  "card_last_4": _.get("cardPanLast4"), "card_id": _.get("id"),
                                                  "expiration_date": _.get("expirationDate")}
                url = BASE_URL + f"/mobile/v1/Cards/info/{_.get('id')}"
                response = self.session.get(url)

                if response.status_code != 200:
                    raise AssertionError(f"Status code for {url} is {response.status_code}")

                else:
                    self.card_data[_.get("brand")].update({"pan": response.json().get("pan"), "cvv": response.json().get("cvv")})

                url = BASE_URL + f"/mobile/v1/Cards/balance/{_.get('id')}"
                response = self.session.get(url)

                if response.status_code != 200:
                    raise AssertionError(f"Status code for {url} is {response.status_code}")
                else:
                    self.card_data[_.get("brand")].update({"balance": response.json().get("balance")})

        return self.card_data
