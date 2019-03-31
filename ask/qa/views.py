from django.http import HttpResponse
# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')
