import re
import tls_client
import json
import urllib.parse
import base64
requests = tls_client.Session(client_identifier="chrome_131", random_tls_extension_order=True)
class Decode:
    def decode_string(W):
        n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/="
        c, t = "", ""
        r, o = 0, 0
        padding_incorrect = False
        if len(W) % 4 != 0:
            padding_incorrect = True
            W += "=" * (4 - (len(W) % 4))
        for e in range(0, len(W)):
            u = n.find(W[e]) 
            if u == -1: 
                continue
            if r % 4 == 0:
                o = u
            else:
                o = (o << 6) + u 

            if r % 4 == 3:
                c += chr(0xFF & (o >> 16))
                c += chr(0xFF & (o >> 8)) 
                c += chr(0xFF & o)
            r += 1
        for char in c:
            t += "%" + f"{ord(char):02x}"
        final_result = urllib.parse.unquote(t, errors='none')
        return final_result, padding_incorrect

    def n(W, key):
        t = 0
        c = list(range(256))
        W, PI = Decode.decode_string(W)
        for d in range(0, 256):
            t = (t + c[d] + ord(key[d % len(key)])) % 256
            r = c[d]
            c[d] = c[t]
            c[t] = r
        u = ""
        e = 0 
        t = 0
        for o in range(0, len(W)):
            e = (e + 1) % 256
            t = (t + c[e]) % 256
            r = c[e]
            c[e] = c[t]
            c[t] = r
            u += chr(ord(W[o]) ^ c[(c[e] + c[t]) % 256])
        if PI:
            u = u[:-2]
        return u


class MOD:
    @staticmethod
    def fetch_X_OF_REV() -> str:
        try:
            return requests.get("https://onlyfans.com").text.split("prod/f/")[1].split("/")[0]
        except:
            print("[ERR]: Error Parsing for OnlyFans Version | Using Staticily Set Version")
            return "202411281154-369f5f0f19"

    @staticmethod
    def fetch_challenge_script(version: str) -> str:
        url = f"https://static2.onlyfans.com/static/prod/f/{version}/2313.js"
        try:
            return requests.get(url).text
        except:
            input(f"[ERR]: Error Fetching JavaScript Challenge ({url})")
            exit(0)

    def initalize_onlyfans_configuration() -> dict:
        x_of_rev = MOD.fetch_X_OF_REV()
        challenge_script = MOD.fetch_challenge_script(x_of_rev)
        for match in re.findall(r"(?:const|let|var)\s+\w+\s*=\s*(\[[^\]]+\]);" , challenge_script):
            try:
                secrets_list = json.loads(match.replace("'", '"'))
                for i in range(26):
                    secrets_list.append(secrets_list.pop(0))
                break
            except:
                pass
        regex_pattern = r'\b([a-zA-Z]{5})\b:\s*c\((\d{3}),\s*"([^"]{4})"\)'
        matches = [(m.start(), m.groups()) for m in re.finditer(regex_pattern, challenge_script)]
        sorted_matches = [match[1] for match in sorted(matches, key=lambda x: x[0])]
        values = {}
        regex_pattern = r'return\s+[a-zA-Z]+\[[a-zA-Z]\(\d+,\s*".*?"\)\]\s*=\s*(.*)'
        match = re.search(regex_pattern, challenge_script, re.DOTALL)
        parsed_value = match.group(1).strip()
        parsed_value = parsed_value.split("[")[1].split("),")[0] + ")"
        sorted_matches.append(("first_segment", parsed_value.split("(")[1].split(",")[0], parsed_value.split('"')[1].split('"')[0]))
        for key_name, W, key in sorted_matches:
            origin_key = key
            W = int(W)
            W -= 572
            key = secrets_list[W]
            decoded_result = Decode.n(key, origin_key)
            if len(decoded_result) == 32:
                key = "sign_key"
                values[str(key)] = decoded_result
            elif len(decoded_result) == 8:
                key = "final_segment"
                values[str(key)] = decoded_result
            elif len(decoded_result) == 5:
                key = "first_segment"
                values[str(key)] = decoded_result
            else:
                pass
        return values, x_of_rev
