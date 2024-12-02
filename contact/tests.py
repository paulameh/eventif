from django.test import TestCase
from django.core import mail
from contact.forms import contactForm

# Create your tests here.

class ContactTest(TestCase):
    def setUp(self):
        self.response = self.client.get("/contato/")

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "contact/contact_form.html")

    def test_html(self):
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, '<textarea')
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context["form"]
        self.assertSequenceEqual(['name', 'email', 'phone', 'message'], list(form.fields))


class ContactValid_Post_Email(TestCase):
    def setUp(self):
        data = dict(name='Fulano de tal', email='Fuladetal@gmail.com', phone='53-12345-6789', message='Site muito bom...')
        self.resp = self.client.post('/contato/', data)

    def test_post(self):
        self.assertEqual(302, self.resp.status_code)

    def test_send_contact_email(self):
        self.assertEqual(1, len(mail.outbox))

    def test_contact_email_subject(self):
        email = mail.outbox[0]
        expect = 'Mensagem de Fulano de tal para a comissão'
        self.assertEqual(expect, email.subject)

    def test_contact_email_from(self):
        email = mail.outbox[0]
        expect = 'Fuladetal@gmail.com'
        self.assertEqual(expect, email.from_email)
    
    def test_contact_email_to(self):
        email = mail.outbox[0]
        expect = ['contato@eventif.com.br', 'Fuladetal@gmail.com']
        self.assertEqual(expect, email.to)

    def test_contact_email_body(self):
        email = mail.outbox[0]
        self.assertIn('Fulano de tal', email.body)
        self.assertIn('Fuladetal@gmail.com', email.body) 
        self.assertIn('53-12345-6789', email.body)
        self.assertIn('Site muito bom...', email.body)


class ContactINvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post('/contato/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(
            self.resp, 'contact/contact_form.html'
        )

    def test_has_form(self): 
        form = self.resp.context['form'] 
        self.assertIsInstance(form, contactForm)

    def test_form_has_error(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
        #aqui
