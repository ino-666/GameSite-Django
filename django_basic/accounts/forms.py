from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateInput(
            format='%m-%d',
            attrs={
                'type': 'date'
            }
        )
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('birth_date', 'age',)

#下の元のやつとの違いは誕生日の日付を入力しやすしている点、DateFieldのウィジェットをカスタマイズしている

#class CustomUserCreationForm(UserCreationForm):
#    class Meta(UserCreationForm.Meta):
#        model = CustomUser
#        fields = UserCreationForm.Meta.fields + ('birth_date', 'age',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text',]