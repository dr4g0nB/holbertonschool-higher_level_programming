#!/usr/bin/node

const fs = require['fs'];
const file_path = process.argv[2];
const stringTowrite = process.argv[3];

fs.writeFile(file_path, stringTowrite, "utf-8", function(error) {
  if (error) {
    console.error(error);
  } else { 
    console.log(stringTowrite);
  }
});
