#Import useful packages
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns

listings_data = pd.read_csv('data/listings.csv', header = 0)
reviews_data = pd.read_csv('data/reviews.csv', header = 0)

list_of_col1 = ['id', 
                'review_scores_rating']
list_of_col2 = ['listing_id', 'comments']

home_scores = listings_data[list_of_col1].dropna()
listings_and_reviews = pd.merge(reviews_data, home_scores, left_on = "listing_id", right_on = "id")
home_comments = listings_and_reviews[list_of_col2].dropna().set_index('listing_id')

for i in list_of_col1[1:]:
    print("############  " + i + "  ############")
    print(home_scores.groupby(i).size())