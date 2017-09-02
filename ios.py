'''
Project: PayU Turkey IOS API Python3 Sample Code
Author: Göktürk Enez
'''
# Importing required libraries.
import hmac
import hashlib
from urllib.parse import urlencode
from urllib.request import Request, urlopen

#Endpoint
url = 'https://secure.payu.com.tr/order/ios.php'

#Secret Key
secret = 'SECRET_KEY'

array = {
'MERCHANT': 'OPU_TEST',
'REFNOEXT': '57786',
}
# Initializing the hashstring @param
hashstring = ''

# Sorting Array @params
for k, v in sorted(array.items()):

# Adding the length of each field value at the beginning of field value
    hashstring += str(len(v)) + str(v)
print(hashstring)

# Calculating ORDER_HASH
signature = hmac.new(secret.encode('utf-8'), hashstring.encode('utf-8'), hashlib.md5).hexdigest()

# Adding ORDER_HASH @param to request array
array['HASH'] = signature

print(signature)

# Sending Request to Endpoint
request = Request(url, urlencode(array).encode())
response = urlopen(request).read().decode()

# Printing result/response
print(response)

