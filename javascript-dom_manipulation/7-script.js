const moviesList = document.getElementById('list_movies');
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (resdata) {
    console.log(resdata);
    const results = resdata.results;
    results.forEach(function (item) {
      const newItem = document.createElement('li');
      newItem.textContent = item.title;
      moviesList.appendChild(newItem);
    });
  });
