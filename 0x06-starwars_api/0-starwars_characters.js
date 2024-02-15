#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + `${process.argv[2]}`;

request(url, (error, response, body) => {
  // Printing the error if occurred
  if (error) throw error;

  const actors = JSON.parse(body).characters;

  async function fetchActors () {
    for (const item of actors) {
      try {
        const response = await getRequest(item);
        const name = JSON.parse(response.body).name;
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  }

  function getRequest (url) {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve(response);
        }
      });
    });
  }

  fetchActors();
});
