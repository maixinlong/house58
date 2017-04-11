import pymongo


def get_db():
    con = pymongo.MongoClient()
    return con.get_database('scrapy')['house58']