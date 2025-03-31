COPY operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM 'Teste_Nivelamento\Teste3\database\Datas\Relatorio_cadop.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2024_Q1(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\1T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2024_Q2(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\2T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2024_Q3(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\3T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2024_Q4(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\4T2024.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2023_Q1(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\1T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2023_Q2(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\2t2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2023_Q3(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\3T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demonstracoes_contabeis_2023_Q4(data, registro_ans, cd_conta_contabil, descricao, saldo_inicial, saldo_final, g)
FROM 'Teste_Nivelamento\Teste3\database\Datas\4T2023.csv' DELIMITER ';' CSV HEADER ENCODING 'UTF8';


SELECT o.nome_fantasia, '2024_Q4' AS periodo, SUM(d.saldo_final - d.saldo_inicial) AS total_despesas 
FROM demonstracoes_contabeis_2024_Q4 d
JOIN operadoras o ON d.registro_ans = o.registro_ans
GROUP BY o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;


SELECT o.nome_fantasia, '2024' AS ano, 
       (SELECT SUM(saldo_final - saldo_inicial) FROM demonstracoes_contabeis_2024_Q1 WHERE registro_ans = o.registro_ans) +
       (SELECT SUM(saldo_final - saldo_inicial) FROM demonstracoes_contabeis_2024_Q2 WHERE registro_ans = o.registro_ans) +
       (SELECT SUM(saldo_final - saldo_inicial) FROM demonstracoes_contabeis_2024_Q3 WHERE registro_ans = o.registro_ans) +
       (SELECT SUM(saldo_final - saldo_inicial) FROM demonstracoes_contabeis_2024_Q4 WHERE registro_ans = o.registro_ans) AS total_despesas
FROM operadoras o
ORDER BY total_despesas DESC
LIMIT 10;
