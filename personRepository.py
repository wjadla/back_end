from model import Person
from config import database
import uuid

class PersonRepo():
    


    @staticmethod
    async def retrieve():
          _person = []
          collection = database.get_collection('person').find()
          async for person in collection:
               _person.append(person)
               return _person
          


    @staticmethod
    async def isnert(person : Person):
         id = str(uuid.uuid4())
         _person= {
              "id": id,
              "name": person.name,
              "password": person.password,
              "job": person.job
         }     

         await database.get_collection('person').update_one({"id": id}, {"$set":_person})


    @staticmethod
    async def retrieve_id(id:str):
         return await database.get_collection('person').find_one({"_id":id})


    @staticmethod
    async def delete(id:str):
         return await database.get_collection('person').delete_one({"id":id})      
