from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Felipe", email='felipe.socolowski@aluno.riogrande.ifrs.edu.br', phone='53-12345-6789', message='Olá, tudo bem?')
        self.client.post(r('contact:new'), data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Confirmação de contato!'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'felipe.socolowski@aluno.riogrande.ifrs.edu.br']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'Felipe',
            'felipe.socolowski@aluno.riogrande.ifrs.edu.br',
            '53-12345-6789',
            'Olá, tudo bem?'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)