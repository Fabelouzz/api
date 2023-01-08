import requests  # läser API
import json  # formaterar javascript syntax
import os  # rensar skärmen

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
r = requests.get(url)  # request till hemsida, returnerar status kod response
response_dic = json.loads(r.text)  # r.text gör om request response till string. Json.loads från str till dict
urlExtra = " "

def extra():
    match = False
    id = " "
    for element in response_dic["artists"]:
        if element["name"] == artistName.title():
            id = element["id"]
            match = True
            break
    if not match:
        print("-" * 30)
        print("|")
        print("ERROR: Artist not found", "\"" + artistName + "\"")
        print("|")
        input("Press enter to continue")
        return
    urlExtra = url+id
    r = requests.get(urlExtra)
    extraInfo = json.loads(r.text)
    print("*"*25+"\n"+"*"*25)
    print(artistName.center(25).title())
    print("*"*25+"\n"+"*"*25)
    print("|Members:",end="\t")
    for element in extraInfo["artist"]["members"]:
        if element == extraInfo["artist"]["members"][-1]:
            print(element,end=" ")
        else:
            print(element,end=", ")
    print()
    print("|Genres:",end="\t")
    for element in extraInfo["artist"]["genres"]:
        if element == extraInfo["artist"]["genres"][-1]:
            print(element, end=" ")
        else:
            print(element, end=", ")
    print()
    print("|Years Active:", end="\t")
    for element in extraInfo["artist"]["years_active"]:
        if element == extraInfo["artist"]["years_active"][-1]:
            print(element, end= " ")
        else:
            print(element, end=", ")
    print()
    print("-"*35)
    input("Press enter to continue")

def menu():
    print("|L| List artists")
    print("|V| View artist profile")
    print("|E| Exit application")
    print(30*"-")

def list_artists():  # skriver ut en lista på alla artiser
    print("-"*30)
    for element in response_dic["artists"]: # går igenom elementen i listan
        print('|',element["name"])  # printar namnet i varje element i listan
    print("*"*30)
    print("*"*30)
    input("Press enter to continue")

while True:  # huvudloopen
    os.system('cls' if os.name == 'nt' else 'clear')  # rensar skärmen
    print(30 * "-")
    print("Artist Database".center(30))  # centrerar rubriken
    print(30 * "-")
    menu() # rad 55
    choice1 = input("| Selection > ")

    match choice1: # matchcase ist för if-else
        case 'L':
            list_artists()  #rad 61
        case 'V':
            artistName = input("|Artist name > ")
            extra() # 10
        case 'E':
            print("SUCCESS: Script exited successfully!")
            exit()
        case Error:  # felhantering om input inte matchar något case
            print("-"*30)
            print("|")
            print(f"ERROR: Unknown command \"{Error}\"")  # felmeddelande
            print("|")
            print("-"*30)
            input("Press enter to continue")

