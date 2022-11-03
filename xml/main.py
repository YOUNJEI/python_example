import xml.etree.ElementTree as elemTree

tree = elemTree.parse('/Users/younjei/Desktop/CORPCODE.xml')
root = tree.getroot()

for child in root:
    print(child.find('corp_name').text)