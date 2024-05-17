class UI:
    @staticmethod
    def display_menu(options):
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    @staticmethod
    def get_choice(prompt, num_options):
        while True:
            try:
                choice = int(input(prompt))
                if 1 <= choice <= num_options:
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_yes_no(prompt):
        while True:
            choice = input(prompt).strip().lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
