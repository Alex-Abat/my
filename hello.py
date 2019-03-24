#!/usr/bin/python3
def wsgi_application(environ, start_response):
	body = ((i + '\n') for i in environ.get('QUERRY_STRING').split('&'))
	header = [ ('Content-Type', 'text/plain') ]
	status = '200 OK'
	start_response(status, header)
	return [ body ]
