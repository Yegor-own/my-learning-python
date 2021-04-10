import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Restaurant.csv')

fig = plt.figure()
axes = fig.add_axes([0, 0, 2, 1])
axes.scatter(x = df['total_bill'], y = df['tip'], marker = '+', color = 'black')
axes.set_title('The total amount of order Vs Amount of tip')
axes.set_ylabel('Amount of bill')
axes.set_xlabel('Amount of tip')
