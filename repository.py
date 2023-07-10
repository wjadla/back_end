from model import Utilisateur
from config import database
import uuid

class UtilisateurRepo():
   



    @staticmethod
    async def retrieve():
        _utilisateur = []
        collection = database.get_collection('utilisateur').find()
        async for utilisateur in collection:
            _utilisateur.append(utilisateur)
        return _utilisateur

    @staticmethod
    async def insert(utilisateur : Utilisateur):
        id = str(uuid.uuid4())
        _utilisateur = {
            "id": id,
            "email": utilisateur.email,
            "password":utilisateur.password,
            "photo": utilisateur.photo,
            "number": utilisateur.number
        }    

        await database.get_collection('utilisateur').insert_one(_utilisateur)

    @staticmethod
    async def update(id:str, utilisateur:Utilisateur):
        _utilisateur = await database.get_collection('utilisateur').find_one({"_id":id}) 
        _utilisateur["email"] = utilisateur.email
        _utilisateur["password"] = utilisateur.password
        _utilisateur["photo"] = utilisateur.photo
        _utilisateur["number"] = utilisateur.number
        await database.get_collection('utilisateur').update_one({"id":id},{"$set":_utilisateur})


    @staticmethod
    async def retrieve_id(id:str):
        return await database.get_collection("utilisateur").find_one({"_id":id})    

    @staticmethod
    async def delete(id:str):
        await database.get_collection('utilisateur').delete_one({"id":id})       