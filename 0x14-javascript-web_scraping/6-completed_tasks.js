#!/usr/bin/node

const request = require('request');
const url = 'https://jsonplaceholder.typicode.com/todos';

request.get(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }

  if (response) {
    const data = JSON.parse(body);
    const todosDict = {};
    for (const travDictUser of data) {
      if (travDictUser.completed) todosDict[travDictUser.userId] = 0;
    }
    for (const travDictCompleted of data) {
      if (travDictCompleted.completed) todosDict[travDictCompleted.userId] += 1;
    }
    console.log(todosDict);
  }
});
