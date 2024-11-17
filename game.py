import random
from flask import Flask, render_template, request, redirect, url_for # type: ignore
import os

class GameSession:
    def __init__(self):
        self.money = 100
        self.ensure_log_directory()
    
    def ensure_log_directory(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
    
    def play(self, bet_type, bet_amount):
        # Броски кубиков
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2

        # Логика выигрыша или проигрыша
        if (bet_type == "OVER" and dice_sum > 7) or (bet_type == "UNDER" and dice_sum < 7):
            self.money += bet_amount
            result = "win"
        elif bet_type == "EVEN" and dice_sum == 7:
            self.money += 4 * bet_amount
            result = "big_win"
        else:
            self.money -= bet_amount
            result = "lose"

        # Логирование результатов
        with open("logs/game_log.txt", "a") as log_file:
            log_file.write(f"Player chose {bet_type}, Bet {bet_amount}, Dice sum {dice_sum}, Result {result}\n")
        
        return result, dice_sum

app = Flask(__name__)
game_session = GameSession()

@app.route('/')
def home():
    return render_template('index.html', money=game_session.money)

@app.route('/play', methods=['POST'])
def play():
    bet_type = request.form['bet_type']
    bet_amount = int(request.form['bet_amount'])
    
    game_session.play(bet_type, bet_amount)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


