#!/usr/bin/node

const request = require('request');
const movieId = 'http://swapi.co/api/films/';
const argv = process.argv[2];

request(movieId + argv, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
