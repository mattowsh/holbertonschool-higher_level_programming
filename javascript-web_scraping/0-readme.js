#!/usr/bin/node
// Reads and prints the content of a file

const FilePath = process.argv[2];
const request = require('fs');

request.readFile(FilePath, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
