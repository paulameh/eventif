from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from contact.forms import contactForm
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            mensageiro = form.cleaned_data['name']
            body = render_to_string('contact/contact_email.txt', form.cleaned_data)
            mail.send_mail(f'Mensagem de {mensageiro} para a comissão', 
                           body, 
                            form.cleaned_data['email'], 
                            ['contato@eventif.com.br', form.cleaned_data['email']]) # isso aqui vai ter de mudar
            messages.success(request, 'Mensagem enviada!')
            return HttpResponseRedirect('/contato/')  
        else:
            return render(request, 'contact/contact_form.html', {'form': form})
    else:
        context = {'form': contactForm()}
        return render(request, 'contact/contact_form.html', context)
