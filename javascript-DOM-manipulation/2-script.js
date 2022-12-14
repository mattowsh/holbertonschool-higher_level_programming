#!/usr/bin/node
// Adds the class red to the header element when the user clicks on the
// tag with id red_header

const button = document.querySelector('#red_header');
button.addEventListener('click', () => addClass());

function addClass () {
  const element = document.querySelector('header');
  element.classList.add('red');
}
