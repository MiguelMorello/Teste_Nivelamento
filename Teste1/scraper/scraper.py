import zipfile
import os

def zip_pdfs(pdf_files, output_zip):
    
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pdf in pdf_files:
            if os.path.exists(pdf):
                zipf.write(pdf, os.path.basename(pdf))  
            else:
                print(f"Arquivo não encontrado: {pdf}")
    print(f"Arquivos compactados com sucesso em {output_zip}")


pdf_files = ['data/Anexo_I.pdf', 'data/Anexo_II.pdf']


output_zip = 'Anexos_test.zip'


zip_pdfs(pdf_files, output_zip)

