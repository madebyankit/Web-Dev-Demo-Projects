import "./App.css";
import ScoreKeeper from "./ScoreKeeper";

function App() {
  return (
    <div>
      <ScoreKeeper numPlayers={5} target={5} />
    </div>
  );
}

export default App;
