#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, function (err, response, body){
  if (err) {
    return console.log(err);
  } else {
    console.log(JSON.parse(body).userId);
  }
});
