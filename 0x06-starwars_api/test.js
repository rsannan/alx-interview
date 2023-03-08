#!/usr/bin/node

const rp = require("request-promise");

const args = process.argv.slice(2);
const id = args[0];
const names = [];

function printNames(api) {
  return new Promise(function (resolve, reject) {
    rp(api).then((body) => {
      const myName = JSON.parse(body);
      resolve(myName.name);
    });
  });
}

function main() {
  rp(`https://swapi-api.alx-tools.com/api/films/${id}`).then(async (body) => {
    const myObj = JSON.parse(body);
    for (const api of myObj.characters) {
      const name = await printNames(api);
      names.push(name);
    }

    for (const n of names) {
      if (n === names[names.length - 1]) {
        process.stdout.write(n);
      } else {
        process.stdout.write(n + "\n");
      }
    }
  });
}

main();
