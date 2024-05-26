import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class card:
    def __init__(self, role, description):
        self.role = role
        self.description = description
    def __repr__(self):
        return self.role
class Deck:
    def __init__(self):
        self.cards = ["a","2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        self.creat_deck()
    def creat_deck(self):
        roles_description = [
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
        for role, description in roles_description:
            self.cards.append(card(role, description))
    def draw_card(self):
        if not self.cards:
            return None
        
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
class cardApp(App):
    def build(self):
        self.deck = Deck
        self.layout = BoxLayout(orientation = "vertical", padding=10, spacing=10)  
        self.draw_button = Button(text = "draw a random role", size_hint= (1, 0.2))
        self.draw_button.bind(on_press=self.draw_random_card) 
        self.layout.add_widget(self.draw_button)
       
        self.result_labal = Label(text = "your random role will apper here", size_hint=(1, 0.8))
        self.layout.add_widget(self.result_labal)
        return self.layout
    
    def draw_random_card(self, instance):
        card = self.deck.draw_card()
        if card is None:
           self.result_labal.text(text = "no more cards!")
        else:
           self.result_labal.text(text = f"Role: {card.role}\n description: {card.description}")

if __name__ =="__main__":
    cardApp().run()