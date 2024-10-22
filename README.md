## MovieLens-100K Dataset: Collaborative Filtering Recommender System

![Python](https://img.shields.io/badge/Python-3.11-brightgreen)
![Surprise](https://img.shields.io/badge/Surprise-1.1.4-lightblue)
![Seaborn](https://img.shields.io/badge/Seaborn-v0.13.2-red)

## Overview
This project utilizes the **MovieLens-100K dataset** to build a movie recommendation system. The goal is to predict user preferences and recommend movies based on their past behavior using collaborative filtering techniques.

The project explores matrix factorization methods and evaluates the performance using relevant metrics. Optional extensions may include content-based filtering and hybrid recommendation approaches.

---

## Dataset
The **MovieLens-100K dataset** contains:
- **100,000 ratings** for **1,682 movies** by **943 users**.
- Ratings are provided on a scale from 1 to 5.
- The dataset includes metadata like movie titles and genres.

The dataset can be downloaded from [here](https://grouplens.org/datasets/movielens/100k/).

---

## Project Structure

```bash
├── data/
│      └──ml-100k                            # Datasets used in the project
├── notebooks/
│     ├──EDA.ipynb                          # Jupyter notebooks with EDA
│     └──test_build.ipynb                   # Slim build for starting
├── README.md                               # Project overview and setup
└── requirements.txt                        # Dependencies and libraries
```

---

## Technologies Used
- **Python** for data processing and implementation.
- **Pandas** and **NumPy** for data manipulation.
- **Scikit-learn** for model evaluation and metrics.
- **Surprise** or **LightFM** for collaborative filtering models.
- **Matplotlib** and **Seaborn** for data visualization.
- **Optuna** for hyperparameter tuning (optional).

---

## Project Structure
- **Data Preprocessing**: Load and clean the dataset, handle missing data, and preprocess the ratings and movie metadata.
- **Exploratory Data Analysis (EDA)**: Visualize user and movie rating distributions, correlations, and trends.
- **Collaborative Filtering**: Build user-based and item-based collaborative filtering models using matrix factorization techniques.
- **Evaluation**: Use metrics like **RMSE** and **MAE** to evaluate recommendation quality.
- **Optional**: Implement content-based or hybrid recommendation approaches.

---

## Implementation Steps
1. **Data Loading**: Load the MovieLens-100K dataset and preprocess it by handling missing values and duplicates.
2. **EDA**: Analyze the data to understand user preferences and trends in movie ratings.
3. **Collaborative Filtering**:
   - Use matrix factorization techniques like **SVD** to decompose the user-item matrix.
   - Calculate cosine similarity for user-based and item-based recommendations.
   - Train a model to predict movie ratings for unseen movies.
4. **Evaluation**:
   - Use **RMSE**, **MAE**, and top-N precision/recall to evaluate the recommendations.
   - Compare different models to determine the best approach.
5. **Hyperparameter Tuning** (Optional): Tune model parameters with **Optuna** or **GridSearchCV**.
6. **Generate Recommendations**: Provide a list of recommended movies for users.

---

## Results
Present the evaluation metrics and examples of recommendations for individual users. Discuss model performance and any insights gained from the results.

---

## Future Work
- **Content-Based Filtering**: Leverage movie metadata (genres, directors) to improve recommendations.
- **Hybrid Models**: Combine collaborative filtering with content-based approaches to mitigate the cold-start problem.
- **Scalability**: Explore scaling the system for larger datasets or incorporating real-time recommendation capabilities.
