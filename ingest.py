from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import psycopg2

# 🔌 conexão com banco
conn = psycopg2.connect(
    dbname="semantic_db",
    user="user_semantic",
    password="123456",
    host="localhost"
)
cur = conn.cursor()

# 📄 carregar texto
with open("documento.txt", "r", encoding="utf-8") as f:
    texto = f.read()

# ✂️ dividir em chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(texto)

# 🧠 modelo local
model = SentenceTransformer('all-MiniLM-L6-v2')

def gerar_embedding(texto):
    return model.encode(texto).tolist()

# 💾 inserir no banco
for chunk in chunks:
    vetor = gerar_embedding(chunk)
    cur.execute(
        "INSERT INTO documentos (conteudo, embedding) VALUES (%s, %s)",
        (chunk, vetor)
    )

conn.commit()
cur.close()
conn.close()

print(f"✅ Ingestão concluída! {len(chunks)} chunks inseridos.")
