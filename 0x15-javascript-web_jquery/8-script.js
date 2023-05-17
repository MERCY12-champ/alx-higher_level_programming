$.get('https://swapi.co/api/films/?format=json', function (data) {
	$('UL3LIST_MOVIES').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
