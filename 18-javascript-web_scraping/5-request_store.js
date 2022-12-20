#!/usr/bin/node
// Gets the contents of a webpage and stores it in a file

const url = process.argv[2];
const FilePath = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(FilePath, body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
