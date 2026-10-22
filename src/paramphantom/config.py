from typing import Dict, List, Optional, Any
from pydantic import BaseModel, Field

class PhantomConfig(BaseModel):
    target_url: str
    method: str = "POST"
    headers: Dict[str, str] = Field(default_factory=dict)
    base_body: Dict[str, Any] = Field(default_factory=dict)
    js_sources: List[str] = Field(default_factory=list)
    custom_params: List[str] = Field(default_factory=list)
    timeout: float = 10.0
