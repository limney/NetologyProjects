#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET


a = ET.Element('a')
b = ET.SubElement(a, 'b')
b.text = "dgdfg"
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')

ET.dump(a)
