##Text file (.txt)
##Ghi dữ liệu
# f = open('test_file.txt', 'w', encoding='utf-8')
# f.write("Muốn đứng hàng đầu thì chớ có đầu hàng\n")
# f.write("Muốn làm chuyện lớn thì chớ làm lớn chuyện\n")
# f.write("Hãy luôn chịu khó thay vì khó chịu!")
# f.close()

# with open('test_file.txt','a', encoding="utf-8") as f
#     f.write("Muốn đứng hàng đầu thì chớ có đầu hàng \n")
#     f.write("Muốn làm chuyện lớn thì chớ làm lớn chuyện \n")
#     f.write("Hãy luôn chịu khó thay vì khó chịu \n")

##Đọc dữ liệu
# f= open('test_file.txt','r', encoding = "utf-8")
# for line in f:
#     print(line.strip())
# f.close()
#
# with open('test_file.txt','r', encoding = "utf-8") as f:
#     print(f.read())


# from xml.dom.minidom import parse
# DOMTree = parse("products.xml")
# elements = DOMTree.documentElement
# products = elements.getElementsByTagName("product")
# for p in products:
#   pro_id = (p.getElementsByTagName("id")[0]).childNodes[0].data
#   pro_name = (p.getElementsByTagName("name")[0]).childNodes[0].data
#   pro_price = (p.getElementsByTagName("price")[0]).childNodes[0].data
#   print(pro_id + " -> " + pro_name + " -> " + pro_price)

# import xml.etree.ElementTree as ET
# import math
# tree = ET.parse("data/products.xml") # hoac ("data/product.xml")
# root = tree.getroot()
# print(f"Tag name: {root.tag}") # -> products
# print(f"Tag Attr: {root.attrib}")
#
# for child in root:
#   print(child.tag, child.attrib)
# print(root[1][2].text)
#
# for p in root.iter('products'):
#   print(p.attrib)
#
# for p in root.findall('products'):
#   p_id = p.find('id').text
#   p_name = p.get('name')
#   p_price = p.find('price').text
#   p_slogan = p.find('slogan').text
#   print(p_id + " - " + p_name + " - " + p_price + " - '" + p_slogan + "'")

import xml.etree.ElementTree as ET
tree = ET.parse("data/products.xml")
root = tree.getroot()
for slogan in root.iter('slogan'):
  formatted_slogan = slogan.text.title()
  slogan.text = formatted_slogan
  slogan.set('formatted', 'yes')
tree.write('new_products_updated.xml', encoding='utf-8')


# import json
# data = {'products': []}
# data['products'].append({
#   'name': 'Heineken',
#   'price': '$1.5',
#   'slogan': 'Chỉ Có Thể Là Heineken'
# })
# data['products'].append({
#   'name': 'Tiger',
#   'price': '$1.3',
#   'slogan': 'Tiger Beer - Bản Lĩnh Đàn Ông'
# })
# data['products'].append({
#   'name': 'Sapporo',
#   'price': '$1.4',
#   'slogan': 'Tận Hưởng Từng Khoảnh Khắc'
# })
# with open('data.txt', 'w', encoding='utf8') as outfile:
#   json.dump(data, outfile, ensure_ascii=False)
#
# import json
# with open('data.txt', encoding='utf8') as json_file:
#   data = json.load(json_file)
#   for p in data['products']:
#       print('Name: ' + p['name'])
#       print('Price: ' + p['price'])
#       print('Slogan: ' + p['slogan'])
#       print('')

# import json
# jsonObject = {
#   'name': 'Heineken',
#   'price': '$1.5',
#   'slogan': 'Chỉ Có Thể Là Heineken'
# }
# jsonString = json.dumps(jsonObject)
# print(jsonString)

# import json
# jsonObject = {
#   'name': 'Heineken',
#   'price': '$1.5',
#   'slogan': 'Chỉ Có Thể Là Heineken'
# }
# jsonString = json.dumps(jsonObject, ensure_ascii=False)
# print(jsonString)

# import json
# jsonObject = {
#   'name': 'Heineken',
#   'price': '$1.5',
#   'slogan': 'Chỉ Có Thể Là Heineken'
# }
# jsonString = json.dumps(jsonObject, ensure_ascii=False, indent=3)
# print(jsonString)


# import json
# import requests
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# # todos = json.loads(response.text)
# todos = response.json()
# print(todos[0])
# for t in todos[:2]:
#   jsonObj = json.dumps(t, ensure_ascii=False, indent=3)
#   print(jsonObj)

# import xmltodict, json
# obj = xmltodict.parse("""
# <employee>
#   <name>Khánh Hưng</name>
#   <role>Lập trình viên</role>
#   <age>30</age>
# </employee>
# """)
# print(json.dumps(obj, ensure_ascii=False, indent=3))
#
# import xmltodict, json
# with open("data/product.xml", "r", encoding="utf8") as f:
# obj = xmltodict.parse(f.read())
# print(json.dumps(obj, indent=3))