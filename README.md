# Movie_Recommender_System
<p>Content-based movie recommender system using Python, employing machine learning techniques to suggest movies based on user preferences and movie attributes.This project implements a movie recommender system using Python and Streamlit. It leverages machine learning techniques to suggest similar movies based on user preferences and movie attributes. The recommender system is built using the TMDB dataset, which contains information about movies, including genres, keywords, cast, crew, and overviews.</p>

# Project Structure
* MovieRecommenderSystem.ipynb: Jupyter Notebook containing data preprocessing, feature engineering, and model building steps.<br>
* recommender.py: Python file containing the Streamlit web application code.<br>
* movies_dict.pkl: Pickle file storing the processed movie data.<br>
* similarity.pkl: Pickle file storing the cosine similarity matrix for the movie recommendations.<br>
* gitignore: File specifying files and directories to be ignored by version control.<br>
* procfile: File specifying the command to run the web application on Heroku.<br>
* requirements.txt: File listing the project dependencies.<br>
* setup.sh: Shell script to set up the required environment.<br>

# How to Run the Project
* Start by running the Jupyter Notebook MovieRecommenderSystem.ipynb, which contains the data preprocessing and feature engineering steps. It processes the data, extracts relevant information, and prepares the dataset for the recommender system.

* Generate the movies_dict.pkl and similarity.pkl files using pickle.dump() in the Jupyter Notebook. These files store the necessary data and the cosine similarity matrix for the recommender system.

* The core machine learning code for the recommender system is encapsulated in the recommender.py file. The Streamlit web application is built using this code. The recommender.py file handles user input, retrieves recommendations, and displays them on the interface.

* To deploy the movie recommender system on Heroku, create a Heroku account and follow the instructions to create a new app. Connect your GitHub repository with the Heroku app for seamless deployment.

* Once the project is deployed on Heroku, users can access the Movie Recommender System by visiting the provided URL. They can select a movie from the dropdown list and click the 'RECOMMEND' button to receive five similar movie recommendations.

* Feel free to explore and enjoy personalized movie recommendations through the interactive interface! For any questions or issues, please refer to the project's documentation or reach out to the project contributors.

# Skills Exhibited
* Data Analysis and Exploratory Data Analysis (EDA)<br>
* Feature Engineering<br>
* Machine Learning<br>
* Python Programming<br>
* File Handling (Pickle)<br>
* Web Development using Streamlit<br>
* Deployment on Heroku<br>
* Data Visualization<br>
* Data Preprocessing<br>
* Version Control (Git)<br>
* Documentation and Readme Writing<br>
* Problem Solving and Troubleshooting<br>

# Snapshots
<img src="https://github.com/EnigmaOfData/Movie_Recommender_System/blob/main/MovieRecommender.PNG" alt="Snapshots" width="800" height="400">
