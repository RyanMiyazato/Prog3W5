def max_money(n, m, prices):
    # Filtrar apenas os preços negativos
    negative_prices = sorted([p for p in prices if p < 0])

    # Pegar os menores valores negativos (até m elementos)
    max_earn = sum(abs(negative_prices[i]) for i in range(min(m, len(negative_prices))))

    return max_earn


# Leitura da entrada
n, m = map(int, input().split())
prices = list(map(int, input().split()))

# Processamento e saída
print(max_money(n, m, prices))
