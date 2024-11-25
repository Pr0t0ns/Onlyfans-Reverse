import random
import hashlib
import base64
import time
from mod import initalize_onlyfans_configuration




class OnlyFans:
    def __init__(self, user_agent: str, verison: str="202411221209-ff9b8e2d99") -> None:
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
        t = {
            "time": self.st
        }
        res = hex(abs(
            ord(W[35360 % len(W)]) - 103 +
            (ord(W[34780 % len(W)]) + 108) +
            (ord(W[35751 % len(W)]) + 63) +
            (ord(W[34550 % len(W)]) - 79) +
            (ord(W[34700 % len(W)]) - 63) +
            (ord(W[34323 % len(W)]) - 136) +
            (ord(W[35073 % len(W)]) - 122) +
            (ord(W[33530 % len(W)]) + 130) +
            (ord(W[33426 % len(W)]) - 107) +
            (ord(W[33582 % len(W)]) + 66) +
            (ord(W[35257 % len(W)]) + 107) +
            (ord(W[34833 % len(W)]) - 70) +
            (ord(W[33337 % len(W)]) + 113) +
            (ord(W[33766 % len(W)]) + 84) +
            (ord(W[33249 % len(W)]) + 55) +
            (ord(W[35175 % len(W)]) + 109) +
            (ord(W[34206 % len(W)]) - 145) +
            (ord(W[35620 % len(W)]) - 105) +
            (ord(W[34952 % len(W)]) - 127) +
            (ord(W[33974 % len(W)]) + 122) +
            (ord(W[34426 % len(W)]) - 129) +
            (ord(W[35695 % len(W)]) - 90) +
            (ord(W[35519 % len(W)]) - 84) +
            (ord(W[33138 % len(W)]) + 100) +
            (ord(W[34493 % len(W)]) - 96) +
            (ord(W[33056 % len(W)]) - 49) +
            (ord(W[34091 % len(W)]) - 128) +
            (ord(W[35466 % len(W)]) + 116) +
            (ord(W[33874 % len(W)]) + 126) +
            (ord(W[34649 % len(W)]) - 124) +
            (ord(W[33195 % len(W)]) - 68) +
            (ord(W[33688 % len(W)]) + 130)
        ))[2:]

        return {"sign": f"{self.first_sign_segment}:{W}:{res}:{self.final_sign_segment}", "Time": self.st, "x-bc": self.x_bc(), "x-of-rev": self.v, "user-agent": self.ua, "endpoint": fe, "computing_time": round(time.time()-t1, 6)}
 

if __name__ == "__main__":
    OF = OnlyFans(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")
    computed_signature = (OF.generate_header_data("https://onlyfans.com/api2/v2/users/me"))
    print(computed_signature)
