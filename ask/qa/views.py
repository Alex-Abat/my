from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def new(request):
    limit = int(request.GET.get('limit', 10))
    page = int(request.GET.get('page', 1))
    paginator = Paginator(Questions.objects.new(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'templates/new.html', {
        paginator :paginator, page:
        page: page.object_list
    })
