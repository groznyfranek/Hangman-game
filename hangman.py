from game import Game

class Hangman:
    def __init__(self):
        self.file = open("file.txt", 'r')
        self.lines = self.file.readlines()
        for line in self.lines:
            if len(line) > 20 or len(line) < 3:
                print('WRONG DATA')
                return
            for i in line:
                if i not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\n":
                    print('WRONG DATA')
                    return
        self.game = Game(self.lines)
        self.game.run()

    def __del__(self):
        self.file.close()