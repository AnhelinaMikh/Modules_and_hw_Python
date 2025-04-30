import random
from game import settings
from game.exceptions import GameOver, EnemyDown


class Player:
    def __init__(self, name: str):
        self.name = name
        self.lives = settings.PLAYER_LIVES
        self.score = 0
    
    def select_attack(self):
        while True:
            print("\nWhat do you want to choose?")
            for k, v in settings.ALLOWED_ATTACKS.items():
                print(f"{k}: {v}")
            choice = input("Your choice: 1, 2 or 3")
            if choice in settings.ALLOWED_ATTACKS:
                return settings.ALLOWED_ATTACKS[choice]
            else:
                print("Invalid input. Try again")

    def decrease_lives(self):
        self.lives -= 1
        print(f"Player {self.name} has {self.lives} lives left")
        if self.lives <= 0:
            raise GameOver(f"{self.name}, You lost!")
        
    def add_score(self, points: int):
        self.score += points
        print(f"You have {self.score} points")


    

class Enemy:
    def __init__(self, level: int, mode: str):
        self.level = level
        base_lives = level
        if mode == settings.MODE_HARD:
            base_lives *= settings.HARD_MODE_MULTIPLIER
            self.lives = base_lives
    
    def select_attack(self):
        return random.choice(list(settings.ALLOWED_ATTACKS.values()))
    
    def decrease_lives(self):
        self.lives -= 1
        print(f"\nThe enemy has {self.lives} lives left")
        if self.lives <= 0:
            raise EnemyDown("The enemy is defeated")
