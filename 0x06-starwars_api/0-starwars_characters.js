#!/usr/bin/node
/**
 * a script that prints all characters of a Star Wars movie
 * use star wars api
 */

const request = require('request');
const movieId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const characters = JSON.parse(body).characters;
  const characterNames = [];

  let count = 0;

  characters.forEach((character, index) => {
    request(character, function (error, response, body) {
      if (error) {
        console.error(error);
      }
      characterNames[index] = JSON.parse(body).name;

      count++;

      if (count === characters.length) {
        characterNames.forEach(name => {
          console.log(name);
        });
      }
    });
  });
});
