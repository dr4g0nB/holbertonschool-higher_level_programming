#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringTowrite = process.argv[3];

fs.writeFile(filePath, stringTowrite, 'utf-8', function (error) {
  if (error) {
    return console.error(error);
  }
  /** else {
    console.log(stringTowrite);
  } */
});
