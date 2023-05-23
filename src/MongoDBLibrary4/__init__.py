from .mongo_connection_manager import MongoConnectionManager
from .mongoquery import MongoQuery
from .version import VERSION


class MongoDBLibrary(MongoConnectionManager, MongoQuery):
    """
    MongoDB Library contains utilities meant for Robot Framework's usage.
    
    This can allow you to query your Mongo database after an action has been made to verify the results.

    References:
    
     + PyMongo Documentation - https://pymongo.readthedocs.io/en/stable/api/index.html
     
    Example Usage:
        | Connect To MongoDB | foo.bar.org | ${27017} |
        | ${QueryJSON}  | Set Variable | {"name" : "username" ,"in_use": false} |
        | ${UpdateJSON} | Set Variable | {"$set": {"in_use" : true}} |
        | &{allResults} | Retrieve and Update One Mongodb Record | DBName | CollectionName | ${QueryJSON} | ${UpdateJSON} |
        | Log | ${allResults} |
    """
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION
