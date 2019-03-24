#!/usr/bin/python3
def wsgi_application(environ, start_response):
	body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
	header = [ ('Content-Type', 'text/plain') ]
	status = '200 OK'
	start_response(status, header)
	return body
