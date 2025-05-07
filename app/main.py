from app.schemas.user_schema import UserData
from app.schemas.plant_match_schema import PlantMatch
from app.services.calculate_distances import calculate_distances
from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.post("/match")
async def calculate(user: UserData):
    """
    Calculates and returns a ranking based on the user's data.
    This asynchronous function takes user data as input, processes it using a pre-trained scaler 
    loaded from a pickle file, and calculates distances to generate a ranking.
    Args:
        user (UserData): An object containing the user's data required for the calculation.
    Returns:
        list: A ranking list generated based on the calculated distances.
    Raises:
        Exception: For any other errors that occur during the calculation process.
    """
    try:
        pickle_file = 'app/pickles/scaler.pkl'

        ranking = calculate_distances(user, pickle_file)
        return ranking
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail=f"An error as occured: {str(e)}")
