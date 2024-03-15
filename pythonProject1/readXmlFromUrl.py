import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

address=input("Enter Url")
uh=urllib.request.urlopen(address,context=ctx)
data=uh.read()
print(data)

tree=ET.fromstring(data)
comments=tree.find('comments')
sum=0
for c in comments.findall('comment') :
    print(c.find('count').text)
    sum=sum+int(c.find('count').text)
print(sum)

