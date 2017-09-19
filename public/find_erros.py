
arquivo1 = "contato.html"
arquivo2 = "index.html"


with open(arquivo1, 'rb') as a1:
	text1 = [x.decode('utf8').strip() for x in a1.readlines()]

with open(arquivo2, 'rb') as a2:
	text2 = [x.decode('utf8').strip() for x in a2.readlines()]


# for line1,line2 in zip(text1,text2):
# 	if line1 != line2:
# 		print("{} || {}".format(line1,line2))

text1 = " ".join(text1)
text2 = " ".join(text2)
tags = ['<html>', '<a', '<li', '<div', '<img', '<meta', '<nav', '<script']

def count_char(text,char):
	count = 0
	for c in text:
		if char == c:
			count += 1
	return count

def count_char1(text,char):
	count = 0
	for tags in text:
		if char in tags:
			count += 1
	return count

def count_letters(text,mode = None):
	for char in "abcdefghijklmnopqrstuvwxyz":
		if mode == 'perc':
		    percentual = 100 * count_char(text,char) / len(text)
		    percentual = round(percentual, 2)
		    yield "{0}:{1}%".format(char,percentual)
		else:
	         yield "{0}:{1}".format(char,count_char(text,char))

def count_tags(text,mode = None):
	for char in tags:
		if mode == 'perc':
		    percentual = 100 * count_char1(text,char) / len(text)
		    percentual = round(percentual, 2)
		    yield "{0}:{1}".format(char,percentual)
		else:
	         yield "{0}:{1}".format(char,count_char1(text,char))

for i in count_tags(text1):
	print(i)
