const mongoose = require("mongoose");
const cities = require("./cities");
const { places, descriptors } = require("./seedHelpers");
const Campground = require("../models/campground");

mongoose.connect("mongodb://localhost:27017/yelp-camp", {
	useNewUrlParser: true,
	useCreateIndex: true,
	useUnifiedTopology: true,
});

const db = mongoose.connection; //variable to shorten "mongoose.connection" term
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
	console.log("Database connected");
});

const sample = (array) => array[Math.floor(Math.random() * array.length)]; //function to return a random element from an array, used for random title generation

const seedDB = async () => {
	await Campground.deleteMany({});
	for (let i = 0; i < 100; i++) {
		const random1000 = Math.floor(Math.random() * 1000);
		const price = Math.floor(Math.random() * 20) + 10;
		const camp = new Campground({
			//my id, under my own localhost,
			author: "69e20749a6c878b322b645a0",
			location: `${cities[random1000].city}, ${cities[random1000].state}`,
			title: `${sample(descriptors)} ${sample(places)}`, //random title generation using the sample function and the descriptors and places arrays
			description:
				"Lorem ipsum dolor sit amet consectetur adipisicing elit. Quibusdam dolores vero perferendis laudantium, consequuntur voluptatibus nulla architecto, sit soluta esse iure sed labore ipsam a cum nihil atque molestiae deserunt!",
			price,
			geometry: {
				type: "Point",
				coordinates: [
					cities[random1000].longitude,
					cities[random1000].latitude,
				],
			},
			images: [
				{
					url: "https://res.cloudinary.com/du3errqmw/image/upload/v1776674189/YelpCamp/a.jpg",
					filename: "YelpCamp/a",
				},
				{
					url: "https://res.cloudinary.com/du3errqmw/image/upload/v1776674183/YelpCamp/b.jpg",
					filename: "YelpCamp/b",
				},
				{
					url: "https://res.cloudinary.com/du3errqmw/image/upload/v1776674179/YelpCamp/c.jpg",
					filename: "YelpCamp/c",
				},
			],
		});
		await camp.save();
	}
};

seedDB().then(() => {
	mongoose.connection.close();
});
