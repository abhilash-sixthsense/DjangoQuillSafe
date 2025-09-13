from django import forms
from .models import Article
from quillsafe.fields import QuillFormField

class ArticleForm(forms.ModelForm):
    content = QuillFormField()

    class Meta:
        model = Article
        fields = ["title", "content"]
