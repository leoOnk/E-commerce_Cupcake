# schema.sql

CREATE DATABASE loja_cupcake;

USE loja_cupcake;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    senha VARCHAR(255)
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    descricao TEXT,
    imagem VARCHAR(255),
    estoque INT
);

CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT,
    status VARCHAR(50),
    data DATETIME,
    valor DECIMAL(10,2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE entregas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    status VARCHAR(50),
    data_envio DATETIME,
    data_entrega DATETIME,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);

CREATE TABLE pagamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT,
    metodo VARCHAR(50),
    status VARCHAR(50),
    valor DECIMAL(10,2),
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
);
