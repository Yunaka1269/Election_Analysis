#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#Assign a variable for the file to load and the path.
file_to_load='Resources/election_results.csv'
#open the election results and read the file
election_data=open(file_to_load,'r')

#to do: perform analysis

#close the file
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
     # To do: perform analysis.
     print(election_data)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter - this needs to be place above the code where we open the file because everytime we run the file the total votes must be set eaqual to zero.
total_votes=0
#declare a new list - candidate
candidate_options=[]
#declary the empty dictionary
candidate_votes={}
#winning candidate and winning count tracker --- declare a variable that holds an empty string value for the winning candidate. declare a variable for "winning count" and "winning_percentage" equal to zero
winning_candidate =""
winning_count=0
winning_percentage=0

# Open the election results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
        #for row in file_reader:
            # print(row)
    # Print the header row.
    headers = next(file_reader)
    # print each row in the CSV file.
    for row in file_reader:
        #add to the total vote count
        total_votes +=1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
        #add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
#save the results to our text file.
with open(file_to_save,"w") as txt_file:    
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results=(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    #print the winning candidate's results to the terminal         
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
