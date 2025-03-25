# California-Housing-Prices-Prediction

A machine learning project that predicts housing prices in California using historical data. This project demonstrates data cleaning, exploratory data analysis (EDA), feature engineering, model training, and evaluation using Python libraries.

## Table-of-Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Dataset Description](#dataset-description)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Project Insights](#project-insights)
- [Future Improvements](#future-improvements)
- [Acknowledgments](#acknowledgments)
- [License](#license)

## Overview

In this project, we build and evaluate predictive models to estimate housing prices in California. The goal is to use various features (such as median income, housing median age, total rooms, and location) to predict the median house value in different regions.

Key steps include:
- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA) to uncover trends and patterns
- Feature engineering to enhance model performance
- Building regression models (e.g., Linear Regression, Decision Trees, and Ensemble methods)
- Evaluating model performance using metrics like RMSE

This project is ideal for showcasing skills in data analysis, machine learning, and Python programming.

## Technologies Used

- **Python 3.x**
- **Pandas** – for data manipulation and cleaning
- **NumPy** – for numerical operations
- **Scikit-learn** – for model building and evaluation
- **Matplotlib** & **Seaborn** – for data visualization
- **Jupyter Notebook** – for interactive coding and analysis

## Dataset Description

The dataset used in this project contains various attributes of California housing areas including:
- **Median Income**
- **Median House Value**
- **Housing Median Age**
- **Total Rooms**
- **Total Bedrooms**
- **Population**
- **Households**
- **Latitude and Longitude**

This dataset is publicly available and is a popular benchmark for housing price prediction tasks.

## Installation and Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DiaHere/California-Hosuing-Prices-Prediction.git
   cd California-Hosuing-Prices-Prediction
   jupyter notebook
   
## Usage

- **Exploratory Data Analysis:** Open the notebook EDA.ipynb to see how the data was visualized and preprocessed.

- **Model Training:** Check out model_training.ipynb for code related to building, training, and evaluating different regression models.

- **Results:** The notebooks include visualizations of model performance and key insights from the data analysis.

Feel free to modify the code, experiment with different models, or add additional features to improve predictions.

## Project Insights
- Data Insights: Initial EDA revealed strong correlations between median income and house value. Other features, such as location, also played a significant role.

- Model Performance: Ensemble methods, such as Random Forest, showed improved performance over simpler linear models.

- Challenges: Handling missing values and ensuring the model generalizes well on unseen data were key challenges during the project.

## Future Improvements
1. Explore additional feature engineering techniques.

2. Experiment with hyperparameter tuning to further boost model performance.

3. Integrate cross-validation to ensure model robustness.

4. Deploy the model as a web application using frameworks like Flask or Django.

## Acknowledgments
Thanks to the open data community for providing the California housing dataset.

Inspired by several tutorials and articles on machine learning and data science.

## License
This project is licensed under the MIT License.

---

