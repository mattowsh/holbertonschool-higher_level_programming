#!/usr/bin/node
// Fetches and prints how to say “Hello” depending on the language
// URL: https://stefanbohacek.com/hellosalut/?lang=<language code>
// English: en; Spanish: es; French: fr

// IMPORTANT: You script must work when it imported from the head tag:
// Thus, APPLIES THE 'async' FEATURE TO SCRIPT IN HTML FILE

const url = 'https://stefanbohacek.com/hellosalut/?lang=';

const button = document.getElementById('btn_translate');
button.addEventListener('click', function() {
    console.log('in process...')
})
