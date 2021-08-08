import pandas as pd
import statistics
import matplotlib.pyplot as plt

# 1. Read the csv file
csv_file_path = 'sales.csv'
df = pd.read_csv(csv_file_path)

# 2. Print list of sales from each month
monthly_sales = df[["month", "sales"]]

# 3. Output monthly sales statistics to Excel
stats = monthly_sales.describe()
stats.to_excel('sales_stats.xlsx')

# 3. Total sales
total_sales = sum(df["sales"])

# 4. Average sales
average_sales = statistics.mean(df["sales"])

# 5. Minimum sale
lowest_sale = monthly_sales.to_records()
minimum = min(lowest_sale, key=lambda month: month[-1])

# 6. Maximum sale
highest_sale = monthly_sales.to_records()
maximum = max(highest_sale, key=lambda month: month[-1])

# 7. Output percentage difference in sales
percentage_sales = df["sales"].pct_change()
percentage_sales = df.set_index('month')
percentage_sales = df.drop(["year", "sales", "expenditure"], axis = 1)

# 8. Add monthly profit column to CSV
df = pd.read_csv('sales.csv')
df['Profits'] = df['sales'] - df['expenditure']
profits_list = df['Profits']
profits_list = df.set_index('month')
profits_list = df.drop(["year", "sales", "expenditure", "Percentage difference"], axis = 1)
df.to_csv("sales.csv",index=False)


# 9. Data visualisation using matplotlibs
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
plt.savefig('my_graph.png')

# 12. Ask user for what data they want to see
user_request = input("Which of the following data points would you like to see (type in a number between 1 - 7):\n1. List of sales from each month \n2. Total sales \n3. Average sales \n4. Minumum sales \n5. Maximum sales\n6. Plot monthly sales and expenditure\n7. List of monthly profit\n")
if user_request == "1":
    print(monthly_sales)
elif user_request == "2":
    print("Total sales:", total_sales)
elif user_request == "3":
    print("The average monthly sales is", round(average_sales))
elif user_request == "4":
    print("The month with the lowest number of sales is {}".format(minimum['month']),"with {} sales!".format(minimum['sales']))
elif user_request == "5":
    print("The month with the highest number of sales is {}".format(maximum['month']),"with {} sales!".format(maximum['sales']))
elif user_request == "6":
    print(plt.show())
elif user_request == "7":
    print(profits_list)
else:
    print("Your request doesn't exist! Try again by picking a number between 1 and 5")