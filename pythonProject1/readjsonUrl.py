import json
import urllib.request, urllib.parse, urllib.error
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

address=input("Enter Url")
uh=urllib.request.urlopen(address,context=ctx)
data=uh.read()
print(data)

info=json.loads(data)
sum=0
for c in info["comments"]:
    x=c["count"]
    sum=sum+x
print(sum)

