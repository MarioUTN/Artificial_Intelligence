import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv("test_ETL.csv", encoding='utf-8', sep=',', header=0)
print(dataset.head(5))

dataset.plot(kind='bar',x='TOTAL_SESSIONS',y='ASSESSMENT_SESSION_COUNT')
plt.show()

dataset.plot(kind='bar',x='TITLE',y='TOTAL_SESSIONS')
plt.show()