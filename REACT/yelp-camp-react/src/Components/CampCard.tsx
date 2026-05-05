import { Link } from "react-router-dom";
import { useState } from "react";

type Campground = {
  _id: string;
  title: string;
  location: string;
  price: number;
};

type CardProps = {
  camp: Campground;
  onDelete: (id: string) => void;
};

const styles = {
  card: {
    border: "1px solid #e2e2e2",
    borderRadius: "10px",
    padding: "16px",
    marginBottom: "16px",
    backgroundColor: "#fff",
  },
  cardHover: {
    boxShadow: "0 6px 16px rgba(0,0,0,0.08)",
    transform: "translateY(-2px)",
  },
  title: {
    fontSize: "18px",
    fontWeight: 500,
    marginBottom: "4px",
  },
  location: {
    fontSize: "14px",
    color: "#666",
  },
  price: {
    fontSize: "16px",
    fontWeight: 600,
    marginTop: "8px",
  },
  actions: {
    display: "flex",
    gap: "10px",
    marginTop: "12px",
  },
  button: {
    padding: "6px 10px",
    borderRadius: "6px",
    border: "none",
    cursor: "pointer",
  },
  buttonHover: {
    opacity: 0.85,
  },
  primary: {
    backgroundColor: "#007bff",
    color: "#fff",
  },
  danger: {
    backgroundColor: "#dc3545",
    color: "#fff",
  },
};

export function CampCard({ camp, onDelete }: CardProps) {
  const [hovered, setHovered] = useState(false);
  const [viewHover, setViewHover] = useState(false);
  const [deleteHover, setDeleteHover] = useState(false);

  return (
    <div
      style={{
        ...styles.card,
        transition: "all 0.2s ease",
        ...(hovered ? styles.cardHover : {}),
      }}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
    >
      <h2 style={styles.title}>{camp.title}</h2>
      <p style={styles.location}>{camp.location}</p>
      <p style={styles.price}>₹{camp.price}</p>

      <div style={styles.actions}>
        <Link to={`/campgrounds/${camp._id}`}>
          <button
            style={{
              ...styles.button,
              ...styles.primary,
              transition: "0.2s",
              ...(viewHover ? styles.buttonHover : {}),
            }}
            onMouseEnter={() => setViewHover(true)}
            onMouseLeave={() => setViewHover(false)}
          >
            View Details
          </button>
        </Link>

        <button
          onClick={() => onDelete(camp._id)}
          style={{
            ...styles.button,
            ...styles.danger,
            transition: "0.2s",
            ...(deleteHover ? styles.buttonHover : {}),
          }}
          onMouseEnter={() => setDeleteHover(true)}
          onMouseLeave={() => setDeleteHover(false)}
        >
          Delete
        </button>
      </div>
    </div>
  );
}