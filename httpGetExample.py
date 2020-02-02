# You'll need to setup Python and import the root certificats for HTTPS requests
# From the Python 3.7 Documentation
# This module defines classes which implement the client side of the HTTP and HTTPS protocols.
# It is normally not used directly — the module urllib.request uses it to handle URLs that use HTTP and HTTPS.
# This would be a better way: https://docs.python.org/3/library/urllib.request.html#module-urllib.request
import http.client
conn = http.client.HTTPSConnection("random-word-api.herokuapp.com")
conn.request("GET","/word?key=BFX7ES4V&number=2")
r1 = conn.getresponse()
#Clear the screen - Worked on MacBook
print('\033c')
print(r1.status, r1.reason)
data1 = r1.read()
print(data1)
print()
