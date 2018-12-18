
#!python3


file_input = open('uuid.json', 'r')


set1 = set()
set2 = set()
def check_uuid():
	for line in f1:
		set1.add(line.strip())
	for line1 in f2:
		set2.add(line1.strip())
	for line2 in set1 - set2:
		f3.write(line2 + "\n")
			


check_ip()