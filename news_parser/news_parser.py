import xml.etree.ElementTree as ET
import codecs
import chardet # импортируем модуль для авто-определения кодировки текстового файла

# windows 1251, iso 8859-5, koi8-r, koi8-u
# unknown windows 866
# self windows 1252 
#file = open('newsfr.xml', 'r')

def code_detecter(path_to_file_text):
	with open(path_to_file_text, 'rb') as source: # бинарное чтение
		lines = source.read()
		result = chardet.detect(lines)
		if result['encoding'] is None:
			raise Exception("Неизвестная кодировка файла!")
		else:	
			return result['encoding']

# print(doc.read())
encoding = code_detecter('newsfr.xml')
print(encoding)

import xml.etree.ElementTree as ET
file = codecs.open('newsfr.xml', mode = 'r', encoding = encoding)
#print(file, encoding)

content_file = "".join([line for line in file.readlines()])
root = ET.fromstring(content_file)

# tree = ET.parse(file)
#xml_string = ET.tostring(tree, encoding = encoding, method = 'xml')
#xml_tree = ET.fromstring(xml_string)
#root = tree.getroot()
print(root)
for element in root.iter(tag = 'description'):
	# print(element.tag, element.attrib)
	print(element.text)  # тут выводим описание каждой новости в файле


# for child in root:
# 	#print(child.tag, child.attrib)
# 	for grandchild in child.findall('item'):
# 		print(grandchild.tag, grandchild.attrib)
# 		for g_grandchild in grandchild.findall('description'):
# 			xml_string = ET.tostring(g_grandchild, encoding = encoding, method = 'xml')
# 			xml_element = ET.fromstring(xml_string)
# 			print(xml_element.tag, xml_element.attrib)
# 			print(xml_element.text)
			 



# with open('newsfr.xml') as file:
# 	root = ET.fromstring(country_data_as_string)
#	print(code_detecter(file))

#with codecs.open('newsfr.xml') as file:
#	tree = ET.parse(file)

#file = codecs.open('newsfr.xml', mode = 'r', encoding = 'windows 1252')
#tostr = ET.tostring(file, )
	
    #print(tree)
#root = tree.getroot()
    #for element in tree.iter(tag='description'):
	#    print(element.text)


	

