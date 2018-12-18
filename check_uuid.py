
#!python

file_input = open('uuid.json', 'r')


from pymongo import MongoClient
client = MongoClient('mongo-gce', 201)

db = client['client']
users = db.user
import pprint

ids = []
count = 0

def check_uuid():
	lines_id = file_input.readlines()
	for i in lines_id:
		if pprint.pprint(users.find_one(i)):
			ids.append(i)
			count = count + 1
	with open('uuid_results.json', 'w') as file_output:
		for item in ids:
			file_output.write('%s\n' % item)

	n = lines_id.__len__()
	ls = []
	ls.append(n)
	ls.append(count)
	print(ls) 

check_uuid()