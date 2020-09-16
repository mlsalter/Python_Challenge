#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 00:46:56 2019

@author: MichelleW
"""

# -*- coding: UTF-8 -*-
"""PyPoll Homework Solution."""

# Incorporated the csv module
import csv
import os

# Files to load and output (Remember to change these)
election_data = os.path.join("Resources", "election_data.csv")
voter_output = os.path.join("analysis", "election_analysis.txt")

#Counters
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_count = 0
winning_candidate = ""

# Read in the csv file
with open(election_data) as votefile:
    reader = csv.reader(votefile)
    
   #Run loader animator
    print(".", end="")
    #Read the header
    header = next(reader)
   
    
    #VoterID[0], County[1], Candidate[2]
    #loop through rows
    for row in reader:
        
        #Calculate total voters
        total_votes = total_votes + 1
        
        #Get candidates' names and assign names column to a variable
        candidate_name = row[2]
        
        #To add to candidate_options we don't want doubles so conditional with appending and start vote_count_can[]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes.update({candidate_name:0})
        
        #If candidate is already in candidate_options then we need to add 1 vote to their count
        else:
            candidate_votes[candidate_name] += 1
#            candidate_votes.update({candidate_name:(x + 1)}) (I was so freaking close!!!!! like I was so on the right path!!!)
    
with open(voter_output, "w") as txt_file:
    
    #Print final vote count to terminal
    final_vote_count =(
            f"\nElection Results\n"
            f"----------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"----------------------------\n")
    
    print (final_vote_count)
    
    #Save final vote count to txt_file
    txt_file.write(final_vote_count)
        
    # Determine the winner by looping through the counts
    for candidate in candidate_options:
        
        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = (float(votes) / float(total_votes)) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        # Print each candidate's voter count and percentage to terminal
        candidate_output = (f"\n{candidate}: {vote_percentage:.3f}% ({votes})\n")
        
        print (candidate_output) #, end=""
        
        #Save candidate's voter count and percentage to txt_file
        txt_file.write(candidate_output)

    # Print the winning candidate (to terminal)
    winner_output = (
            f"\n----------------------------\n"
            f"Winner: {winning_candidate} {winning_count}\n"
            f"----------------------------\n")
    print (winner_output)
    
    txt_file.write(winner_output)



    
