#Christina Joes Simon
#30/12/2023
'''
Background story:
Eaven City, once a beacon of prosperity and unity, finds itself at a crossroads. Nestled amidst towering skyscrapers and bustling streets lies a mystery that
threatens the very heart of this vibrant metropolis. Mayor Eleanor Thompson, a charismatic leader and a symbol of hope for Eaven City, has vanished under
inexplicable circumstances. Her sudden disappearance casts a pall of uncertainty and fear, leaving citizens questioning their safety and the future of their
city. As days turn into weeks, the once-unified city begins to fracture. Rumors swirl, pointing to political conspiracies, rival factions, and dark secrets
lurking in the shadows. Amidst this turmoil, the city's leaders, desperate for answers, turn to you, a renowned detective known for unraveling the most
perplexing of mysteries. Your reputation precedes you, and the weight of Eaven City's future rests squarely on your shoulders. Armed with determination,
wit, and a keen eye for detail, you embark on a perilous journey into the heart of the city's power—the Mayor's Office. Inside the Mayor's Office lies a
labyrinth of secrets, alliances, and betrayals. Every clue, every piece of evidence, holds the key to unlocking the truth behind Mayor Thompson's
disappearance.

Function intro():
    Display message to introduce the player about Eaven City and the situation.
    wait for 6 seconds
    Display mission details about uncovering the Mayor's disappearance
    wait for 5 seconds
    Display instructions to the next step
    wait for 3 seconds
    Prompt user to press Enter to start investigation
    call investigate_mayors_office()
end function

Function continue_or_exit():
    Endless Loop:
    Prompt the player if they want to continue playing or exit the game and remove any leading/trailing whitespace, and convert to lowercase.

        If "yes":
            call continue_game()
            exit loop
        Elif "no":
            display "Thank you for playing! Goodbye."
            exit loop
        Else:
            display an error message for invalid input
end function

Function game_over():
    Display "Mission Failed!"
    Display the outcome of mission failure and its consequences for the city and the player's reputation
    wait for 7 seconds

    Endless Loop:
        Prompt the player if they want to restart or exit the game
        If user chooses to restart:
            call intro()  # Restart the game
            exit loop
        Elif user chooses to exit:
            display a farewell message
            exit loop
        Else:
            display an error message for invalid input
end function

Function investigate_mayors_office():
    Display a scenario for the player upon arriving at the Mayor's Office
    Display options for the player's next move:
        1. Investigate the painting.
        2. Look around the room.

    Prompt the user for their choice (1 or 2)
    
    If user chooses "1":
        call outcome_a1()
    Elif user chooses "2":
        call outcome_b1()
    Else:
        display an error message for invalid input
        call investigate_mayors_office() to allow the player to choose again
end function

Function outcome_a1():
    Display a scenario for the player upon discovering a locked safe behind the painting
    wait for 3 seconds
    Display options for the player's next move:
        1. Attempt to crack the safe.
        2. Leave it for now and look elsewhere.

    Prompt the user for their choice (1 or 2)
    
    If user chooses "1":
        call crack_safe()
    Elif user chooses "2":
        display a message indicating the decision to leave the safe
        call outcome_b1()
    Else:
        display an error message for invalid input
        call outcome_a1() to allow the player to choose again
end function

Function crack_safe():
    Define function validate_input(guess):
        Validate the input to ensure it's a 3-digit number

    Define function provide_hint(code, guess):
        Initialize an empty list named hint
        For each position i in range(3):
            if guess[i] matches code[i]:
                add "✓" to the hint list  # ✓ represents a correct digit in the correct position
            elif guess[i] is present in code:
                add "~" to the hint list   # ~ represents a correct digit but in the wrong position
            else:
                add "✗" to the hint list  # ✗ represents a wrong digit
            endif
        endfor
        return the concatenated string as "Hint: <hint content>"

    Set attempts to 5
    Set safe_code to "739"

    Display instructions and symbols for the safe-cracking process

    Loop while attempts > 0:
        Prompt the user for the guess
        If guess is not a valid 3-digit number:
            display an error message and continue to the next iteration
        Elif guess matches the safe_code:
            display success message and reveal contents
            call outcome_a1_1() function
            exit loop
        Else:
            decrement attempts by 1
            if attempts > 0:
                display incorrect guess message, remaining attempts, and provide a hint
            else:
                display failure messages due to running out of attempts
                call game_over() function
                exit loop
end function

Function outcome_a1_1():
    Display a description of the documents found by the player
    Display options for the player's next move:
        1. Share the documents with the police.
        2. Keep the documents and continue the investigation alone.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a scenario about sharing the documents with the police
        wait for 5 seconds
        display a situation where the player feels uneasy
        provide options to either hide or confront
        call choose_hide_or_confront() function
    Elif user chooses "2":
        display a scenario about the player's decision to keep the documents
        wait for 5 seconds
        call the game_over() function 
    Else:
        display an error message for invalid input
        call outcome_a1_1() to allow the player to choose again
end function

Function outcome_b1():
    Display a scenario of discovering a hidden compartment under the desk
    wait for 4 seconds
    Display options for the player's next move:
        1. Explore the hidden compartment.
        2. Ignore and look elsewhere.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a narrative about finding a mysterious key within the hidden compartment
        call the outcome_b1_1() function
    Elif user chooses "2":
        display a narrative about not finding any valuable evidence and leaving the premises
        wait for 4 seconds
        display a narrative about the consequences of overlooking a critical document 
        wait for 5 seconds
        call the game_over() function 
    Else:
        display an error message for invalid input
        call outcome_b1() to allow the player to choose again
end function

Function outcome_b1_1():
    Display options for the player's next move:
        1. Use the key on a locked drawer noticed earlier.
        2. Ignore the key and continue investigating.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a narrative about using the key 
        wait for 4 seconds
        display a narrative about successfully opening the drawer and finding potentially important documents
        call the outcome_a1_1() function 
    Elif user chooses "2":
        display a narrative about deciding not to use the key 
        wait for 3 seconds
        call the game_over() function 
    Else:
        display an error message for invalid input
        call outcome_b1_1() to allow the player to choose again
end function

Function choose_hide_or_confront():
    Prompt the user for their choice (1 or 2)
    
    If user chooses "1":
        display a narrative of observing shadowy figures 
        wait for 5 seconds
        display options for the player's next move:
            1. Quietly exit the room.
            2. Confront them now.

        Prompt the user for their choice (1 or 2)

        if user chooses "1":
            display a narrative of slipping out quietly 
            wait for 4 seconds
            call continue_or_exit() function
        elif user chooses "2":
            display a narrative of confronting the figures 
            wait for 3 seconds
            call game_over() function
        else:
            display an error message for invalid input
            call choose_hide_or_confront()

    Elif user chooses "2":
        display a narrative of direct confrontation
        wait for 3 seconds
        call game_over() function
    Else:
        display an error message for invalid input
        call choose_hide_or_confront() 
end function

Function continue_game():
    Display a scenario where a cryptic message received
    Display the option whether to go to the warehouse or not
    
    Prompt the user for their choice (yes or no) and convert to lowercase
    
    If user chooses to go ("yes"):
        display a scenario about the decision to go to the warehouse
        wait for 3 seconds
        call warehouse_scenario() function
    Elif user chooses not to go ("no"):
        display a scenario about choosing not to go
        wait for 2 seconds
        display a narrative about the case remaining unsolved
        wait for 3 seconds
        call game_over() function
    Else:
        display an error message for invalid input
        call continue_game() 
end function

Function warehouse_scenario():
    Display a scenario as the player cautiously enters the warehouse and encounters 'Shadow'
    wait for 7 seconds
    Display options for investigating three different individuals:
        1. Vincent Blackwood - wealthy magnate
        2. Elena Martinez - rising star in city council
        3. Marcus Stone - investigative journalist

    Prompt the user to choose which individual to investigate (1, 2, or 3)

    If user chooses "1":
        call vincent_scenario() function
    Elif user chooses "2":
        call elena_scenario() function
    Elif user chooses "3":
        call marcus_scenario() function
    Else:
        display an error message for invalid input
        call warehouse_scenario() function
end function

Function vincent_scenario():
    Display a scenario as the player enters Vincent Blackwood's office
    Display options to investigate Vincent:
        1. Look into his finances for suspicious transactions.
        2. Follow Vincent discreetly to observe his interactions.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a scenario about investigating Vincent's financial records 
        wait for 6 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Elif user chooses "2":
        display a scenario about shadowing Vincent to an upscale restaurant 
        wait for 7 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Else:
        display an error message for invalid input
        call vincent_scenario() 

    wait for user input to continue (press Enter)
    call continuation() function
end function

Function elena_scenario():
    Display a scenario as the player enters Elena Martinez's office
    Display options to approach Elena:
        1. Approach Elena directly for insights about the Mayor's disappearance.
        2. Investigate her colleagues in the city council for signs of a conspiracy.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a scenario about engaging Elena in conversation 
        wait for 5 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Elif user chooses "2":
        display a scenario about discreetly looking into city council members 
        wait for 5 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Else:
        display an error message for invalid input
        call elena_scenario() 

    wait for user input to continue (press Enter)
    call continuation() function
end function

Function marcus_scenario():
    Display a scenario as the player enters Marcus Stone's office
    Display options to approach Marcus:
        1. Confront Marcus with evidence linking him to the Mayor's disappearance.
        2. Read Marcus's recent articles to find hidden messages or clues.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a scenario about confronting Marcus with evidence
        wait for 6 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Elif user chooses "2":
        display a scenario about diving into Marcus's articles
        wait for 7 seconds
        display a message about continuing the investigation of other suspects
        wait for 2 seconds
    Else:
        display an error message for invalid input
        call marcus_scenario()

    wait for user input to continue (press Enter)
    call continuation() function
end function

Function continuation():
    Display options:
        1. Go to the police station to share all the evidence.
        2. Meet 'Shadow' again to discuss further.

    Prompt the user for their choice (1 or 2)

    If user chooses "1":
        display a scenario about sharing evidence with the police 
        wait for 7 seconds
        display a scenario about the police mobilizing resources, arresting suspects
        wait for 7 seconds
        call end_game() function
    Elif user chooses "2":
        display a scenario about meeting 'Shadow'
        wait for 4 seconds
        display a scenario about being ambushed
        wait for 3 seconds
        call game_over() function
    Else:
        display an error message for invalid input
        call continuation()
end function

Function end_game():
    Display narrative about solving the mystery, bringing justice, and rebuilding the city
    Display a congratulatory message for solving the mystery and achieving justice
    Display a message inviting players to replay the game for different paths or outcomes
end function

Start the game by calling the intro function
'''
import time

def intro():
   
    print("\nWelcome to Eaven City, a metropolis renowned for its bustling streets, shimmering skyscrapers, "
          "and a heartbeat that resonates with promise and ambition."
          " However, today, a shadow looms over this vibrant city. The esteemed Mayor, a symbol of hope, progress,"  
          " and unity, has disappeared, leaving behind a void that threatens to engulf Eaven City in chaos."
          " Amidst whispers of conspiracy and treachery, the city's leaders turn to you, a seasoned investigator"
          " with a reputation for untangling the most intricate of mysteries. ")
    time.sleep(6)
    print("\nYour mission is to uncover the mystery behind the disappearance of the city's leader in Eaven City. "
          "Navigate through shadowy paths, expose hidden secrets, and make decisions that will shape the fate of the city.")
    time.sleep(5)
    print("\nYour next step is to investigate the Mayor's Office. This is a pivotal location filled with potential clues "
          "that could unravel the mystery. \nYour choices will either bring back peace to Eaven City or make things worse.")
    time.sleep(3)
    input("\nPress Enter to begin your investigation...")
    investigate_mayors_office()

def continue_or_exit():
    while True:
        choice = input("\nDo you want to continue playing? (yes/no): ").strip().lower()
        
        if choice == "yes":
            continue_game()
            break
        elif choice == "no":
            print("\nThank you for playing! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' to continue or 'no' to exit.")

def game_over():
    print("\nMission Failed!")
    print("\nYou messed up, and now the city's in trouble. The mayor is still missing, and the city's hope dwindles. "
          "People are talking, and they're not happy with you. Your reputation is ruined. Your once-respected name is now tied to bad times.")
    print("\nAs days pass, the city's chaos grows. Without its leader, Eaven City spirals deeper into uncertainty. "
          "Your mission's failure casts a long shadow, affecting not just you, but the very fabric of the city.")
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

def investigate_mayors_office():
    print("\nAs you step into the Mayor's Office, the atmosphere is palpable with tension and intrigue. "
          "The room, adorned with opulent furnishings and ornate decorations, exudes an air of authority and mystery. "
          "Your eyes are immediately drawn to a striking painting hanging prominently on the wall, its intricate details ")

    print("\nWhat will you do?")
    print("1. Investigate the painting.")
    print("2. Look around the room.")
        
    decision = input("Enter your choice (1/2): ")
        
    if decision == "1":
        outcome_a1()
    elif decision == "2":
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        investigate_mayors_office()

def outcome_a1():
    print("\nCarefully removing the painting from the wall, you're surprised to find a hidden compartment. "
          "Inside this secret space lies an old, sturdy safe, its metallic surface bearing the marks of time "
          "and perhaps, the weight of the secrets it guards. The safe's presence deepens the mystery, raising "
          "questions about its contents and its connection to the Mayor's disappearance.")
    time.sleep(3)
    print("\nCracking this safe could unveil crucial clues, "
          "but it could also be a risky endeavor.")

    print("\nWhat will you do?")
    print("1. Attempt to crack the safe.")
    print("2. Leave it for now and look elsewhere.")
            
    decision = input("Enter your choice (1/2): ")
            
    if decision == "1":
        crack_safe()
    elif decision == "2":
        print("\nYou decide to leave the safe and explore other areas.")
        outcome_b1()
    else:
        print("Invalid choice. Please try again.")
        outcome_a1()
        
def crack_safe():
    def validate_input(guess):
        return guess.isdigit() and len(guess) == 3

    def provide_hint(code, guess):
        hint = []
        for i in range(3):
            if guess[i] == code[i]:
                hint.append("✓")  # ✓ represents a correct digit in the correct position
            elif guess[i] in code:
                hint.append("~")  # ~ represents a correct digit but in the wrong position
            else:
                hint.append("✗")  # ✗ represents a wrong digit
        return f"Hint: {' '.join(hint)}"

    attempts = 5  # Number of attempts allowed
    safe_code = "739"  # Predefined code for the safe

    print("\nYou attempt to crack the safe. It requires a 3-digit code.")
    print("✓ represents a correct digit in the correct position.")
    print("~ represents a correct digit but in the wrong position.")
    print("✗ represents a wrong digit.")
                
    while attempts > 0:
        guess = input("Enter your guess: ")
                    
        if not validate_input(guess):
            print("Invalid input. Please enter a 3-digit number.")
            continue
                    
        if guess == safe_code:
            print("\nSuccess! With a satisfying click, the safe's door swings open, revealing a trove of critical documents."
                  "You quickly sift through the papers, piecing together a web of deception and intrigue that spans the highest echelons of power.")
            time.sleep(3)
            outcome_a1_1()
            return
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect code. {attempts} attempts remaining. {provide_hint(safe_code, guess)}")
            else:
                print("You've run out of attempts. The safe remains locked.")
                time.sleep(2)
                print("\nUnfortunately, your failure to crack the safe has alerted the security system.")
                print("Sirens blare throughout the building, and security personnel rush to the scene.")
                print("You are quickly apprehended, and your mission comes to an abrupt end.")
                time.sleep(2)
                game_over()
                return

def outcome_a1_1():
    print("Among the documents, you find coded messages, financial records, and a list of names that send a chill down your spine.")
    print("\nWhat will you do next?")
    print("1. Share the documents with the police.")
    print("2. Keep the documents and continue the investigation alone.")
    
    decision = input("Enter your choice (1/2): ")
    
    if decision == "1":
        print("\nYou decide to share the documents with the police, realizing the value of their resources and expertise. "
              "Handing over the documents, you see detectives immediately dive into action. They begin analyzing the information, "
              "organizing surveillance, and coordinating with other units. The atmosphere is tense as they work tirelessly to "
              "piece together the puzzle. While progress is being made, you decide to continue the investigation, searching for additional clues ")
        time.sleep(5)
        print("\nBut as you continue your investigation, you start to feel uneasy, sensing that someone is watching you. ")
        print("Moments later, the distinct sound of footsteps catches your attention, growing closer with each passing second.")
        print("\nWhat will you do?")
        print("1. Hide and observe who is coming.")
        print("2. Confront the individual directly.")
        choose_hide_or_confront()        
    
    elif decision == "2":
        print("\nYou decide to keep the documents, believing that you can handle the investigation alone. "
              "As you delve deeper into the case, you encounter numerous challenges and obstacles. "
              "Without the support and resources of the police, you find it increasingly difficult to make progress. "
              "Time is running out, and your solo efforts fall short, leading to frustration and setbacks. "
              "Ultimately, your decision to go it alone proves costly, and the culprits evade capture, resulting in mission failure.")
        time.sleep(5)
        game_over()
        
    else:
        print("Invalid choice. Please try again.")
        outcome_a1_1()

def outcome_b1():
    print("\nYou start looking around the office, keen to uncover any clues that might help solve the mystery. "
          "Your keen eyes spot a subtle irregularity beneath the desk, a concealed compartment obscured from casual view. "
          "The compartment's presence raises questions about its contents and its significance in the unfolding mystery.")
    time.sleep(4)
    print("It looks intriguing. \nWhat will you do?")
    print("1. Explore the hidden compartment.")
    print("2. Ignore and look elsewhere.")
    
    decision = input("Enter your choice (1/2): ")
    
    if decision == "1":
        print("\nAs you carefully explore the hidden compartment, your fingers brush against something cold and metallic. "
              "Drawing it closer, you discover a mysterious key!")
        outcome_b1_1()
    elif decision == "2":
        print("\nYou looked around but failed to find any substantial evidence or leads. "
              "As you exit the premises, you're oblivious to the fact that you missed a critical document lying inconspicuously on a desk."
              "Unbeknownst to you, that overlooked document held the key to the Mayor's disappearance.")
        time.sleep(4)
        print("Days later, the Mayor's whereabouts remain unknown, and rumors swirl about corruption at the highest levels. "
              "Your oversight becomes the subject of intense scrutiny. Fellow investigators and the public alike question your competence. "
              "In the shadows, the real culprits breathe a sigh of relief, knowing they've successfully evaded capture, thanks in part to your oversight.")
        time.sleep(5)
        game_over()
    else:
        print("Invalid choice. Please try again.")
        outcome_b1()

def outcome_b1_1():
    print("The key could be useful. \nWhat's your next move?")
    print("1. Use the key on a locked drawer you noticed earlier.")
    print("2. Ignore the key and continue investigating.")
    
    decision = input("Enter your choice (1/2): ")
    
    if decision == "1":
        print("\nWith determination fueling your actions, you carefully approach the locked drawer, key in hand. "
              "Inserting the key into the lock, and... ")
        time.sleep(4)
        print("\nThe key fits perfectly! "
              "The drawer springs open. Inside, you find some documents that might hold important clues.")
        outcome_a1_1()
    elif decision == "2":
        print("\nYou decide to leave the key and the desk alone, finding no other leads. "
              "Time passes, and you left without pursuing leads. "
              "Not using the key has cost you the chance to solve the case.")
        time.sleep(3)
        game_over()
    else:
        print("Invalid choice. Please try again.")
        outcome_b1_1()
        
def choose_hide_or_confront():
    hide_or_confront = input("Enter your choice (1/2): ")
        
    if hide_or_confront == "1":

        print("\nYou quickly hide behind a curtain and observe as two shadowy figures enter the room."
              " With focused determination, they methodically search through drawers, cabinets, and behind paintings, "
              "clearly looking for something of importance. Their whispered exchanges hint at the significance of their mission, "
              "leaving you intrigued yet wary of their intentions."
              "The room's atmosphere grows tense with each passing moment, punctuated by the soft rustling of papers and the "
              "occasional muted click of a hidden compartment being examined. As you remain hidden, you realize that whatever they're "
              "searching for holds crucial importance. ")
        time.sleep(5)
        print("\nWhat's your next move?")
        print("1. Quietly exit the room to avoid confrontation.")
        print("2. Confront them now, hoping to catch them off guard.")
            
        surprise_decision = input("Enter your choice (1/2): ")

        if surprise_decision == "1":
            print("\nYou quietly slip out of the room, ensuring not to make any noise that could alert the figures."
                  "The decision to avoid confrontation buys you time, allowing you to regroup and consider your next steps in the investigation.")
            time.sleep(4)
            continue_or_exit()
        elif surprise_decision == "2":
            print("\nYou leap out from your hiding spot, catching the figures off guard.")
            print("However, in the chaos of the moment, you lose your grip on the documents, and they scatter in the struggle. "
                  "as you attempt to grab the documents, one of the figures swiftly snatches them from your hands."
                  " You're left empty-handed, realizing the figures were more prepared than you anticipated."
                  " Losing the documents to the figures is a critical setback in your investigation.")
            time.sleep(3)
            game_over()
        else:
            print("Invalid choice. Please try again.")
            
    elif hide_or_confront == "2":
        print("\nYou confront the individual directly but are outnumbered.")
        print("A struggle ensues, and you're overpowered, losing the documents in the process.")
        time.sleep(3)
        game_over()
    else:
        print("Invalid choice. Please try again.")
        choose_hide_or_confront()   

def continue_game():
    print("As you sift through stacks of the documents and tangled leads, a cryptic message arrives:")
    print("'Meet me at the dilapidated warehouse near the city docks,' it reads, signed only as 'Shadow'.")
    print("Curiosity piqued, you weigh the risks and the potential breakthrough this could bring.")
    
    choice = input("\nWill you go to the warehouse? (yes/no): ").lower()
    
    if choice == "yes":
        print("\nWith a resolute determination, you decide to go to the dilapidated warehouse near the city docks.")
        time.sleep(3)
        warehouse_scenario()
    elif choice == "no":
        print("\nYou decide the risks outweigh the rewards. ")
        time.sleep(2)
        print("\nHowever, your choice to stay back leaves you wondering and the case remains unsolved.")
        time.sleep(3)
        game_over()
    else:
        print("\nPlease type 'yes' or 'no'.")
        continue_game()


def warehouse_scenario():
    print("\nYou cautiously step into the warehouse, the faint smell of aged wood and rusted metal filling the air. "
          "A shadowy figure stands in the corner, their silhouette distorted by the scant light filtering through the broken windows. "
          "As you approach, the figure steps forward, revealing themselves to be 'Shadow'. "
          "'I've been expecting you,' Shadow murmurs, their voice echoing slightly in the vast emptiness of the warehouse. "
          "Without wasting time, Shadow hands you a worn file, its edges frayed and its cover marked with the emblem of a raven. "
          "'Inside are names and locations that might unravel the mystery of Mayor Greene's disappearance,' Shadow explains cryptically.")
    time.sleep(7)
    print("\nYou flip open the file, scanning its contents. Three names catch your eye, and you decide to delve into one of them first:")
    print("1. Vincent Blackwood - A wealthy magnate known for his lavish parties and influential connections.")
    print("2. Elena Martinez - A rising star within the city council, known for her ambition and cunning.")
    print("3. Marcus Stone - A tenacious journalist with a knack for uncovering the city's darkest secrets.")

    choice = input("\nWho will you investigate first? (Enter a number): ")

    if choice == "1":
        vincent_scenario()
    elif choice == "2":
        elena_scenario()
    elif choice == "3":
        marcus_scenario()
    else:
        print("\nPlease select a valid option.")
        warehouse_scenario()


def vincent_scenario():
    print("\nYou step into Vincent Blackwood's office. It's impressive with shiny decorations, golden trims, and pricey paintings hanging on the walls.")
    print("\nAs you glance around, two ideas pop into your mind on how to get closer to the truth:")
    print("1. Look into his finances, searching for suspicious transactions or hidden money.")
    print("2. Follow Vincent discreetly, hoping to catch him meeting with questionable individuals.")

    choice = input("\nHow do you investigate Vincent? (1/2): ")
    if choice == "1":
        print("\nYou meticulously sift through Vincent's financial records, navigating through layers of complex transactions and companies. "
              "As you dig deeper, you unearth a trail of offshore accounts and covert payments. "
              "These transactions seem to connect Vincent with several influential figures within the city's political and business circles. "
              "You even find some coded messages suggesting a big plan that could change things in the city.")
        time.sleep(6)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    elif choice == "2":
        print("\nOpting for a more discreet strategy, you shadow Vincent during one of his evening outings. "
              "Your pursuit leads you to an upscale restaurant known for its privacy and exclusivity. From a vantage point, "
              "you observe Vincent engaging in an intense conversation with a group of individuals, discussing strategies and plans that "
              "hint at a sinister plot. You catch words about controlling important things in the city.")
        print("\nAs you strain to listen, you realize Vincent is part of a plan that might harm the city's future.")
        time.sleep(7)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    else:
        print("\nPlease choose a valid option.")
        vincent_scenario()

    input("\nPress Enter to continue...")
    continuation()

def elena_scenario():
    print("\nElena Martinez's office is adorned with political posters and gleaming awards, showcasing her influence. "
          "As you stand there, you notice Elena glancing over some documents on her desk. \nYou have two paths ahead:")
    print("1. Approach Elena directly, trying to get insights about Mayor's sudden disappearance.")
    print("2. Investigate her colleagues in the city council, looking for any signs of a conspiracy.")
    
    choice = input("\nHow do you approach Elena? (1/2): ")

    if choice == "1":
        print("\nTaking a deep breath, you decide to engage Elena in conversation. "
              "She seems momentarily caught off guard but quickly regains her composure. "
              "After some questions, Elena hints about some powerful people behind city decisions. It sounds suspicious...")
        time.sleep(5)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    elif choice == "2":
        print("\nRather than confronting Elena directly, you decide to see who she works with in the city council. "
              "After some discreet inquiries, you uncover that several council members are indebted to Elena, "
              "hinting at a web of influence that goes beyond mere politics. "
              "This revelation makes you realize the depth of Elena's reach and how intertwined it might be with the Mayor's disappearance.")
        time.sleep(5)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    else:
        print("\nPlease choose a valid option.")
        elena_scenario()
        
    input("\nPress Enter to continue...")
    continuation()
    
def marcus_scenario():
    print("\nMarcus Stone's office is cluttered with newspapers, files, and coffee cups.")
    print("You observe Marcus, who seems engrossed in his work, occasionally pausing to scribble notes or sip his coffee."
          "Your investigation has led you here, and now you must choose your approach.")
    print("\nYou decide to:")
    print("1. Confront Marcus, showing him evidence that might link him to Mayor's disappearance.")
    print("2. Read Marcus's recent articles closely, looking for hidden messages or clues.")
    
    choice = input("\nHow will you approach Marcus? (1/2): ")
        
    if choice == "1":
        print("\nYou steel yourself, deciding that direct confrontation is the best course of action. "
              "As you lay out the evidence, Marcus's looks surprised for a moment but tries to keep his cool. "
              "He vehemently denies any wrongdoing but stumbles over his words, hinting at a 'big story' that could unravel everything.")
        print("\nYou're left with a nagging feeling that Marcus knows more than he's letting on, and this 'big story' might be the key to solving the mystery.")
        time.sleep(6)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    elif choice == "2":
        print("\nOpting for a more subtle approach, you dive deep into Marcus's articles, scouring each line for hidden meanings.")
        print("\nAfter hours of meticulous reading, you uncover coded messages scattered throughout his recent pieces. "
              "These messages hint at a web of deceit, with cryptic references that align eerily with the Mayor's sudden disappearance.")
        print("\nYour discovery sends chills down your spine, realizing that Marcus's articles are not mere reporting but "
              "a carefully crafted narrative designed to mislead the public.")
        time.sleep(7)
        print("\nAfter gathering initial clues from your first lead, you continue investigating the other two suspects. ")
        time.sleep(2)
    else:
        print("\nPlease choose a valid option.")
        marcus_scenario()

    input("\nPress Enter to continue...")
    continuation()

def continuation():
    print("\nAfter gathering valuable information from your investigations, you feel the weight of responsibility.")
    print("With the evidence in hand, you decide to:")
    print("1. Go directly to the police station to share all the information.")
    print("2. Meet 'Shadow' again to discuss the next steps.")

    choice = input("\nWhat will you do next? (1/2): ")

    if choice == "1":
        print("\nTrusting your instincts, you head straight to the police station, sharing all the evidence and information you've meticulously gathered."          
              "The police are immediately intrigued by the information you provide, the critical documents discovered in the Mayor's office,:")
        print("- The documents reveal financial transactions connecting Vincent Blackwood to Mayor's office, hinting at corruption.")
        print("- There are emails between Elena Martinez and Marcus Stone discussing a plot against Mayor Greene.")
        print("- A coded message deciphered from Marcus Stone's articles that implicates 'Shadow' directly in Mayor's disappearance.")
        time.sleep(7)
        print("\nWith this newfound evidence, the police mobilize their resources. Vincent Blackwood is arrested while attempting to destroy more evidence. "
              "Elena Martinez and Marcus Stone are interrogated, leading to a confession that 'Shadow' manipulated them.")
        print("\nPiecing together the puzzle, a coordinated effort by the police corners 'Shadow'. The evidence you provided becomes the cornerstone of the prosecution's case.")        
        time.sleep(7)
        end_game()
    elif choice == "2":
        print("\nFeeling a sense of loyalty, you decide to meet 'Shadow' once more, hoping to get a clearer picture."
              "However, as the conversation progresses, you notice inconsistencies in 'Shadow's' story."
              "Suddenly, 'Shadow' reveals their true colors, admitting to orchestrating Mayor Greene's disappearance and manipulating you.")
        time.sleep(4)
        print("Before you can react, you're ambushed by unknown assailants. "
              "They manage to steal all the evidence, leaving you stunned and without evidence.")
        time.sleep(3)
        game_over()
    else:
        print("\nPlease select a valid option to continue.")
        continuation()

def end_game():
# Conclusion of the game
    print("\nWith 'Shadow' in custody, the city heaves a collective sigh of relief. His network, once vast and insidious, crumbles without his guidance. "
          "During his interrogation, 'Shadow' reveals the extent of his operations. It's a revelation that shocks the city and exposes layers of corruption.")
    time.sleep(5)
    print("\nThe evidence you provided not only leads to 'Shadow's' downfall but also uncovers other nefarious activities within the city's elite. "
          "Several high-profile individuals, who were once untouchable, face the consequences of their actions, thanks to your relentless pursuit of truth.")
    time.sleep(5)
    print("\nThe Mayor, now safe and back in office, publicly acknowledges your contribution. He announces reforms and initiatives to ensure that such incidents never occur again. "
          "The city starts to rebuild, not just physically but also morally, guided by the transparency and integrity that your actions have inspired.")
    time.sleep(5)
    print("\nCongratulations! You've successfully solved the mystery and brought justice to Mayor Greene and peace to the city.")
    time.sleep(2)
    print("Hope you enjoyed the game! Play again to explore different paths.")

# Start the game
intro()


