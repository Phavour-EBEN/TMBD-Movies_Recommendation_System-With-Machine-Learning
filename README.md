# Movie Recommendation System

This project is a **Movie Recommendation System** built using **cosine similarity** to recommend movies based on a user's input. The system suggests movies that are most similar to a given movie using data from a pre-processed movie dataset.

## Features
- **Input:** Movie title provided by the user.
- **Output:** List of 5 movies similar to the input movie based on cosine similarity.
- **API-based interaction:** You can interact with the system through a REST API.

## Project Structure
```
.
├── app.py               # Flask application (API)
├── recommendation_engine.py  # Recommendation logic
├── new_dataset.csv      # Pre-processed dataset containing movie information
├── cosine_matrix.npy    # Precomputed cosine similarity matrix
├── README.md            # Project description and instructions
└── requirements.txt     # Python dependencies
```

## How to Use

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2. Install dependencies:
Make sure you have Python 3.x installed. Install the required dependencies with:

```bash
pip install python
pip install flask
```

### 3. Run the Application:
To start the Flask API, use the following command:

```bash
python app.py
```

The app will run locally at `http://127.0.0.1:5000/`.

### 4. Using the API:
You can use Postman or `curl` to interact with the recommendation API.

#### **Endpoint:**
- **URL:** `http://127.0.0.1:5000/api/recommend`
- **Method:** POST
- **Content-Type:** `application/json`

#### **Request Body:**
Provide a JSON object with the `movie_name` key:
```json
{
  "movie_name": "Batman"
}
```

#### **Example `curl` Request:**
```bash
curl -X POST http://127.0.0.1:5000/api/recommend \
-H "Content-Type: application/json" \
-d '{"movie_name": "Inception"}'
```

#### **Response:**
The API will return a list of 5 recommended movies:
```json
{
  "movie_name": "Batmna",
  "recommendations": [
        "Batman",
        "Batman & Robin",
        "Batman Begins",
        "Batman Returns",
        "The Dark Knight Rises"]
}
```

### 5. Customization:
- To change the dataset or modify the recommendation logic, edit the `recommendation_engine.py` file.
- You can replace `new_dataset.csv` with another dataset, but make sure to preprocess the data and compute a cosine similarity matrix.

## Dataset
- The system uses a pre-processed movie dataset (`new_dataset.csv`) containing movie titles and other relevant information.
- A **cosine similarity matrix** (`cosine_matrix.npy`) is precomputed based on the movie feature vectors.

## Future Enhancements
- Add collaborative filtering or hybrid recommendation approaches.
- Implement user-based recommendations.
- Improve the dataset with additional metadata (e.g., genres, directors).

## Contributing
Feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License.
