from typing import Tuple, Any

import requests
import json

from config import BASE_URL


def get_otp_code(user_phone: str) -> tuple[str, str]:
    url = BASE_URL + "/auth/api/Phone/login"

    payload = json.dumps({
        "phoneNumber": user_phone
    })
    headers = {
        'Content-Type': 'application/json',
        'Cookie': '.AspNetCore.Identity.Application=CfDJ8H3pdZk2mktBtxknIHRblkUwnzMCgaUbANWJMJzFeSOjhMZxG_NxTnL-ADMYqIJ'
                  'fwugXrTaSTIY5m64U0dwP_zamThqzeY1m1e8G8JEqu4WAkE5M-9nBFGO6OWld_xmBhfr80EnZCLzRFMXTC1gGJrizV7l2gky3B5n'
                  '7WM4kYthEdvgk7jRkoQW9BsEwAFnFHfaWaWiikWSbql9iATlum61wBA9hg13xA1g589kZ3AVNHjUoThBEvi_uTAp85gC9JUFNFDp'
                  'BdeuljbIV2L_w-O6yyooty8wkDguFXGE1lEXeXjjcfrRNjX-25wWEy6JJRAh5CmP47TRSsn5FDMktYiURRL5wZoaj8_C433BoUl_'
                  'DX7IOtWFel3WQl6eo0QcVcbzpDoMoK2axaxIERjXD4M8lF_u2maRnXnkUDmrW6FUlSdthd3c2nyv4_AQuDS7kZHkWlyHtZ8jiSz_'
                  'Q7HiL07FHXqeYMWsU8muJElCcOrBc76yGNsaHzGAPCIzZ5-kJj0KD4orYDLZgr-FhUoVugfWduk8oyMoAoxx2YlLGBIDHyJFMLzk'
                  'e0ZAh63_KsYZbSlPszZjxavAtbClqksIzoT74HRGwAv9em-OuRWmECmN0moc4oE03ZQ_CeTTfssayF6vhjPxCYC9Iv6vru44Ka3k'
                  '47mZJKPDoUklW2UjAXMnYyXrb-1tHsxIQ64MEMgJ0lskoeRGL_i7PFmYd3k_w9s8Jovfd-8GoD8QMd_ZEIqGF-f3mrNJV3uc3LT7p'
                  'ffuasipC1jbA0XAbkAuKy0ipvPGUXGv-IHsR5ML51Qyr8NC9Vye6xFKBWg23CM9zbRnzGoy0QMJJQrFNd0vh1yg982wpWOeHPtepV'
                  'K_IfqJJU12C1SMM-5Bn7qFuLqHmZTk8fwB2Q0L4XTHwQJdCgU3oY_iun5n2NqcGdd_zp8p9Il5empk9mm5JcP8BLoznoNSIGw'
    }

    response = requests.post(url=url,
                             data=payload,
                             headers=headers)

    if response.status_code != 202:
        raise AssertionError(f"Response status is {response.status_code}")

    else:
        return response.json().get("verify_token"), user_phone
