# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import median function from numpy
from numpy import median
student_data=pd.read_csv('student-alcohol-consumption.csv')

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,estimator=median)

# Show plot
plt.show()