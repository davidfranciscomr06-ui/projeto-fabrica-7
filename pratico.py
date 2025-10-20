import streamlit as st

def separar_pares_impares(lista):
    """Retorna duas listas: pares e ímpares, preservando a ordem."""
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    return pares, impares

def main():
    st.title("Particionador de IDs por Shard (A/B)")

    st.markdown("""
    Informe exatamente 6 IDs inteiros para simular a distribuição entre:
    - Shard A (pares)
    - Shard B (ímpares)
    """)

    # Criar 6 campos para entrada
    ids = []
    cols = st.columns(3)
    for i in range(6):
        col = cols[i % 3]
        val = col.text_input(f"ID {i+1}", key=f"id_{i}")
        ids.append(val)

    if st.button("Separar IDs em Shards"):
        try:
            # converter para int e validar
            ids_int = []
            for i, v in enumerate(ids, start=1):
                if v.strip() == "":
                    st.error(f"ID {i} está vazio.")
                    return
                n = int(v.strip())
                ids_int.append(n)
            
            # separar pares e ímpares
            pares, impares = separar_pares_impares(ids_int)

            st.subheader("Lista Original")
            st.write(ids_int)

            st.subheader(f"Shard A (PAR) — total: {len(pares)}")
            st.write(pares)

            st.subheader(f"Shard B (ÍMPAR) — total: {len(impares)}")
            st.write(impares)

            # Mostrar percentuais
            total = len(ids_int)
            pct_par = (len(pares) / total) * 100
            pct_impar = (len(impares) / total) * 100

            st.info(f"Percentual Shard A (PAR): {pct_par:.1f}%")
            st.info(f"Percentual Shard B (ÍMPAR): {pct_impar:.1f}%")

        except ValueError:
            st.error("Por favor, insira somente números inteiros válidos.")

if __name__ == "__main__":
    main()
