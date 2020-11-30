###############################################################################
##################### Send POST request to non csrf domain ####################
############### Tested against Django server with csrf disabled ###############
###############################################################################

import requests

url = 'http://localhost:8000/domains'
myobj = {'keywords': 'name, slate'}

response = requests.post(url, data=myobj)
print(response.text)