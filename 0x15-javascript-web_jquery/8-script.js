$.get('https://swapi.co/api/films/?format=json', function (data) {
  const movieTitle = data.movies;
  for (let trav in movieTitle) {
    $('#list_movies').append('<LI>' + movieTitle[trav].title + '</LI>');
  }
});  
