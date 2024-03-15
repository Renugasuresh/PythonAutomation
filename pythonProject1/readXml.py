import xml.etree.ElementTree as ET
file=open("C:\\Users\\renug\\OneDrive\\Documents\\sample.xml","r+")
xml_string=file.read()
tree=ET.fromstring(xml_string)
comments=tree.find('comments')
sum=0
for c in comments.findall('comment') :
    print(c.find('count').text)
    sum=sum+int(c.find('count').text)
print(sum)

