from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label="Nome")
    email = forms.EmailField(label="email")
    phone = forms.CharField(label="Telefone", required=False)
    message = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={"rows":"5"}))
