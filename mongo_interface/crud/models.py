from pymongo import MongoClient
from django.conf import settings

client = MongoClient('mongodb://localhost:27017')
db = client['mai_example']

class Student:
    collection = db["students"]

    @staticmethod
    def create(name, faculty):
        return Student.collection.insert_one({"name": name, "faculty": faculty})

    @staticmethod
    def read_all():
        return Student.collection.find()

    @staticmethod
    def read_one(student_id):
        return Student.collection.find_one({"name": student_id})

    @staticmethod
    def update(student_id, name, faculty):
        return Student.collection.update_one({"name": student_id}, {"$set": {"name": name, "faculty": faculty}})

    @staticmethod
    def delete(student_id):
        return Student.collection.delete_one({"name": student_id})
