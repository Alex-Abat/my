from django.http import HttpResponseRedirect, Http404
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm
from django.shortcuts import render
from django.contrib.auth import login

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
        'page':      page.object_list,
        'user': request.user,
    })
def popular(request):
    limit = 10
    page = int(request.GET.get('page', 1))
    paginator = Paginator(Question.objects.popular(), limit)
    page = paginator.page(page)
    paginator.baseurl = '/question/'
    return render(request, 'list.html',{
        'page':      page.object_list,
        'paginator': paginator,
        'user' : request.user,
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
    else:
        form = AnswerForm()
    a = Answer.objects.all().filter(question=q)
    return render(request, 'question.html',{
        'q': q,
        'a': a,
        'form': form
    })

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {
        'form':form,
        'user': request.user,
    })

def login1(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        form.is_valid()
        user = form.save()
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup1(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else: form = SignupForm()
    return render(request, 'signup.html', {'form': form})
