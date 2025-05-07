from pydantic import BaseModel

class PlantMatch(BaseModel):
    distance: float
    plant_index: int
    plant_name: str
    group: str
    compatibility: float
    image: str