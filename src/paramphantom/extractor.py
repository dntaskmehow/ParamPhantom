import re
import requests
from typing import Set

class JSExtractor:
    @staticmethod
    def extract_keys_from_code(js_code: str) -> Set[str]:
        key_pattern = re.compile(r'\b([a-zA-Z_][a-zA-Z0-9_]{2,25})\s*:\s*[\'\"\[\{0-9]')
        matches = key_pattern.findall(js_code)
        noise = {"true", "false", "null", "undefined", "function", "return", "const", "let", "var", "if", "else", "switch", "case"}
        return {m for m in matches if m.lower() not in noise}

    @staticmethod
    def harvest_from_url(url: str) -> Set[str]:
        try:
            resp = requests.get(url, timeout=10)
            if resp.status_code == 200:
                return JSExtractor.extract_keys_from_code(resp.text)
        except Exception:
            pass
        return set()
