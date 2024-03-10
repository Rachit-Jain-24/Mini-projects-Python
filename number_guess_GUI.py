import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self):
        self.numbers = list(range(1, 10))
        self.user_score = 0
        self.result = 0
        self.create_gui()

    def generate_random_number(self):
        self.result = random.choice(self.numbers)

    def guess(self):
        user_input = int(self.user_guess.get())
        self.generate_random_number()

        messagebox.showinfo("Result", f"The number wans {self.result}")

        if user_input == self.result:
            messagebox.showinfo("Congratulations!", "Yay, your luck has shined!")
            self.user_score += 1
        else:
            messagebox.showinfo("Better luck next time", "Ahh, bad luck. Try again!")

        self.update_score()
        self.user_guess.set("")  # Clear the entry field

    def update_score(self):
        self.score_label.config(text=f"Your score: {self.user_score}")

    def play_again(self):
        self.generate_random_number()
        self.update_score()
        self.user_guess.set("")  # Clear the entry field

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Number Guessing Game")

        # Entry field for user's guess
        self.user_guess = tk.StringVar()
        guess_entry = tk.Entry(self.root, textvariable=self.user_guess, width=10)
        guess_entry.grid(row=0, column=0, padx=10, pady=10)

        # Guess button
        guess_button = tk.Button(self.root, text="Guess", command=self.guess)
        guess_button.grid(row=0, column=1, padx=10, pady=10)

        # Score label
        self.score_label = tk.Label(self.root, text=f"Your score: {self.user_score}")
        self.score_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Play again button
        play_again_button = tk.Button(self.root, text="Play Again", command=self.play_again)
        play_again_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    NumberGuessingGame()
