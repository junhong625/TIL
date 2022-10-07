from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    Romance = '로맨스'
    Comedy = '코미디'
    Horror = '호러'
    Action = '액션'
    Fantasy = '판타지'
    GENRE_CHOICES = [
        (Romance, 'Romance'),
        (Comedy, 'Comedy'),
        (Horror, 'Horror'),
        (Action, 'Action'),
        (Fantasy, 'Fantasy'),
    ]
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'제목'}))
    audience = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'관객 수'}))
    genre = forms.ChoiceField(choices=GENRE_CHOICES, widget=forms.Select(attrs={'class':'form-control', 'placeholder':'genre'}))
    score = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'type':'number', 'step':0.5, 'min':0.0, 'max':5.0, 'placeholder':'score'}))
    release_date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    poster_url = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'포스터 URL'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'설명'}))
    class Meta:
        model = Movie
        fields = '__all__'