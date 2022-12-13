#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args[2] && isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else if (args[2] > 0) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
}
