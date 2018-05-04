var scraper = require('google-search-scraper');
var lyrics_site = " site:letras.mus.br";
const args = require('minimist')(process.argv.slice(2));

var options = {
  query: '',
  host: 'www.google.com',
  lang: 'br',
  limit: "1",
};

function searchSongs (url, err) {
	if(err) throw err;
	console.log(url)
	console.log(options.query);
}

function main () {
	options.query = args.t + " " + args.a + lyrics_site;
	scraper.search(options, function(err, url) {
		searchSongs(url, err)
	});
}

main()
