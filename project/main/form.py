from django import forms

class CommentForm(forms.Form):
    text= forms.CharField(max_length=500, label='Matn', widget=forms.Textarea(attrs={
        "style":"font-size: 22pt; padding: 15px; border-radius: 15px;",
        "rows":"4",
        "cols": "40"       
    }))