import time
import requests
from typing import List, Dict, Any, Set
from pydantic import BaseModel
from .config import PhantomConfig

class PhantomFinding(BaseModel):
    parameter: str
    payload_value: Any
    baseline_status: int
    injected_status: int
    baseline_len: int
    injected_len: int
    anomaly_detected: bool
    description: str

class PhantomEngine:
    DEFAULT_PAYLOADS = [True, False, 1, 9999, "admin", "true", "1", ["admin"], {"role": "admin"}]

    def __init__(self, config: PhantomConfig, discovered_params: Set[str]):
        self.config = config
        self.params_to_test = discovered_params.union(set(self.config.custom_params))

    def run(self) -> List[PhantomFinding]:
        findings: List[PhantomFinding] = []
        session = requests.Session()

        try:
            base_resp = session.request(
                method=self.config.method,
                url=self.config.target_url,
                headers=self.config.headers,
                json=self.config.base_body,
                timeout=self.config.timeout
            )
        except Exception as e:
            raise RuntimeError(f"Failed to connect to target baseline: {e}")

        base_len = len(base_resp.content)
        base_status = base_resp.status_code

        for param in sorted(self.params_to_test):
            for val in self.DEFAULT_PAYLOADS:
                test_body = {**self.config.base_body, param: val}
                try:
                    inj_resp = session.request(
                        method=self.config.method,
                        url=self.config.target_url,
                        headers=self.config.headers,
                        json=test_body,
                        timeout=self.config.timeout
                    )
                except Exception:
                    continue

                inj_len = len(inj_resp.content)
                inj_status = inj_resp.status_code

                anomaly = False
                desc = "Standard response behavior."
                if inj_status != base_status:
                    anomaly = True
                    desc = f"HTTP Status shift detected ({base_status} -> {inj_status})."
                elif abs(inj_len - base_len) > 50:
                    anomaly = True
                    desc = f"Significant response length variance (Delta: {inj_len - base_len} bytes)."

                if anomaly:
                    findings.append(PhantomFinding(
                        parameter=param,
                        payload_value=str(val),
                        baseline_status=base_status,
                        injected_status=inj_status,
                        baseline_len=base_len,
                        injected_len=inj_len,
                        anomaly_detected=True,
                        description=desc
                    ))
                time.sleep(0.02)
        return findings
