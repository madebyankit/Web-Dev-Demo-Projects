const Campground = require("../models/campground");
const maptilerClient = require("@maptiler/client");
maptilerClient.config.apiKey = process.env.MAPTILER_API_KEY;
const { cloudinary } = require("../cloudinary");

module.exports.index = async (req, res) => {
	const campgrounds = await Campground.find({}).populate("popupText");
	res.render("campgrounds/index", { campgrounds });
};

module.exports.renderNewForm = (req, res) => {
	res.render("campgrounds/new");
};

// This line in app.js -> app.use(express.urlencoded({ extended: true })); //tells the app to parse "req.body" for incoming post requests, by default the field will be empty
module.exports.createCampground = async (req, res, next) => {
	const geoData = await maptilerClient.geocoding.forward(
		req.body.campground.location,
		{ limit: 1 },
	);
	// console.log(geoData);
	if (!geoData.features?.length) {
		req.flash(
			"error",
			"Could not geocode that location. Please try again and enter a valid location.",
		);
		return res.redirect("/campgrounds/new");
	}
	//how this data is structured, this is imprtant while working with map features of our app

	const campground = new Campground(req.body.campground);

	campground.geometry = geoData.features[0].geometry;
	campground.location = geoData.features[0].place_name;

	campground.images = req.files.map((f) => ({
		url: f.path,
		filename: f.filename,
	})); //returns the array that we'll store in database
	campground.author = req.user._id; //author is a referene to the user, it's a id
	// console.log("Before Campground Save:", campground);
	await campground.save();
	req.flash("success", "Successfully made a new campground!");
	res.redirect(`/campgrounds/${campground._id}`);
};

module.exports.showCampground = async (req, res) => {
	const campground = await Campground.findById(req.params.id)
		.populate({
			path: "reviews",
			populate: {
				path: "author", //this author refers the author of the review, the one who made that specific review
			},
		})
		.populate("author"); //this author refers the author of campground
	if (!campground) {
		req.flash("error", "Cannot find that campground!");
		return res.redirect("/campgrounds");
	}
	//This populate is needed, so we can chexk whether logged in user has authority over the campground being displayed
	// console.log(campground);
	res.render("campgrounds/show", { campground });
};

module.exports.renderEditForm = async (req, res) => {
	const { id } = req.params;
	const campground = await Campground.findById(id);
	if (!campground) {
		req.flash("error", "Cannot find that campground!");
		return res.redirect("/campgrounds");
	}
	res.render("campgrounds/edit", { campground });
};

module.exports.updateCampground = async (req, res) => {
	const { id } = req.params;
	// console.log(req.body);

	const geoData = await maptilerClient.geocoding.forward(
		req.body.campground.location,
		{ limit: 1 },
	);
	// console.log(geoData);
	if (!geoData.features?.length) {
		req.flash(
			"error",
			"Could not geocode that location. Please try again and enter a valid location.",
		);
		return res.redirect(`/campgrounds/${id}/edit`);
	}

	const campground = await Campground.findByIdAndUpdate(id, {
		...req.body.campground,
	});

	campground.geometry = geoData.features[0].geometry;
	campground.location = geoData.features[0].place_name;

	const imgs = req.files.map((f) => ({ url: f.path, filename: f.filename }));
	campground.images.push(...imgs); // we are not gonna overwrite images while updating, we'll we adding onto the exisiting images, hence the spread operator
	await campground.save();
	if (req.body.deleteImages) {
		for (let filename of req.body.deleteImages) {
			await cloudinary.uploader.destroy(filename); //deleting images stored in cloudinary
		}
		await campground.updateOne({
			$pull: { images: { filename: { $in: req.body.deleteImages } } },
		}); //removing images from database
	}
	req.flash("success", "Successfully updated campground!");
	res.redirect(`/campgrounds/${campground._id}`);
};

module.exports.deleteCampground = async (req, res) => {
	const { id } = req.params;
	await Campground.findByIdAndDelete(id);
	req.flash("success", "Successfully deleted campground");
	res.redirect("/campgrounds");
};
