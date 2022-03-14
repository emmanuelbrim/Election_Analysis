#Add our dependencies
import csv
import os
#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign variable to save file
file_to_save = os.path.join("Analysis", "election_analysis")
#initialize a total vote counter
total_votes = 0
#Create Candidate list
candidate_options = []
#Create a dictionary to hold candidates votes
candidate_votes = {}
#Wining Candidate and Wining count Tracker
winning_Candidate = ""
winning_count = 0
winning_percentage = 0
#Open and read election results file
with open(file_to_load) as election_data:
#To do: Read and analyze the data
#Read the file object with the reader function
    file_reader = csv.reader(election_data)
#Read the header row
    header = next(file_reader)
#Print each row in the CSV file 
    for row in file_reader:
#Increase the total votes counter
        total_votes +=1
        #Print the candidate names from each row
        candidate_name = row[2]
        #If statement for Candidate Names
        if candidate_name not in candidate_options:
            #Add the candidate name to candidate list
            candidate_options.append(candidate_name)
            #Track Each candidate's votes
            candidate_votes[candidate_name]=0
            #Add a vote to candidates count
        candidate_votes[candidate_name]+=1
        #Save results to text file
    with open(file_to_save,"w") as txt_file:
            #Print the final vote count to the terminal
            election_results = (
                f"\nElection Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes:,}\n"
                f"---------------------------\n")
            print(election_results, end="")
            txt_file.write(election_results)
            #iterate through the candidate list
            for candidate_name in candidate_votes:
                #Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
                #Calculate the percentage of votes
                vote_percentage = float(votes) / float(total_votes) * 100
                candidate_results=(f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')
                #Print each candidate, their voter count and percentage
                print(candidate_results)
                #save the candidates results to our text file
                txt_file.write(candidate_results)
                #Determine wining vote count and candidate
                if(votes>winning_count) and (vote_percentage > winning_percentage):
                    winning_count = votes
                    winning_percentage = vote_percentage
                    winning_candidate = candidate_name
                #Print winning candidates' results                    
                winning_candidate_summary = (
                            f"---------------------\n"
                            f'Winner: {winning_candidate}\n'
                            f'Winning Vote Count: {winning_count:,}%\n'
                            f"Wining Percentage: {winning_percentage:.1f}%\n"
                            f"---------------------------\n")
                print(winning_candidate_summary)
            txt_file.write(winning_candidate_summary)
        