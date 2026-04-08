# 🔍 Semantic Search com PostgreSQL + pgvector + Local Embeddings

Projeto de busca semântica utilizando embeddings locais (sem custo) com Sentence Transformers e armazenamento vetorial no PostgreSQL.

## 🚀 Tecnologias

- Python
- PostgreSQL + pgvector
- Sentence Transformers
- LangChain (text splitter)

## 🧠 Como funciona

1. Texto é dividido em chunks
2. Cada chunk vira um embedding vetorial
3. Embeddings são armazenados no PostgreSQL
4. Perguntas são convertidas em embedding
5. Busca retorna conteúdos semanticamente similares

## 📥 Instalação

```bash
git clone https://github.com/seu-usuario/semantic-search.git
cd semantic-search

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

# 🧱 Configurar banco
CREATE EXTENSION vector;

CREATE TABLE documentos (
    id SERIAL PRIMARY KEY,
    conteudo TEXT,
    embedding VECTOR(384)
);

## DEMO

<img width="1919" height="790" alt="image" src="https://github.com/user-attachments/assets/0768cf32-bbf6-4eb8-990e-ebd0d1d77a00" />
