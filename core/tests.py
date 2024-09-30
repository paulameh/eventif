from django.test import TestCase

# class Hometest(TestCase):
#     def setUp(self):
#         self.response = self.client.get('/')

#     def test_get(self):
#         '''
#         Testa se a página inicial retorna status code
#         '''
#         self.assertEqual(200, self.response.status_code)

#     def test_templete(self):
#         '''
#         Verifica se o diretório template está sendo usado
#         '''
#         self.assertTemplateUsed(self.response, 'index.html')

class SubscriTest(TestCase):
    def setUp(self):
        response = self.client.get("/inscicao/")
        
    def test_get(self):
        self.assertEqual(200, response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, "index.html")

    def test_html(self):
        self.assertContains(self.response, "<form")
        self.assertContains(self.response, "<input", 6)
        self.assertContains(self.response, "<type='text'", 3)
        self.assertContains(self.response, "<type='email'")
        self.assertContains(self.response, "<type='submit'")

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.response.context("form")
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))