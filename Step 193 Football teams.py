#Input format:

#The first line specifies the integer n — the number of completed games.
#After this follow the n lines, which contain the game results in the following format:
#First_team;Goals_by_first_team;Second_team;Goals_by_second_team
#Output of your program should look like the following:
#Team:Total_games Wins Draws Defeats Total_points

#You can output teams in an arbitrary order.

#Sample Input:

#3
#Zenit;3;Spartak;1
#Spartak;1;CSKA;1
#CSKA;0;Zenit;2
#Sample Output:

#CSKA:2 0 1 1 1
#Zenit:2 2 0 0 6
#Spartak:2 0 1 1 1



teams={}

def addTeam(team):
    if team not in teams:
        teams[team]={'Totalgames': 0, 'Wins': 0, 'Draws': 0, 'Defeats': 0, 'Totalpoints': 0}


def draw(team):
    teams[team]['Draws'] += 1
    teams[team]['Totalpoints'] += 1

def wins(team):
    teams[team]['Wins'] +=1
    teams[team]['Totalpoints'] += 3

def defeats(team):
    teams[team]['Defeats'] += 1

def total(team):
    teams[team]['Totalgames']+=1

def score(match):
    Firsteam, Goalsbyfirstteam, Secondteam, Goalsbysecondteam = match
    addTeam(Firsteam);
    addTeam(Secondteam);
    if Goalsbyfirstteam == Goalsbysecondteam:
        draw(Firsteam)
        draw(Secondteam)
    elif Goalsbyfirstteam<Goalsbysecondteam:
        defeats(Firsteam)
        wins(Secondteam)
    else:
        defeats(Secondteam)
        wins(Firsteam)

    total(Firsteam)
    total(Secondteam)

n = int(input())
for _ in range(n):
    match = input().split(sep=';')
    score(match)
    
for team, stat in teams.items():
    print(team, end=':')
    print(stat['Totalgames'], stat['Wins'], stat['Draws'], stat['Defeats'], stat['Totalpoints'])



