
# AI_Assignment

Assignment for Chess AI framework implementing Minimax and Alpha-Beta pruning search strategies.  
Slides
[Open Slides](https://docs.google.com/presentation/d/1A549pqeG7qADBszxbrLwBr2roFhwSeCCA7cdDc94_aA/edit?usp=sharing)

---

## Features

- **Minimax Search** (`minimax.py`):  
  - Pure minimax with optional move-ordering (captures first)  
  - Randomized move exploration for diversity  

- **Alpha-Beta Pruning** (`alphabeta.py`):  
  - Standard alpha-beta search with cut-offs  
  - Efficient branch pruning to accelerate deep searches  

- **Evaluation Module** (`evaluate.py`):  
  - `evaluate_board(board)` — full-board heuristic for positional strength  
  - `E(board)` — streamlined evaluation for terminal/depth-limit positions  

- **Play Script** (`play_game.py`):  
  - Command-line interface to pit two AI agents (Minimax vs Alpha-Beta) or AI vs. human  

---

## Prerequisites

- **Python** 3.8 or higher  
- **Git**  
- **pip**

---

## Installation

```bash
# 1. Clone this repository
git clone https://github.com/The0winner0/AI-Assignment.git
cd AI_Assignment

# 2. Create a virtual environment
python3 -m venv venv

# 3. Activate the environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

---

## Usage

Run the main play script:

```bash
python3 play_game.py
```

---

## Code Structure

```
AI_Assignment/
├── evaluate.py        # Board evaluation functions: evaluate_board, E
├── minimax.py         # `minimax(env, board, depth, is_maximizing, use_randomness)`
├── alphabeta.py       # `alphabeta(env, board, depth, alpha, beta, is_maximizing)`
├── play_game.py       # Main CLI for running matches
├── requirements.txt   # Python package dependencies
└── README.md          # Project overview and instructions
```
## Anuj Sharma CS22B007
## Jyothiraditya CS22B002
---
