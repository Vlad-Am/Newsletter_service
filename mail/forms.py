from django import forms
from django.forms import widgets

from mail.models import Newsletter, Message, Client


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class NewsletterForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ("frequency", "message", "status", "client", "datetime_start_send", "datetime_end_send")

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.fields['datetime_start_send'].widget = widgets.AdminSplitDateTime()
        # # "start_date": DateTimeInput(
        # #     attrs={"placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ:СС",
        # #            "type": "datetime-local"}
        # # ),


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ("message", "subject",)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("name", "surname", "email")




