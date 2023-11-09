#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 * use star wars api
 */

const request = require('request');

// Function to retrieve and print character names
function printMovieCharacters (filmId) {
  const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

  return new Promise((resolve, reject) => {
    request(apiUrl, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error || new Error(`Request failed with status code ${response.statusCode}`));
        return;
      }

      const filmData = JSON.parse(body);
      const characterUrls = filmData.characters;

      // Use Promise.all to wait for all character requests
      const characterPromises = characterUrls.map(characterUrl => new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error || response.statusCode !== 200) {
            reject(error || new Error(`Request failed with status code ${response.statusCode}`));
            return;
          }
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        });
      }));

      Promise.all(characterPromises)
        .then(characters => resolve(characters))
        .catch(reject);
    });
  });
}

// Get movie ID from command line argument
const movieId = process.argv[2];

// Call the function with the provided movie ID
printMovieCharacters(movieId)
  .then(characters => {
    // Print characters in the correct order
    characters.forEach(character => {
      console.log(character);
    });
  })
  .catch(error => {
    console.error('An error occurred:', error.message);
  });
