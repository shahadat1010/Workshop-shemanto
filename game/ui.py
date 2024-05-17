# ui.py

class UI:
    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def display_options(options):
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

    @staticmethod
    def get_input(prompt):
        return input(prompt)
