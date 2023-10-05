
#import modules
import csv
import os

#Row[0]=date
#Row[1]=Profit/losses

#file path
file_path = './Resources/budget_data.csv'

#setting storage for variables
month_count=0 #counter for total months
total_prof_loss=0 #counter for the total of profit aand losss
val_total=0 #set the column to integer
change=0 #counter for the change
dates=[]#list to stotage the dates
profits=[]#list to storage the profits and losses

#read the file
with open(file_path,newline="") as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")
   
    #reading the heaader to skip it
    header=next(csvreader)
    #go to first row
    row=next(csvreader)

    month_count+=1

    #print (('Total Months:'),month_count)

    

    total_prof_loss+=int(row[1])
    val_total=int(row[1])

    for row in csvreader:
        dates.append(row[0])

    #count months
        month_count += 1

    #sum prof_loss column    

        change=int(row[1])-val_total
        profits.append(change)
        val_total=int(row[1])

        total_prof_loss=total_prof_loss + int(row[1])

    #average of the changes in "profit/losses"
        avg_change=sum(profits)/len(profits)

    #The greatest increase in profits (date and amount) over the entire period    
        gi= max(profits)
        gi_index= profits.index(gi)
        gidate=dates[gi_index]
        #The greatest decrease in profits (date and amount) over the entire period
        gd= min(profits)
        gd_index= profits.index(gd)
        gddate=dates[gd_index]

    results=(
        f"Financial Analysis\n"
        f"-------------------------------------\n"
        f"Total Months: {str(month_count)}\n"
        f"Total: ${str(total_prof_loss)}\n"
        f"Average Change: ${str(round(avg_change,2))}\n"
        f"Greatest Increase in Profits: {gidate} (${str(gi)})\n"
        f"Greatest Decrease in Profits: {gddate} (${str(gd)})\n"
        )
    

    print(results)

    #export

    file= os.path.join('analysis','PyBank_Results.txt')
    PyBankResults= open(file, 'w')

    line1 = "Financial Analysis"
    line2 = "------------------------------------------"
    line3 = str(f"Total Months: {str(month_count)}")
    line4 = str(f"Total: ${str(total_prof_loss)}")
    line5 = str(f"Average Change: ${str(round(avg_change,2))}")
    line6 = str(
        f"Greatest Increase in Profits: {gidate} (${str(gi)})")
    line7 = str(
        f"Greatest Decrease in Profits: {gddate} (${str(gd)})")
    PyBankResults.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
        line1, line2, line3, line4, line5, line6, line7))


    



