import os
import csv

os.chdir(os.path.dirname(__file__))
# set csv path and file location
csv_path = os.path.join("..", "Resources", "budget_data.csv")
output_txt_file = os.path.join("..", "Resources", "budget_data_text.txt")

total_num_month = 0
total_profit_loss = 0
profit_loss_changes = []
avg_profit_loss = 0
greatest_increase = 0
greatest_decrease = 0
greatest_inc_date = ""
greatest_dec_date = ""

# open csv file and read till next line empty
with open (csv_path, newline="" ) as csv_file:
    # read csv file with comma delimeter
    read_csv = csv.reader(csv_file, delimiter=",")
    # skip header, first row of csv file 
    header = next(read_csv)

    # loop all the row's in the csv file    
    for row in read_csv:
        # get total number of month
        total_num_month = total_num_month + 1   
        # get total profit and locess over entire period
        total_profit_loss = total_profit_loss + int (row[1])
        
        #profit_loss_changes  = int(row[row]) - prev_profit_loss
        #prev_profit_loss = int(row[row]) 
        #prev_profit_loss.append(int(row[row])
    #avg_profit_loss = sum(profit_loss_changes) / len(profit_loss_changes)

        # get the max profit / losses
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_inc_date = row[0]
        # get the min profit / losses
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_dec_date = row[0]

    avg_profit_loss = int(total_profit_loss)/ int(total_num_month)

    # print all the values    
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_num_month))
    print("Total Revenue: " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(round(avg_profit_loss)))
    print("Greatest Increase in Profits: " + str(greatest_inc_date) + " ($" +  str(greatest_increase) + ")") 
    print("Greatest Decrease in Profits: " + str(greatest_dec_date) + " ($" +  str(greatest_decrease) + ")")


   # print to the text file
   # open file to write
with open (output_txt_file, "w" ) as txt_file:
    txt_file.write("Financial Analysis")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_num_month))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(avg_profit_loss)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_inc_date) + " ($" +  str(greatest_increase) + ")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(greatest_dec_date) + " ($" +  str(greatest_decrease) + ")")
