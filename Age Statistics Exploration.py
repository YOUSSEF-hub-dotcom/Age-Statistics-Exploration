from statistics import variance
import scipy.stats as stats
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.width',None)

df = pd.read_csv(r"C:\Users\sara\Downloads\Student_performance_data _.csv")
print(df)

# How many times appear data unique in column Age
freq_table = df['Age'].value_counts().reset_index()
freq_table.columns = ['Age','Frequency']

freq_table['Relative Frequency'] = freq_table['Frequency'] / freq_table['Frequency'].sum()
#freq_table['Relative Frequency'] * 100
freq_table['Percentage (%)'] = (freq_table['Frequency'] / freq_table['Frequency'].sum()) * 100

freq_table['Central Angle'] = (freq_table['Percentage (%)'] / 100 ) * 360

freq_table['Cumulative Frequency'] = freq_table['Frequency'].cumsum()

freq_table['Cumulative Relative Frequency'] = freq_table['Cumulative Frequency'] / freq_table['Frequency'].sum()

freq_table['Cumulative Percentage'] = freq_table['Cumulative Relative Frequency'] * 100

freq_table = freq_table.sort_values(by = 'Age')
print(freq_table)

print("----------------------------------")

plt.bar(freq_table['Age'],freq_table['Frequency'],color='green')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Frequency Distribution ')
plt.show()


print("-----------------------------------")
plt.figure(figsize=(6, 6))
plt.pie(freq_table['Percentage (%)'],labels=freq_table['Age'],autopct='%1.1f%%',colors=['lightblue', 'lightgreen','lightcoral','lightskyblue'],startangle=140)
plt.title('Percentage Distribution')
plt.show()

mean_value = df['Age'].mean()
median_value = df['Age'].median()
mode_value = df['Age'].mode()[0]

variance_value = df['Age'].var()
std_dev_value = df['Age'].std()
range_value = df['Age'].max() - df['Age'].min()

print(f"Mean:{mean_value}")
print(f"Median:{median_value}")
print(f"Mode:{mode_value}")
print(f"Variance:{variance_value}")
print(f"Standard Deviation:{std_dev_value}")
print(f"Range:{range_value}")
print('=============================================================================================================')