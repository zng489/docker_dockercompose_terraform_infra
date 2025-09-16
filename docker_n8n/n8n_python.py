import pandas as pd
import numpy as np

# Criar um DataFrame com dados aleatórios
df = pd.DataFrame({
    'id': np.arange(1, 6),                     # IDs de 1 a 5
    'valor': np.random.randint(10, 100, 5),    # Valores aleatórios entre 10 e 99
    'nome': ['Alice', 'Bob', 'Carol', 'Dave', 'Eve']  # Nomes
})

# Salvar em CSV
df.to_csv('random_doc.csv', index=False)

# Imprimir "n8n"
print('n8n')