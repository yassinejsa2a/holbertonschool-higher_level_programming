document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').innerHTML = data.hello;
    })
    .catch(function (error) {
      console.error(error);
    });
});