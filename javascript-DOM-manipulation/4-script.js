#!/usr/bin/node
// Adds a li element to a list when the user clicks on the element
// with id add_item

const button = document.querySelector('#add_item');
button.addEventListener('click', () => addLI());

function addLI () {
  const element = document.querySelector('.my_list');
  const newLI = document.createElement('LI');
  const text = document.createTextNode('Item');

  newLI.appendChild(text);
  element.appendChild(newLI);
}
