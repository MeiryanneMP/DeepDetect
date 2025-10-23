Como funciona:

Embutimento detectado: O código detecta o rosto e gera o embedding.

Comparação: Esse embedding é comparado com os embeddings armazenados em real_faces_db e ai_faces_db.

Resultado: O código imprime o resultado da comparação e exibe a imagem com o rosto detectado.

Próximos passos:

Substituir os embeddings gerados aleatoriamente no real_faces_db e ai_faces_db por embeddings reais.

Ajustar o limiar de distância (dist < 1.0) para encontrar o valor que melhor funcionar.

Esse código deve ser capaz de detectar um rosto e classificá-lo como "real" ou "de IA" com base na comparação de embeddings.
