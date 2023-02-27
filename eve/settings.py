MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'ProjectDiamondTeam1DB2022'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {

    'id': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
	'unique': True,
    },
    'activityDescription': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'timestamp': {
        'type': 'string',
    },
    'pass': {
        'type': 'boolean',
    },
}



logs = {
    'item_title': 'log',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'id'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET','DELETE','POST'],

    'schema': schema
}

DOMAIN = {
    'logs': logs,
}


