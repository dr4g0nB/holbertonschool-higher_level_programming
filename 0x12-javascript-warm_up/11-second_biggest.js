#!/usr/bin/node

const arg = process.argv.slice(2);
if (arg.length <= 1) {
  console.log(0);
} else {
  const values = arg.map(value => parseInt(value));
  let max = Math.max(...values);

  const list = [];
  for (let i = 0; i < values.length; i++) {
    if (values[i] !== max) {
      list.push(values[i]);
    }
  }
  max = Math.max(...list);
  console.log(max);
}
