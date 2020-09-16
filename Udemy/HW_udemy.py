#import modules os to allow us to create file paths across operating systems
#csv to read csv files
import os
import csv

udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []
course_hours=[]

# with open(udemy_csv, newline=""?, encoding='utf-8') as csvfile:
with open(udemy_csv, newline="") as csvfile:
    #CSV reader specifies delimiter and variable that holds contents?
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
    
        #Title[1], Price[4], Subscribers[], Reviews[], Length[]
        # Add title (are columns still starting at 0 and why are we saying row when it is a column)
         title.append(row[1])
         course_hours.append(row[9])

        # Add price 
         price.append(row[4])

        # Add number of subscribers
         subscribers.append(row[5])

        # Add amount of reviews
         reviews.append(row[6])

        # Determine percent of review left to 2 decimal places
         percent = (int(row[6])/int(row[5])) * 100
         percent_decimal = (f"{percent:.2f}")
        
         review_percent.append(percent_decimal)

        # Get length of the course to just a number
        #Must import row as a variable as its type is a string
         length_string = row[9]
        #Can parse a string but apparently not a list?
         length_list = length_string.split(" ")
        #Now it's a list and we want the first value only 3.5 hours is now ('3.5', 'hours')
        #print(length_list[0]) (check point)
         length.append(length_list[0])

# Zip lists together
zipped_data = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(zipped_data)
