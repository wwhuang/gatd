import pymongo
import time
from bson.json_util import dumps

DATABASE          = 'getallthedata'
TABLE_UNFORMATTED = 'unformatted_archive'
TABLE_FORMATTED   = 'formatted_data'
TABLE_CONFIG      = 'configuration'
MONGO_HOST  = 'inductor.eecs.umich.edu'
MONGO_PORT  = 19000


def mineData(query=None, host=MONGO_HOST, port=MONGO_PORT, table=TABLE_FORMATTED, sort_key=None):
	client = pymongo.MongoClient(host, port)
	db = client[DATABASE]
	t = db[table]

	if not query:
		return dumps(t.find_one())

	if sort_key:
		data = t.find(query).sort(sort_key)
	else:
		data = t.find(query)

	return dumps(data)

