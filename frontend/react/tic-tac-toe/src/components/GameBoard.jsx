// const initialGameBoard = [
// 	[null, null, null],
// 	[null, null, null],
// 	[null, null, null],
// ];

export default function GameBoard({ onSelectSquare, board }) {
	// let gameBoard = initialGameBoard;

	// for (const turn of turns) {
	// 	const { square, player } = turn;
	// 	const { row, col } = square;

	// 	gameBoard[row][col] = player;
	// }

	// const [gameBoard, setGameBoard] = useState(initialGameBoard);

	// function handleSquareClick(rowIndex, colIndex) {
	//   setGameBoard((prevGameBoard) => {
	//     const newGameBoard = [...prevGameBoard.map(row => [...row])]; // Deep copy of the game board
	//     newGameBoard[rowIndex][colIndex] = activePlayerSymbol; // Update the clicked square with the active player's symbol
	//     return newGameBoard;
	//   });
	//   onSelectSquare();
	// }

	return (
		<ol id="game-board">
			{board.map((row, rowIndex) => (
				<li key={rowIndex}>
					<ol>
						{row.map((playerSymbol, colIndex) => (
							<li key={colIndex}>
								<button
									onClick={() => onSelectSquare(rowIndex, colIndex)}
									disabled={playerSymbol !== null}
								>
									{playerSymbol}
								</button>
							</li>
						))}
					</ol>
				</li>
			))}
		</ol>
	);
}
