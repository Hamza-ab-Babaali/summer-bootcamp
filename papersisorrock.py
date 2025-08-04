import random
player_point=0
pc_point=0


options=["paper","sisor","rock"]


for i in range(3):
    pc_choice=str(random.choice(options))
    player_choice=input("chose paper or sisor or rock :\n")

    if pc_choice == "rock" and player_choice == "sisor":
        print("Pc win!")
        pc_point+=1
    if pc_choice == "rock" and player_choice == "rock":
        print("Tie!")

    if pc_choice == "rock" and player_choice == "paper":
        print("Player win!")
        player_point+=1


    if pc_choice == "paper" and player_choice == "rock":
        print("Pc win!")
        pc_point+=1

    if pc_choice == "paper" and player_choice == "sisor":
        print("Player win!")    
        player_point+=1
    if pc_choice == "paper" and player_choice == "paper":
        print("Tie!")


    if pc_choice == "sisor" and player_choice == "paper":
        print("Pc win!")
        pc_point+=1

    if pc_choice == "sisor" and player_choice == "sisor":
        print("Tie!")

    if pc_choice == "sisor" and player_choice == "rock":
        print("Player win!")
        player_point+=1

if player_point>pc_point:
    print(player_point,":",pc_point,"player won!!!!")
if player_point<pc_point:
    print(player_point,":",pc_point,"Pc won!!!!")
if player_point==pc_point:
    print(player_point,":",pc_point,"Tie!!!!")