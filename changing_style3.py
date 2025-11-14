# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

survey_data=pd.read_csv('young-person-survey-responses.csv')
# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
custom_palette=['#39A7D0','#36ADA4']
sns.set_palette(custom_palette)
# Create the box plot of age distribution by gender
sns.catplot(x="Gender", y="Age", 
            data=survey_data, kind="box")

# Show plot
plt.show()