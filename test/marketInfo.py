import os
import jwt
import time
import uuid
import hashlib
from urllib.parse import urlencode

import requests

UPBIT_OPEN_API_ACCESS_KEY=open("UPBIT_OPEN_API_ACCESS_KEY.cfg","r").read()
UPBIT_OPEN_API_SECRET_KEY=open("UPBIT_OPEN_API_SECRET_KEY.cfg","r").read()
UPBIT_OPEN_API_SERVER_URL="https://api.upbit.com"

def market_info(market):
    query = {
        'market': market,
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': UPBIT_OPEN_API_ACCESS_KEY,
        'nonce': str(uuid.uuid4()), 
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, UPBIT_OPEN_API_SECRET_KEY)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(UPBIT_OPEN_API_SERVER_URL + "/v1/orders/chance", params=query, headers=headers)
    json_data=res.json()

    for key in json_data.keys():
        print(key," : ",json_data[key])
    print()

querystring = {"isDetails":"False"}

response = requests.request("GET", UPBIT_OPEN_API_SERVER_URL + "/v1/market/all", params=querystring)
for currency in response.json():
    if("KRW" in currency["market"]):
        market_info(currency["market"])
        time.sleep(1)
