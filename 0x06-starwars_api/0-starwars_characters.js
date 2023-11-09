#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 * use star wars api
 */

const request = require('request');

// Function to retrieve and print character names
function printMovieCharacters (filmId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const filmData = JSON.parse(body);
      const characterUrls = filmData.characters;

      // Iterate through characters and print names
      characterUrls.forEach((characterUrl) => {
        request(characterUrl, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
          }
        });
      });
    }
  });
}

// Get movie ID from command line argument
const movieId = process.argv[2];

// Call the function with the provided movie ID
printMovieCharacters(movieId);
