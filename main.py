import json
import os
from datetime import date

ARQUIVO = "gastos.json"


def carregar_gastos():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_gastos(gastos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(gastos, f, indent=4, ensure_ascii=False)


def adicionar_gasto(gastos):
    descricao = input("Descrição: ").strip()
    categoria = input("Categoria: ").strip()

    try:
        valor = float(input("Valor: ").replace(",", "."))
    except ValueError:
        print("Valor inválido. Digite um número, como 25.50")
        return
    if valor <= 0:
        print("O valor precisa ser maior que zero.")
        return

    gasto = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": str(date.today()),
    }
    gastos.append(gasto)
    salvar_gastos(gastos)
    print("Gasto adicionado!")
