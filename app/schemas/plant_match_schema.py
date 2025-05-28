from pydantic import BaseModel

class Plant(BaseModel):
    index: int
    family: str
    categories: str
    origin: str
    climate: str
    img_url: str
    name: str
    water_category: str
    venomous: bool
    size: str
    soil: str
    sunlight: str
    experience_level: float
    group_name: str
    compatibility: float

class PlantMatch(Plant):
    distance: float