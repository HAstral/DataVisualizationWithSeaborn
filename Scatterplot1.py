# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

countries = pd.read_csv('countries-of-the-world.csv')
# countries['Literacy (%)'] = pd.to_numeric(countries['Literacy (%)'], errors='coerce')
gdp=countries['GDP ($ per capita)']
phones=countries['Phones (per 1000)']
percent_literate=countries['Literacy (%)']
# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x=gdp,y=phones)

plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()

