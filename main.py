from pprint import pprint

from config import USER_PHONE
from src.api.empployee.api_get_access_token import api_get_access_token
from src.api.empployee.api_get_card_info import GetCardInfo
from src.api.empployee.api_get_otp_code import get_otp_code


def get_all_user_data():
    card_data = {}
    if USER_PHONE:
        user_phone = USER_PHONE
    else:
        user_phone = input("Enter a user phone number: ")

    otp_code, user_phone = get_otp_code(user_phone)
    access_token, refresh_token = api_get_access_token(verify_token=otp_code, phone_number=user_phone)
    card_data["cards"] = GetCardInfo(access_token).api_get_card_info()
    card_data["tokens"] = {"access token": access_token, "refresh_token": refresh_token}
    card_data["user_phone"] = user_phone

    pprint(card_data)


if __name__ == "__main__":
    get_all_user_data()
