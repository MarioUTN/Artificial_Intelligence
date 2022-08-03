import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame({
    'Fname':['Harry','Sally','Paul','Abe','June','Mike','Tom'],
    'Age':[21,34,42,18,24,80,22],
    'Weight': [180, 130, 200, 140, 176, 142, 210],
    'Gender':['M','F','M','M','F','M','M'],
    'State':['Washington','Oregon','California','Washington','Nevada','Texas','Nevada'],
    'Children':[4,1,2,3,0,2,0],
    'Pets':[3,2,2,5,0,1,5]
})
print (df)

df.plot(kind='scatter', x='Age', y='Weight', color='red')
plt.show()

ax = plt.gca()
df.plot(kind='line',x='Fname',y='Children',ax=ax)
df.plot(kind='line',x='Fname',y='Pets', color='red', ax=ax)
df.plot(kind='line',x='Fname',y='Age', color='green', ax=ax)
df.plot(kind='line',x='Fname',y='Weight', color='gray', ax=ax)
plt.show()

df.plot(kind='bar',x='Fname',y='Age')
plt.show()

#pd = pd.to_numeric(df['Pets'], downcast='float')
print(np.array(df['Pets']))
print(np.array(df['Fname']))
plt.pie(df['Pets'], labels = df['Fname'], autopct="%0.1f %%")
plt.axis("equal")
plt.show()