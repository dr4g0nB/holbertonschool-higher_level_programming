#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request.get(argv, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    const code = response.statusCode;
    console.log('code:', code);
  }
});
