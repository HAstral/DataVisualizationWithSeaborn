# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load student data
student_data = pd.read_csv('student-alcohol-consumption.csv')

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            col='study_time')

# Show plot
plt.show()

# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter",
            row='study_time')

# Show plot
plt.show()