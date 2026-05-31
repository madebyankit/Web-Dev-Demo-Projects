import { useState } from "react";

import Player from "./components/Player.jsx";
import GameBoard from "./components/GameBoard.jsx";
import Log from "./components/Log.jsx";
import GameOver from "./components/GameOver.jsx";

import { WINNING_COMBINATIONS } from "./winning-combinations.js";

const PLAYERS = {
  X: "Player 1",
  O: "Player 2",
};

const INITIAL_GAME_BOARD = [
	[null, null, null],
	[null, null, null],
	[null, null, null],
];


function derivedActivePlayer(gameTurns) {
	let curPlayer = "X";
	if (gameTurns.length > 0 && gameTurns[0].player === "X") {
		curPlayer = "O";
	}
	return curPlayer;
}


function derivedWinner(gameBoard, players) {
  let winner = null;

  for (const combination of WINNING_COMBINATIONS) {
    const firstSquare = gameBoard[combination[0].row][combination[0].column];
    const secondSquare = gameBoard[combination[1].row][combination[1].column];
    const thirdSquare = gameBoard[combination[2].row][combination[2].column];

    if (
      firstSquare &&
      firstSquare === secondSquare &&
      firstSquare === thirdSquare
    ) {
      winner = players[firstSquare];
      break;
    }
  }

  return winner;
}


function deriveGameBoard(gameTurns) {
	let gameBoard = [...INITIAL_GAME_BOARD.map((row) => [...row])]; // Deep copy of the initial game board

	for (const turn of gameTurns) {
		const { square, player } = turn;
		const { row, col } = square;

		gameBoard[row][col] = player;
	}
	return gameBoard;
}


function App() {
	const [players, setPlayers] = useState(PLAYERS);

	const [gameTurns, setGameTurns] = useState([]);
	// const [hasWinner, setHasWinner] = useState(false);
	// const [activePlayer, setActivePlayer] = useState('X');

	let activePlayer = derivedActivePlayer(gameTurns);

	let gameBoard = deriveGameBoard(gameTurns);

	let winner = derivedWinner(gameBoard, players);

	const hasDraw = gameTurns.length === 9 && !winner;

	function handleSelectSquare(rowIndex, colIndex) {
		// setActivePlayer((curActivePlayer) => (curActivePlayer === 'X' ? 'O' : 'X'));

		setGameTurns((prevturns) => {
			const activePlayer = derivedActivePlayer(prevturns);

			const updatedTurns = [
				{ square: { row: rowIndex, col: colIndex }, player: activePlayer },
				...prevturns,
			];
			return updatedTurns;
		});
	}

	function resetGame() {
		setGameTurns([]);
	}

	function handlePlayerNameChange(playerSymbol, newName) {
		setPlayers((prevPlayers) => {
			return {
				...prevPlayers,
				[playerSymbol]: newName,
			};
		});
	}

	return (
		<main>
			<div id="game-container">
				<ol id="players" className="highlight-player">
					<Player
						initialName={PLAYERS.X}
						symbol="X"
						isActive={activePlayer === "X"}
						onNameChange={handlePlayerNameChange}
					/>
					<Player
						initialName={PLAYERS.O}
						symbol="O"
						isActive={activePlayer === "O"}
						onNameChange={handlePlayerNameChange}
					/>
				</ol>

				{(winner || hasDraw) && (
					<GameOver winner={winner} onRestart={resetGame} />
				)}

				<GameBoard onSelectSquare={handleSelectSquare} board={gameBoard} />
			</div>

			<Log turns={gameTurns} />
		</main>
	);
}

export default App;
