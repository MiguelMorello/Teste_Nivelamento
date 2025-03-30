import unittest
import os
import zipfile
from Teste_Nivelamento.Teste1.scraper.scraper import zip_pdfs  

class TestScraper(unittest.TestCase):

    def setUp(self):
       
        self.pdf_files = ['Teste_Nivelamento\data\Anexo_I.pdf', 'Teste_Nivelamento\data\Anexo_II.pdf']
        self.output_zip = 'Anexos_test.zip'
        
        
        os.makedirs(os.path.dirname(self.pdf_files[0]), exist_ok=True)
        for pdf in self.pdf_files:
            if not os.path.exists(pdf):  
                with open(pdf, 'w') as f:
                    f.write("Conteúdo do arquivo PDF")
        
    def test_zip_pdfs(self):
        
        for pdf in self.pdf_files:
            self.assertTrue(os.path.exists(pdf), f"O arquivo {pdf} não foi encontrado.")
        
        
        zip_pdfs(self.pdf_files, self.output_zip)

      
        self.assertTrue(os.path.exists(self.output_zip), f"O arquivo {self.output_zip} não foi criado.")

       
        if os.path.exists(self.output_zip):
            with zipfile.ZipFile(self.output_zip, 'r') as zipf:
                zip_contents = zipf.namelist()
                for pdf in self.pdf_files:
                    self.assertIn(os.path.basename(pdf), zip_contents, f"{os.path.basename(pdf)} não está no ZIP.")
    
if __name__ == '__main__':
    unittest.main()
