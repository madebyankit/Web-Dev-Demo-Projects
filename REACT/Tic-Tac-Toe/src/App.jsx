import { useState } from 'react';
import Player from './components/Player.jsx';
import GameBoard from './components/GameBoard.jsx';
import Log from './components/Log.jsx';

function derivedActivePlayer(gameTurns) {
  let curPlayer = 'X';
  if(gameTurns.length>0 && gameTurns[0].player === 'X') {
        curPlayer = 'O';
  }
  return curPlayer;
}

function App() {
  const [gameTurns, setGameTurns] = useState([]);
  // const [activePlayer, setActivePlayer] = useState('X');
  
 let activePlayer = derivedActivePlayer(gameTurns);

  function handleSelectSquare(rowIndex, colIndex) {
    // setActivePlayer((curActivePlayer) => (curActivePlayer === 'X' ? 'O' : 'X'));
  
    setGameTurns( prevturns=> {
      const activePlayer = derivedActivePlayer(prevturns);

      const updatedTurns = [
        { square: {row: rowIndex, col: colIndex }, player: activePlayer }, 
        ...prevturns
      ];
      return updatedTurns;
    })
  }

  return (
    <main>
      <div id="game-container">
        <ol id="players" className='highlight-player'>
          <Player initialName="Player 1" symbol="X" isActive={activePlayer==='X'}/>
          <Player initialName="Player 2" symbol="O" isActive={activePlayer==='O'} />
        </ol>
        <GameBoard onSelectSquare={handleSelectSquare} 
          turns={gameTurns}/>
      </div>
      <Log turns={gameTurns}/>
    </main>
  );
}

export default App;