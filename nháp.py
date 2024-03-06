import xml.etree.ElementTree as ET
import math
tree = ET.parse("./data/products.xml") # hoac ("data/products.xml")
root = tree.getroot()
print(f"Tag name: {root.tag}") # -> products
print(f"Tag Attr: {root.attrib}")