import { useParams } from "react-router-dom";
import { campgrounds } from "../data/seeds";
import "./CamgroundDetail.css";

export default function CampgroundDetail() {
  const { id } = useParams();

  const campground = campgrounds.find((c) => c._id === id);

  if (!campground) {
    return <h1>Campground not found</h1>;
  }

  return (
    <div className="detail-container">
      <div className="detail-card">
        <h1 className="detail-title">{campground.title}</h1>
        <p className="detail-location">{campground.location}</p>
        <p className="detail-price">₹{campground.price}</p>

        <button
          onClick={() => window.history.back()}
          className="detail-back"
        >
          Back
        </button>
      </div>
    </div>
  );
}