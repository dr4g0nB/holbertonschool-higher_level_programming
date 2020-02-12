#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/';
const argv = process.argv[2];

request(url + argv, function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    for (let i = 0; i < url.lenght; i++) {
      console.log(i.characters);
    }
  }
});
