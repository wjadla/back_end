from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Utilisateur(BaseModel):
    id: str = None
    email : str
    password : str
    photo : str
    number : int

class Book(BaseModel):
    id:str = None
    title : str
    description: str
    

class Response(BaseModel):
    code : str
    status : str
    message : str
    result : Optional[T] = None    
