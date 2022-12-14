#!/usr/bin/node
// Fetches and lists the title for all movies by using this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
// The name must be displayed in the HTML tag with id 'character'

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#list_movies');
    for (const film of data.results) {
      const newLI = document.createElement('LI');
      const text = document.createTextNode(film.title);

      newLI.appendChild(text);
      element.appendChild(newLI);
    }
  })
  .catch(error => console.log(error));
