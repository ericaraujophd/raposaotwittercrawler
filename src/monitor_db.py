
import mongodb_config as mdb
'''
This file verifies the collections and print the timestamps of the tweets found in the DB
'''

connect = mdb.connect(local=True)
db = mdb.create_db(connect,'RaposaocomPhD')

print('Current databases active: ', connect.list_database_names())
print('Current collections active: ', db.list_collection_names())

collnames = db.list_collection_names()

for coll in collnames:
	coll_data = list(db[coll].find())
	print('Collection {0} contains {1} tweets saved.'.format(coll,len(list(coll_data))))
	# for data in coll_data:
	# 	print(data['created_at'])