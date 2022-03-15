# ELECTION ANALYSIS 
_An Audit of Election Results with Python_


## Overview of the Project
Every group have established way by which individuals are selected to represent it in matters of concern. Popular among these ways is Universal Adult suffrage and its within this contest of elections specifically the popular vote system that this project worked on.
The purpose of this project was to develop a system using python, that will analyze recent congressional election results of 3 candidates and provide valid information on which the Colorado Board of Elections will act. 

## Election Audit Results

* **Total Votes Cast**

The congressional election under review covered votes from electorates in 3 counties in Colorado, namely; Arapahoe, Denver and Jefferson. The analysis of the election      data presented in comma separated value (CSV) file showed that a total of **369711**votes was the total number of votes that was recorded for this election.
This figure was arrived at by creating an inital total_votes varable to hold data whiles looping through the total number of rows in the CSV file after the header row was eliminated. The final total_votes value showed the results of each incremnetal after each loop.

_**Example of code used to generate the total_votes of the election_**      


* Total Votes and Percentage of Votes per County

One request from the Election Board was to generate the total number of votes cast in each county and the percentage of that to the overall votes cast for the election.
To honor this, two data structures; "county_list" and "county_votes" dictionary were created to hold data. 
A script to extract all county names was added under the For loop "row in reader:" by assiging the second index to the variable "county_name".
Next an if statement was introduced to help obtain the values for the county list and county votes.
The final value for county_votes was based on increasing it by 1 after each loop.

_**Example of code used to generate total votes per county**_

The Percentage of votes per county was determined by dividing the total votes per county(ie the values in the county_votes dictionary) by the total votes cast in the election and multipling it by 100.
The Votes_percentage variable was assigned with the results of this mathematical operation to provide the percentage of votes per county.
_**Example of code to generate percentage votes per county**_


An f'string statement was printed to terminal to show results.
_**Example of F'string statement and terminal results of script**_


* County with Largest Voter Turnout

To find the county with the largest turnout required the introduction of two new variables; "winning_county count" and "winning_county".
Next a decision statement was created to determine the winning county and its vote count.
The results printed to terminal showed that Denever had the largest turnout with 306,855 votes.
_**Example of decision statement and terminal results of largest turnout county**_


* Total Candidate Votes and Percentage

An initail candidate_votes dictionary and Candidate_options list was created to hold data.
All candidate names was extracted from the third index after looping through all the rows in the CSV file.
Next, an if statement is introduced to generate candidate votes by increasing the candidate_votes by 1.
_**Example of code used to generate total votes per candidate**_

A for loop was created to loop through candidate_votes and the vote percentage variable assigned with the results of dividing the candidate_votes by total votes and multiply by 100.

_**Example of code to generate percentage votes per candidate*_


* Winning Candidate

From the analysis of the data set it was revealed that Diana DeGette won the election with 272,892 being 73.8% of the total votes cast.
An if statement was used to generate winning_count and winning_percentage form the candidates_votes and vote_percentage respectively.

_**Example of code to generatewinning Candidate*_

 
![Alt text](https://github.com/emmanuelbrim/Stock-analysis/blob/main/Resources/VBA_Challenge_2018.PNG)


## Election Audit Summary
- The advantages of refactoring code includes fewer bugs, faster execution and easy to read whiles the time involved in refactoring and the tendency of making mistakes serve as its cons.

- Much time was invested in restructing the script though the runtime of the original VBA script was improved after refactoring. 


