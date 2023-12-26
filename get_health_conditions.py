# https://5jocnrfkfb.execute-api.us-east-1.amazonaws.com/PersonalRemedies/nutridigm/api/v2/healthconditions?subscriptionID=es5wxqHI6Szv_zRHl6S8k

import requests

url = "https://5jocnrfkfb.execute-api.us-east-1.amazonaws.com/PersonalRemedies/nutridigm/api/v2/healthconditions"

params = dict(
    'subscriptionID': 'es5wxqHI6Szv_zRHl6S8k'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response

print (data);