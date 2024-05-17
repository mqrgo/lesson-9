from django import forms
from main_board.models import NewsPost


class NewsPostForm(forms.ModelForm):

    class Meta:
        model = NewsPost
        fields = ['title', 'cover', 'body', 'author', 'category']
