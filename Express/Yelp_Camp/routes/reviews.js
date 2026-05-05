const express = require("express");
const router = express.Router({ mergeParams: true });
//mergeParams:true is used to merge the parameters from the parent route, which is defined in app.js,
// so that we can access the campground id in this file, otherwise we won't be able to access it,
// because this file is a separate router and it won't have access to the parameters defined in app.js

// by default express router keeps the parameter from prefixes (which is defined in another file)
// and parameter in this file separate, so if we don't specify mergeParams:true,
// it won't merge the whole request "/campground/:id/reviwes/:reviewId" into one
// and we won't be able to retrieve any campground in this file, because we won't have access to it,

const { validateReview, isLoggedIn, isReviewAuthor } = require("../middleware");
const Campground = require("../models/campground");
const Review = require("../models/review");
const reviews = require("../controllers/reviews");
const ExpressError = require("../utils/ExpressError");
const catchAsync = require("../utils/catchAsync");

router.post("/", isLoggedIn, validateReview, catchAsync(reviews.createReview));

router.delete(
	"/:reviewId",
	isLoggedIn,
	isReviewAuthor,
	catchAsync(reviews.deleteReview),
);

module.exports = router;
