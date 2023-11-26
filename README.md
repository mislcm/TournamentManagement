# TournamentManagement
It's a user-friendly application designed to handle various aspects of organizing and monitoring a sports tournament. Let me walk you through its features and the technologies I employed to develop it.

Features 

1. Registration I have a registration feature that allows participants to input their details, including their name (userReg), whether they are part of a team or individual (TeamID), and their choice of event (eventChoice). The information is then stored in a file named "userReg.txt". Additionally, each participant starts with an initial score of 0, recorded in the "scores.txt" file. 

2. Leaderboard To keep things competitive, I implemented a leaderboard feature. It reads the scores from "scores.txt", organizes them in descending order, and saves the sorted leaderboard in a file called "leaderboard.txt". Users can then view the leaderboard, offering a snapshot of the tournament's current standings. 

3. Display Users I have a feature that displays a preview of the added users by reading from the "userReg.txt" file. It provides organizers with a quick overview of the participants. 

4. Search Users Participants can be searched by name using the search feature. Upon entering a name, the system scans "userReg.txt" and displays the relevant information if a match is found. 

5. Display Events For clarity on available events, I offer a feature that displays a list of the current events participants can choose from. 

6. Scoring To keep scores up-to-date, there's a scoring feature. Users input their name (checkName), and if found in the "scores.txt" file, their score is updated by adding 5 points. The updated scores are then saved back to "scores.txt". 

7. Menu System A menu system ties everything together. Participants navigate through the functionalities seamlessly by choosing options such as registration, user display, user search, event display, leaderboard viewing, and scoring. 

Development Tools 
I developed this project using Python, leveraging its simplicity and versatility. The core functionalities are achieved through file operations, reading and writing to text files for user data, scores, and leaderboard information.
