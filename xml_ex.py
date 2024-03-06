import xml.etree.ElementTree as ET
import math
tree = ET.parse("./data/products.xml") # hoac ("data/products.xml")
root = tree.getroot()
print(f"Tag name: {root.tag}") # -> products
print(f"Tag Attr: {root.attrib}")

print("****"*7)

for child in root:
    print(f"ChildTag: {child.tag}, ChildAttr:{child.attrib}")

print(root[1][2].text)
print(root[2][1].text)
print(root[0][1].text)

print("****"*7)
for productNode in root.iter("product"): #lấy ra tất cả các thẻ có tên product
    print(productNode.tag)
print("****"*7)
for productNode in root.iter("product"): #lấy ra tên sản phẩm
    print(productNode[1].text)
print("****"*7)
for productNode in root.iter("product"): #lấy ra tên sản phẩm + giá
    print(productNode[1].text + " - " + productNode[2].text)

print("****"*7)
for productNode in root.findall("product"): #lấy ra tất cả các thẻ có tên product
    print(productNode.tag)
#iter tìm tất cả các cặp thẻ có tên product tận gốc tìm hết, findall tìm các thẻ con cấp 1

print("****"*7)
for productNode in root.findall("product"):
    #print(productNode[1].text)
    print(productNode.find("name").text)
    print(productNode.find("price").text)
print("****"*7)
for nameNode in root.iter("name"):
    modifiedName = nameNode.text.upper()
    nameNode.text = modifiedName
    nameNode.set("formated", "yes")
tree.write("data/new_file.xml", encoding= "utf-8")

#Chuyển giá sp sang usd
for priceNode in root.iter("price"):
    changePrice = int(priceNode.text)/23000
    priceNode.text = "$" + str(round(changePrice,2))
    priceNode.set("changed", "yes")
tree.write("data/price_file.xml", encoding= "utf-8")