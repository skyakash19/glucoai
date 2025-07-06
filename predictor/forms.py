from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# 🔹 Custom Signup Form for CustomUser
class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        label="Register as",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "role", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# 🔹 Diabetes Input Form for Prediction
class DiabetesForm(forms.Form):
    pregnancies = forms.IntegerField(label="Pregnancies")
    glucose = forms.FloatField(label="Glucose")
    blood_pressure = forms.FloatField(label="Blood Pressure")
    skin_thickness = forms.FloatField(label="Skin Thickness")
    insulin = forms.FloatField(label="Insulin")
    bmi = forms.FloatField(label="BMI")
    diabetes_pedigree_function = forms.FloatField(label="Diabetes Pedigree Function")
    age = forms.IntegerField(label="Age")

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if cleaned_data.get(field) is None:
                raise forms.ValidationError(f"{field.replace('_', ' ').capitalize()} is required.")
        return cleaned_data
