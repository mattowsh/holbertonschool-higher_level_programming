#!/usr/bin/node
// Updates the text color of the header element to red (#FF0000) when the user
// clicks on the tag with id red_header

const button = document.querySelector('#red_header');
button.addEventListener('click', () => changeColor());

function changeColor () {
  const element = document.querySelector('header');
  element.style.color = '#FF0000';
}
