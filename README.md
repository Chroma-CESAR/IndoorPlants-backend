# 🌿 IndoorPlants

A plant recommendation system based on user preferences and characteristics. Using machine learning, the system compares user input with a plant dataset and returns the top matching plants based on compatibility.

---

## 🧠 How It Works
- The user sends preferences to the /match endpoint.
- The system calculates Euclidean distances between user preferences and all plants in the dataset.
- The top 4 most compatible plants are returned based on a compatibility percentage.

## 🚀 API Endpoint

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/match` | Receives user data (apartment suitability, pet presence, experience level, availability, and preferred plant size) and returns a ranked list of up to 4 most compatible plants. |

### 📥 Request Payload Example

```json
{
  "ind_pets": true,
  "ind_apartment": true,
  "size_code": "Medium",
  "experience_level_code": "Beginner",
  "disponibility_level_code": "High"
}   
```

## 🧰 Technologies Used

| Technology       | Description                                   |
| ---------------- | --------------------------------------------- |
| **Python 3.11+** | Core language used for the application        |
| **FastAPI**      | Web framework for building asynchronous APIs  |
| **Uvicorn**      | ASGI server to run FastAPI applications       |
| **Pandas**       | Data manipulation and analysis                |
| **Scikit-Learn** | Data preprocessing and scaling                |
| **SciPy**        | Euclidean distance calculations using `cdist` |
| **Pydantic**     | Data validation and schema definition         |


## 🛠️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd IndoorPlants
```

### 2. Install Justfile and gum

- On macOS, you can use Homebrew to install Justfile and gum:

```bash
brew install just
brew install gum
```

- On Linux, you can use the following commands to install Justfile and gum:

```bash
sudo apt-get install just
sudo snap install gum
```

- On Windows, you can use the following commands to install Justfile and gum:

```bash
winget install --id Casey.Just --exact
winget install charmbracelet.gum
or
scoop install just
scoop install charm-gum
```

### 3. Install dependencies

```bash
just
```

Select the option `install-requirements` to install the required dependencies and create venv.

## 📁 Project Structure

📦 IndoorPlants
├── 📂 app
│ ├── 📂 datasets
│ │ └── 📄 plants_complete.csv
│ ├── 📂 pickles 
│ │ └── 📄 scaler.pkl
│ ├── 📂 schemas # Pydantic data models
│ │ ├── 📄 user_schema.py 
│ │ └── 📄 plant_match_schema.py 
│ └── 📂 services # Core service logic
│ └── 📄 calculate_distances.py
├── 📄 main.py # FastAPI app with POST /match endpoint
├── 📄 requirements.txt 
├── 📄 justfile # Task runner configuration
└── 📄 README.md 