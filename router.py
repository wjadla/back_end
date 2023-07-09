from fastapi import FastAPI,APIRouter
from repository import UtilisateurRepo
from model import Utilisateur,Response
router = APIRouter()



@router.get("/utilisateur/")
async def utilisateur():
    _utilisateurList = await UtilisateurRepo.retrieve()
    return Response(code =200, status ="OK", message="success retrieve of data", result =_utilisateurList).dict(exclude_none=True)


@router.post("/utilisateur/create")
async def create(utilisateur: Utilisateur):
    await UtilisateurRepo.insert(utilisateur)
    return Response(code =200, status ="OK",message="success create user").dict(exclude_none=True)



@router.get("/utilisateur/{id}")
async def get_id(id:str):
     _utilisateur = await UtilisateurRepo.retrieve_id(id)
     return Response(code =200, status ="OK", message="success retrieve user").dict(exclude_none=True)


@router.post("utilisateur/update")
async def update(utilisateur: Utilisateur):
    await UtilisateurRepo.update(utilisateur.id, utilisateur)
    return Response(code =200, status ="OK", message="succes update user").dist(exclude_noe=True)




@router.delete("/utilisateur/{id}")
async def delete(id: str):
    await UtilisateurRepo.delete(id)
    return Response(code=200, status ="OK",message="deleted user with succes")
