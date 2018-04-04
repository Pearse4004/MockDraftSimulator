"""
file: draft.py
language: python
author: Pearse Lehmann dpearse88@gmail.com
description: takes in a file of lines that have position name and raiting
puts them in to a class named player sorts the players based on raiting
and does a mock draft based on their overalls
"""
class Player:
    def __init__(self,position,name,rating):
        self.position = position
        self.name = name
        self.rating = rating
class Teams:
    def __init__(self,name,rank,needs):
        self.name = name
        self.rank = rank
        self.needs = needs
def makelist(file):
    """
    Takes in a file that has position name and raiting in that order
    then puts them in to the player class and puts those players into
    a list and returns the list full of players
    """
    list_of_players = []
    for line in open(file):
        line = line.split()
        player = Player(line[0],line[1]+' '+line[2],int(line[3]))
        list_of_players.append(player)
    return list_of_players

def bigboard(list_of_players):
    count = 0
    list_of_players.sort(key=lambda x:x.rating,reverse=True)
    while count < len(list_of_players):
        for player in list_of_players:
            count += 1
            if count > len(list_of_players):
                break
            else:
                print(count,':',player.position,player.name,player.rating)

def postionrank(list_of_players):
    list_of_players.sort(key=lambda x:x.rating,reverse=True)
    rankp = {}
    for player in list_of_players:
        if player.position in rankp.keys():
            rankp[player.position].append((player.name,player.rating))
        else:
            rankp[player.position] = [(player.name,player.rating)]
    return rankp

def mockdraft(rankp,lst):
    count = 0
    roundp = 0
    while count < 32 * 7:
        if (count % 32) == 0:
            roundp += 1
            print('Round',roundp)
        count += 1
        pickn = count % 32
        for team in lst:
            if team.rank == pickn:
                teamn = team.name
                needlst = team.needs
        """
        weight = 1
        for need in needlst:
            if 'QB' == need[0]:
                weight = need[1]
        player = rankp['QB'][0]
        playerr = player[1] * weight
        finalweight = weight
        playerposition = 'QB'
        """
        playerr = 0
        player = ('Not enough players',0)
        finalweight = 1
        playerposition = 'None'
        for key in rankp:
            weight = 1
            if rankp[key] == []:
                pass
            else:
                for need in needlst:
                    if key == need[0]:
                        weight = need[1]
                if playerr < rankp[key][0][1] * weight:
                    player = rankp[key][0]
                    playerposition = key
                    finalweight = weight
                    playerr = rankp[key][0][1] * weight
        if playerposition != 'None':
            rankp[playerposition].pop(0)
        if finalweight != 1:
            needlst.remove((playerposition,finalweight))
        print(count,teamn,':',playerposition,player[0])

def maketeams(file):
    rank = 0
    list_of_teams = []
    for line in open(file):
        rank += 1
        line = line.split()
        needlst = []
        for i in range(1,5):
            if line[i] == '-':
                pass
            else:
                weighted = 1.06 - (i/100)
                need = line[i]
                needlst.append((need,weighted))
        team = Teams(line[0],rank,needlst)
        list_of_teams.append(team)
    list_of_teams[-1].rank = 0
    return list_of_teams   
    
def main():
    filet = '2017team.txt'
    list_of_teams = maketeams(filet)
    filep = '2017draft.txt'
    list_of_players = makelist(filep)
    view = input('Show big board? (Y/N):')
    if view == 'Y':
        bigboard(list_of_players)
    rankp = postionrank(list_of_players)
    key = 'QB'
    while key != ' ':
        key = input('What position group do you want to see?(QB,RB,WR,TE,OT,OG,C,DL,EDGE,LB,CB,S) Press enter to move on.')
        if key == '':
            break
        elif key in rankp.keys():
            count = 0
            for player in rankp[key]:
                count = count + 1
                print(count,':',player[0],player[1])
        else:
            print('Postition not there')
    mockdraft(rankp,list_of_teams)
    
    
main()
    
