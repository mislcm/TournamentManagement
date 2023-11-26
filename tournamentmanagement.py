import fileinput
def Registration():
    userReg=input("Please enter the participant: ")
    TeamID = input("Team or Individual (T/I)? ")

    print("Current events:  ")
    print("A. Hurdles")
    print("B. 100M Sprint")
    print("C. 800M Sprint")
    print("D. 80M Sprint")
    print("E. 200M Sprint")
    
    eventChoice = input("Which event do you want to participate in?: ")

    userFile=open("userReg.txt","a")
    userFile.write(userReg + "," + TeamID + "," + eventChoice + "\n")
    userFile.close()       
    
    scoringFile = open("scores.txt","a")
    scoringFile.write(userReg + "," + "0" + "\n")
    scoringFile.close()

    print("Users were successfully saved\n")
    print("The following users were added: \n", userReg)
    menu()


 
def leaderboard():
    currentScore = open("scores.txt", "r")
    finalscore = open("leaderboard.txt", "w")
    for line in sorted(currentScore, reverse=True, key=lambda line: int(line.split(",")[1])):
        finalscore.write(line)
    finalscore.close()

    leaderboard = open("leaderboard.txt", "r")
    num=1
    
    print("------Tournament Leaderboard---------")
    for line in leaderboard:
        print(str(num)+" - "+line.upper())
        num += 1
    menu()


def displayUsers() :
    print("Previewing Added Users:")
    userFile = open('userReg.txt', 'r')
    for eachUser in userFile:
        print(eachUser)
    userFile.close()

    menu()



def searchUsers():
    searchUser = input("Please enter the name of the User: ")

    userFile = open('userReg.txt', 'r')
    for eachUser in userFile:
        if searchUser in eachUser:
            print("The following PARTICIPANT has been found: \n", eachUser)
    userFile.close()
    menu()

    print("Your score has been updated: ", newScore , "points")
    menu()

    

def displayEvents():
    print("A.Hurdles")
    print("B.100M Sprint")
    print("C.800M Sprint")
    print("D.80M Sprint")
    print("E.200M Sprint")
    menu()



def scoring():

    searchedPlayer = ""
    checkName = input("Enter your name: ")
    with open ('scores.txt','rt') as scoreFile:
        for eachPlayer in scoreFile:
            if eachPlayer.split(",")[0] == checkName:
                print ("Player Exists") 
                searchedPlayer = eachPlayer
                print (searchedPlayer)
                break
            

    currentScore = int(eachPlayer.split(",")[1])
    newScore = currentScore+5
    

    with fileinput.FileInput("scores.txt", inplace=True, backup='.bak') as file:
        for everyplayer in file:
            print(everyplayer.replace(checkName + "," + str(currentScore) , checkName + "," + str(newScore)), end='')

    print("Your score has been updated:", newScore , "Points!")
    menu()

def menu():
    print("-----Tournaments Main Menu-----")
    print("A - Registration")
    print("B - Display Users")
    print("C - Search User")
    print("D - Display Events")
    print("E - Leaderboard")
    print("F - Scoring")
   
    

    choice = input("Choose an option: ")
    choice = choice.lower()
    if choice == "a":
        Registration()
    elif choice == "b":
        displayUsers()
    elif choice == "c":
        searchUsers()
    elif choice == "d":
        displayEvents()
    elif choice == "e":
        leaderboard()
    elif choice == "f":
        scoring()

menu()
