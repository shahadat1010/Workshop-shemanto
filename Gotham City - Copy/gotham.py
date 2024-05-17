import time

# Scenario Outcomes
def outcome_a1():
    print("\nYou enter the police department and gather information from your colleagues.")
    time.sleep(3)
    print("\nDetective Bullock informs you that Commissioner Gordon was last seen at Arkham Asylum, investigating reports of a disturbance.")
    time.sleep(4)
    print("\nWith this lead in hand, you prepare to embark on your investigation, determined to uncover the truth about Gordon's disappearance.")
    time.sleep(4)
    investigate_arkham_asylum()

def outcome_b1():
    print("\nYou decide to keep the evidence of Commissioner Gordon's disappearance to yourself and pursue the investigation alone.")
    time.sleep(3)
    print("\nAs you delve deeper into the case, you realize the magnitude of the conspiracy surrounding Gordon's disappearance.")
    time.sleep(4)
    print("\nEvery clue leads to more questions, and you find yourself facing a web of intrigue that stretches far beyond Gotham City.")
    time.sleep(4)
    print("\nDetermined to uncover the truth, you set out on your investigation, ready to face whatever challenges lie ahead.")
    time.sleep(4)
    investigate_arkham_asylum()

def outcome_b2():
    print("\nYou shapeshift into Commissioner Gordon, hoping to encrypt the files.")
    time.sleep(3)
    print("\nHowever, you did not notice the hidden camera in the corner of the room.")
    print("\nBefore you can do anything, guards enter the room.")
    print("1. Kill the guards")
    print("2. Try to earn their trust by stating you are Commissioner Gordon.")
    print("3. Flee from the scene")
    print("4. Enter their body to erase their memory.")

    decision = input("Enter your choice (1/2/3/4): ")

    if decision == "1":
        print("\nYou did the unthinkable. To serve justice, you took the wrong path.")
        time.sleep(4)
        print("\nBatman found out what you did. He captured you and put you in a special cage that can hold Aliens from Mars.")
        time.sleep(4)
        game_over_worst_ending()
    elif decision == "2":
        print("\nRecognizing the officers' apprehension, you adopt a more empathetic approach, taking the time to build rapport and earn their trust.")
        time.sleep(4)
        print("\nSlowly but surely, the officers begin to open up, sharing tidbits of information that could prove crucial to your investigation.")
        time.sleep(4)
        print("\nAfter they leave, you encrypt the files and gather information.")
        time.sleep(4)
        print("\nArmed with newfound leads, you leave the police department with renewed determination, ready to pursue the truth wherever it may lead.")
        time.sleep(4)
        print("\nBut you forgot to erase the footage from the hidden security camera.")
        time.sleep(4)
        game_over_bad_ending()
    elif decision == "3":
        print("\nYou use your ability to fly through the walls.")
        time.sleep(4)
        print("\nBatman found out what you did and suggests you get off the case. You are making things worse.")
        time.sleep(4)
        game_over()
    elif decision == "4":
        print("\nYou enter their body and erase their memory, discovering the camera's position.")
        time.sleep(4)
        print("\nYou wander into the soldiers' memories to find some lead, then hypnotize them to clear the footage from the security camera.")
        time.sleep(4)
        print("\nAfter making them leave the room, you unlock the encrypted files with Commissioner Gordon's fingerprint.")
        time.sleep(4)
        print("\nYou find out Gordon's disappearance is related to Batman.")
        continue_or_exit2()
    else:
        print("Invalid choice. Please try again.")
        outcome_b2()

def continue_game():
    print("\nContinuing your investigation, you ponder your next move. There are still many unanswered questions, "
          "and time is running out. The fate of Commissioner Gordon and Gotham City hangs in the balance.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Investigate Arkham Asylum, where Gotham's most dangerous criminals are held.")
    print("2. Explore the abandoned Wayne Manor, searching for clues from Batman's past.")
    print("3. Patrol the streets of Gotham, listening for whispers of conspiracy and intrigue.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        investigate_arkham_asylum()
    elif decision == "2":
        explore_wayne_manor()
    elif decision == "3":
        patrol_gotham_streets()
    else:
        print("Invalid choice. Please try again.")
        continue_game()

def continue_game_alternative():
    print("\nAfter you got a clue from Arkham Asylum, you decide to continue.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Explore the abandoned Wayne Manor, searching for clues from Batman's past.")
    print("2. Patrol the streets of Gotham, listening for whispers of conspiracy and intrigue.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        explore_wayne_manor()
    elif decision == "2":
        patrol_gotham_streets()
    else:
        print("Invalid choice. Please try again.")
        continue_game_alternative()

def continue_game_alternative2():
    print("\nContinuing your investigation, you ponder your next move. There are still many unanswered questions, "
          "and time is running out. The fate of Commissioner Gordon and Gotham City hangs in the balance.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Investigate Arkham Asylum, where Gotham's most dangerous criminals are held.")
    print("2. Explore the abandoned Wayne Manor, searching for clues from Batman's past.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        investigate_arkham_asylum()
    elif decision == "2":
        explore_wayne_manor()
    else:
        print("Invalid choice. Please try again.")
        continue_game_alternative2()

def continue_game2():
    print("\nContinuing your investigation, you ponder your next move. There are still many unanswered questions, "
          "and time is running out. The fate of Commissioner Gordon and Gotham City hangs in the balance.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Investigate Arkham Asylum, where Gotham's most dangerous criminals are held.")
    print("2. Contact the Justice League and explore the abandoned Wayne Manor with them, searching for clues from Batman's past.")
    print("3. Patrol the streets of Gotham, listening for whispers of conspiracy and intrigue.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        investigate_arkham_asylum_with_justice_league()
    elif decision == "2":
        explore_wayne_manor_with_justice_league()
    elif decision == "3":
        patrol_gotham_streets()
    else:
        print("Invalid choice. Please try again.")
        continue_game2()

def continue_or_exit():
    decision = input("\nDo you want to continue your investigation? (1.Yes/2.No): ")
    if decision == "1":
        continue_game()
    elif decision == "2":
        game_over()
    else:
        print("Invalid choice. Please try again.")
        continue_or_exit()

def continue_or_exit2():
    decision = input("\nDo you want to continue your investigation? (1.Yes/2.No): ")
    if decision == "1":
        continue_game_alternative()
    elif decision == "2":
        game_over()
    else:
        print("Invalid choice. Please try again.")
        continue_or_exit2()

def continue_or_exit3():
    decision = input("\nDo you want to continue your investigation? (1.Yes/2.No): ")
    if decision == "1":
        continue_game_alternative2()
    elif decision == "2":
        game_over_guilty_ending()
    else:
        print("Invalid choice. Please try again.")
        continue_or_exit3()

def continue_or_exit4():
    decision = input("\nDo you want to continue your investigation? (1.Yes/2.No): ")
    if decision == "1":
        continue_game2()
    elif decision == "2":
        game_over_bad_ending()
    else:
        print("Invalid choice. Please try again.")
        continue_or_exit4()

# Scenarios
def investigate_arkham_asylum():
    print("\nAs you approach Arkham Asylum, the air grows thick with a sense of dread. This institution houses some of Gotham's most dangerous criminals, "
          "each more unhinged than the last.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Speak with the staff and inmates, hoping to uncover any information about Commissioner Gordon's disappearance.")
    print("2. Search the asylum's records for any mentions of Gordon or recent disturbances.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou enter the asylum, steeling yourself against the madness within. Speaking with staff and inmates alike, "
              "you gather fragments of information that hint at a larger conspiracy.")
        time.sleep(4)
        print("\nHowever, the inmates' ramblings are often incoherent and cryptic, making it difficult to separate fact from fiction.")
        time.sleep(4)
        print("\nLeaving Arkham Asylum, you can't shake the feeling that you're missing a crucial piece of the puzzle. "
              "Perhaps a closer interrogation of the criminal masterminds will yield more concrete leads.")
        time.sleep(4)
        continue_or_exit_alternative()
    elif decision == "2":
        print("\nYou make your way to the asylum's records room, sifting through dusty files and faded paperwork.")
        time.sleep(3)
        print("\nAmidst the chaos, you find mention of a recent disturbance in one of the high-security wards, coinciding with Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nCould this be the breakthrough you've been searching for?")
        time.sleep(3)
        print("\nWith renewed determination, you prepare to investigate the disturbance further, knowing that the truth may lie within the walls of Arkham Asylum.")
        time.sleep(4)
        print("You Decided to call Batman")
        continue_or_exit4()
    else:
        print("Invalid choice. Please try again.")
        investigate_arkham_asylum()

def investigate_arkham_asylum_with_justice_league():
    print("\nAs Justice League approach Arkham Asylum,Joker is hiding in a corner and the inmates are scared to see the whole justice league except for Riddler. This institution houses some of Gotham's most dangerous criminals, "
          "each more unhinged than the last.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Speak with the staff and inmates, hoping to uncover any information about Commissioner Gordon's disappearance.")
    print("2. Search the asylum's records for any mentions of Gordon or recent disturbances.")
    print("3. Question Riddler about what he knows")
    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nYou enter the asylum, steeling yourself against the madness within. Speaking with staff and inmates alike, "
              "you gather fragments of information that hint at a larger conspiracy.")
        time.sleep(4)
        print("\nHowever, the inmates' ramblings are often incoherent and cryptic, making it difficult to separate fact from fiction.")
        time.sleep(4)
        print("\nLeaving Arkham Asylum, you can't shake the feeling that you're missing a crucial piece of the puzzle. "
              "Perhaps a closer examination of the asylum's records will yield more concrete leads.")
        print("Clue=Gordon was last seen talking to Riddler about Batman, but this information seems irrelevant. ")
        time.sleep(4)
        decision = input("Do you want to talk to riddler? (1.Yes/2.NO): ")
        if decision == "1":
            continue_or_exit2()
        elif decision == "2":
            print("\nYou make your way to the asylum's records room, sifting through dusty files and faded paperwork.")
            time.sleep(3)
            print("\nAmidst the chaos, you find mention of a recent disturbance in one of the high-security wards, coinciding with Commissioner Gordon's disappearance.")
            time.sleep(4)
            print("\nCould this be the breakthrough you've been searching for?")
            time.sleep(3)
            print("\nWith renewed determination, you prepare to investigate the disturbance further, knowing that the truth may lie within the walls of Arkham Asylum.")
            time.sleep(4)
            continue_or_exit()
        elif decision == "3":
            question_riddler()
        else:
            print("Invalid input")
    elif decision == "2":
        print("You got lead from the inside")
        print("Clue= Batman is involved in this")
        continue_game2()
    else:
        print("Invalid choice. Please try again.")
        investigate_arkham_asylum_with_justice_league()

def question_riddler():
    print("\nYou interrogate Riddler.")
    time.sleep(3)
    print("\nHe seems to know something that he is not saying.")
    time.sleep(4)
    print("\nCould this be the breakthrough you've been searching for?")
    time.sleep(3)
    print("\nSo you investigate his cell and find a riddle")
    time.sleep(4)
    print("\nThe riddle is 'What happens when you cross the bridge of time?'")
    time.sleep(4)
    print("\nWhat is the answer to the riddle?")
    time.sleep(3)
    print("\n1. Time travel is not possible?")
    print("\n2. I don't know?")
    print("\n3. Beat up Riddler?")
    decision = input("Enter your choice (1/2/3): ")
    if decision == "1":
        print("\nYou are correct.")
        time.sleep(3)
        print("\nIt seems like you wasted your time here.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "2":
        print("\nRiddler seems disappointed.")
        time.sleep(3)
        print("\nIt seems like you wasted your time here.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "3":
        print("\nRiddler cries in pain")
        time.sleep(3)
        print("\nYou found a key.")
        time.sleep(4)
        print("\nYou go to the office room of the asylum and find the bookshelf.")
        time.sleep(4)
        print("\nAfter trying the key in all the locks, you find the hidden office.")
        time.sleep(4)
        print("\nAfter reading the diary, you find out that Commissioner Gordon was searching for Batman's cave.")
        time.sleep(4)
        print("\nSo you go to the abandoned Wayne Manor and find a cave.")
        time.sleep(4)
        print("\nYou Enter the Cave")
        time.sleep(4)
        continue_game_alternative2()
    else:
        print("Invalid choice. Please try again.")
        question_riddler()

def explore_wayne_manor():
    print("\nYou arrive at the abandoned Wayne Manor, a sprawling estate shrouded in mystery and decay.")
    time.sleep(3)
    print("\nDespite its dilapidated state, the manor exudes an eerie grandeur, hinting at its former glory.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Search the manor for any clues or artifacts that may shed light on Batman's past.")
    print("2. Investigate the surrounding grounds, looking for hidden passages or secret entrances.")
    print("3. Call for backup to assist in the search.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nYou carefully explore the interior of the manor, scouring every room and corridor for any trace of Batman's presence.")
        time.sleep(4)
        print("\nAmidst the dust and cobwebs, you uncover artifacts from Batman's early years, each offering a glimpse into the life of Gotham's Dark Knight.")
        time.sleep(4)
        print("\nHowever, there's no sign of Commissioner Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nYou decide to expand your search to the surrounding grounds, hoping to uncover more secrets hidden within the shadows of Wayne Manor.")
        time.sleep(4)
        patrol_gotham_streets()
    elif decision == "2":
        print("\nYou venture into the sprawling grounds of Wayne Manor, navigating overgrown gardens and crumbling statues.")
        time.sleep(4)
        print("\nYour keen eye catches sight of a hidden entrance concealed behind a tangle of ivy, leading to an underground tunnel.")
        time.sleep(4)
        print("\nCould this be the secret passage that Batman used to traverse the city unnoticed?")
        time.sleep(4)
        print("\nWith cautious determination, you enter the tunnel, ready to face whatever secrets lie hidden beneath Wayne Manor.")
        time.sleep(4)
        print("\nYou descend deeper into the darkness, your heart pounding with anticipation.")
        time.sleep(4)
        print("\nAs you navigate the labyrinthine passages, you stumble upon a hidden chamber, its walls lined with ancient artifacts and forbidden knowledge.")
        time.sleep(4)
        print("\nBut there's no sign of Commissioner Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nFrustrated but undeterred, you vow to continue your search, knowing that the truth may be hidden in the most unexpected of places.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "3":
        print("\nYou call for backup, summoning additional resources to assist in the search.")
        time.sleep(3)
        print("\nTogether, you scour every inch of Wayne Manor, leaving no stone unturned in your quest for answers.")
        time.sleep(4)
        print("\nHowever, despite your best efforts, there's no sign of Commissioner Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nAs the hours pass, frustration mounts, and you realize that time is running out.")
        time.sleep(4)
        print("\nYou must redouble your efforts and explore every avenue if you hope to uncover the truth behind Gordon's disappearance.")
        time.sleep(4)
        continue_or_exit3()
    else:
        print("Invalid choice. Please try again.")
        explore_wayne_manor()

def explore_wayne_manor_with_justice_league():
    print("\nAs the Justice League arrives at Wayne Manor, you are greeted by the sight of overgrown gardens and crumbling statues, "
          "each a testament to the estate's former grandeur.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Split up and search the manor and its grounds for any clues or artifacts that may shed light on Batman's past.")
    print("2. Use the Justice League's resources to scan the area for hidden passages or secret entrances.")
    print("3. Contact Batman directly and ask for his assistance in the investigation.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nYou split up, each member of the Justice League using their unique abilities to search every nook and cranny of Wayne Manor.")
        time.sleep(4)
        print("\nSuperman's X-ray vision reveals hidden chambers and secret compartments, while Wonder Woman's lasso uncovers long-forgotten artifacts and relics.")
        time.sleep(4)
        print("\nTogether, you piece together clues from Batman's past, each discovery bringing you one step closer to unraveling the mystery of Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nHowever, there's no sign of Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nUndeterred, you vow to continue your search, knowing that the fate of Gotham City hangs in the balance.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "2":
        print("\nYou utilize the Justice League's advanced technology to scan the area for hidden passages or secret entrances.")
        time.sleep(4)
        print("\nBatman's Batcomputer analyzes the data, pinpointing several potential locations of interest within the manor and its grounds.")
        time.sleep(4)
        print("\nArmed with this information, you set out to investigate each site, determined to leave no stone unturned in your search for Commissioner Gordon.")
        time.sleep(4)
        print("\nHowever, despite your best efforts, there's no sign of Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nAs frustration mounts, you realize that time is running out, and you must redouble your efforts if you hope to uncover the truth.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "3":
        print("\nYou contact Batman directly, asking for his assistance in the investigation.")
        time.sleep(4)
        print("\nReluctantly, Batman agrees to help, joining forces with the Justice League to uncover the truth behind Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nTogether, you search every inch of Wayne Manor, leaving no stone unturned in your quest for answers.")
        time.sleep(4)
        print("\nHowever, despite your best efforts, there's no sign of Gordon or any clue to his whereabouts.")
        time.sleep(4)
        print("\nAs the hours pass, frustration mounts, and you realize that time is running out.")
        time.sleep(4)
        print("\nYou must redouble your efforts and explore every avenue if you hope to uncover the truth behind Gordon's disappearance.")
        time.sleep(4)
        continue_or_exit3()
    else:
        print("Invalid choice. Please try again.")
        explore_wayne_manor_with_justice_league()
def continue_or_exit_alternative():
    while True:
        continue_game_alternative()
def patrol_gotham_streets():
    print("\nYou take to the streets of Gotham, your senses alert for any sign of trouble or wrongdoing.")
    time.sleep(4)
    print("\nThe city is alive with activity, each shadow and alleyway holding the potential for danger or discovery.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Question locals and gather information about recent disturbances or suspicious activity.")
    print("2. Investigate known criminal hotspots, hoping to uncover any leads or clues related to Commissioner Gordon's disappearance.")
    print("3. Keep an eye out for any signs of Batman or his associates, knowing that they may hold the key to unlocking the mystery.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nYou question locals and gather information about recent disturbances or suspicious activity.")
        time.sleep(4)
        print("\nWhile most of the rumors are nothing more than idle gossip, one particular story catches your attention.")
        time.sleep(4)
        print("\nAccording to a witness, Commissioner Gordon was spotted near Crime Alley, investigating reports of a new criminal organization operating in the area.")
        time.sleep(4)
        print("\nCould this be the lead you've been searching for?")
        time.sleep(4)
        print("\nWith renewed determination, you make your way to Crime Alley, ready to confront whatever dangers lie in wait.")
        time.sleep(4)
        continue_or_exit_alternative()
    elif decision == "2":
        print("\nYou investigate known criminal hotspots, hoping to uncover any leads or clues related to Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nWhile most of your inquiries yield little results, one particular location stands out.")
        time.sleep(4)
        print("\nThe Iceberg Lounge, a notorious nightclub owned by the Penguin, has been abuzz with rumors of a new player in Gotham's underworld.")
        time.sleep(4)
        print("\nCould this mysterious figure be connected to Gordon's disappearance?")
        time.sleep(4)
        print("\nWith a sense of anticipation, you make your way to the Iceberg Lounge, ready to confront whoever or whatever lies within.")
        time.sleep(4)
        continue_or_exit_alternative()
    elif decision == "3":
        print("\nYou keep an eye out for any signs of Batman or his associates, knowing that they may hold the key to unlocking the mystery.")
        time.sleep(4)
        print("\nWhile you don't encounter the Dark Knight himself, you do stumble upon a clue that may prove crucial to your investigation.")
        time.sleep(4)
        print("\nA piece of torn fabric, bearing the emblem of the Bat, lies discarded in a nearby alleyway.")
        time.sleep(4)
        print("\nCould this be a message from Batman, signaling his involvement in the case?")
        time.sleep(4)
        print("\nWith renewed determination, you pocket the fabric and continue your patrol, ready to face whatever challenges lie ahead.")
        time.sleep(4)
        continue_or_exit_alternative()
    else:
        print("Invalid choice. Please try again.")
        patrol_gotham_streets()

# Game Over Scenarios
def game_over():
    print("\nGAME OVER")
    print("The investigation into Commissioner Gordon's disappearance has stalled, and Gotham City remains shrouded in darkness.")
    print("Your failure to uncover the truth has left the city vulnerable to the machinations of its enemies, and the consequences may be dire.")
    print("Perhaps in another time, another world, things could have been different.")
    print("But here and now, there is only darkness.")
    print("\nThank you for playing!")

def game_over_bad_ending():
    print("\nGAME OVER")
    print("Your actions have only served to escalate the situation, and now Gotham City stands on the brink of chaos.")
    print("Your misguided attempts to uncover the truth have only brought more suffering to the city and its inhabitants.")
    print("As you languish in your cell, you can only wonder how things could have gone differently.")
    print("But in the end, it's too late for regrets.")
    print("\nThank you for playing!")

def game_over_worst_ending():
    print("\nGAME OVER")
    print("Your descent into darkness has left a trail of destruction in its wake, and now there's no turning back.")
    print("The city you once swore to protect now lies in ruins, a testament to your failure and betrayal.")
    print("As you sit in your prison cell, you can only reflect on the choices that led you down this path.")
    print("In the end, there are no winners in Gotham, only survivors.")
    print("\nThank you for playing!")

def game_over_guilty_ending():
    print("\nGAME OVER")
    print("Your quest for justice has only brought more pain and suffering to Gotham City.")
    print("Your actions, while well-intentioned, have led to dire consequences for the city and its inhabitants.")
    print("As you reflect on your failures, you can't help but feel a sense of guilt and remorse.")
    print("But in the end, the city is stronger than any one individual, and it will endure, despite the darkness that surrounds it.")
    print("\nThank you for playing!")

# Introduction
def start_game():
    print("Welcome to Gotham City, detective.")
    time.sleep(2)
    print("Commissioner Gordon has gone missing under mysterious circumstances, and it's up to you to uncover the truth.")
    time.sleep(3)
    print("The fate of Gotham City hangs in the balance, and every decision you make will shape its future.")
    time.sleep(3)
    print("Are you ready to begin your investigation?")
    time.sleep(2)
    print("\nChoose your path wisely, for the road ahead is fraught with danger and deception.")
    time.sleep(3)
    print("Let the hunt for truth begin.")

    print("\nYou enter the police department, ready to gather information from your colleagues.")
    time.sleep(4)
    print("As you approach your desk, you notice a file labeled 'TOP SECRET' lying conspicuously on the table.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Open the file and investigate its contents.")
    print("2. Leave the file untouched and continue with your investigation.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou open the file and discover evidence of a vast conspiracy surrounding Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nHowever, before you can investigate further, you're interrupted by a knock on the door.")
        time.sleep(3)
        print("\nDetective Bullock enters the room, his expression grave.")
        time.sleep(3)
        print("\n'We need to talk,' he says, his voice barely above a whisper.")
        time.sleep(3)
        outcome_a1()
    elif decision == "2":
        print("\nYou decide to leave the file untouched and focus on your investigation.")
        time.sleep(3)
        print("\nAs you gather information from your colleagues, you can't shake the feeling that you're missing something important.")
        time.sleep(4)
        print("\nHowever, with no other leads to pursue, you decide to leave the police department and continue your investigation elsewhere.")
        time.sleep(4)
        continue_game()
    else:
        print("Invalid choice. Please try again.")
        start_game()

# Start the game
start_game()
