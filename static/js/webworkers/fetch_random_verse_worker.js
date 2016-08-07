importScripts('/static/js/lib/fetch.js')

var url_get_verse = ""
var timeout = 5 * 60 * 1000;
var _id;

self.onmessage = function (event) {
		
	switch(event.data.cmd) {
		
		case "start":
			update_settings(event.data.options);
			schedule_next_fetch();
		
		case "update":
			update_settings(event.data.options);
		
		case "refresh_verse":
			fetch_verse_from_server();
	}
	
};

function update_settings(options) {
				
	timeout = options.timeout || timeout;
	url_get_verse = options.url_get_verse || url_get_verse;
	
	console.log(timeout);
	console.log(url_get_verse);
	
};

function fetch_verse_from_server() {
	
	clearTimeout(_id);
	
	fetch(url_get_verse).then(fetch_success, fetch_error);
	
};

function fetch_success(response) {
			
	var promise = response.json()
	
	promise.then(function(json_data) {
		
		self.postMessage(json_data);
		
	});
	
	schedule_next_fetch();
	
};

// handle network error
function fetch_error(error) {
	schedule_next_fetch();
};

function schedule_next_fetch() {
	_id = setTimeout(fetch_verse_from_server, timeout);
};

