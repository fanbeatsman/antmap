#from __future__ import print_function

#from __future__ import unicode_literals
# -*- coding: UTF-8 -*-
from docx import *
import sys
import os
import re

document = Document('antdata.docx')

tables = document.tables
i = 0
for table in tables:

	x = 0
	y = 0
	p = 0
#document.tables[i].cell(x,y).paragraphs[p].text != None



	while True:
		try:
			test_end = document.tables[i].cell(x,y).paragraphs[p].text
			p=0	
			while True:

				try:
					paragraphs = document.tables[i].cell(x,y).paragraphs

					for paragraph in paragraphs:
					
						print (u"paragraph {0}:   {1}".format(p, document.tables[i].cell(x,y).paragraphs[p].text).encode('UTF-8'))
						p = p+1

					x=x+1
					print ("----------------y+1------------------")
					p=0
				except IndexError:
					x=0
					break
		except IndexError:
			break
		p=0
		y = y + 1
		print ("-----------------------x+1----------------------------")
	i = i + 1

print ("REACHED").encode('UTF-8')
