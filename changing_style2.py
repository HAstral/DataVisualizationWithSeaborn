# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

survey_data=pd.read_csv('young-person-survey-responses.csv')
# # Set the context to "paper"
# sns.set_context("paper")
# # Change the context to "notebook"
# sns.set_context("notebook")
# # Change the context to "talk"
# sns.set_context("talk")
# Change the context to "poster"
sns.set_context("poster")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Show plot
plt.show()