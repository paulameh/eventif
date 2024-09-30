from django.test import TestCase

class Hometest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

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