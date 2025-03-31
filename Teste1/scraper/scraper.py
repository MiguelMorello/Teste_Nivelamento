import requests
from bs4 import BeautifulSoup
import zipfile
import os


def download_pdf(url, download_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, 'wb') as f:
            f.write(response.content)
        print(f"Arquivo {download_path} baixado com sucesso!")
    else:
        print(f"Falha ao baixar o arquivo de {url}")


def find_pdf_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pdf_links = []
        for a_tag in soup.find_all('a', href=True):
            link = a_tag['href']
            
            if 'pdf' in link.lower() and ('Anexo I' in a_tag.get_text() or 'Anexo II' in a_tag.get_text()):
                pdf_links.append(link if link.startswith('http') else url + link)
        return pdf_links
    else:
        print(f"Falha ao acessar o site {url}")
        return []


def zip_pdfs(pdf_files, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for pdf in pdf_files:
            if os.path.exists(pdf):
                zipf.write(pdf, os.path.basename(pdf))  
            else:
                print(f"Arquivo não encontrado: {pdf}")
    print(f"Arquivos compactados com sucesso em {output_zip}")


url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'


pdf_links = find_pdf_links(url)


download_dir = 'data/'


if not os.path.exists(download_dir):
    os.makedirs(download_dir)


pdf_files = []
for link in pdf_links:
    filename = link.split('/')[-1]
    file_path = os.path.join(download_dir, filename)
    download_pdf(link, file_path)
    pdf_files.append(file_path)


output_zip = 'Anexos.zip'
zip_pdfs(pdf_files, output_zip)