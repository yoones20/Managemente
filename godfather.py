import tkinter as tk
import random
from typing import Self

class card:
    def __init__(self, role, des):
        self.role = role
        self.des = des
    def __reper__(self):
        return self.role
class Deck:
    def __init__(self):
        self.cards = ["a","2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        self.creat_deck()
    def creat_deck(self):
        roles_des = [
            ("a", "aaa"),
            ("2", "222"),
            ("3", "333"),
            ("40","444"),        
            ("5", "555"),
            ("6", "666"),
            ("7", "777"),
            ("8", "888"),
            ("9", "999"),
            ("10", "101010"),
            ("11", "111111")
        ]
        for role, des in roles_des:
            self.cards.append(card(role, des))
    def draw_card(self):
        if not self.cards:
            return None
        
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
def draw_random_card():
    card = deck.draw_card()
    if card is None:
       result_labal.config(text = "no more cards!")
    else:
       result_labal.config(text = f"Role: {card.role}\n des: {card.des}")

deck = Deck()
root = tk.Tk()
root.title("random card role")


draw_button = tk.Button(root, text = "draw a random role", command=draw_random_card)
draw_button.pack(pady=20)

result_labal = tk.Label(root, text = "your random role will apper here", wraplength=300)
result_labal.pack(pady=20)
root.mainloop()