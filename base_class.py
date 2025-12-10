from abc import ABC, abstractmethod
from datetime import datetime
import uuid
from typing import List, Dict, Any, Optional

class Club(ABC):
    # Club ana sınıf 
    def __init__(self,name, member_count, description, created_at):
        self.name = name
        self.member_count = member_count
        self.description = description
        self.created_at = created_at
        
