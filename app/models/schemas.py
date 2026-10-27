from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class QueryRequest(BaseModel):
    question: str

class QueryResult(BaseModel):
    question: str
    answer: str
    sql: str
    validated: bool
    result_preview: List[Dict[str, Any]]
    row_count: int
    chart_data: Optional[Dict[str, Any]] = None
    execution_metadata: Dict[str, Any]
    timestamp: datetime
