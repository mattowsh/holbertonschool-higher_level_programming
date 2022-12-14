#!/usr/bin/node
// Displays the value of 'hello' from the fetch in the HTML element
// with id 'hello'
// URL: https://fourtonfish.com/hellosalut/?lang=fr

fetch('https://stefanbohacek.com/hellosalut/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const element = document.querySelector('#hello');
    element.innerHTML = data.hello;
  })
  .catch(error => console.log(error));
