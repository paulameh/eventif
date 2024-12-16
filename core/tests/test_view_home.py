from django.test import TestCase
from django.shortcuts import resolve_url as r

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from django.core import mail
from django.template.loader import render_to_string
from subscriptions.forms import SubscriptionForm

class Hometest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))


    def test_get(self):
        '''
        Testa se a página inicial retorna status code
        '''
        self.assertEqual(200, self.response.status_code)

    def test_templete(self):
        '''
        Verifica se o diretório template está sendo usado
        '''
        self.assertTemplateUsed(self.response, 'index.html')

    def test_link_subscription(self):
        self.assertContains(
            self.response, 'href="{}"'.format(r('subscriptions:new'))
        )
    
    def test_speakers(self):
        contents = [
            'Grace Hopper',
            'https://abre.ai/hopper-pic',
            'Alan Turing',
            'https://abre.ai/turing-pic'
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)
    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)