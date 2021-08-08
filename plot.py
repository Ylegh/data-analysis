import main
import pandas as pd
import matplotlib.pyplot as plt

# 11. Data visualisation using matplotlibs
df = pd.read_csv('sales.csv')

month = df['month']
sales = df['sales']
expenditure = df['expenditure']

plt.figure('Graph 1')
plt.subplot(2,1,1)
plt.title('Monthly sales and expenditure')

plt.plot(month, sales, label = "sales")
plt.plot(month, expenditure, label = "expenditure")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig('my_graph.png')


