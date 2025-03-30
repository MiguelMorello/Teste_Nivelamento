-- setupdb.sql (Criação das Tabelas)

CREATE TABLE operadoras (
    id_operadora SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE NOT NULL,
    cnpj VARCHAR(18) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(255),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(3),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(255),
    cargo_representante VARCHAR(255),
    regiao_de_comercializacao VARCHAR(100),
    data_registro_ans DATE
);

-- Tabelas para 2024
CREATE TABLE demonstracoes_contabeis_2024_Q1 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2024_Q2 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2024_Q3 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2024_Q4 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

-- Tabelas para 2023
CREATE TABLE demonstracoes_contabeis_2023_Q1 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2023_Q2 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2023_Q3 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);

CREATE TABLE demonstracoes_contabeis_2023_Q4 (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    registro_ans VARCHAR(20) REFERENCES operadoras(registro_ans),
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    saldo_inicial NUMERIC(18,2),
    saldo_final NUMERIC(18,2),
    g NUMERIC(18,2)
);
