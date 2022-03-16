# ELECTION ANALYSIS 
_An Audit of Election Results with Python_


## Overview of the Project
Every group have established way by which individuals are selected to represent it in matters of concern. Notable among these ways is Universal Adult suffrage, and its within this contest of elections specifically the popular vote system that this project worked on.
The purpose of this project was to develop a system using python, that will analyze recent congressional election results of 3 candidates and provide valid information on which the Colorado Board of Elections will act. 

## Election Audit Results

* **Total Votes Cast**

The congressional election under review covered votes from electorates in 3 counties in Colorado, namely; Arapahoe, Denver and Jefferson. 
The analysis of the election data presented in comma separated value (CSV) file showed that a total of **369711**votes was cast during this election.
This figure was arrived at by creating an inital total_votes variable to hold data. Then a for loop was introduced to loop through the total number of rows in the CSV file after the header row was eliminated. The final total_votes value showed the results of increasing it value by 1 after each loop.


_*Example of code used to generate the total_votes of the election*_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/Total%20Votes.PNG)


* **Total Votes and Percentage of Votes per County**

One request from the Election Board was to generate the total number of votes cast in each county and the percentage of that to the overall votes cast in the election.
To honor this, two data structures; "county_list" and "county_votes" dictionary were created to hold data. 
A script to extract all county names was added under a For loop; "row in reader:" by assiging the second index to the variable "county_name".
Next an if statement was introduced to help obtain the values for the county list and county votes.
The final value for county_votes was based on increasing it by 1 after each loop.


_Example of code used to generate total votes per county_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/Total%20Votes%20per%20county.PNG)



The Percentage of votes per county was determined by dividing the total votes per county(ie the values in the county_votes dictionary) by the total votes cast in the election and multipling the results by 100.
The Votes_percentage variable was assigned with the results of this mathematical operation to provide the percentage of votes per county.
An f'string statement was then printed to terminal to show results.

_Example of code to generate percentage votes per county_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/votes%20per%20county.PNG)



_Example of F'string statement and terminal results of script_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/F%20string%20county%20votes%20and%20percentage.PNG)


![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/terminal%20view.PNG)




* **Largest Turnout County**

To find the county with the largest turnout required the introduction of two new variables; "winning_county count" and "winning_county".
Next a decision statement was created to determine the winning county and its vote count.
The results printed to terminal showed that Denever had the largest turnout with 306,855 votes.


_Example of decision statement and terminal results of largest turnout county_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/largest%20turnout.PNG)


![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/wining%20county.PNG)


* **Total Votes per Candidate and Percentage**

A similar outline like that used in generating Total votes per county was used to provide the total candidate votes. 
An initail candidate_votes dictionary and candidate_options list was created to hold data.
All candidate names were extracted from the third index after looping through all the rows in the CSV file.
Next, an if statement was introduced to generate total candidate votes by increasing the value of candidate_votes by 1 under the for loop "row in reader".
A second for loop was then created to loop through candidate_votes by candidate_name to get the unique votes per candidate which was assigned to the "votes" variable. Then the results of dividing votes by total votes multiplied by 100 was given as vote percentage.

_Example of code to generate percentage votes per candidate_

![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/percentage%20votes%20per%20candidate.PNG)


![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/terminal%20percentage%20vote%20per%20candidate.PNG)


* **Winning Candidate**

From the analysis of the data set it was revealed that Diana DeGette won the election with 272,892 votes being 73.8% of the total votes cast.
The winner was arrived at by the use of an if statement to generate winning_count and winning_percentage fromm the candidates_votes and vote_percentage respectively.

_Example of code to generate winning Candidate_

 
![Alt text](https://github.com/emmanuelbrim/Election_Analysis/blob/main/Resources/winning%20candidate.PNG)

## Election Audit Summary
- The Resources folder can be used to hold data set from other elections and modifing the path to reflect that particular file.
- 


