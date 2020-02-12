#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request(argv, (err, response, body) => {
  if (err) {
    console.log(err);
  }
  if (response) {
    const data = JSON.parse(body);
    let count = 0;
    for (const travDict of data.results) {
      for (const travCharac of travDict.characters) {
        if (travCharac.search('people/18') !== -1) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
