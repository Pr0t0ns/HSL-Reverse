# Made by Pr0t0n

import jwt # 2 less imports (pip install pyjwt)
from datetime import datetime

def generate_hsl(jwt_token: str): # around 50 less lines of code with unnecessary hashing (I read line by line and it's all useless)
    data = jwt.decode(jwt_token, options={"verify_signature": False}) # decodes json web token to get values
    return ":".join([ #":".join to add : after every list value
     "1", # always 1
      str(data['s']), # s value in decoded JWT
  str(datetime.fromtimestamp(int(data['e'])).isoformat().replace("-", "").replace("T", "").replace(":", "")), # h0nde never used the unix timestamp provided in the decoded JWT token LOL
      data['d'], # d value in decoded JWT token
      "", # blank so .join can add two :: 
      "1" # this is the value h0nde made all that unnecessary code for 
    ])
