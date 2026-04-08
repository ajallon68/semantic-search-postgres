from sentence_transformers import SentenceTransformer
import psycopg2

# 🧠 carregar modelo local (carrega 1x só)
model = SentenceTransformer('all-MiniLM-L6-v2')

def gerar_embedding(texto):
    return model.encode(texto).tolist()

def vetor_para_string(v):
    return "[" + ",".join(map(str, v)) + "]"

# 🔌 conexão com banco
conn = psycopg2.connect(
    dbname="semantic_db",
    user="user_semantic",
    password="123456",
    host="localhost"
)
cur = conn.cursor()

print("🔎 Busca semântica iniciada! (digite 'sair' para encerrar)")

# 🔁 loop interativo
while True:
    pergunta = input("\nDigite sua pergunta: ")

    if pergunta.lower() == "sair":
        break

    # gerar embedding da pergunta
    query_vector = gerar_embedding(pergunta)

    # converter vetor para formato pgvector
    vector_str = vetor_para_string(query_vector)

    # 🔍 busca semântica (com cast para vector)
    cur.execute(
        """
        SELECT conteudo
        FROM documentos
        ORDER BY embedding <-> %s::vector
        LIMIT 3;
        """,
        (vector_str,)
    )

    resultados = cur.fetchall()

    print("\n📄 Resultados mais relevantes:\n")

    if not resultados:
        print("Nenhum resultado encontrado.")
    else:
        for i, r in enumerate(resultados, 1):
            print(f"{i}. {r[0]}")

# 🔒 fechar conexão
cur.close()
conn.close()

print("\n👋 Encerrado.")
