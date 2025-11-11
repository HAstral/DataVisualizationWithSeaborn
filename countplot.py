# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd

countries = pd.read_csv('countries-of-the-world.csv')
region=countries['Region']
# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()
