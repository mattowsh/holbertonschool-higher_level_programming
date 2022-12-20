#!/usr/bin/node
// Script that adds, removes and clears li elements from a list when
// the user clicks
// IMPORTANT: You script must work when it imported from the head tag:
// Thus, APPLIES THE 'async' FEATURE TO SCRIPT IN HTML FILE

// Selects all actionables
const addButton = document.querySelector('#add_item');
const removeButton = document.querySelector('#remove_item');
const clearButton = document.querySelector('#clear_list');

// Creates all click events and their respective functions
addButton.addEventListener('click', () => addLI());
removeButton.addEventListener('click', () => removeLI());
clearButton.addEventListener('click', () => clearLI());

// A new element is added to the list:
function addLI () {
  const element = document.querySelector('.my_list');
  const newLI = document.createElement('LI');
  const text = document.createTextNode('Item');

  newLI.appendChild(text);
  element.appendChild(newLI);
}

// The last element is removed from the list:
function removeLI () {
  const element = document.querySelector('.my_list');
  element.removeChild(element.lastChild);
}

// All elements of the list are removed:
function clearLI () {
  const element = document.querySelector('.my_list');
  while (element.hasChildNodes()) {
    element.removeChild(element.lastChild);
  }
}
