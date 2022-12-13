#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length <= 3) {
  console.log('0');
} else {
  const newList = [];
  // removes unused arguments
  args.splice(0, 2);
  // converts every item into an int
  args.forEach(element => {
    newList.push(parseInt(element));
  });
  // sorts
  newList.sort((a, b) => b - a);
  console.log(newList[1]);
}
