# Tic-Tac-Toe (Python + Tkinter)
## 👥 Contributors
**Team 15**
- **Dhyan Patel:** Game Logic & UI Integration
- **A. Pardhiv:** History & CSV Management
- **Suhith:** Game Logic
- **T. Hemanth:** UI Design & Start Page
## 💻 How to Run

> **⚠️ Important:** You must run the script from inside the `Game` directory. This is required so the application can correctly load the background image (`MBG.png`).

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/dhyanspatel49/Tic-Tac-Toe.git](https://github.com/dhyanspatel49/Tic-Tac-Toe.git)
2. **Navigate to the Game directory:**
   
   ```bash
   cd Tic-Tac-Toe/Game
3. **Run the application:**
   ```bash
   python Tic-Tac-Toe.py

#About the Project   
A fully functional, GUI-based Tic-Tac-Toe game developed in Python using the **Tkinter** library. This project features a multi-page interface, local 2-player support, and a persistent history system that tracks game results in a CSV file.

##  Overview
This application was developed by **Team 15** as part of a Python software development project. It moves beyond simple console logic by implementing a complete event-driven GUI with distinct screens for the Menu, Player Input, Gameplay, and History.

##  Key Features
- **Interactive GUI:** Built with `tkinter`, featuring a custom background and responsive buttons.
- **Multi-Page Navigation:** Seamlessly switch between the Start Menu, Game Board, and History screens using a frame-based architecture.
- **2-Player Mode:** Input custom names for Player 1 (X) and Player 2 (O).
- **History Tracking:** Automatically saves every game result (Winner, Date, & Time) to a `History.csv` file.
- **Game Logic:** Real-time win detection logic for rows, columns, and diagonals, with handling for draw conditions.

##  Tech Stack
- **Language:** Python 3.x
- **GUI Framework:** Tkinter (Standard Python library)
- **Data Persistence:** CSV (Comma-Separated Values)
- **Modules Used:** `tkinter`, `csv`, `datetime`, `os`

## 📂 Project Structure
```text
Tic-Tac-Toe/
│
├── Game/
│   ├── Tic-Tac-Toe.py    # Main application script
│   ├── MBG.png           # Background image for the GUI
│   └── History.csv       # Auto-generated file storing past game results
│
├── Project Proposal.pdf
└── README.md
```
