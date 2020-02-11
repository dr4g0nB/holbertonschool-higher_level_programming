#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request.get(argv, function (err, response, body) {
  const code = response.statusCode;
  if (err) {
    console.log(err);
  } else {
    console.log('code: ', code);
  }
});
