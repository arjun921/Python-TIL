open_file = open('file.txt','r')

line = open_file.readline()
while line:
	print(line)
	line = open_file.readline()
