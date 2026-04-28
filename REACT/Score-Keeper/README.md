# Score Keeper

A simple React application for keeping track of scores in multiplayer games. Built with Vite and React.

## Features

- **Multiplayer Support**: Track scores for multiple players (default: 3 players)
- **Score Increment**: Click buttons to increment individual player scores
- **Winner Detection**: Automatically highlights when a player reaches the target score
- **Reset Functionality**: Reset all scores to zero
- **Configurable**: Easily adjust number of players and target score

## Technologies Used

- **React**: Frontend framework with hooks (useState)
- **Vite**: Build tool and development server
- **ESLint**: Code linting

## Getting Started

### Prerequisites

- Node.js (v16 or higher)
- npm or yarn

### Installation

1. Navigate to the project directory:

   ```bash
   cd REACT/Score-Keeper
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm run dev
   ```

4. Open [http://localhost:5173](http://localhost:5173) in your browser.

## Usage

- Click the "+1" button next to each player to increment their score
- The first player to reach the target score (default: 5) is declared the winner
- Click "Reset" to start a new game with all scores at zero

## Customization

You can modify the component props in `ScoreKeeper.jsx`:

```jsx
<ScoreKeeper numPlayers={5} target={10} />
```

- `numPlayers`: Number of players (default: 3)
- `target`: Score needed to win (default: 5)

## Project Structure

```
src/
├── ScoreKeeper.jsx    # Main score keeper component
├── App.jsx           # Application entry point
├── main.jsx          # React root rendering
├── App.css           # Component styles
└── index.css         # Global styles
```

## Learning Objectives

This project demonstrates:

- React state management with useState
- Array manipulation in React state
- Component props and default values
- Event handling in React
- Conditional rendering
