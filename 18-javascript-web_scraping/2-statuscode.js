#!/usr/bin/node
// Display the status code of a GET request

const FilePath = process.argv[2];
const request = require('request');

request(FilePath, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
