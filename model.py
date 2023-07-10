from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Utilisateur(BaseModel):
    id: str = None
    email : str
    password : str
    photo : str
    number : int

class Person(BaseModel):
    id:str = None
    name : str
    job: str


class Notification(BaseModel):
    id: str = None
    title:str 
    description : str


class Rule(BaseModel):
    id:str = None
    role_name= str
        
    

class Response(BaseModel):
    code : str
    status : str
    message : str
    result : Optional[T] = None    
