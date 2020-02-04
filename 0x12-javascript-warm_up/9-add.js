#!/usr/bin/node

function add (a,b) {
  const number = Number(process.argv[2]);
  const numbertoadd = Number(process.argv[3]);
  const result = number + numbertoadd;
  console.log(result);
}
add();
