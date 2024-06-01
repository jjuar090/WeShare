from django import forms
from .models import Comment
from .models import Post
import string
import random
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']


from django import forms
from .models import Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            # Generate a random slug
            slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            instance.slug = slug
        if commit:
            instance.save()
        return instance


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if not instance.slug:
            # Generate a random slug
            slug = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
            instance.slug = slug
        if commit:
            instance.save()
        return instance