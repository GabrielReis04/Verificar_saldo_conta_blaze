import re

def convert_to_toml_format(url_list):
    toml_entries = []

    for url in url_list:
        # Usa expressão regular para extrair o email e a senha
        match = re.search(r":([^:]+@[^:]+):([^:]+)$", url)
        if match:
            email = match.group(1)
            password = match.group(2)
            toml_entry = f'[[authentication]]\nemail = "{email}"\npassword = "{password}"\n'
            toml_entries.append(toml_entry)
    
    # Junta todas as entradas em uma única string
    return "\n".join(toml_entries)

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        # Lê todas as linhas do arquivo e remove espaços em branco
        url_list = [line.strip() for line in file.readlines()]
    return url_list

def write_toml_to_file(toml_data, output_path):
    with open(output_path, 'w') as file:
        file.write(toml_data)

# Caminho do arquivo de entrada contendo as URLs
input_file = 'urls.txt'

# Caminho do arquivo de saída para o formato TOML
output_file = 'output.toml'

# Ler as URLs do arquivo
url_list = read_urls_from_file(input_file)

# Converte a lista de URLs para o formato TOML
toml_result = convert_to_toml_format(url_list)

# Escreve o resultado no arquivo de saída
write_toml_to_file(toml_result, output_file)

print(f"Conversão concluída! O resultado foi salvo em {output_file}")
