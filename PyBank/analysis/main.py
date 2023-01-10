# Import the os module
import os

# Module for reading CSV files
import csv

#budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
budget_csv = "/Users/damilolashobo/Desktop/Rice Uni /Instructions 2/PyBank/Resources/budget_data.csv"
print(budget_csv)

# Use CSV module

with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents 
    csv_reader = csv.reader(csvfile, delimiter=',')

    print(csv_reader)

    def net_profit(revenues,expenses):
        net_profit = sum(revenues) - sum(expenses)
        return net_profit



    from datetime import datetime

    # Represents a record in the dataset
    records = [
        {'date': 'Jan-10'},
        {'date': 'Feb-10'},
        {'date': 'Mar-10'},
        {'date': 'Apr-10'},
    ]

    months = set()

    # Loop through records and extract the month from data 
    for record in records:
        date = datetime.strptime(record['date'], '%m-%Y')
        month = date.month
        months.add(month)

    # Print total number of months
    print(len(months))

    # Calculate changes in profit
    changes = [net_profit[i+1] - net_profit[i] for i in range(len(net_profit)-1)]

    #Calculate average change in profit
    average_change = sum(changes)/len(changes)

    print(average_change)


    max_increase = 0
    start_index = 0
    end_index = 0

    for i in range(1, len(net_profit)):
        increase = net_profit[i] - net_profit[i-1] 

        if increase > max_increase:
            max_increase = increase
            start_index = i-1
            end_index = i
        
    print("The greatest increase in profits over the entire period was:", max_increase)
    print()

    

        






            


        

            






    



