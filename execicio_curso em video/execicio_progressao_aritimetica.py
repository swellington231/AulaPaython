primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
decimo = primeiro+ (10 - 1) * razão
for c in range(primeiro, decimo + razão , razão):
    print(c, end=" ")