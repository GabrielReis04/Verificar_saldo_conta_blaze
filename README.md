# BlazeAPI Automation

Este projeto é uma ferramenta automatizada para autenticação e verificação de saldos em contas da plataforma Blaze. Ele foi desenvolvido com fins educacionais e de estudo, para demonstrar como interagir com APIs de terceiros usando Python.

## Funcionalidades

- **Autenticação automática**: Faz login nas contas da Blaze usando credenciais armazenadas em um arquivo TOML.
- **Verificação de saldo**: Recupera o saldo de cada conta e salva os resultados em um arquivo de texto.
- **Conversão de URLs para formato TOML**: Converte uma lista de URLs contendo emails e senhas no formato `serviço_url:email:senha` para o formato TOML.
- **Extração de saldos**: Calcula o saldo total de todas as contas a partir de um arquivo de texto.

## Requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:

- Python 3.x
- `requests` e `toml` (você pode instalá-los via pip)
  
```bash
pip install requests toml

Configuração:

Clone o repositório:
git clone https://github.com/GabrielReis04/Verificar_saldo_conta_blaze.git
cd BlazeAPI-Automation

Crie um arquivo TOML com suas credenciais de autenticação. Você pode usar o script tranformaremconf.py para gerar automaticamente esse arquivo a partir de uma lista de URLs no formato serviço_url:email:senha.

Coloque o arquivo TOML gerado na pasta settings com o nome config.toml.

Como Usar:

1. Verificar Saldo das Contas
Este script irá autenticar em cada conta configurada no arquivo config.toml e salvar o saldo de cada uma no arquivo resultado.txt.
python app.py

2. Extrair Saldos de um Arquivo
Se você já tem um arquivo com os saldos listados, use o script extrairsaldo.py para calcular o saldo total:
python extrairsaldo.py

3. Converter URLs para Formato TOML
Se você tem uma lista de URLs no formato serviço_url:email:senha, use o script tranformaremconf.py para convertê-las para o formato TOML:
python tranformaremconf.py


Estrutura do Projeto:

app.py: Script principal para autenticação e verificação de saldos.
extrairsaldo.py: Script para extrair e somar saldos de um arquivo de texto.
tranformaremconf.py: Script para converter URLs de contas no formato serviço_url:email:senha para o formato TOML.
settings/config.toml: Arquivo TOML contendo as credenciais das contas.
resultados/resultado.txt: Arquivo de saída com os resultados das verificações.


Aviso Legal
Este projeto foi criado com fins exclusivamente educacionais e de estudo. Não nos responsabilizamos pelo uso indevido deste código. O uso deste projeto para fins ilegais, antiéticos ou prejudiciais é estritamente proibido. Caso você decida usá-lo, estará assumindo total responsabilidade por quaisquer consequências que possam surgir.

Licença: Este projeto é de código aberto e está licenciado sob a MIT License.
