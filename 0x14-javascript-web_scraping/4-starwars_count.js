#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request(argv, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    /** for () {} */
    console.log(JSON.parse(body).id);
  }
});
