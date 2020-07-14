
from django import forms


class Form1(forms.Form):
    text = forms.CharField(label='Отзыв', min_length=3, max_length=10)
    number = forms.IntegerField(label='Оценка', min_value=1, max_value=100)
    photo = forms.FileField(label='Фотография', required=False)

    def clean_text(self):
        if 'abc' not in self.cleaned_data['text']:
            raise forms.ValidationError('Неверный текст')