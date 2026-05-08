CREATE TABLE notas_fiscais (
    id SERIAL PRIMARY KEY,
    numero_nota VARCHAR(50),
    data_emissao DATE,
    cliente VARCHAR(100),
    valor NUMERIC(10,2),
    imposto NUMERIC(10,2)
);