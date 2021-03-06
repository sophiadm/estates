from django import forms
from .models import Property, Review, QandA, BlogPost

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'content')

class QandAForm(forms.ModelForm):
    class Meta:
        model = QandA
        fields = ('question', 'answer')
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'description', 'content')

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('photo', 'rent', 'description', 'available')

class EmailForm(forms.Form):
    email = forms.EmailField(label='Your email address')
    msg = forms.CharField(widget=forms.Textarea, label="Message")
