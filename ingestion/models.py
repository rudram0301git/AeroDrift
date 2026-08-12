from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class CloudResource:
    resource_id: str
    resource_type: str
    provider: str
    name: Optional[str] = None
    region: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    relationships: List[str] = field(default_factory=list)