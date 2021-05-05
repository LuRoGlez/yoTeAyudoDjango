from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    email=forms.EmailField(required=True,help_text="Requerido. 254 caracteres como maximo")

    class Meta:
        model=User
        fields=('username','password1','password2','email')

    def clean_email(self):
        value=self.cleaned_data['email']
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Email ya registrado, prueba otro")
        return value

    def save(self, commit=True):
        user = super(UserCreationForm, self).save()
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user