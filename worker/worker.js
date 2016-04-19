var options = { promiseLib: require("bluebird") };
var pgp = require("pg-promise")(options);
var db = pgp("postgres://www@db/voting");

var redis = require("redis");
var client = redis.createClient(6379, "redis");

client.on("error", function(err) {
  console.log("Error " + err);
});

var interval = 5;
console.log("Starting worker process with interval of " + interval + "ms");

setInterval(function() {
  var multi = client.multi();
  multi.exec(multiCommandCallback);
}, interval);


function multiCommandCallback(err, res) {
  client.llen("votes", function(err, len) {
    if (err === null && len > 0) {
      client.lpop("votes", function(err, queueItem) {
        console.log("recieved item " + queueItem + " from redis queue");
        var number = parseInt(queueItem, 10);
        if (!isNaN(number)) storeVoteInDb(number);
      });
    }
  });
}

function storeVoteInDb(number) {
  db.none("INSERT INTO votes(vote) VALUES($1)", [number])
    .then(function() {
      console.log("saved vote " + number + " in database");
    })
    .catch(function (error) {
      console.log("error: " + error);
    });
}
