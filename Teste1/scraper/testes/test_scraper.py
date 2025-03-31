import unittest
from unittest.mock import patch, MagicMock
import os
from Teste_Nivelamento.Teste1.scraper.scraper import download_pdf, find_pdf_links, zip_pdfs

class TestScraper(unittest.TestCase):

    @patch('requests.get')
    def test_download_pdf(self, mock_get):
        
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = 'Teste de conteúdo do PDF'
        mock_get.return_value = mock_response
        
        
        download_pdf('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf', 'data/teste.pdf')

        
        mock_get.assert_called_once_with('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf')

        
        self.assertTrue(os.path.exists('data/teste.pdf'))
        
        
        os.remove('data/teste.pdf')

    @patch('requests.get')
    def test_find_pdf_links(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '''
        <html>
            <body>
                <a href="Anexo_I.pdf">Anexo I</a>
                <a href="Anexo_II.pdf">Anexo II</a>
            </body>
        </html>
        '''
        mock_get.return_value = mock_response
        
        
        pdf_links = find_pdf_links('https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos')

        # Verifica se os links "Anexo I" e "Anexo II" foram encontrados
        self.assertEqual(len(pdf_links), 2)
        self.assertIn('Anexo_I.pdf', pdf_links)
        self.assertIn('Anexo_II.pdf', pdf_links)
    
    
    def test_zip_pdfs(self):
        test_files = ['data/teste1.pdf', 'data/teste2.pdf']
        
        os.makedirs('data', exist_ok=True)

        for file in test_files:
            with open(file, 'w') as f:
                f.write('Conteúdo de teste')


        zip_pdfs(test_files, 'data/teste.zip')

        
        self.assertTrue(os.path.exists('data/teste.zip'))

        os.remove('data/teste1.pdf')
        os.remove('data/teste2.pdf')
        os.remove('data/teste.zip')

if __name__ == '__main__':
    unittest.main()
