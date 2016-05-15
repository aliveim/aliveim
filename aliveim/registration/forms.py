from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    # User won't set a username directly. This will be set automatically to the
    # email value by the backend.
    username = forms.CharField(required=False, widget=forms.HiddenInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_username(self):
        return self.cleaned_data.get("email")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = user.email
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
