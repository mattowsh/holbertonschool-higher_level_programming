#!/usr/bin/node
// Script that writes a string to a file

const FilePath = process.argv[2];
const NewString = process.argv[3];
const request = require('fs');

request.appendFile(FilePath, NewString, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
