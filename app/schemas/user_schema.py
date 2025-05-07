from pydantic import BaseModel, Field
from enum import Enum

class Size(Enum):
    Small = 0
    Medium = 1
    Big = 2
    Very_Big = 3

class ExperienceLevel(Enum):
    Beginner = 0
    Amateur = 1
    Experienced = 2

class DisponibilityLevel(Enum):
    Low = 0
    Medium = 1
    High = 2

class UserData(BaseModel):
    ind_pets: bool = Field(..., description="Indica se o usuário tem pets em casa")
    ind_apartment: bool = Field(..., description="Indica se a planta é adequada para apartamentos")
    size_code: Size = Field(..., description="Tamanho da planta")
    experience_level_code: ExperienceLevel = Field(..., description="Nível de experiencia com cuidar de plantas")
    disponibility_level_code: DisponibilityLevel = Field(..., description="Nível de disponibilidade")