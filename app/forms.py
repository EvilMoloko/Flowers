"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment, Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class AnketaForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=25)
    order = forms.ChoiceField(label='Ранее Вы уже заказывали у нас цветы?',
                             choices=[('1','Да'),('2','Нет')],
                             widget=forms.RadioSelect, initial=2)
    notice = forms.BooleanField(label='Получать специальные предложения на E-mail?', required=False)
    email = forms.EmailField(label='Ваш E-mail', min_length=7)
    message = forms.CharField(label='Оставьте здесь свой отзыв',
                              widget=forms.Textarea(attrs={'rows':12,'cols':25}))


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm (forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ('title', 'description', 'content', 'image') 
        labels = {'title': "Комментарий",'description': 'Краткое содержание', 'content': 'Полное содержание', 'image': 'Картинка'} # метка к полю формы text