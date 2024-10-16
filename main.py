import sys 
import os

#import csp.py

class lesson():
	def __init__(self,semester,name,teacher,difficult,lab):
		self.semester=semester
		self.name=name
		self.teacher=teacher
		self.difficult=difficult
		self.lab=lab

	def getsemester(self):
		return semester
	def getname(self):
		return name
	def getteacher(self):
		return teacher
	def getdifficulty(self):
		return difficult
	def getlab(self):
		return lab


def readfile(datapath):                                     
	fstream=open(datapath,'r');                        
	dataset=[]										
	line = fstream.readline();
	flag=True;
	while flag:
		line = fstream.readline();
		if line in ['\n', '\r\n','']:
			flag=False
			break
		word=line.split(',')
		word[4]=word[4].rstrip("\n")
		dataset.append(word)
	fstream.close();
	return dataset;


dataset=readfile("Στοιχεία Μαθημάτων.csv")
print (dataset)

