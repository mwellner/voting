var pgp = require("pg-promise")({promiseLib: require("bluebird")});
var db = pgp("postgres://www@db/voting");
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/result', function(req, res, next) {
  db.any("SELECT vote, COUNT(*) AS count FROM votes GROUP BY vote ORDER BY vote")
	  .then(function(data) {
		  var count1 = parseInt(data[0].count);
		  var count2 = parseInt(data[1].count);
		  var count3 = parseInt(data[2].count);
  		var counts = { count1: count1, count2: count2, count3: count3, count: count1 + count2 + count3, title: "Voting Results" }
      res.render('index', counts);
		})
		.catch(function(error) {
      console.log("error getting counts!");
      res.render('error', {message: "Could not get counts", error: error});
		});
});

router.get('/contact', function(req, res, next) {
  res.render('contact');
});

module.exports = router;
