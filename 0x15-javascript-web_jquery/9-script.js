$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  const salut = data.hello;
  $('#hello').append(salut);
});
