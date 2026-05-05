export type Campground = {
  _id: string;
  title: string;
  price: number;
  location: string;
};

export const campgrounds: Campground[] = [
  {
    _id: "1",
    title: "Everest Base Camp",
    price: 1200,
    location: "Nepal",
  },
  {
    _id: "2",
    title: "Sahara Retreat",
    price: 800,
    location: "Morocco",
  },
  {
    _id: "3",
    title: "Alpine Escape",
    price: 950,
    location: "Switzerland",
  },
];