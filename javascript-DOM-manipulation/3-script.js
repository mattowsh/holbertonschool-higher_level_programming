#!/usr/bin/node
// Toggles the class of the header element when the user clicks on the
// tag id 'toggle_header'

const button = document.querySelector('#toggle_header');
button.addEventListener('click', () => toggleClass());

function toggleClass () {
  const element = document.querySelector('header');
  element.classList.toggle('red');
  element.classList.toggle('green');
}
