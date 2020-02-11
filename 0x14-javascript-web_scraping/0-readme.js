#!/usr/bin/node

const fs = require('fs');
const argv = process.argv[2];

fs.readFile(argv, 'utf-8', function (error, data) {
  if (error) {
    process.stdout.write(error);
  } else {
    process.stdout.write(data);
  }
});
