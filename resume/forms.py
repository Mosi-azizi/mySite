from django.forms import ModelForm
from .models import Profile,Skill,Message

class MessageFrom(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']
        labels = {
            'body': 'Your Message', 'name': 'Name', 'email': 'E-mail', 'subject': 'Subject'
        }

    def __init__(self, *args, **kwargs):
        super(MessageFrom, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.widget.attrs.update({'placeholder': field.label})
