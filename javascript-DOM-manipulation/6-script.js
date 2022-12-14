#!/usr/bin/node
// Fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag with id 'character'

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#character');
    element.innerHTML = `<ul><li>${data.name}</li></ul>`;
  })
  .catch(error => console.log(error));
