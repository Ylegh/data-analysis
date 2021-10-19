import pandas as pd
import statistics
from UliPlot.XLSX import auto_adjust_xlsx_column_width
from pyfiglet import Figlet
from termcolor import colored

# 1. Read the csv file
csv_file_path = 'sales.csv'
df = pd.read_csv(csv_file_path)

# Formatting
header = Figlet(font="colossal")
print(colored(header.renderText("Your data report"),"green"))

space = '-----------------------------------------------------------------'
print(space)
title = "Total sales by month:"
print(title)

# 2. Print list of sales from each month
monthly_sales = df[["month", "sales"]]
print(monthly_sales.to_string(index=False))
border = '-----------------------------------------------------------------'
print(border)

# 3. Output monthly sales statistics to Excel
title = "Statistics by month:\n"
print(title)
stats = monthly_sales.describe()
print(round(stats))
stats.to_excel('sales_stats.xlsx')
border = '-----------------------------------------------------------------'
print(border)

# 4. Total sales
total_sales = sum(df["sales"])
print('Total sales across all months: £{}'.format(total_sales))
border = '-----------------------------------------------------------------'
print(border)

# 5. Average sales
average_sales = statistics.mean(df["sales"])
print('Average monthly sales: £{}'.format(round(average_sales)))
border = '-----------------------------------------------------------------'
print(border)

# 6. Minimum sale
lowest_sale = monthly_sales.to_records()
minimum = min(lowest_sale, key=lambda month: month[-1])
print("The month with lowest sales is {}".format(minimum['month']))
border = '-----------------------------------------------------------------'
print(border)

# 7. Maximum sale
highest_sale = monthly_sales.to_records()
maximum = max(highest_sale, key=lambda month: month[-1])
print("The month with highest sales is {}".format(maximum['month']))
border = '-----------------------------------------------------------------'
print(border)

# 8. Output percentage difference in sales
title = 'Percentage difference month on month:\n'
print(title)
percentage_sales = df["sales"].pct_change()
percentage_sales = df.set_index('month')
percentage_sales = df.drop(["year", "sales", "expenditure", "Profits"], axis = 1)
print(percentage_sales.to_string(index=False))
border = '-----------------------------------------------------------------'
print(border)

# 9. Add monthly profit column to CSV
title = 'Monthly profit:\n'
print(title)
df = pd.read_csv('sales.csv')
df['Profits'] = df['sales'] - df['expenditure']
profits_list = df['Profits']
profits_list = df.set_index('month')
profits_list = df.drop(["year", "sales", "expenditure", "Percentage difference"], axis = 1)
df.to_csv("sales.csv",index=False)
print(profits_list)
border = '-----------------------------------------------------------------'
print(border)

# 10. Output summary to Excel spreadsheet
data = {"Lowest Sales":[minimum], "Highest Sales":[maximum], "Sales Average":[average_sales], "Sales Total":[total_sales]
        }
df1 = pd.DataFrame(data, columns=['Lowest Sales','Highest Sales','Sales Average', 'Sales Total'])
sum_row = df1.sum()
title = 'Data summary:\n'
print(title)
print(sum_row)

writer = pd.ExcelWriter('final_data.xlsx', engine='xlsxwriter')
df1.to_excel(writer, sheet_name='Data Summary', index = False)


workbook = writer.book #Access the workbook
worksheet= writer.sheets['Data Summary'] #Access the Worksheet

header_list = df.columns.values.tolist() #Generate list of headers
for i in range(1, len(header_list)):
    worksheet.set_column(i, i, len(header_list[i])) #Set column widths based on len(header)
writer.save()

# adding changes as a test
