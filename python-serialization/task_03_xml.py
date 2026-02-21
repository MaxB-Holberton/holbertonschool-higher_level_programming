#!/usr/bin/env python3
"""
    Module with the functions to convert xml to python dicts
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
	"""
		function to create XML file from dictionary
	"""
	root_tag = ET.Element("data")

	for key, value in dictionary.items():
		ET.SubElement(root_tag, key).text = str(value)

	xml_file = ET.ElementTree(root_tag)
	xml_file.write(filename)


def deserialize_from_xml(filename):
	"""
		function to create dictionary from XML file
	"""
	new_tree = ET.parse(filename)
	new_root = new_tree.getroot()
	dictionary = {}

	for item in new_root:
		dictionary[item.tag] = item.text

	return dictionary
