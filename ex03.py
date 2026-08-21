import locale

# Configurando para o padrão brasileiro
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except:
        # Fallback manual se locale não estiver disponível
        def formatar_real_alternativo(valor):
            return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        formatar_real = formatar_real_alternativo
    else:
        def formatar_real(valor):
            return locale.currency(valor, grouping=True, symbol='R$ ').replace('R$ ', '').strip()
else:
    def formatar_real(valor):
        return locale.currency(valor, grouping=True, symbol='R$ ')

# ============ ENTRADA DE DADOS ============
print("=" * 50)
print("         SISTEMA DE COMPRAS")
print("=" * 50)

nome_cliente = input("Nome do cliente: ")
produto = input("Nome do produto: ")
preco = float(input("Preco unitario (R$): "))
quantidade = int(input("Quantidade: "))
percentual_desconto = float(input("Percentual de desconto (%): "))

# ============ PROCESSAMENTO ============
subtotal = preco * quantidade
valor_desconto = subtotal * (percentual_desconto / 100)
total_final = subtotal - valor_desconto
valor_medio = total_final / quantidade

# ============ SAÍDA FORMATADA ============
print("\n" + "=" * 50)
print("         RECIBO DA COMPRA")
print("=" * 50)

print(f"Cliente:          {nome_cliente}")
print(f"Produto:          {produto}")
print(f"Quantidade:       {quantidade} unidade(s)")
print(f"Preco unitario:   R$ {formatar_real(preco)}")
print("-" * 50)
print(f"Subtotal:         R$ {formatar_real(subtotal)}")
print(f"Desconto:         {percentual_desconto:.0f}% (R$ {formatar_real(valor_desconto)})")
print("-" * 50)
print(f"TOTAL A PAGAR:    R$ {formatar_real(total_final)}")
print(f"\nValor medio por unidade: R$ {formatar_real(valor_medio)}")

print("\n" + "=" * 50)
print("          OBRIGADO PELA COMPRA!")
print("=" * 50)

print("Processando dados", end="... ")
print("Finalizado!", end="\n\n")