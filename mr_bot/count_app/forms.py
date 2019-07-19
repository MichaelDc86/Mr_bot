import django.forms as forms
from count_app.models import BotUser, Count

from django.contrib.auth.forms import UserCreationForm


class BotUserRegisterForm(UserCreationForm):
    class Meta:
        model = BotUser
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, commit=True):
        print('Hallo')
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            user_counter = Count(usr=user)
            user_counter.save()

        return user


class CounterForm(forms.ModelForm):
    class Meta:
        model = Count
        fields = ('count',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
