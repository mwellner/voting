var express = require('express');
var router = express.Router();

var redis = require('redis');
var client = redis.createClient(6379, "redis");

client.on("error", function(err) {
  console.log("Error " + err);
});

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { });
});

router.post('/', function(req, res, next) {
  console.log(req.body);
  client.rpush('votes', req.body.vote);  
  res.render('confirm', {vote: req.body.vote});
});

module.exports = router;
