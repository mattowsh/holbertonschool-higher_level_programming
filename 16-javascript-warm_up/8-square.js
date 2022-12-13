#!/usr/bin/node
const process = require('process');
const area = process.argv[2];

if (isNaN(area)) {
  console.log('Missing size');
} else if (area > 0) {
  for (let i = 0; i < area; i++) {
    if (i !== 0) {
      console.log();
    }
    for (let j = 0; j < area; j++) {
      process.stdout.write('X');
    }
  }
  console.log();
}

// Alternative way using console.log('X'.repeat(area))
