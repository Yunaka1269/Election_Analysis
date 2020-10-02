#Election Analysis

##Project Overview and Election-Audit Results

The election commission has requested additional data to futher analyze the local election. 
Following are the complete tasks of the project and election results

1. Calculate the total number of votes 

	-Total votes: 369,711

2. Breakdown of the percentage of total votes and the number of votes for each county 

	-Jefferson: 10.5% (38,855)
	
	-Denver: 82.8% (306,055)
	
	-Arapahoe: 6.7% (24,801)

3. Determine the county with the highest votes

	-The largest county turnout: Denver

4. Breakdown of the percentage of total votes and the number of votes for each candidate

	-Charles Casper Stockham: 23.0% (85,213)
	
	-Diana DeGette: 73.8% (272,892)
	
	-Raymon Anthony Doane: 3.1% (11,606)

5. Determine the winning candidate

	-Winner: Diana DeGette
	
	-Vote count: 272,892
	
	-Vote percentage: 73.8%

###Resources
- Data Source: election_result.csv
- Software: Python 3.8.5 , Visual Studio Code 1.49.2

##Summary

Depending on the dataset structure, you may modify the index number (hardcode or use of variable) in "candidate_name=[2]" and "county_name=[1]" for any election. 
We can also declare more list and dictionary to track additional information such as age, gender, ...etc and add another set of **for** loop and **if** statement to deeper analysis of election (see below).

        ####create list/dictionary
	-create an empty list and dictionary
		candidate_options = []
		candidate_votes = {}
		county_options=[]
		county_votes={}

	-Track the winning candidate, vote count and percentage
		winning_candidate = ""
		winning_count = 0
		winning_percentage = 0

	-Track the largest county and county voter turnout.
		winning_county=""
		winning_turnout=0
		winning_c_percentage=0

        ####calculating votes
	-Total candidate and county votes
	-use for loop to extract candidate name and county name by index number
		candidate_name=[2]
		county_name=[1]
	-within for loop, make candidate and county list if the name does not match any existing one in the list, then calculate vote counts
		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name]=0
			candodate_votes[candidate_name]+=1
		if county_name not in county_options:
			county_options.append(county_name)
			county_votes[county_name]=0
			county_votes[county_name]+=1 
        ####output
	-use f-string to format and display the election result 
		election_results = (
        		f"\nElection Results\n"
        		f"-------------------------\n"
        		f"Total Votes: {total_votes:,}\n"
        		f"-------------------------\n"
        		f"\nCounty Votes:\n")
    		print(election_results, end="")
	-use for loop to get the county name from the county dictionary then calculate county votes and its percentage
		for county_name in county_votes:
			c_votes=county_votes[county_name]
        		c_vote_percentage=float(c_votes) / float(total_votes)*100
	-use f-string to format and display the county results
		county_results=(f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        	print(county_results)
	-determine the winning county
		if(c_votes>winning_turnout) and (c_vote_percentage>winning_c_percentage):
            	winning_county=county_name
            	winning_turnout=c_votes
	-use f-string to format and display the winning county
		county_results=(
   		        f"\n-------------------------\n"
        		f"Largest County Turnout: {winning_county:}\n"
        		f"-------------------------\n")
    		print(county_results)	
	-use for loop to get candidate name from the candidate dictionary then calculate the number of votes and percentage
		for candidate_name in candidate_votes:
        		votes = candidate_votes.get(candidate_name)
        		vote_percentage = float(votes) / float(total_votes) * 100 
	-use f-string to format and display candidate results
		candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
		print(candidate_results)
	-determine winning candidate
		if (votes > winning_count) and (vote_percentage > winning_percentage):
            	winning_count = votes
            	winning_candidate = candidate_name
            	winning_percentage = vote_percentage
	-use f-string to format and display the winning candidate summary
		winning_candidate_summary = (
        	f"-------------------------\n"
        	f"Winner: {winning_candidate}\n"
        	f"Winning Vote Count: {winning_count:,}\n"
        	f"Winning Percentage: {winning_percentage:.1f}%\n"
        	f"-------------------------\n")
    		print(winning_candidate_summary)
