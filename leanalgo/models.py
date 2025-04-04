"""
Data models for the LeanAlgo application.
Using Pydantic for data validation and type checking.
"""

from typing import List, Optional, Dict, Any
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
    data: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None


class TradingParameters(BaseModel):
    """Model for trading algorithm parameters."""
    symbol: str
    quantity: int
    entry_price: float
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    position_size_percent: Optional[float] = Field(default=5.0, ge=0.0, le=100.0)
    
    
class BacktestResult(BaseModel):
    """Model for backtest results."""
    strategy_name: str
    start_date: str
    end_date: str
    initial_capital: float
    final_capital: float
    total_trades: int
    win_rate: float
    sharpe_ratio: Optional[float] = None
    max_drawdown: Optional[float] = None
    trades: List[Dict[str, Any]] = Field(default_factory=list) 