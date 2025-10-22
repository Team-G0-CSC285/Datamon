## Datamon Group Project

### Math Practice Game

A simple text-based math practice game built with Python.  
Players can solve math problems, track their answers, and accumulate scores across different mini-games.

---

## Quick Start

### Run Locally

```bash
# From the repository root
python main.py
```

> Requires Python 3.x.

---

## Currently Implemented Mini-Game

- **Answer Checker** – Create math problems, input answers, and get immediate feedback.

Other games (**Memory Bank** and **Number Guesser**) are placeholders for future development.

---

## Features

### Player Profile  
Each session stores:
- Player name  
- Answer history (correct/incorrect)  
- Scores for each mini-game  

### Answer Checker
- Create math problems step-by-step (number → operator → number)
- Checks answers, including division with quotient + remainder
- Supports retry attempts
- Tracks performance per round and overall accumulated score
- Displays a summary of all attempted problems

---

## Terminal UI
- ASCII-art start screen and menus
- Clears the terminal between screens for readability

---

## Roadmap

- **Sprint 1 ✅** – Implement `answer_checker` game  
- **Sprint 2 🚧** – Add `memory_bank` game (pattern recall)  
- **Sprint 3 🚧** – Add `number_guesser` game (higher/lower guessing)  
- **Future** – Persistent save files, difficulty levels, multiplayer turns

