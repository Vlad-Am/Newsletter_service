from django import forms
from django.forms import widgets

from mail.models import Client, Message, Newsletter


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class NewsletterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = (
            "frequency",
            "message",
            "client",
            "datetime_start_send",
            "datetime_end_send",
        )

    datetime_start_send = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        ),
        input_formats=[
            "%Y-%m-%dT%H:%M",
        ],
    )
    datetime_end_send = forms.DateTimeField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "type": "datetime-local"}
        ),
        input_formats=[
            "%Y-%m-%dT%H:%M",
        ],
    )


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            "message",
            "subject",
        )


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("name", "surname", "email")


class NewsletterModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ("is_active",)
