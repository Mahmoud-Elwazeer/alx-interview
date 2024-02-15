#!/usr/bin/node

'use strict';
const request = require('request')

let url = "https://swapi-api.alx-tools.com/api/films/" + `${process.argv[2]}`

request(url, (error, response, body) => {
    // Printing the error if occurred
    if (error) throw error

    const actors = JSON.parse(body).characters;

    actors.forEach(item => {
        request(item, (error, response, body) => {
            // Printing the error if occurred
            if (error) throw error

            const name = JSON.parse(body).name
            console.log(name)
        })
    });
});