# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "employee_data.csv")
file_to_output = os.path.join("output", "employee_data_reformatted.csv")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    #ID0, Name1, DOB2, SSN3, State4
    # Loop through each row, re-grab each field and store in a new list
    for row in reader:

        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row[0]]

        # Grab names, split them, and store them in a temporary variable
        split_name = row[1].split(" ")
#        print(split_name)

        # Then save first and last name in separate lists
        emp_first_names.append(split_name[0])
        emp_last_names.append(split_name[1])

        # Grab DOB and reformat it
        #Then store it into a list
        dob_split = row[2].split("-")
        dob_new = (f"{dob_split[1]}/{dob_split[2]}/{dob_split[0]}")
        emp_dobs.append(dob_new)

        # Grab SSN and reformat it
        # then store it in a list       
        ssn_split = row[3].split("-")
 #       print(ssn_split)
        ssn_new = (f"***-**-{ssn_split[2]}")
        emp_ssns.append(ssn_new)

        # Grab the states and use the dictionary to find the replacement
        # Then store the abbreviation into a list
#        state_list = row[4]
        state_list = us_state_abbrev.get(row[4], row)
#        print(state_list)
        emp_states.append(state_list)


# Zip all of the new lists together
zipped_data = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)


#  Open the output file
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(zipped_data)