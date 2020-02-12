#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const argv = process.argv[2];
const file = process.argv[3];

request(argv, function (err, body) {
  if (err) {
    return console.log(err);
  } else {
    fs.write(file, 'utf-8', body);
  }
});
