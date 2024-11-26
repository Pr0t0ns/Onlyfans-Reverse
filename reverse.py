import random
import hashlib
import base64
import time
from mod import initalize_onlyfans_configuration

class OnlyFans:
    def __init__(self, user_agent: str, verison: str="202411250920-9b8114829c") -> None:
        self.ua = user_agent
        self.v = verison
        self.st = int(time.time()) * 1000
        self.n = initalize_onlyfans_configuration()
        self.secret = self.n['reRtQ']
        self.first_sign_segment = self.n['QvSwh']
        self.final_sign_segment = self.n['HrBVl']

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
        data = f"{self.secret}\n{self.st}\n{endpoint}\n{params}"
        W = hashlib.sha1(data.encode()).hexdigest()
        res = hex(abs(
            ord(W[35975 % len(W)]) + 129 +
            (ord(W[34586 % len(W)]) - 135) +
            (ord(W[35853 % len(W)]) + 79) +
            (ord(W[34776 % len(W)]) - 109) +
            (ord(W[33882 % len(W)]) + 110) +
            (ord(W[33534 % len(W)]) - 131) +
            (ord(W[34477 % len(W)]) - 96) +
            (ord(W[35561 % len(W)]) - 86) +
            (ord(W[35484 % len(W)]) + 82) +
            (ord(W[35787 % len(W)]) + 99) +
            (ord(W[35612 % len(W)]) - 79) +
            (ord(W[34897 % len(W)]) - 138) +
            (ord(W[33433 % len(W)]) + 97) +
            (ord(W[35699 % len(W)]) - 106) +
            (ord(W[33939 % len(W)]) - 76) +
            (ord(W[33606 % len(W)]) + 78) +
            (ord(W[35341 % len(W)]) - 126) +
            (ord(W[35145 % len(W)]) - 110) +
            (ord(W[34055 % len(W)]) + 123) +
            (ord(W[34124 % len(W)]) - 81) +
            (ord(W[34691 % len(W)]) - 108) +
            (ord(W[33361 % len(W)]) - 124) +
            (ord(W[33254 % len(W)]) + 114) +
            (ord(W[35044 % len(W)]) + 102) +
            (ord(W[33798 % len(W)]) - 127) +
            (ord(W[35430 % len(W)]) - 95) +
            (ord(W[34946 % len(W)]) - 51) +
            (ord(W[34201 % len(W)]) - 102) +
            (ord(W[34394 % len(W)]) + 134) +
            (ord(W[33677 % len(W)]) - 84) +
            (ord(W[35228 % len(W)]) - 111) +
            (ord(W[34286 % len(W)]) - 99)
        ))[2:]

        return {"sign": f"{self.first_sign_segment}:{W}:{res}:{self.final_sign_segment}", "Time": self.st, "x-bc": self.x_bc(), "x-of-rev": self.v, "user-agent": self.ua, "endpoint": fe, "computing_time": round(time.time()-t1, 6)}
 

if __name__ == "__main__":
    OF = OnlyFans(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    computed_signature = (OF.generate_header_data("https://onlyfans.com/api2/v2/users/me"))
    print(computed_signature)
