#!/usr/bin/node

const fs = require('fs');
const argv = process.argv[2];

fs.readFile(argv, 'utf-8', function (err, data) {
  if (err) {
    process.stdout.write(err);
  } else {
    process.stdout.write(data);
  }
});
