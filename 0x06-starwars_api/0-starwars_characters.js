#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 * use star wars api
 */

const request = require('request');
const movieId = process.argv[2];
if (!movieId  || isNaN(movieId)) {
  process.exit(1);
}

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const characters = JSON.parse(body).characters;
  characters.forEach(character => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
