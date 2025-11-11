# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

countries = pd.read_csv('countries-of-the-world.csv')
# countries['Literacy (%)'] = pd.to_numeric(countries['Literacy (%)'], errors='coerce')

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x='GDP ($ per capita)',y='Phones (per 1000)',data=countries)

plt.show()

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x='GDP ($ per capita)', y='Literacy (%)',data=countries)

# Show plot
plt.show()

