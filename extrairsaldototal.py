import re

def extract_balances_from_list(lines):
    total_balance = 0.0

    for line in lines:
        # Usa expressão regular para encontrar a linha que contém o saldo
        match = re.search(r"Saldo:\s*([\d.]+)", line)
        if match:
            balance = float(match.group(1))
            total_balance += balance

    return total_balance

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# Caminho do arquivo de entrada contendo as informações de contas
input_file = 'contas.txt'

# Ler as linhas do arquivo
lines = read_lines_from_file(input_file)

# Extrair e somar os saldos
total_balance = extract_balances_from_list(lines)

# Exibir o total
print(f"O saldo total de todas as contas é: R$ {total_balance:.2f}")
