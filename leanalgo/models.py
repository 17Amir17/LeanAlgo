"""
Data models for the LeanAlgo application.
Using Pydantic for data validation and type checking.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class UserData(BaseModel):
    """Model for user data."""
    id: int
    name: str
    email: str
    is_active: bool = Field(default=True)
    tags: List[str] = Field(default_factory=list)
    description: Optional[str] = None
    
    
class AlgorithmResult(BaseModel):
    """Model for algorithm execution results."""
    algorithm_name: str
    execution_time_ms: float
    success: bool
    data: Optional[dict] = None
    error_message: Optional[str] = None 