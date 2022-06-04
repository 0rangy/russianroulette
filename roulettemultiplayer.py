import requests
import time
import os
import multiprocessing

class color:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       DARKCYAN = '\033[36m'
       BLUE = '\033[94m'
       GREEN = '\033[92m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'

os.system("clear")

server = input(color.CYAN + "Enter server IP: " + color.END)
print("\n\n" + color.YELLOW + "Connecting to server..." + color.END)
if server.startswith("http://"):
    req = requests.get(server) # if
    if req.status_code == 404:
        print(color.GREEN + "\nConnected!")
elif server.startswith("https://"):
    req = requests.get(server) # elif
    if req.status_code == 404:
        print(color.GREEN + "\nConnected!")
else:
    server = "http://" + server
    req = requests.get(server) # else
    if req.status_code == 404:
        print(color.GREEN + "\nConnected!") 

action = input(color.CYAN + "Do you want to " + color.BOLD + "create" + color.END + color.CYAN +  " or " + color.BOLD + "join" + color.END + color.CYAN + " a game: " + color.END)
username = input(color.CYAN + "What is your name: " + color.END)
if action == "join":
    code = input(color.CYAN + "Enter Multiplayer Code: " + color.END)
    requests.get(server + "/joingame?name=" + username + "&id=" + code)
elif action == "create":
    req1 =  requests.get(server + "/createroom?name=" + username)
    print(color.YELLOW + "Creating game room...")
    rmdecode = req1.content.decode()
    time.sleep(1)
    reqjoin1 = requests.get(server + "/joingame?name=" + username +"&id=" + rmdecode)
    print(color.GREEN + "Success!")
    print(color.CYAN + "Your game code is " + color.BOLD + rmdecode + color.CYAN + "." + color.END)

if action == "create":
    code = rmdecode 

os.system("clear")
gamestart = False

def userInput():
    if action == "create":
        try:
            print(color.CYAN + color.BOLD + "start " + color.END + color.CYAN + "or " + color.BOLD +"end " + color.END + color.CYAN + "the game: " + color.END)
            stdin = open(0)
            i = stdin.readline()
            if i.find("start") != -1:
                print(color.GREEN + "Game will start" + color.END)
                requests.get(server + "/startgame?id=" + code)
            elif i.find("end") != -1:
                print("Game will end")
        except:
            i = ""


while gamestart is not True:
    req63 = requests.get(server + "/refresh?id=" + code)
    file1 = req63.content.decode()
    filea = file1.split('|')
    print(color.BLUE + "Game Code: " + color.BOLD + code)
    for i in filea:
        print(color.BLUE + i + color.END)
    t = multiprocessing.Process(target=userInput)
    t.start()
    time.sleep(5)
    t.terminate()
    os.system("clear")
    




