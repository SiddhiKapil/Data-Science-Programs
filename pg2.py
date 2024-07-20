# Histogram to check the frequency distribution
#  For the given dataset mtcars.csv (www.kaggle.com/ruiromanini/mtcars), plot a histogram to
#  check the frequency distribution of the variable ‘mpg’ (Miles per gallon)

import pandas as pd
import matplotlib.pyplot as plt

 # Load the dataset
mtcars = pd.read_csv('mtcars.csv')  # Replace 'path_to_your_mtcars.csv' with the ac

 # Plotting the histogram
plt.hist(mtcars['mpg'], bins=10, color='skyblue', edgecolor='black')

 # Adding labels and title
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title('Histogram of Miles per gallon (mpg)')

 # Displaying the plot
plt.show()