# Teste de Nivelamento 

Este repositório contém as soluções para o teste de nivelamento envolvendo Web Scraping, Transformação de Dados, Banco de Dados e API, conforme os requisitos solicitados.

## Descrição dos Testes

### 1. **Teste de Web Scraping**
O objetivo deste teste é:
1. Acessar o site: [Acesso à Informação - ANS](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).
2. Baixar os Anexos I e II em formato PDF.
3. Compactar os arquivos em um único arquivo ZIP.

**Tecnologias usadas**: Python

### 2. **Teste de Transformação de Dados**
O objetivo deste teste é:
1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I.
2. Salvar os dados extraídos em formato CSV.
3. Compactar o arquivo CSV em um arquivo ZIP nomeado como "Teste_{seu_nome}.zip".
4. Substituir abreviações de colunas (OD e AMB) pelas descrições completas, conforme a legenda no rodapé do PDF.

**Tecnologias usadas**: Python com jupyter notbook

### 3. **Teste de Banco de Dados**
O objetivo deste teste é:
1. Baixar os arquivos de dados cadastrais das operadoras ativas da ANS e as demonstrações contábeis do último ano, usando os links fornecidos.
2. Criar queries SQL para estruturar as tabelas no banco de dados.
3. Importar os arquivos CSV para as tabelas.
4. Desenvolver queries analíticas para responder:
   - Quais as 10 operadoras com maiores despesas no último trimestre em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"?
   - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

**Tecnologias usadas**: MySQL

### 4. **Teste de API**
O objetivo deste teste é:
1. Criar uma interface web utilizando Vue.js.
2. Desenvolver um servidor em Python que interaja com a interface, realizando uma busca textual nos dados dos cadastros de operadoras.
3. Criar uma coleção no Postman para demonstrar o funcionamento da API.

**Tecnologias usadas**: Vue.js, Python, Postman e Replit
