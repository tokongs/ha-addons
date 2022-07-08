from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Context:
    id: str
    parent_id: Optional[str] = None
    user_id: Optional[str] = None

@dataclass
class State:
    attributes: Dict
    entity_id: str
    last_changed: str
    last_updated: str
    state: str
    context: Context

@dataclass
class StatesResponse:
    items: List[State]
