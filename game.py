import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class Game:
    def __init__(self, lines: list): 
        self.random_line = random.randint(0,len(lines) - 1)      
        self.word = lines[self.random_line] 
        self.word = self.word[:-1]  
        self.word = self.word.lower()
        self.list_to_show = [(letter, False) for letter in self.word]
        self.root = tk.Tk()
        self.root.resizable(False,False)
        self.root.geometry('500x500')
        self.root.title('Hangman')        

        self.user_input= tk.Entry(self.root, width=7)
        self.user_input.place(x=400, y=440)  
        self.enter_input = tk.Button(self.root, text='ENTER', command=self.load_inputs)
        self.enter_input.place(x = 400, y = 460)
        self.root.bind('<Return>', lambda event: self.load_inputs())
        
        self.images = [Image.open(f"img/stage{i + 1}.png").resize((150, 150)) for i in range(12)]
        self.tk_images = [ImageTk.PhotoImage(img) for img in self.images]
        self.stage = 1
        self.game_label = tk.Label(image=self.tk_images[self.stage - 1])
        self.game_label.place(x=100, y=100)

        self.used = ''
        self.text_to_show = ''

        self.output_label = tk.Label(self.root, text=self.text_to_show, font=60)
        self.output_label.place(x=10, y=460)
        self.used_label = tk.Label(self.root, text=f"Used: {self.used}", font=60)
        self.used_label.place(x=10, y=360)

        self.print_output()
        #print(self.word)

    def load_inputs(self):
        letter_guessed = str(self.user_input.get())            
        if len(letter_guessed) != 1 or letter_guessed not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            messagebox.showerror("Error", "Wrong inputs!")
            return False
        if letter_guessed in self.used:
            messagebox.showerror("Error", "Already used!")
            return
        
        self.user_input.delete(0, tk.END) 
        self.used += f"{letter_guessed}, "
        if letter_guessed not in self.word:
            self.stage += 1
            self.game_label.config(image=self.tk_images[self.stage - 1])
            if self.stage >= 12:
                messagebox.showinfo("Game Over", f"You lost! The word: {self.word}")
                self.root.destroy()
        else:
            #print('Guessed')
            self.change_flags(letter_guessed)
        self.print_output()


    def change_flags(self, let: str):
        self.list_to_show = [(letter, is_guessed) if letter != let or is_guessed else (letter, True) for letter, is_guessed in self.list_to_show]
        #print(self.list_to_show)

    def win_check(self):
        for el in self.list_to_show:
            if el[1] == False:
                return
        messagebox.showinfo("Game Over", f"You won!")
        self.root.destroy()

    def print_output(self):
        #print(self.list_to_show)
        self.text_to_show = ''
        for letter, is_guessed in self.list_to_show:
            if is_guessed:
                self.text_to_show += letter
            else:
                self.text_to_show += '_ '
        #print(self.text_to_show)
        self.output_label.config(text=self.text_to_show)
        self.used_label.config(text=f"Used: {self.used}")
        self.win_check()    

    def run(self):        
        self.root.mainloop()    
        