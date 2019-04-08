from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from qa.models import Question
from django.shortcuts import render

# Create your views here.
def test(request, *args, **kwargs):
	return HttpResponse('OK')

def new(request):
    limit = 10
    page = int(request.GET.get('page', 1))
    paginator = Paginator(Question.objects.new(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'list.html', {
        'paginator': paginator,
        'page':      page.object_list
    })
def popular(request):
    limit = 10
    page = int(request.GET.get('page', 1))
    paginator = Paginator(Question.objects.popular(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'list.html',{
        'page':      page.object_list,
        'paginator': paginator

    })
def question(request, num):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else form = AskForm()
    return render(request, 'question.html',{
        'q': q,
        'form': form,
    })

def ask(request):
    if request.method == "POST":
        form = AddPostForm(request.GET)
        if form.is_valid():
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form':form,})
