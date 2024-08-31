import toml
import requests
import os

# Carregar a configuração do arquivo TOML
config = toml.load('settings/config.toml')

URL_API = "https://blaze.com"

class Browser(object):

    def __init__(self):
        self.response = None
        self.headers = None
        self.session = requests.Session()

    def set_headers(self, headers=None):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) "
                          "Chrome/87.0.4280.88 Safari/537.36"
        }
        if headers:
            for key, value in headers.items():
                self.headers[key] = value

    def get_headers(self):
        return self.headers

    def send_request(self, method, url, **kwargs):
        return self.session.request(method, url, **kwargs)


class BlazeAPI(Browser):

    def __init__(self, username=None, password=None):
        super().__init__()
        self.token = None
        self.is_logged = False
        self.wallet_id = None
        self.username = username
        self.password = password
        self.set_headers()
        self.headers = self.get_headers()

    def auth(self):
        data = {
            "username": self.username,
            "password": self.password
        }
        self.headers["referer"] = f"{URL_API}/pt/?modal=auth&tab=login"
        self.response = self.send_request("PUT",
                                          f"{URL_API}/api/auth/password",
                                          json=data,
                                          headers=self.headers)

        if not self.response.json().get("error"):
            self.token = self.response.json()["access_token"]
            self.is_logged = True
        return self.response.json()

    def get_profile(self):
        self.headers["authorization"] = f"Bearer {self.token}"
        self.response = self.send_request("GET",
                                          f"{URL_API}/api/users/me",
                                          headers=self.headers)
        if not self.response.json().get("error"):
            self.is_logged = True
        return self.response.json()

    def get_balance(self):
        self.headers["referer"] = f"{URL_API}/pt/games/double"
        self.headers["authorization"] = f"Bearer {self.token}"
        self.response = self.send_request("GET",
                                          f"{URL_API}/api/wallets",
                                          headers=self.headers)
        if self.response.status_code == 502:
            self.auth()  # Tenta reautenticar se necessário
            return self.get_balance()
        elif self.response:
            self.wallet_id = self.response.json()[0]["id"]
        return self.response.json()

    def get_user_info(self):
        result_dict = {}
        result_dict["balance"] = self.get_balance()[0]["balance"]
        result_dict["username"] = self.get_profile()["username"]
        result_dict["wallet_id"] = self.get_balance()[0]["id"]
        result_dict["tax_id"] = self.get_profile()["tax_id"]
        return result_dict


def check_accounts_balances():
    # Cria a pasta para salvar os resultados, se ela não existir
    output_dir = "resultados"
    os.makedirs(output_dir, exist_ok=True)

    # Caminho do arquivo de saída
    output_file = os.path.join(output_dir, "resultado.txt")

    with open(output_file, "w") as file:
        for account in config["authentication"]:
            email = account["email"]
            password = account["password"]
            blaze_api = BlazeAPI(username=email, password=password)

            file.write(f"Verificando conta: {email}\n")
            print(f"Verificando conta: {email}")

            login_response = blaze_api.auth()

            if blaze_api.is_logged:
                user_info = blaze_api.get_user_info()
                result = f"Usuário: {user_info['username']}, Saldo: {user_info['balance']}\n"
                file.write(result)
                print(result)
            else:
                result = f"Falha ao logar na conta: {email}\n"
                file.write(result)
                print(result)

    print(f"Resultados foram salvos em {output_file}")


# Verificar saldo de todas as contas configuradas no arquivo TOML
check_accounts_balances()
