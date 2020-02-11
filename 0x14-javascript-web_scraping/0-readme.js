#!/usr/bin/node

const fs = require('fs');
const argv = process.argv[2];

fs.readFile(argv, 'utf-8', function (err, data) {
  if (err) {
    return console.log(err);
  } else {
    process.stdout.write(data);
  }
});
