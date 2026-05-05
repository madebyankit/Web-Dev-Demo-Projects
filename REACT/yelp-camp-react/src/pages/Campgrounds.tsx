import { useState } from "react";
import { campgrounds as seedData } from "../data/seeds";
import type { Campground } from "../data/seeds";
import "./Campgrounds.css";
import { CampCard } from "../Components/CampCard";

export default function Campgrounds() {
  const [campgrounds, setCampgrounds] = useState<Campground[]>(seedData);

  const addCampground = () => {
    const newCamp: Campground = {
      _id: Date.now().toString(),
      title: "New Camp",
      price: 500,
      location: "India",
    };

    setCampgrounds((prev) => [...prev, newCamp]);
  };

  const deleteCampground = (id: string) => {
    setCampgrounds((prev) => prev.filter((camp) => camp._id !== id));
  };

  return (
    <div className="container">
      <h1 className="title">Campgrounds</h1>

      <button onClick={addCampground} className="add-btn">
        Add Campground
      </button>

      {campgrounds.map((camp) => (
        <CampCard
          key={camp._id}
          camp={camp}
          onDelete={deleteCampground}
        />
      ))}
    </div>
  );
}
