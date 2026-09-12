from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            "name",
            "email",
            "phone",
            "message",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": "Ismingiz",
                    "required": True,
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": "Emailingiz",
                    "required": True,
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": "Telefon raqamingiz",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "class": "form-input form-control",
                    "placeholder": "Xabaringiz...",
                    "rows": 6,
                    "required": True,
                }
            ),
        }
