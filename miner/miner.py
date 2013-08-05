import pymongo
import time
from bson.json_util import dumps

DATABASE          = 'getallthedata'
TABLE_UNFORMATTED = 'unformatted_archive'
TABLE_FORMATTED   = 'formatted_data'
TABLE_CONFIG      = 'configuration'

def mineData(query, host="localhost", port=18222, sort_key=None):
	client = pymongo.MongoClient(host, port)
	db = client[DATABASE]
	if sort_key:
		data = db.find(query).sort(sort_key)
	else:
		data = db.find(query)

	return dumps(data)
