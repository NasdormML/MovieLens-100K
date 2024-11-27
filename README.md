# MovieLens-100K Dataset: Collaborative Filtering Recommender System

![Python](https://img.shields.io/badge/Python-3.11-brightgreen)
![PySpark](https://img.shields.io/badge/PySpark-3.4.1-orange)
![LightGBM](https://img.shields.io/badge/LightGBM-3.3.5-blue) 


## Overview
This project builds a hybrid recommendation system using the MovieLens 100k dataset. By combining collaborative filtering (ALS algorithm) with content-based features and a machine learning model (LightGBM), the system achieves an RMSE of **0.6625**, significantly outperforming the standalone ALS model. The hybrid approach integrates user-item interactions with metadata like genres and movie popularity for enhanced recommendation accuracy.

---

## Key Features
- **Collaborative Filtering**: Implemented the ALS algorithm to generate user-item recommendations.
- **Hybrid Model**: Integrated ALS predictions with movie metadata (genres and popularity) to train a LightGBM model.
- **Hyperparameter Tuning**: Optimized ALS parameters (rank, max iterations, regularization) using cross-validation.
- **Weighted Time Decay**: Incorporated timestamp-based weights to prioritize recent interactions.
- **Genre Analysis**: Leveraged movie genres as additional content-based features.

---

## Results
- **Hybrid Model RMSE**: 0.6625 (on test data).
- **Improvement**: The hybrid system reduces error by approximately 14%, demonstrating the value of combining collaborative and content-based approaches.

---

## Tools & Technologies
- **Programming Languages**: Python (PySpark, LightGBM, Pandas, NumPy)
- **Libraries**: PySpark MLlib, LightGBM, Scikit-learn
- **Tools**: Jupyter Notebook
- **Dataset**: [MovieLens 100k](https://grouplens.org/datasets/movielens/100k/)

---

## How to Run
### Prerequisites
- Install Python and the required libraries:
  ```bash
  pip install pyspark lightgbm pandas numpy scikit-learn
  ```

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/MovieLens-100k-Recommender.git
   cd MovieLens-100k-Recommender
   ```
2. Download the MovieLens 100k dataset from [here](https://grouplens.org/datasets/movielens/100k/) and place it in the `data/` directory.
3. Open the notebooks in the `notebooks/` directory:
   - `EDA.ipynb`: Exploratory analysis, and filtering.
   - `ALS.ipynb`: ALS model training, hybrid integration, and recommendations.

---

## Data
- **Source**: [MovieLens 100k Dataset](https://grouplens.org/datasets/movielens/100k/)
- **Files Used**:
  - `u.data`: Ratings data containing user, movie, rating, and timestamp.
  - `u.item`: Movie metadata with genres, titles, and release dates.
- **Key Features**:
  - **Ratings**: User-movie interactions with timestamps.
  - **Genres**: Binary indicators for 19 genres.
  - **Popularity**: Calculated as the number of ratings per movie.
  - **Weighted Time Decay**: Derived feature to prioritize recent ratings.

---

## Project Structure
```
MovieLens-100k-Recommender/
├── data/                            # MovieLens dataset files
│     ├── u.data                     # Ratings data
│     └── u.item                     # Movie metadata
├── notebooks/
│     ├── EDA.ipynb                  # Data preparation and EDA
│     └── ALS.ipynb                  # ALS and hybrid model training
├── README.md                        # Project overview and instructions
├── requirements.txt                 # Dependencies and libraries
```

---

## Business Value
- **Improved Recommendations**: By combining collaborative filtering and content-based data, the hybrid model enhances recommendation accuracy.
- **Personalized Experiences**: Tailored suggestions for individual users increase satisfaction and engagement.
- **Actionable Insights**: Analyzing movie genres and popularity provides additional value to content curators and platforms.
