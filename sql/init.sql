CREATE TABLE IF NOT EXISTS notas_fiscais (
    id SERIAL PRIMARY KEY,
    numero_nota VARCHAR(50) UNIQUE,
    data_emissao DATE,
    cliente VARCHAR(255),
    valor NUMERIC(10,2),
    imposto NUMERIC(10,2)
);