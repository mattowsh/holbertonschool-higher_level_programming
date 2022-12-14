#!/usr/bin/node
// Updates the text of the header element to New Header!!! when the user
// clicks on the element with id update_header

const button = document.querySelector('#update_header');
button.addEventListener('click', () => updateHeader());

function updateHeader () {
  const element = document.querySelector('header');
  element.innerText = 'New Header!!!';
}
