import random
import hashlib
import base64
import time
import tls_client
from mod import MOD

class OnlyFans:
    def __init__(self, user_agent: str, secrets: list=None) -> None:
        self.ua = user_agent
        self.st = int(time.time()) * 1000
        if secrets == None or len(secrets) != 2:
            self.n, self.v = MOD.initalize_onlyfans_configuration()
            self.secrets = [self.n['sign_key'], self.n['first_segment'], self.n['final_segment']]
        else:
            self.v = MOD.fetch_X_OF_REV()
            self.secrets = secrets

    @staticmethod
    def fetch_X_HASH(proxy: str=None):
        session = tls_client.Session(client_identifier="chrome_131", random_tls_extension_order=True)
        if proxy != None:
            session.proxies = {
                'https': f'http://{proxy}',
                'http': f'http://{proxy}'
            }
        try:
            return session.get("https://cdn2.onlyfans.com/hash/").text
        except:
            return None

    def x_bc(self) -> str:
        _list= [self.st, OnlyFans.he(), OnlyFans.he(), self.ua]
        x_bc_unformed = ""
        for itm in _list:
            x_bc_unformed += base64.b64encode(str(itm).encode()).decode()
            x_bc_unformed += "."
        x_bc_unformed = x_bc_unformed.removesuffix(".")
        return hashlib.sha1(x_bc_unformed.encode()).hexdigest()
    
    @staticmethod
    def he() -> float:
        return random.random() * 1e12
    
    def generate_header_data(self, endpoint, params=0):
        t1 = int(time.time())
        try:
            fe = endpoint
            endpoint = endpoint.split("://onlyfans.com")[1]
        except:
            pass
        data = f"{self.secrets[0]}\n{self.st}\n{endpoint}\n{params}"
        W = hashlib.sha1(data.encode()).hexdigest()
        res = hex((
            abs(
                ord(W[33848 % len(W)]) - 89 +
                (ord(W[34604 % len(W)]) - 119) +
                (ord(W[34328 % len(W)]) - 93) +
                (ord(W[34828 % len(W)]) + 100) +
                (ord(W[34740 % len(W)]) + 108) +
                (ord(W[34497 % len(W)]) - 120) +
                (ord(W[34011 % len(W)]) - 112) +
                (ord(W[34984 % len(W)]) + 110) +
                (ord(W[33584 % len(W)]) + 104) +
                (ord(W[35840 % len(W)]) + 76) +
                (ord(W[34174 % len(W)]) - 105) +
                (ord(W[35501 % len(W)]) - 128) +
                (ord(W[35050 % len(W)]) + 76) +
                (ord(W[35386 % len(W)]) + 76) +
                (ord(W[35764 % len(W)]) - 101) +
                (ord(W[34652 % len(W)]) + 76) +
                (ord(W[35888 % len(W)]) + 64) +
                (ord(W[35570 % len(W)]) - 87) +
                (ord(W[34378 % len(W)]) + 60) +
                (ord(W[35167 % len(W)]) + 79) +
                (ord(W[33783 % len(W)]) + 107) +
                (ord(W[33699 % len(W)]) - 118) +
                (ord(W[33409 % len(W)]) + 111) +
                (ord(W[35119 % len(W)]) - 84) +
                (ord(W[35683 % len(W)]) - 116) +
                (ord(W[34882 % len(W)]) + 56) +
                (ord(W[33926 % len(W)]) + 84) +
                (ord(W[35336 % len(W)]) - 125) +
                (ord(W[34259 % len(W)]) - 104) +
                (ord(W[33496 % len(W)]) - 111) +
                (ord(W[34099 % len(W)]) + 107) +
                (ord(W[35219 % len(W)]) + 71)
            )
        ))[2:]

        return {"sign": f"{self.secrets[1]}:{W}:{res}:{self.secrets[2]}", "Time": self.st, "x-bc": self.x_bc(), "x-of-rev": self.v, "user-agent": self.ua, "endpoint": fe, "computing_time": round(time.time()-t1, 6)}
 



if __name__ == "__main__":
    OF = OnlyFans(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    computed_signature = (OF.generate_header_data("https://onlyfans.com/api2/v2/users/me"))
    X_hash = OF.fetch_X_HASH()
    print(computed_signature, X_hash)
