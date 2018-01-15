from pymongo import MongoClient
from os.path import expanduser

path = expanduser("~/.credentials/aerotropolis.txt")
mongo_connect = open(path, 'r')
ip, port, user, pwd = map(lambda x: x.strip(), mongo_connect.readlines())
ip = "localhost"
client = MongoClient(ip, int(port))


def connect_collection(document, source):
    """

    :source: str, the name of the desired collection in db
    """
    db = client["aerotropolis"]         
    db.authenticate(user, pwd)
    collection = eval("db." + source)
    collection.insert(document)

    return collection

