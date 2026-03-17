const character = document.getElementById('character');

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (resdata) {
    console.log(resdata);
    character.textContent = resdata.name;
  });
