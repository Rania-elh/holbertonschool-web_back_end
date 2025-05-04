#!/usr/bin/env python3
""" Commentaire encore"""


def update_topics(mongo_collection, name, topics):
    """ Toujours """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
