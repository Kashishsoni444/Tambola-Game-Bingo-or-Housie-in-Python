# Tambola-Game-Bingo-or-Housie-in-Python
Built a Python-based Tambola number caller that shuffles and draws numbers from 1 to 90 one at a time, displays each draw, and maintains a running list of all called numbers — mimicking a real Tambola game host.


# 🎱 Tambola Number Caller

A simple command-line Tambola (Housie/Bingo) number caller built in Python. Randomly draws numbers from 1 to 90 one at a time — just like a real Tambola game — and keeps track of all numbers called so far.

---

## 🎮 What is Tambola?

Tambola (also known as Housie or Bingo) is a popular number game where a caller randomly draws numbers from 1 to 90. Players mark off the numbers on their tickets, and the first to complete a row, column, or full house wins.

---

## ✨ Features

- Draws numbers randomly from 1–90 with no repeats
- Displays the current number called after each draw
- Shows a running list of all numbers called so far
- Stop the game at any time by pressing `s`
- Automatically ends when all 90 numbers have been called

---

## 🗂️ Project Structure

```
├── tambola_game.py   # Main game script
└── README.md
```

---

## 🚀 Getting Started

### Requirements

- Python 3.x (no external libraries needed)

### Run the game

```bash
python tambola_game.py
```

---

## 🧭 How to Play

1. Run the script
2. Press **Enter** to draw the next number
3. Call out the number to your players
4. Press **`s`** to stop the game at any time
5. The game ends automatically once all 90 numbers have been called

### Example output

```
Press any key to call out a number or 's' to stop:
Number called: 47
Numbers called so far: [47]

Press any key to call out a number or 's' to stop:
Number called: 12
Numbers called so far: [47, 12]

Press any key to call out a number or 's' to stop: s
Game stopped.
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
