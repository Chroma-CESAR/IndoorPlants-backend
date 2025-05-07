import pandas as pd
from scipy.spatial.distance import cdist
import pickle
from app.schemas.plant_match_schema import PlantMatch
from app.schemas.user_schema import UserData



def calculate_distances(new_user_data:UserData, scaller_local:str) -> list[PlantMatch]:
    """
        Calculates the compatibility distances between a new user's preferences and a dataset of plants.
        This function normalizes the user's data using a pre-trained scaler, computes the Euclidean distances
        between the user's preferences and the dataset, and ranks the plants based on compatibility percentage.
        Args:
            new_user_data (UserData): An object containing the new user's preferences. It must be convertible to a dictionary.
            scaller_local (str): The file path to the pre-trained scaler object (pickle file) used for normalization.
        Returns:
            list[PlantMatch]: A list of PlantMatch objects representing the top 4 most compatible plants, 
            sorted by compatibility percentage in descending order. Only plants with a compatibility percentage 
            greater than 0 are included.
        Raises:
            FileNotFoundError: If the scaler file or the dataset file is not found.
            ValueError: If there is an issue with the data transformation or distance calculation.
    """
    
    with open(scaller_local, 'rb') as file:
        scaler = pickle.load(file)

    data_complete = pd.read_csv('./app/datasets/plants_complete.csv')

    data = data_complete[['ind_pets', 'ind_apartment', 'size_code', 'experience_level_code', 'disponibility_level_code']]
    
    new_user = pd.DataFrame([new_user_data.model_dump(mode="json")]) # new_user_data precisa ser umm Dict

    new_user_normalized = scaler.transform(new_user)


    distances = cdist(new_user_normalized, data, metric='euclidean')

    distances_df = pd.DataFrame(distances.T, columns=['Distance'])
    distances_df['Plant Index'] = data.index
    distances_df['Plant Name'] = data_complete.loc[data_complete.index, 'name'].values
    distances_df['Group'] = data_complete.loc[data_complete.index, 'group_name'].values
    distances_df['Image'] = data_complete.loc[data_complete.index, 'img_url'].values

    distances_df['Compatibility Percentage'] = round(100 - (distances_df['Distance'] / distances_df['Distance'].max() * 100), 0)
    distances_df = distances_df.sort_values(by='Compatibility Percentage', ascending=False).head(4)

    ranking = [
        PlantMatch(
            distance=row['Distance'],
            plant_index=row['Plant Index'],
            plant_name=row['Plant Name'],
            group=row['Group'],
            compatibility=row['Compatibility Percentage'],
            image=row['Image']
        )
        for _, row in distances_df.iterrows()
        if row['Compatibility Percentage'] > 0
    ]

    return ranking