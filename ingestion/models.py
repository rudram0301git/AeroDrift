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

    def to_dict(self) -> Dict[str, Any]:
         """Convert the cloud resource into a dictionary."""
         return {
         "resource_id": self.resource_id,
        "resource_type": self.resource_type,
        "provider": self.provider,
        "name": self.name,
        "region": self.region,
        "metadata": self.metadata,
        "relationships": self.relationships,
    }