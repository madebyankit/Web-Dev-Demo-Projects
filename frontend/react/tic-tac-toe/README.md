# Tic-Tac-Toe

A simple React game built with Vite. Players take turns marking squares on a 3x3 board. The app detects wins, draws, and allows a rematch while keeping a turn log.

## Features

- **Classic tic-tac-toe gameplay** on a 3x3 board
- **Two-player support**: Player X and Player O alternate turns
- **Win detection** using predefined winning combinations
- **Draw detection** when all squares are filled and no winner is found
- **Editable player names** with instant UI updates
- **Reset / rematch** button to start a new game
- **Move log** shows selected square coordinates for each turn
- **Button disabling** prevents overwriting occupied squares

## Technologies Used

- React with `useState`
- Vite build tool
- JavaScript modules
- CSS styling

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

```bash
cd frontend/react/Tic-Tac-Toe
npm install
npm run dev
```

Open the local dev server shown in the terminal, typically `http://localhost:5173`.

## Usage

- Click an empty square to place the active player’s symbol
- The active player changes automatically after each turn
- When a win or draw occurs, the game shows a result message
- Click **Rematch!** to reset the board and start again
- Edit player names with the **Edit / Save** buttons

## Project Structure

```
Tic-Tac-Toe/
├── public/                      # Static assets and images
├── src/
│   ├── components/              # React UI components
│   ├── winning-combinations.js  # Game logic constants
│   ├── App.jsx                  # Main game logic
│   ├── index.jsx                # React entry point
│   └── index.css                # Global styles
├── package.json
└── vite.config.js
```
