from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contgib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(**self.cleaned_data)
        question.save()
        return question

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(id=question_id)
        except Question.DoesNotExist:
            question = None
        return question

    def clean(self):
        return self.cleaned_data

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

class LoginForm(forms.Form):
    username = forms.CharField(max_lenght=100)
    email = forms.CharField(max_lenght=100)
    password = forms.CharField(widget_forms.PasswordInput)

    def clean_password(self):
        return make_password(self.password)

    def save(self):
        user = User(**self.cleaned_data)
        user.save()
        return user

class SignupForm(forms.Form):
    username = forms.CharField(max_lenght=100)
    password = forms.CharField(widget_forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        user_name = User.objects.filter(username = username)[:]
        user_email = User.objects.filter(email = email)[:]
        if (len(user_name) != 0):
            raise forms.ValidationError(u'Пользователь с таким именем уже существует', code=1)
        if (len(user_email) != 0):
            raise forms.ValidationError(u'Пользователь с таким электронным адресом уже существует', code=2)

        def save(self):
            user = User.objects.create_user(**self.cleaned_data)
            user.save()
            return user
