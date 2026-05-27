import { BrowserRouter, Routes, Route } from "react-router-dom";
import Campgrounds from "./pages/Campgrounds";
import CampgroundDetail from "./pages/CampgroundDetail";
  
function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<h1>Home</h1>} />
        <Route path="/campgrounds" element={<Campgrounds />} />
        <Route path="/campgrounds/:id" element={<CampgroundDetail />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App
