from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

CARD_FILE = 'cards.json'

def load_cards():
    if not os.path.exists(CARD_FILE):
        return []
    with open(CARD_FILE, 'r') as f:
        return json.load(f)

def save_cards(cards):
    with open(CARD_FILE, 'w') as f:
        json.dump(cards, f, indent=4)

@app.route('/')
def index():
    cards = load_cards()
    return render_template('index.html', cards=cards)

@app.route('/add', methods=['GET', 'POST'])
def add_card():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']
        cards = load_cards()
        cards.append({'question': question, 'answer': answer})
        save_cards(cards)
        return redirect(url_for('index'))
    return render_template('add_card.html')

@app.route('/quiz')
def quiz():
    cards = load_cards()
    return render_template('quiz.html', cards=cards)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5020, debug=True, use_reloader=False)

