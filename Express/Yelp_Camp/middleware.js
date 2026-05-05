const { campgroundSchema, reviewSchema } = require("./schemas.js"); //for validating the data coming from the form, we are using JOI, check schemas.js for more details

// const passport = require('passport'); //these suggested by ai, but we are already requiring it in app.js, and since we are exporting these functions as middleware, we can just require it in app.js and use it here without requiring it again
// const LocalStrategy = require('passport-local');
// const User = require('./models/user'); //for authentication, we are using passport and passport-local-mongoose, check models/user.js for more details

const ExpressError = require("./utils/ExpressError");
const Campground = require("./models/campground");
const Review = require("./models/review");

//If any of these authentications fail, notice that we not just redirecting, but returning it, so that next() isn't called
//In case of authentication failure, this prevents the next middleware from being called

module.exports.isLoggedIn = (req, res, next) => {
	// console.log("REQ.USER:", req.user);   //this is automatically coming from the session, thnx to passport, we are also passing it to every route (check app.js)
	if (!req.isAuthenticated()) {
		//isAuthenticated() is coming from passport and is automatically added to req object, all that serilize and deserilize is taking care of this
		req.session.returnTo = req.originalUrl;
		//this is to store the url that the user is trying to access, so that after login, we can redirect them back to that url,
		// this is useful when the user is trying to access a protected route and they are not logged in, after they login,
		// they will be redirected back to that protected route instead of the default route
		req.flash("error", "You must be signed in first!");
		return res.redirect("/login");
	}
	next();
};

module.exports.validateCampground = (req, res, next) => {
	const { error } = campgroundSchema.validate(req.body);
	console.log(req.body);
	if (error) {
		const msg = error.details.map((el) => el.message).join(",");
		throw new ExpressError(msg, 400);
	} else {
		next();
	}
};

module.exports.isAuthor = async (req, res, next) => {
	const { id } = req.params;
	const campground = await Campground.findById(id);
	if (!campground.author.equals(req.user._id)) {
		//equals is a mongoose method to compare the id of the author of the campground with the id of the currently logged in user, if they are not equal, then the user is not the author of the campground and we will redirect them back to the campground page with an error message
		//req.user._id is coming from the session, thnx to passport, we are also passing it to every route (check app.js)
		req.flash("error", "You do not have permission to do that!");
		return res.redirect(`/campgrounds/${id}`);
	}
	next();
};

module.exports.isReviewAuthor = async (req, res, next) => {
	const { id, reviewId } = req.params;
	const review = await Review.findById(reviewId);
	if (!review.author.equals(req.user._id)) {
		req.flash("error", "You do not have permission to do that!");
		return res.redirect(`/campgrounds/${id}`);
	}
	next();
};

module.exports.validateReview = (req, res, next) => {
	const { error } = reviewSchema.validate(req.body);
	if (error) {
		const msg = error.details.map((el) => el.message).join(",");
		throw new ExpressError(msg, 400);
	} else {
		next();
	}
};

module.exports.storeReturnTo = (req, res, next) => {
	if (req.session.returnTo) {
		res.locals.returnTo = req.session.returnTo;
	}
	next();
};
