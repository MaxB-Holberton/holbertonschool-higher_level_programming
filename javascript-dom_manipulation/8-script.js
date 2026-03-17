const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';
fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (resdata) {
    const helloTag = document.getElementById('hello');
    helloTag.textContent = resdata.hello;
  });
