import itertools
from colorama import init,Fore,Back,Style   #for colour
init()

def win(curent_game):
    def all_same(l):
        if l.count(l[0])==len(l) and l[0]!=0 :
            return True
        else:
            return False
    #winning->horizontally
    for row in game:
        print(row)
        if all_same(row) :
            print("Player "+str(row[0])+"is the winner horizontally")
            return True 
    #winning ->vertically 
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
        if all_same(check) :
            print("Player "+str(check[0])+"is the winner vertically")
            return True
# main diagonals
    diags=[]
    for i in range(len(game)):
        diags.append(game[i][i])
    if all_same(diags):
        print("Player "+str(diags[0])+"is the winner diagonally(main)")
        return True
#secondary diagonal
    diags=[]

    col=reversed(range(len(game)))   #reversed list values
    for rows,cols in enumerate(col):
        diags.append(game[rows][cols])
    if all_same(diags):
        print("Player "+str(diags[0])+"is the winner diagonally(sec)")
        return True

    return False

def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game_map[row][column] !=0:
            print('this position is occupied')
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))      #print(0 1 2)  list comprehension
        if player !=0:
            game_map[row][column]=player
        for count,row in enumerate(game_map):
            colored_row= ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item ==1:
                    colored_row += Fore.RED +' X ' +Style.RESET_ALL
                elif item ==2:
                    colored_row += Fore.GREEN +' 0 ' +Style.RESET_ALL
            print(count,colored_row)

        return game_map,True
        #error handling
    except IndexError as e:
        print("Error:Make sure that you input row/column as 0,1,2 or not",e)
        return game_map,False
    except Exception as e:
        print("something went wrong",e)
        return game_map,False
      
play=True
players=[1,2]
while play:
    game_size=int(input("enter the size of game"))
    game=[[0 for i in range(game_size)] for i in range(game_size)]   #dynamic size game list of list of any size
    game_won=False
    game,_ =game_board(game,just_display=True)  # _ is null
    player_choice=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        print("Current_player ",current_player)
        played=False
        while not played:
            row_choice=int(input("enter the row choice:0,1,2 ->"))
            column_choice=int(input("enter the column choice:0,1,2 ->"))
            game,played=game_board(game,current_player,row_choice,column_choice)

        if win(game):
            game_won=True
            again=input("The game is over,do you want to play again:(y/n) ")
            if again.lower()=="y" : #lower case convert
                print("restarting")
            elif again.lower()=="n" :
                print("bye")
                play=False  #end of game
            else:
                print("wrong input go back ") 
                play=False
