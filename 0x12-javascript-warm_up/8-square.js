#!/usr/bin/node

if (parseInt(process.argv[2])) {
  for (let height = 0; height < process.argv[2]; height++) {
    let stickedX = '';
    for (let width = 0; width < process.argv[2]; width++) {
      stickedX += 'X';
    }
    console.log(stickedX);
  }
} else {
  console.log('Missing size');
}
