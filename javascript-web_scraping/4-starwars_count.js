#!/usr/bin/node
// Prints the number of movies where the character “Wedge Antilles” is present

const url = process.argv[2];
const request = require('request');
const characterURL = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  let counter = 0;
  data.results.forEach(film => {
    if (film.characters.includes(characterURL)) {
      counter++;
    }
  });
  console.log(counter);
});
