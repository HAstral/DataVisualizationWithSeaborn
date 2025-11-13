# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

student_data=pd.read_csv('student-alcohol-consumption.csv')
# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet",y="G3",data=student_data,kind='box',hue='location',sym='')






# Show plot
plt.show()