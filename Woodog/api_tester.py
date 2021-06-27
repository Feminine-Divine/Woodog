import requests
import json

URL="http://127.0.0.1:8000/contact/"
data_to_put={
    'name':'Nitin',
    'email':'Lets_grow_more@gmail.com',
    'contact_no':'9477655',
    'message':'we are enjoying this open source',
}
changed_tojson=json.dumps(data_to_put) # Changing a Python Object to json here !

R=requests.post(url=URL,data=changed_tojson) # this will also store the response if any from the backend server 

data=R
print(data)
# else:
#     print("not getting the data !")