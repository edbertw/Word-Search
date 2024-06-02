import random #calling random library
import time #calling time library
#initialization
words = {} #{"integer":[False, [[2,3],[2,4],[2,5],[2,6]....]]}
files = ["Data Types", "Countries","Food Types", "Sports", "Brands"]
longest = [10,13,10,11,15]
bestTime = {"Easy1": "--:--:--", "Medium1": "--:--:--", "Hard1": "--:--:--", "Easy2": "--:--:--", "Medium2": "--:--:--", "Hard2": "--:--:--"}

#code starts here:
def hint(word, word_):
    word = word
    word_ = list(word_)
    if "_" not in word_ or word == "":
        for w in words:
            if words[w][0] == False:
                word = list(w)
                word_ = ["_" for i in range(len(word))]
                break
    replaced = False
    while not replaced:
        i = random.randint(0,len(word_)-1)
        if word_[i] == "_":
            word_[i] = word[i]
            replaced = True
    return ''.join(word), ''.join(word_)

def createboard(row, col): #define function to create initial board
    board = []
    for i in range(row):
        tmp = []
        for j in range(col):
            tmp.append("-")
        board.append(tmp)
    return board

def printboard(board, row, col): #defined function to print board with its contents
    print("\t\t\t======================================================")
    print("\t\t\t\t\033[1m"+"#"*(col*3+3)+'\033[0m')
    for index, row in enumerate(board):
        print("\t\t\t\t\033[1m#"+'\033[0m',end=" ")
        for letter in row:
            print(" " + letter.lower() + " ", end="")
        print("\033[1m#\033[0m")

    print("\t\t\t\t\033[1m"+"#"*(col*3+3)+'\033[0m')
    print("\t\t\t\t\tBEST TIME: \033[1m"+ "\033[93m" + bestTime[difficulty] +'\033[0m')

def printsolution(board, row, col):
    solboard = board
    notfoundwords = []
    for word in words:
        if words[word][0] == False:
            notfoundwords.append(word)
            indexes = words[word][1]
            for index in indexes:
                l = solboard[index[0]][index[1]]
                solboard[index[0]][index[1]] = '\033[31m\033[1m' + l + '\033[0m'
    time.sleep(0.25)
    print("\t\t\tBetter luck next time, You should have gotten these...")
    for word in notfoundwords:
        time.sleep(0.15)
        print("\t\t\t"+word)
    time.sleep(1)
    printboard(solboard, row, col)
    time.sleep(3)


def insert(board, word, srow, scol, pr, pc): #defined function to insert values to the board
    srow2 = srow
    scol2 = scol
    indexes = []
    for j in word:
        if board[srow][scol] != "-" and  board[srow][scol] != j:
            return board, False, []
        srow += pr
        scol += pc 
    for m in word:
        indexes.append([srow2,scol2])
        board[srow2][scol2] = m
        srow2 += pr
        scol2 += pc
    return board, True, indexes

def setboard(f, board, row, col): #defined function used to randomly generate letters and insert to board
    global tmp,words
    WordList=[]
    file1 = open(f, "r").readlines() #code ensures that the word exists on the randomly generated board either horizontally,vertically or diagonally
    if row==8:
        for word in file1:
            if len(word)<=8:
                WordList.append(word)
        tmp=random.sample(WordList, 5)
    elif row==11:
        for word in file1:
            if len(word)<=11:
                WordList.append(word)
        tmp=random.sample(WordList, 8)
    elif row==15:
        for word in file1:
            if len(word)<=15:
                WordList.append(word)
        tmp=random.sample(WordList, 10)
    for word in tmp:
        word = word.rstrip("\n")
        oriword = word
        wordl = len(word)
        inserted = False
        indexes = []
        while not inserted:
            if random.randint(1,2) == 1:
                word = word[::-1]
            srow, scol, pr, pc = 0, 0, 0, 0
            dice = random.randint(1,4)
            if dice == 1:
                srow = random.randint(0, row-1)
                scol = random.randint(0, col-wordl)
                pr, pc = 0, 1
            elif dice == 2:
                srow = random.randint(0, row-wordl)
                scol = random.randint(0, col-1)
                pr, pc = 1, 0
            elif dice == 3:
                srow = random.randint(0, row-wordl)
                scol = random.randint(0, col-wordl)
                pr, pc = 1, 1
            elif dice == 4:
                srow = random.randint(0, row-wordl)
                scol = random.randint(wordl-1, col-1)
                pr, pc = 1, -1
            boardtmp, inserted, indexes = insert(board, word, srow, scol, pr, pc)
        words[oriword] = [False, indexes]

    for x in range(row):
        for y in range(col):
            if board[x][y] == "-":
                board[x][y] = chr(random.randint(97,122))
    return board

def blindgame(board, row, col, hints): #defined function for blindgame mode
    global words
    start_time = time.time()
    found = 0
    lstore = []
    hword = ""
    hword_ = ""
    while found != len(words):
        printboard(board, row, col)
        if hword != "":
            print("\t\t\t"+'\033[1m\033[93m'+ "Hint: "+ hword_+'\033[0m')
        print("\t\t\t\033[1m\033[95m"+str(hints)+" hints remaining, enter h to use hints"+'\033[0m')
        word = input("\t\t\tEnter word (-1 to exit): ").strip().lower()
        if word == "-1":
            printsolution(board, row, col)
            words={}
            return mainmenu()
        elif word == "h":
            if hints > 0:

                hword, hword_ = hint(hword,hword_)
                hints -= 1
                
            else:
                print("\t\t\tHint: "+hword_)
                print("\t\t\tNo hints remaining")
        else:
            if word not in words:
                print("\t\t\t", word, "not in board")
            else:
                x = words[word]
                if not x[0]:
                    print("\t\t\t"+word+" is in the board")
                    indexes = x[1]
                    words[word] = [True, x[1]]
                    for index in indexes:
                        tmp = '\033[1m\033[34m'+board[index[0]][index[1]]+'\033[0m'
                        board[index[0]][index[1]] = tmp
                    found += 1
                    if word == hword:
                        hword = ""
                else:
                    print("\t\t\tWord already found!")
    printboard(board, row, col)
    print("\t\t\tCongratulations! You have found all words")
    best_time = time.time() - start_time
    bestTime[difficulty] = f"{int(best_time//60)}:{int((best_time%60)//1)}:{round((best_time%1) * 100)}"
    print("\t\t\tYou completed it in" + "\033[1m" + "\033[93m" , str(bestTime[difficulty]), "\033[0m")
    print("\t\t\tReturning back to main menu>>>>>>")
    words={}
    return mainmenu()

def huntgame(board, row, col,hints): #defined function for the huntgame mode
    global words
    start_time = time.time()
    hword = ""
    hword_ = ""
    yxlist,xylist,wordlist,enteredletters=[],[],[],[]
    flag,total,x,visited=False,5,True,False#total = total number of words to be found
    print(f'\n\t\t\tThere are {total} words to search for. Good Luck!!\n')
    for line in tmp:
        wordlist.append(line[:-1]) #appending words from text file to list
    i=row//2 #current row value
    j=col//2 #current column value
    temp=board[i][j]
    board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m' #ANSI escape code for red bolded text
    printboard(board,row,col)
    while True:
        x=True
        time.sleep(0.2) #delays program running by 0.2 seconds every loop
        word=''.join(enteredletters)
        print('\t\t\t\t\tEntered Letters: '+word)       
        if word in wordlist:
            if words[word][1] == xylist or words[word][1][::-1] == xylist:
                print("\t\t\t\tFound word:",word)
                total=total-1
                words[word] = [True, x[1]]
                print(f'\t\t\tThere are {total} words left to search for!')
                wordlist.remove(word)
                xylist,enteredletters=[],[]
                printboard(board,row,col)
            else:
                print('\t\tYou might have entered letters from the wrong diagonal,horizontal or vertical. Sorry the game has to reset!!')
                printboard(board,row,col)
        if len(wordlist)==0:
            print("\t\t\tCongratulations! You have found all words")
            best_time = time.time() - start_time
            bestTime[difficulty] = f"{int(best_time//60)}:{int((best_time%60)//1)}:{round((best_time%1) * 100)}"
            print("\t\t\tYou completed it in" + "\033[1m" + "\033[93m", str(bestTime[difficulty]) , "\033[0m")
            return mainmenu()
        move=input("\t\tEnter move W/A/S/D to move, Q to exit, M to mark it, U to undo mark and H for hint: ").upper()
        while move != 'W' and move != 'A' and move !='S' and move !='D' and move !='Q' and move!='M' and move!='U' and move!='H': #validation
            move=input("\t\tRe-enter move W/A/S/D to move, Q to exit, M to mark it, U to undo mark and H for hint: ").upper()
        if move=='W' and i>0: #prevents List OutOfIndex Error
            visited=False #flag to ensure letter not marked twice in a row
            if flag==True:
                i=i-1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m' #ANSI escape code for red bolded text
                flag=False
            else:
                board[i][j]=temp
                i=i-1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
        elif move=='S' and i<row-1:
            visited=False
            if flag==True:
                i=i+1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
                flag=False
            else:
                board[i][j]=temp
                i=i+1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
        elif move=='A' and j>0:
            visited=False
            if flag==True:
                j=j-1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
                flag=False
            else:
                board[i][j]=temp
                j=j-1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
        elif move=='D' and j<col-1:
            visited=False
            if flag==True:
                j=j+1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
                flag=False
            else:
                board[i][j]=temp
                j=j+1
                temp=board[i][j]
                board[i][j]='\033[1m\033[31m' + board[i][j] + '\033[0m'
        elif move=='Q':
            printsolution(board,row,col)
            words={}
            return mainmenu()
        elif move=='M' and visited==False:
            visited=True
            for y in range(len(yxlist)):
                if yxlist[y][1]==i and yxlist[y][2]==j:
                    board[i][j]=temp
                    yxlist.append([temp,i,j])
                    xylist.append([i,j])
                    enteredletters.append(yxlist[y][0])
                    flag,x=True,False
                    break
            if x==True:
                board[i][j]=temp
                yxlist.append([temp,i,j])
                xylist.append([i,j])
                board[i][j]='\033[1m\033[34m'+board[i][j]+'\033[0m' #ANSI escape code for blue bolded text
                enteredletters.append(temp)
                flag=True 
        elif move=='U':
            visited=False
            if yxlist[len(yxlist)-1][1]==i and yxlist[len(yxlist)-1][2]==j:
                board[i][j]=temp
                temp=yxlist[len(yxlist)-1][0]
                yxlist.remove([temp,i,j])
                xylist.remove([i,j])
                enteredletters.remove(temp)
                board[i][j]='\033[1m\033[31m'+temp+'\033[0m'
                flag=False
        elif move=='H':
            if hints > 0:
                hword, hword_ = hint(hword,hword_)
                hints -= 1
            else:
                print("\t\t\tHint: "+hword_)
                print("\t\t\tNo hints remaining")
            if hword != "":
                print("\t\t\t"+'\033[1m\033[93m'+ "Hint: "+ hword_+'\033[0m')
        if word==hword:
            hword=''
        printboard(board,row,col)

def inputchoice(): #defined function to enter and validate choice value
    accept = False
    back = False
    while not accept:
        choice = input("\t\t\t\t\tEnter choice: ")
        if choice in "-123":
            accept = True
    print("\t\t\t======================================================")
    return int(choice)

def mainmenu(): #starting screen
    global choice
    print('\033[1m\033[31m\t\t\tHoward Anggawijaya, Sebastian, Noah, Edbert, Howard Tse PRESENTS:\033[0m')
    time.sleep(0.5) #time delay of 0.5 seconds
    print("====================================================================================================================")
    print('\033[31m'+'\033[107m'+'\033[1m' + "___    __    ____   ______   .______     _______       _______. _______     ___      .______       _____  __    __  "+"\033[0m")
    time.sleep(0.25) #time delay of 0.25 seconds
    print('\033[31m'+'\033[107m'+"\033[1m" + "\  \  /  \  /    / /  __  \  |   _  \   |       \     /       ||   ____|   /   \     |   _  \    /      ||  |  |  | " + "\033[0m")
    time.sleep(0.25) #time delay of 0.25 seconds
    print('\033[31m'+'\033[107m'+"\033[1m" + " \  \/    \/    / |  |  |  | |  |_)  |  |  .--.  |   |   (----`|  |__     /  ^  \    |  |_)  |  |  ,----'|  |__|  | "+"\033[0m")
    time.sleep(0.25) #time delay of 0.25 seconds
    print('\033[34m'+'\033[107m'+"\033[1m" +"  \            /  |  |  |  | |      /   |  |  |  |    \   \    |   __|   /  /_\  \   |      /   |  |     |   __   | "+"\033[0m")
    time.sleep(0.25) #time delay of 0.25 seconds
    print('\033[34m'+'\033[107m'+"\033[1m" +"   \    /\    /   |  `--'  | |  |\  \--.|  '--'  |.----)   |   |  |____ /  _____  \  |  |\  \--.|  `----.|  |  |  | "+"\033[0m")
    time.sleep(0.25) #time delay of 0.25 seconds
    print('\033[34m'+'\033[107m'+"\033[1m" +"    \__/  \__/     \______/  | _| `.___||_______/ |_______/    |_______/__/     \__\ | _| `.___| \______||__|  |__| "+"\033[0m")
    print("====================================================================================================================")
    time.sleep(0.25) #time delay of 0.25 seconds
    print("\t\t\t\t\t\033[31m\033[1mLET THE SEARCH BEGIN!\033[0m")
    time.sleep(0.5) #time delay of 0.5 seconds
    print("\n\t\t\t\t\tChoose your option:")
    print("\t\t\t    (1) Start\t(2) Tutorial\t(-1) Exit")
    choice = inputchoice()
    if choice == -1:
        return -1
    elif choice == 1:
        return choosegame()
    elif choice == 2:
        return tutorial()

def tutorial():
    with open('readme.txt') as file:
        for line in file:
            if line.strip()=='':
                print(line)
                time.sleep(2)
            else:
                print(line)
                time.sleep(0.15)
    print('\t\t\t\033[31m\033[1m Now you can start playing the game !!!\033[0m')
    print("====================================================================================================================")
    print('\n')
    return mainmenu()

def choosegame():#defined function to choose game modes by inputting integers -1/1/2
    global choice
    global difficulty
    print("\t\t\t\t\t\033[1m\033[93m Choose Game Mode:\033[0m")
    print("\t\t\t    (1)Blind Mode\t(2) Hunt Mode\t(-1) Back")
    choice = inputchoice() 
    if choice == -1:
        return mainmenu()
    elif choice == 1:
        return chooseboard()
    elif choice == 2:
        return chooseboard()
        
def chooseboard(): #defined function to choose specs of board
    global choice1
    global time_mode
    global difficulty
    print("\t\t\t\t\t\033[1m\033[92m Topics: \033[0m")
    for i in range(1, len(files)+1):
        print("\t\t\t\t\t"+str(i) + "." + files[i-1])
    choice1 = int(input("\t\t\t\t\tChoose Topic: ")) 
    if choice1 == -1:
        return choosegame()
    else:
        h = 0
        print("\t\t\t===================================================")
        print("\t\t\t\t\t\033[1m\033[93m Difficulty Levels: \033[0m")
        print("\t\t\t(1)Easy \t(2)Intermediate \t(3)Advanced")
        diff = inputchoice()
        if diff == 1:
            row, col=8,8
            difficulty = "Easy" + str(choice)
            h = 5
        elif diff == 2:
            row, col=11,11
            difficulty = "Medium" + str(choice)
            h = 5
        elif diff == 3:
            row, col=15,15
            difficulty = "Hard" + str(choice)
            h = 5
        elif diff == -1:
            return mainmenu()
        return playgame(files[choice1-1] + ".txt", int(row), int(col), h)

def playgame(f, row, col, h): #defined function to start game by choice of different game modes
    board = createboard(row,col)
    board = setboard(f, board, row, col)
    if choice == 1:
        return blindgame(board, row, col, h)
    elif choice==2:
        return huntgame(board, row, col, h)

def main(): #main procedure
    x = mainmenu()      
    if x == -1:
        print("\t\t\t\t\tGoodbye ...")
        exit()
main() 
