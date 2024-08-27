## MovieLens-100K

![Python](https://img.shields.io/badge/Python-3.11+-brightgreen)
![Pandas](https://img.shields.io/badge/Pandas-v2.2.2-white)
![Seaborn](https://img.shields.io/badge/Seaborn-v0.13.2-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-v3.9.0-red)

A movie recommendation service

## Project Structure
- `data/ml-100k`: Full dataset from Kaggle.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model evaluation.
  - `prep_note.ipynb`: Starter import, merge and visual data, been reworked.
- `README.md`: Project overview and instructions.

## Data

# DETAILED DESCRIPTIONS OF DATA FILES
Here are brief descriptions of the data.

ml-data.tar.gz -- Compressed tar file. To rebuild the u data files do this:
gunzip ml-data.tar.gz
tar xvf ml-data.tar
mku.sh

u.data -- The full u data set, 100000 ratings by 943 users on 1682 items.
Each user has rated at least 20 movies. Users and items are
numbered consecutively from 1. The data is randomly
ordered. This is a tab separated list of
user id | item id | rating | timestamp.
The time stamps are unix seconds since 1/1/1970 UTC

u.info -- The number of users, items, and ratings in the u data set.

u.item -- Information about the items (movies); this is a tab separated.

## Getting Started

### Prerequisites

Make sure you have the following libraries installed:
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

You can install them using:
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
```
