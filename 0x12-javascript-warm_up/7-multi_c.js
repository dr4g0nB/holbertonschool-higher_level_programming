#!/usr/bin/node

if (parseInt(process.argv[2])) {
  let multi = 0;
  while (multi < process.argv[2]) {
    console.log('C is fun');
    multi++;
    }
} else {
  console.log('Missing number of occurrences');
}
