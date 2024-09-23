# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = []
candidate_votes = {}

# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        #print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
            
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    report = (
    f"Election Results\n"

    "-------------------------\n"

    f"Total votes:, {total_votes}\n"

    "-------------------------"
    )
    print(report)

    # Write the total vote count to the text file
    txt_file.write(report)

    # Loop through the candidates to determine vote percentages and identify the winner
    print("Candidates who received votes:")
    winning_candidate = ""
    winning_count = 0

    for candidate in candidates:
        

        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        percentage = (votes / total_votes) * 100
        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_report = f"{candidate}: {percentage:.3f}% ({votes})"
        print(candidate_report)
        txt_file.write(candidate_report + "\n")

    # Generate and print the winning candidate summary
    winning_report = (
        "-------------------------\n"
        f"Winner: {winning_candidate}\n"
        "-------------------------\n"
    )
    print(winning_report)   

    # Save the winning candidate summary to the text file
    txt_file.write(winning_report)