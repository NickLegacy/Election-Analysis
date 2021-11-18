# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
total_cvotes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# 2: Track the largest county and county voter turnout.
winning_county = ""
county_vote = 0
win_percentage = 0
win_count = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        total_cvotes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # 3: Extract the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    print("County Votes:")



    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_options:

        # 6b: Retrieve the county vote count.
        cvotes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        cvote_percentage = float(cvotes) / float(total_cvotes) * 100
        county_results = (
            f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")

         # 6d: Print the county results to the terminal.
        print(county_results, end="")

         # 6e: Save the county votes to a text file.

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (cvotes > county_vote) and (cvote_percentage > win_percentage):
            county_vote = cvotes
            winning_county = county_name
            win_percentage = cvote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"

        f"-------------------------\n")
    print(winning_county_summary)    

    # 8: Save the county with the largest turnout to a text file.


    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)