"""
Background Story: In this game, players dive into the heart of Gotham City's mysteries as Martian Manhunter and they investigate the disappearance of Commissioner Gordon. The journey begins with crucial choices: collaborate with colleagues or pursue the investigation alone. From there, players embark on a thrilling adventure, exploring Arkham Asylum, Wayne Manor, and the streets of Gotham, encountering Batman and the Justice League along the way. Key moments include discovering a spell book, unraveling the truth behind Gordon's disappearance, and confronting challenging dilemmas. Ultimately, players navigate through multiple endings, from success to failure, culminating in a gripping conclusion that reflects their choices and actions throughout the game.
Short Overview: 
Investigate Commissioner Gordon's disappearance in Gotham City as Martian Manhunter, encountering Batman, the Justice League, and unraveling the truth through pivotal choices. Navigate through multiple endings, from success to failure, shaping the fate of Gotham in this thrilling adventure. 

Import necessary libraries
import time

Function to display introduction and start the game
function start_game():
    intro()

Function to introduce the player to the game
function intro():
    print("Hello, Green Martian!")
    time.sleep(2)
    print("Welcome to Gotham City...")
    time.sleep(4)
    print("Your mission is to uncover the mystery behind Commissioner Gordon's disappearance.")
    time.sleep(5)
    print("You find yourself standing outside the Gotham City Police Department...")
    time.sleep(3)
    input("Press Enter to begin your investigation...")
    investigate_police_department()

Function to prompt the player to continue or exit the game
function continue_or_exit():
    loop:
        choice = input("Do you want to continue playing? (yes/no): ")
        if choice.lower() == "yes":
            continue_game()
            break
        else if choice.lower() == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")
Function to investigate the Gotham City Police Department
function investigate_police_department():
    print("As you step into the Gotham City Police Department...")
    time.sleep(3)
    print("What will you do?")
    print("1. Search Commissioner Gordon's office for clues.")
    print("2. Speak with officers and gather information.")
    decision = input("Enter your choice (1/2): ")
    if decision == "1":
        outcome_a1()
    else if decision == "2":
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        investigate_police_department()

Function to handle outcome a1
function outcome_a1():
    print("Carefully searching through Commissioner Gordon's office...")
    time.sleep(3)
    print("What will you do?")
    print("1. Attempt to decrypt the files.")
    print("2. Leave them for now and search elsewhere.")
    print("3. ShapeShift into Commissioner Gordon to unlock the encrypted files.")
    decision = input("Enter your choice (1/2/3): ")
    if decision == "1":
        decrypt_files()
    else if decision == "2":
        print("You decide to leave the files for now and search for other leads.")
        outcome_b1()
    else if decision == "3":
        print("You shapeshifted into Commissioner Gordon in the corner of his room.")
        outcome_b2()
    else:
        print("Invalid choice. Please try again.")
        outcome_a1()

Function to decrypt files
function decrypt_files():
    print("You begin the decryption process...")
    time.sleep(3)
    print("What will you do?")
    print("1. Continue decrypting the files, risking exposure.")
    print("2. Leave the files for now and search elsewhere.")
    decision = input("Enter your choice (1/2): ")
    if decision == "1":
        continue_decryption()
    else if decision == "2":
        print("You reluctantly leave the files behind...")
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        decrypt_files()

Function to continue decryption
function continue_decryption():
    print("Hours pass as you tirelessly work to decrypt the files...")
    time.sleep(3)
    print("You've cracked the encryption!...")
    time.sleep(3)
    outcome_a1_1()

Function to handle outcome a1_1
function outcome_a1_1():
    print("Among the decrypted files...")
    print("What will you do next?")
    print("1. Share the evidence with Batman for further analysis.")
    print("2. Keep the evidence and continue the investigation alone.")
    decision = input("Enter your choice (1/2): ")
    if decision == "1":
        print("You decide to share the evidence with Batman...")
        continue_or_exit()
    else if decision == "2":
        print("You choose to keep the evidence...")
        continue_or_exit()
    else:
        print("Invalid choice. Please try again.")
        outcome_a1_1()

Function to handle outcome b1
function outcome_b1():
    print("You approach a group of officers...")
    time.sleep(3)
    print("What will you do?")
    print("1. Press the officers for information, using your authority.")
    print("2. Try to earn their trust before asking any questions.")
    decision = input("Enter your choice (1/2): ")
    if decision == "1":
        print("You adopt a firm tone...")
        game_over()
    else if decision == "2":
        print("Recognizing the officers' apprehension...")
        continue_or_exit()
    else:
        print("Invalid choice. Please try again.")
        outcome_b1()

Function to handle outcome b2
function outcome_b2():
    print("You shapeshift into Commissioner Gordon...")
    time.sleep(3)
    print("What will you do?")
    print("1. Kill the guards.")
    print("2. Try to earn their trust by stating you are Commissioner Gordon.")
    print("3. Flee from the scene.")
    print("4. Enter their body to erase their memory.")
    decision = input("Enter your choice (1/2/3/4): ")
    if decision == "1":
        game_over_worst_ending()
    else if decision == "2":
        continue_or_exit()
    else if decision == "3":
        game_over()
    else if decision == "4":
        continue_or_exit()
    else:
        print("Invalid choice. Please try again.")
        outcome_b2()

Function to handle game over scenario
function game_over():
    print("Game over! You failed to uncover the mystery.")
    continue_or_exit()

Function to handle the worst ending scenario
function game_over_worst_ending():
    print("Game over! You chose a disastrous path.")
    continue_or_exit()

Function to continue the game
function continue_game():
    print("You decide to continue your investigation...")
    time.sleep(2)
     Call the next scenario or function here

function continue_or_exit():
    loop:
        choice = input("Do you want to continue playing? (yes/no): ")
        if choice.lower() == "yes":
            continue_game()
            break
        else if choice.lower() == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")

Function to handle the best ending scenario
function game_over_best_ending():
    print("Congratulations! You have successfully solved the mystery.")
    continue_or_exit()

Function to handle the guilty ending scenario
function game_over_guilty_ending():
    print("Game over! You chose a path that led to failure.")
    continue_or_exit()

Function to handle the lost ending scenario
function game_over_lost_ending():
    print("Game over! You were unable to complete your mission.")
    continue_or_exit()

Function to handle the continuation of the game after encountering the Joker
function continue_or_exit2():
    loop:
        choice = input("Do you want to continue playing? (yes/no): ")
        if choice.lower() == "yes":
            continue_game2()
            break
        else if choice.lower() == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")

Function to continue the game after encountering the Joker
function continue_game2():
    print("You decide to continue your investigation...")
    time.sleep(2)
     Call the next scenario or function here
Function to handle the continuation of the game after successfully solving the mystery
function continue_or_exit3():
    loop:
        choice = input("Do you want to continue playing? (yes/no): ")
        if choice.lower() == "yes":
            continue_game3()
            break
        else if choice.lower() == "no":
            print("Thank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")

Function to handle the continuation of the game after successfully solving the mystery
function continue_game3():
    print("You continue your journey in Gotham City...")
    time.sleep(2)
    # Call the next scenario or function here

function joker():
    print("You encounter the Joker...")
    time.sleep(2)
    print("What will you do?")
    print("1. Confront and fight the Joker.")
    print("2. Try to read Joker's mind by getting into his body.")
    print("3. Take the spellbook from Joker and inform Batman.")
    decision = input("Enter your choice (1/2/3): ")
    if decision == "1":
        game_over_worst_ending()
    else if decision == "2":
        continue_or_exit2()
    else if decision == "3":
        continue_or_exit3()
    else:
        print("Invalid choice. Please try again.")
        joker()


function win_game():
    print("Congratulations! You have successfully solved the mystery of Commissioner Gordon's disappearance and saved Gotham City.")
    print("You are a true hero!")
    exit_game()


function exit_game():
    print("Thank you for playing 'Gotham City'. Goodbye!")
    exit()


start_game()



"""

import time

def intro():
    print(" \n Hello Green Martian")
    time.sleep(3)
    print("\n Welcome to Gotham City,  a sprawling urban jungle shrouded in darkness, where towering skyscrapers cast long shadows over the streets below. "
          "But tonight, Gotham's darkness runs deeper than ever. The esteemed Commissioner Gordon, a beacon of justice, has vanished without a trace, "
          "leaving behind a city gripped by fear and uncertainty. Amidst whispers of conspiracy and villainy, Gotham's fate hangs in the balance.")
    time.sleep(6)
    print("\n Your mission is to unravel the mystery behind Commissioner Gordon's disappearance in Gotham City. "
          "Navigate through the city's darkest alleys, expose hidden secrets, and make decisions that will determine the fate of Gotham.")
    time.sleep(5)
    print("\n Your next step is to investigate the Gotham City Police Department. This is a pivotal location filled with potential clues "
          "that could unravel the mystery. \nYour choices will either restore hope to Gotham or plunge it deeper into darkness.")
    time.sleep(3)
    input("\nPress Enter to begin your investigation...")
    investigate_police_department()

def continue_or_exit():
    while True:
        continue_game()
def continue_or_exit_alternative():
    while True:
        continue_game_alternative()
def continue_or_exit2_alternative():   
    while True:
        continue_game2_alternative()             
           
def continue_or_exit2():
    print("With your newly found truth. You can't trust anyone")
    while True:
        continue_game2()
            
def continue_or_exit3():
    time.sleep(2)
    continue_game3()

def continue_or_exit4():
    time.sleep(2)
    continue_game4()            

def game_over():
    print("\nMission Failed!")
    print("\nYou messed up, and now Gotham is in trouble. Commissioner Gordon is still missing, and the city's hope dwindles. "
          "People are talking, and they're not happy with you. Your reputation is tarnished. Your once-admired name is now associated with Gotham's darkest hour.")
    print("\nAs days pass, Gotham's chaos grows. Without its stalwart defender, the city spirals deeper into uncertainty. "
          "Your mission's failure casts a long shadow, affecting not just you, but the very soul of Gotham.")
    print("\nBetter luck next time!")
    time.sleep(7)
    while True:
        choice = input("\nDo you want to restart the game? (yes/no): ").strip().lower()
        
        if choice == "yes":
            intro()  # Restart the game
            break
        elif choice == "no":
            print("\nThank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to restart or 'no' to exit.")

def investigate_police_department():
    print("\nAs you step into the Gotham City Police Department, the atmosphere is tense, "
          "with officers rushing about, their faces etched with concern and determination. "
          "Your eyes are immediately drawn to Commissioner Gordon's office, now vacant and foreboding.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Search Commissioner Gordon's office for clues.")
    print("2. Speak with officers and gather information.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        outcome_a1()
    elif decision == "2":
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        investigate_police_department()

def outcome_a1():
    print("\nCarefully searching through Commissioner Gordon's office, you uncover a hidden compartment behind a bookshelf. "
          "Inside, you find a dossier labeled 'Top Secret' and a set of encrypted files protected by fingerprint scanner. These could hold vital information about Gordon's disappearance.")
    time.sleep(4)
    print("\nThe dossier appears to contain sensitive information about Gotham's underworld, including known criminal activities and potential suspects.")
    print("\nWhat will you do?")
    print("1. Attempt to decrypt the files.")
    print("2. Leave them for now and search elsewhere.")
    print("3. ShapeShift into comissioner Gordon to unlock the encrypted files .")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        decrypt_files()
    elif decision == "2":
        print("\nYou decide to leave the files for now and search for other leads.")
        outcome_b1()
    elif decision == "3":
        print("\nYou shapeshifted into Comissioner Gordon in the corner of his room.")
        outcome_b2()    
    else:
        print("Invalid choice. Please try again.")
        outcome_a1()

def decrypt_files():
    # Function to decrypt files
    print("\nYou begin the decryption process, using your expertise to crack the code. The files contain a wealth of information, "
          "including surveillance footage, intercepted communications, and confidential reports. ")
    time.sleep(4)
    print("\nHowever, as you delve deeper, you realize that the encryption is more complex than anticipated. It will take time to decipher the files.")
    print("\nWhat will you do?")
    print("1. Continue decrypting the files, risking exposure.")
    print("2. Leave the files for now and search elsewhere.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou decide to press on, knowing that time is of the essence. With each passing moment, you edge closer to unlocking the truth behind Commissioner Gordon's disappearance.")
        time.sleep(4)
        # Continue decryption process
        continue_decryption()
    elif decision == "2":
        print("\nYou reluctantly leave the files behind, knowing that every moment wasted could mean another innocent life in danger.")
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        decrypt_files()

def continue_decryption():
    # Function to simulate decryption process
    print("\nHours pass as you tirelessly work to decrypt the files. Each line of code feels like a piece of a puzzle, "
          "slowly revealing the bigger picture. Suddenly, a breakthrough!")
    time.sleep(4)
    print("\nYou've cracked the encryption! The files reveal a web of corruption within Gotham, implicating key figures in the city's criminal underworld.")
    print("\nArmed with this newfound knowledge, you prepare to take the next step in your investigation.")
    time.sleep(4)
    # Proceed with investigation
    outcome_a1_1()

def outcome_a1_1():
    print("\nAmong the decrypted files, you find evidence pointing to several individuals who may have had a hand in Commissioner Gordon's disappearance.")
    print("\nWhat will you do next?")
    print("1. Share the evidence with Batman for further analysis.")
    print("2. Keep the evidence and continue the investigation alone.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou decide to share the evidence with Batman, recognizing his unparalleled skills and resources. "
              "Handing over the files, you see the determination in Batman's eyes as he vows to uncover the truth and bring Commissioner Gordon home safely.")
        time.sleep(5)
        print("\nWith Batman on the case, you continue your investigation, knowing that Gotham's Dark Knight will stop at nothing to bring justice to the city.")
        time.sleep(4)
        continue_or_exit4()
    elif decision == "2":
        print("\nYou choose to keep the evidence and pursue the investigation alone, determined to see justice served without outside interference.")
        time.sleep(4)
        print("\nAs you delve deeper into the case, you realize the gravity of the situation. Commissioner Gordon's life may hang in the balance, "
              "and every decision you make could have far-reaching consequences for Gotham.")
        time.sleep(5)
        print("\nWith determination in your heart, you vow to uncover the truth and bring Commissioner Gordon home safely, no matter the cost.")
        time.sleep(4)
        continue_or_exit2()
    else:
        print("Invalid choice. Please try again.")
        outcome_a1_1()

def outcome_b1():
    print("\nYou approach a group of officers, hoping to gather information about Commissioner Gordon's disappearance.")
    time.sleep(3)
    print("\nHowever, the officers seem hesitant to speak openly, their expressions guarded and wary.")
    time.sleep(2)
    print("\nWhat will you do?")
    print("1. Press the officers for information, using your authority.")
    print("2. Try to earn their trust before asking any questions.")
    print("3. Use your hypnosis power to read their mind.")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nYou adopt a firm tone, demanding answers from the officers. However, your authoritative approach only serves to alienate them further, "
              "and they clam up, refusing to divulge any information.")
        time.sleep(4)
        print("\nFrustrated by the lack of cooperation, you leave the police department empty-handed, your investigation stalled.")
        time.sleep(4)
        game_over()
    elif decision == "2":
        print("\nRecognizing the officers' apprehension, you adopt a more empathetic approach, taking the time to build rapport and earn their trust.")
        time.sleep(4)
        print("\nSlowly but surely, the officers begin to open up, sharing tidbits of information that could prove crucial to your investigation.")
        time.sleep(4)
        print("\nArmed with newfound leads, you leave the police department with renewed determination, ready to pursue the truth wherever it may lead.")
        time.sleep(4)
        continue_or_exit2()
    elif decision == "3":
        print("\nSlowly but surely, the officers begin to open up their mind, sharing tidbits of information that could prove crucial to your investigation.")
        
        time.sleep(4)
        
        print("\nYou found out about Gordon's secret decrypted file and you also found the password. You Decided to Head for Gordon's office to get information from the file")
  
        time.sleep(4)
        print("\nArmed with newfound leads, you leave the police department with renewed determination, ready to pursue the truth wherever it may lead.")
        print("Clue = The disapperance is related to Batman")
        time.sleep(4)
        continue_or_exit2_alternative()

    else:
        print("Invalid choice. Please try again.")
        outcome_b1()
def outcome_b2():
    print("\nYou Shapeshift into Comissioner Gordon, hoping to encrypt the files.")
    time.sleep(3)
    print("\nHowever, you did not notice the hidden camera in the corner of the room.")
    print("\nBefore you can do anything guards enter the room")
    print("1. Kill the guards")
    print("2. Try to earn their trust by stating you are Comissioner Gordon.")
    print("3. Flee from the scene ")
    print("4. Enter their body to erase their memory. ")

    decision = input("Enter your choice (1/2/3/4): ")

    if decision == "1":
        print("\nYou did the unthinkable. To serve justice you took the wrong path.")
        time.sleep(4)
        print("\nBatman found out what you did. He captured you and put in a special cage that can hold Aliens from Mars.")
        time.sleep(4)
        game_over_worst_ending()
    elif decision == "2":
        print("\nRecognizing the officers' apprehension, you adopt a more empathetic approach, taking the time to build rapport and earn their trust.")
        time.sleep(4)
        print("\nSlowly but surely, the officers begin to open up, sharing tidbits of information that could prove crucial to your investigation.")
        time.sleep(4)
        print("\nAfter they leave you encrypt the files and gather information.")
        time.sleep(4)

        print("\nArmed with newfound leads, you leave the police department with renewed determination, ready to pursue the truth wherever it may lead.")
        time.sleep(4)
        print("\nBut you forgot to erase the footage from the hidden security camera.")
        time.sleep(4)
        game_over_bad_ending()
    elif decision == "3":
        print("\nYou used your ability to fly through the walls")
        time.sleep(4)
        print("\nBatman found out what you did. suggested you to get off the case. You are making things bad.")
        time.sleep(4)
        game_over()    
    elif decision == "4":
        print("\nYou entered their body and erased their memory where you discovered the camera position.")
        time.sleep(4)
        print("\nYou wandered into the soldiers memories to find some lead, then you also hypnotised them to clear the footage from security camera.")
        time.sleep(4)
        print("\nAfter making them leave the room, you unlocked the encrypted files with Comissioner Gordons fingerprint.")
        time.sleep(4)
        print("\nYou found out Gordon's disappearance is related to Batman")
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
    print("\nAfter you got clue from the Arkham Asylum, you decided to continue")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Explore the abandoned Wayne Manor, searching for clues from Batman's past.")
    print("2. Patrol the streets of Gotham, listening for whispers of conspiracy and intrigue.")

    decision = input("Enter your choice (1/2/3): ")

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
    print("2. Contact the Justice league and Explore the abandoned Wayne Manor With Justice League, searching for clues from Batman's past.")
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
def continue_game2_alternative():
    print("\nYou are in a Dilemma that you can trust Batman or not")
    time.sleep(4)
    print("\nDo you Trust Batman?")
    print("1. Yes")
    print("2. No")
    

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        investigate_arkham_asylum_with_justice_league()
    elif decision == "2":
        print(" Keep Batman in a House arrest with 24/7 survellence for everyone's safety")
        time.sleep(2)
        print(" You have a call from the Arkham Asylym that Ridder wants to talk to you so you head out to Arkhm Asylym")
        time.sleep(2)
        print("Clue = Talk to *RIDDLER* ")
        investigate_arkham_asylum_with_justice_league2()
 
    else:
        print("Invalid choice. Please try again.")
        
        continue_game2_alternative()       
def continue_game3():
    print("\nContinuing your investigation, you ponder your next move. There are still many unanswered questions, "
          "and time is running out. The fate of Commissioner Gordon and Gotham City hangs in the balance.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("\n1. Give up")
    print("2. Patrol the streets of Gotham, listening for whispers of conspiracy and intrigue.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        game_over_guilty_ending()
    elif decision == "2":
        patrol_gotham_streets()
    else:
        print("Invalid choice. Please try again.")    
        continue_game3()       
def continue_game4():
    print("\nBatman Contacted Justice League to help with this case as he suspects the danger is far greater than it appears.")
    time.sleep(4)
    print("\nWhere will you go next?")
    print("1. Investigate Arkham Asylum, where Gotham's most dangerous criminals are held.")
    print("2. Interrogate Joker as Batman confidently suspects 'His shoes are dirty' ")

    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        investigate_arkham_asylum_with_justice_league()
    elif decision == "2":
        joker()
    else:
        print("Invalid choice. Please try again.")
        
        continue_game4()


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
        print("Clue=Gordon was last seen talking to Riddler about Batman, but this information seems irrelavent. ")
        time.sleep(4)
        decision = input("Do you want to talk to riddler? (1.Yes/2.NO): ")
        if decision=="1":
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
    elif decision=="2":
        print("You got lead from the inside")
        print("Clue= Batman is involved in this")
        continue_game2_alternative()
            
    else:
        print("Invalid choice. Please try again.")
        investigate_arkham_asylum_with_justice_league()
def question_riddler():
    print("\nYou interrogation Riddler.")
    time.sleep(3)
    print("\nHe seems to know something that he is not saying.")
    time.sleep(4)
    print("\nCould this be the breakthrough you've been searching for?")
    time.sleep(3)
    print("\nSo you investigate his cell and find a riddle")
    time.sleep(4)
    print("\nThe riddle is'What happend when you Cross the bridge of time")
    time.sleep(4)
    print("\nWhat is the answer of the riddle?")
    time.sleep(3)
    print("\n1.Time travel is not possible?")
    print("\n2.I dont know?")
    print("\n3.Beat up Riddler?")
    decision = input("Enter your choice (1/2): ")
    if decision == "1":
        print("You failed to find any lead from here")
        continue_or_exit3()
    elif decision == "2":
        joker()
    elif decision == "3":
        game_over_worst_ending()    
    
    else:
        print("Invalid choice. Please try again.")
        question_riddler()
        

def investigate_arkham_asylum_with_justice_league2():
    print("\nAs Justice League approach Arkham Asylum,Joker is hiding in a corner and the inmates are scared to see the whole justice league except for Riddler. This institution houses some of Gotham's most dangerous criminals, "
          "each more unhinged than the last.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Speak with the staff and inmates, hoping to uncover any information about Commissioner Gordon's disappearance.")
    print("2. Search the asylum's records for any mentions of Gordon or recent disturbances.")
    print("3. Question Riddler about his motive")
    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("\nWasting time. Lets talk with riddler")
        time.sleep(4)
        question_riddler()
        investigate_arkham_asylum_with_justice_league2()
    elif decision == "2":
        print("\nI already know these information. Lets talk with Riddler")
        time.sleep(4)
        question_riddler()
        investigate_arkham_asylum_with_justice_league2()
    elif decision == "3":
        question_riddler()
        
        
    else:
        print("Invalid choice. Please try again.")
        investigate_arkham_asylum_with_justice_league2()



def explore_wayne_manor():
    print("\nWayne Manor stands as a silent sentinel atop the hills overlooking Gotham City, its imposing facade a testament to a bygone era.")
    time.sleep(4)
    print("\nAs you step through the overgrown gardens and crumbling hallways, you're reminded of the Wayne family's storied past.")
    time.sleep(4)
    print("\nWhat will you do?")
    print("1. Search for clues in the Wayne family archives, hoping to uncover any connections to Commissioner Gordon's disappearance.")
    print("2. Explore the secret passages and hidden chambers rumored to exist within the manor.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou make your way to the Wayne family archives, where centuries of history are preserved in dusty tomes and faded photographs.")
        time.sleep(4)
        print("\nAmidst the stacks of books and artifacts, you find mention of a longstanding alliance between the Waynes and the GCPD, "
              "forged in the crucible of Gotham's darkest hours.")
        time.sleep(4)
        print("\nCould this alliance hold the key to Commissioner Gordon's disappearance?")
        time.sleep(3)
        print("\nWith newfound purpose, you vow to delve deeper into the Wayne family's legacy, knowing that the answers you seek may be hidden within the pages of history.")
        time.sleep(4)
        continue_or_exit()
    elif decision == "2":
        print("\nRumors of secret passages and hidden chambers echo through the halls of Wayne Manor, whispered by those who dare to tread its haunted halls.")
        time.sleep(4)
        print("\nWith curiosity as your guide, you embark on a journey through the manor's labyrinthine corridors, searching for any signs of the past.")
        time.sleep(4)
        print("\nAs you explore further, you stumble upon a concealed chamber, its entrance hidden behind a bookshelf.")
        time.sleep(3)
        print("\nInside, you find a cache of documents and artifacts, each hinting at a deeper mystery.")
        time.sleep(3)
        print("\nCould this be what you've been searching for?")
        time.sleep(3)
        print("\nWith newfound determination, you prepare to uncover the truth behind Commissioner Gordon's disappearance, no matter where the path may lead.")
        time.sleep(4)
        continue_or_exit2()
    else:
        print("Invalid choice. Please try again.")
        explore_wayne_manor()

def patrol_gotham_streets():
    print("\nAs you patrol the streets of Gotham, you can't help but feel a sense of unease. The city is a powder keg, ready to explode at any moment.")
    time.sleep(4)
    print("\nEvery shadow seems to conceal a new threat, every alleyway a potential danger.")
    time.sleep(3)
    print("\nWhat will you do?")
    print("1. Listen for rumors and whispers among the city's inhabitants, hoping to glean any information about Commissioner Gordon's disappearance.")
    print("2. Investigate recent disturbances in the hopes of finding a lead.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou move through the streets with a keen ear, listening for any hints or whispers that may lead you to the truth.")
        time.sleep(4)
        print("\nAmidst the hustle and bustle of the city, you pick up fragments of information, each adding a new layer to the mystery surrounding Commissioner Gordon's disappearance.")
        time.sleep(4)
        print("\nThough the truth remains elusive, you leave the streets of Gotham with a renewed sense of purpose, determined to uncover the secrets hidden within the city's heart.")
        time.sleep(4)
        investigate_arkham_asylum_with_justice_league()
    elif decision == "2":
        print("\nYou investigate recent disturbances throughout the city, following a trail of breadcrumbs that leads you deeper into the heart of Gotham's darkness.")
        time.sleep(4)
        print("\nWith each clue you uncover, the true scope of the conspiracy becomes clearer, and you realize that Commissioner Gordon's disappearance may be just the tip of the iceberg.")
        time.sleep(4)
        print("\nArmed with this newfound knowledge, you leave the streets behind, ready to confront the forces that threaten to tear Gotham apart.")
        time.sleep(4)
        investigate_arkham_asylum_with_justice_league()
    else:
        print("Invalid choice. Please try again.")
        patrol_gotham_streets()
def explore_wayne_manor_with_justice_league():
    print("\nAfter investigating secretly on Batman , you found out nothing that ties batman to this case")
    print(" There is a security log that says Comissioner Gordon came here before the day of disapperance")        
    print("You decided to ask batman about it so he can explain himself")
    print("Batman got hurt that you did not trust him but he still explained why did Gordon come the day before his disapperance.")
    print("Batman said it was his parent's death anniversiry and he was getting drunk with Gordon. While talking he asked Gordon if he can fix everything again.")
    print("Now what do you want to do")
    print("1. Say sorry to batman and move on with your investigation")
    print("2. Tell batman about the spellbook")
    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        print("\nYou felt guilty about your decision.")
        time.sleep(4)
        print("\nYou said sorry to Batman for misunderstanding")
        time.sleep(4)
        print("\nYou start to question your ability to be a detective.")
        time.sleep(4)
        continue_or_exit3()
    elif decision == "2":
        print("\nBatman get's angry and kills joker")
        time.sleep(4)
        
        game_over_worst_ending()
        

def joker():
    print("Joker starts laughing and says 'Right Answer' at the top of his lungs.")
    time.sleep(4)
    print("\nHe tells you that you are the the right place at the wrong time.")
    time.sleep(4)
    print("\nHe gives you a *Spell Book* which has some writing in it.")
    time.sleep(4)
    print("\nIt seems it is a notebook that can send user to past time if you write the time and date in it. And there is a date on a page and it is the date that Batman's parents were killed. Very few knew it was joker")
    time.sleep(4)

    print("\nEverybody know's Batman's parents died when he was 8 and after that he lost his heart.")
    time.sleep(4)
    print("\nMartian thought joker time traveled to kill the Batman's parents and he also might have killed Comissioner Gordon like that.") 
    time.sleep(2)  
    print("\nWhat would you like to do now.")
    time.sleep(4)   
    print("\n1.Kill joker.")
    print("\n2.Get in joker's body with your superpower and read his mind.")
    print("\n3.Take the book from joker and tell Batman about joker murdering his parent")
    decision = input("Enter your choice (1/2/3): ")

    if decision == "1":
        print("You solved the case in a violent way. But is it the true story that you uncovered or is it another lie")
        game_over_worst_ending()
    elif decision == "2":
        game_over_best_ending()
    elif decision == "3":
        print("Batman got very angry and devasted getting the news that Joker killed his parents. ")
        time.sleep(4)   
        print("\nBatman decided to kill Joker and end the problem.")
        game_over_worst_ending()   
    else:
        print("Invalid choice. Please try again.")
        intro_scenario()
# Game Over Function
def game_over():
    print("\nGAME OVER")
    print("You failed to find lead uncover the truth about Commissioner Gordon's disappearance.")
    print("Without your help, the fate of Gotham City hangs in the balance.")
    print("Thank you for playing!")
    print("You failed at unlocking any ending.")
    exit()
def game_over_guilty_ending():
    print("\nGAME OVER")
    print("You lost all your confidence and decided to return to Mars.")
    print("Without your help, the fate of Gotham City hangs in the balance.")
    print("Thank you for Trying!")
    exit()    
def game_over_bad_ending():
    print("\nGAME OVER")
    print("You found the lead of what happend to Comissioner Gordon.")
    print("But the Security cam footage got leaked and now everyone thinks you are the one who killed/kidnapped Comissioner Gordon")
    print("Thank you for Trying!")
    print("You unlocked the Bad Ending!")
    exit()    
def game_over_worst_ending():
    print("\nGAME OVER")
    print("You failed to uncover the truth about Commissioner Gordon's disappearance.")
    print("With your help things have gone from bad to worse.")
    print("You have unlocked the worst ending!")
    print("Are you proud of yourself now!")
    exit()
def game_over_best_ending():
    time.sleep(1)
    print("\nAs you dive deep in jokers mind, you start getting overwhelmed by joker's thought.")
    time.sleep(1)
    print("There are 3 door's that connect to different memories of joker")
    time.sleep(1)
    print("But be careful if you fail more than once, you might loose your sanity and consciousness forever ")
    fail=0
    while fail<2 :
        decision = input("There is 3 doors infront of you. Choose 1 (1/2/3): ")

        if decision == "1":
            print("You picked the wrong door")
            fail=fail+1
           

        
        elif decision == "2":
            print("You picked the right door")
            game_over_best_ending_mystery_solved()
            break
        elif decision == "3":
            print("You picked the wrong door")
            fail=fail+1  
            
        else:
            print("You walked into the void. You lost yourself. You cant comeback from there.")
            game_over_lost_ending()
    game_over_lost_ending()
def game_over_best_ending_mystery_solved():
    time.sleep(2)
    print("You enter door 2,You see gordon confronting Joker about him killing Batman's parents. ")
    time.sleep(2)
    print("Joker told Gordon that it was his destiny to create the greatest Super Hero in the universe so he can be the greatest villian in the universe")
    time.sleep(2)
    print("After much interrogating Gordon found this spell book of Al' ZAhur the Magician that Joker used to kill Batman's parents.")
    time.sleep(2)
    print("He decided to use that book to travel back to time and stop joker from killing Batman's parents")
    print("Martian Manhunter got out of jokers mind with this discovery and decided to inform Justice League about this discovery.")
    win_game()
def win_game():
    print(" With your discovery your tension arises as you know one can not simply change the timeline with damaging the sacred 'Tree of Time'")    
    time.sleep(2)
    print(" Martian Manhunter knows he must protect the sacred timeline at any cost")
    time.sleep(2)
    print("So he informs the Justice League about the danger of all universes. They assemble again to stop and bring Gordon back while keeping the 'Tree of Time' intact.")
    time.sleep(2)
    print(' This game end here, be ready for the next chapter.')
    time.sleep(2)
    print("You won the game and you unlocked the best possible ending")
    exit()
def game_over_lost_ending():
    print("You are screaming on top of your lungs")
    time.sleep(2)
    print("You cant escape")
    time.sleep(2)  
    print("Game Over")
    time.sleep(2)  
    print("Now someone else needs to investicate your missing report, good job")
    exit()
# Begin the game
def start_game():
    print("Hello Green Martian.")
    time.sleep(2)
    print("Welcome to Gotham City!")
    time.sleep(2)
    print("As you can shapeshift you will be taking place of a detective with the Gotham City Police Department, tasked with investigating the mysterious disappearance of Commissioner James Gordon.")
    time.sleep(4)
    print("Commissioner Gordon is a beloved figure in Gotham, known for his unwavering commitment to justice and his tireless efforts to keep the city safe.")
    time.sleep(4)
    print("However, he has gone missing under suspicious circumstances,Batman is suspecting Two face a.k.a. Harvey Dent is responsible but he isn't able to prove it yet so it's up to you to unravel the mystery and bring him home.")
    time.sleep(4)
    print("Your investigation begins now.")
    time.sleep(2)

    # Start the first scenario
    intro_scenario()

def intro_scenario():
    print("\nYou stand outside Gotham City Police Department, pondering your next move.")
    time.sleep(3)
    print("\nWhat will you do?")
    print("1. Enter the police department and gather information from your colleagues.")
    print("2. Keep the evidence of Commissioner Gordon's disappearance to yourself and pursue the investigation alone.")

    decision = input("Enter your choice (1/2): ")

    if decision == "1":
        outcome_a1()
    elif decision == "2":
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        intro_scenario()

start_game()
