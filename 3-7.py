# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
# 4 3 1

def vlozh(elem, lvl=1):
    if elem.tag == 'cube' and elem.attrib['color'] in dd.keys():
        dd[elem.attrib['color']] += lvl
        # print(lvl, elem.tag, elem.attrib['color'])
    for child in elem.getchildren():
        vlozh(child, lvl+1)


from xml.etree import ElementTree as ET

cd = ['red', 'green', 'blue']
dd = {'red': 0, 'green': 0, 'blue': 0}
root = ET.fromstring(input())

# print(root)
# print(root.tag, root.attrib)
# for child in root:
#     print(child.tag, child.attrib)
# for element in root.iter("cube"):
#     print(element.attrib)

vlozh(root)
print(dd['red'], dd['green'], dd['blue'])