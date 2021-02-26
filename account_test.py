import os
import jwt
import json
import uuid
import hashlib
from urllib.parse import urlencode

import requests

UPBIT_OPEN_API_ACCESS_KEY=open("UPBIT_OPEN_API_ACCESS_KEY.cfg","r").read()
UPBIT_OPEN_API_SECRET_KEY=open("UPBIT_OPEN_API_SECRET_KEY.cfg","r").read()
UPBIT_OPEN_API_SERVER_URL="https://api.upbit.com"

payload = {
    'access_key': UPBIT_OPEN_API_ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, UPBIT_OPEN_API_SECRET_KEY)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(UPBIT_OPEN_API_SERVER_URL + "/v1/accounts", headers=headers)

for currency in res.json():
    for key in currency.keys():
        print(key," : ",currency[key])
    print()
#깃허브 실험
