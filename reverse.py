import random
import hashlib
import base64
import time


class OnlyFans:
    def __init__(self, user_agent: str) -> None:
        self.ua = user_agent
        self.st = int(time.time())

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
        return random.uniform(0, 1) * 1e12

    def get_sign_header(self, endpoint, params=0):
        data = f"j6CYtfx3q9o7TCjVxWKKgUekVUj3L0q3\n{self.st}\n{endpoint}\n{params}"
        hash_value = hashlib.sha1(data.encode()).hexdigest()
        key_map = {
            9483: 113, 
            8874: 94,
            9097: -66, 
            8929: -56, 
            7607: 129,
            7778: 88, 
            8531: 139, 
            7326: -143, 
            9809: 71, 
            8790: -89,
            8324: -79, 
            7692: -97, 
            9755: -94, 
            7885: -120, 
            8071: -92,
            9040: -127, 
            9599: 147, 
            8249: -100, 
            7501: -64, 
            9688: -113,
            9210: -139, 
            8617: 95, 
            9261: -64, 
            9915: 133, 
            8411: -114,
            7450: 102, 
            7986: -119, 
            8174: -117, 
            8723: 125, 
            7213: -64,
            9381: 125, 
            7374: 62
        }
        part3 = 0
        for key, value in key_map.items():
            part3 += ord(hash_value[key % len(hash_value)]) + value
        part3_hex = hex(abs(part3))[2:]
        return f"32162:{hash_value}:{part3_hex}:672a15de"


if __name__ == "__main__":
    OF = OnlyFans(user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
    print(f"X-BC: {OF.x_bc()}")
    print(f"sign: {OF.get_sign_header("v2/init/users")}")
    input()