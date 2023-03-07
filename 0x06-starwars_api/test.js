const rp = require("request-promise");

const args = process.argv.slice(2);
const id = args[0];

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
    for (let api of myObj.characters) {
      var name = await printNames(api);
      console.log(name);
    }
  });
}

main();
