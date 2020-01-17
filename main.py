from time import time

# check this out
import string
# try string.ascii_letters
# there are many more...


class TypingTest:

    def __init__(self):
        self.main()

    def main(self):
        while True:
            choice = self.main_menu()
            choice()

    def main_menu(self):
        prompt = """Welcome to a typing test!
        choose an option:
        [1]: random keys
        [2]: quit
        """
        options = {1: self.random_keys, 2: self.quit}
        while True:
            answer = input(prompt)
            try:
                choice = options[int(answer)]
            except KeyError:
                print("That was not one of the choices")
            else:
                return choice

    def game_loop(self):
        pass


    def random_keys(self):
        pass

    def quit(self):
        print('Good Bye')
        exit()


if __name__ == "__main__":
    TypingTest()
