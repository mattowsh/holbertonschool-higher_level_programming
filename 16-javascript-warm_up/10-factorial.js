#!/usr/bin/node
const process = require('process');
const number = process.argv[2];

console.log(factorial(parseInt(number)));
function factorial (number) {
  if (isNaN(number) || number === 0) {
    return 1;
  } return number * factorial(number - 1);
}
