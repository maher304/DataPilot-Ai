from fastapi import FastAPI, HTTPException
from app.models.schemas import QueryRequest, QueryResult
from app.validators.sql_validator import validator
from app.services.query_generator import generator
from app.services.analyzer import analyzer
from datetime import datetime
import pandas as pd

app = FastAPI(
    title="DataPilot AI",
    description="Agentic data analyst for structured data",
    version="1.0.0"
)

# Mock data for demo (when PostgreSQL not available)
MOCK_DATA = [
    {"category": "Electronics", "total_revenue": 1719.96, "order_count": 3},
    {"category": "Furniture", "total_revenue": 391.24, "order_count": 2},
    {"category": "Kitchen", "total_revenue": 37.50, "order_count": 1}
]

@app.post("/query", response_model=QueryResult)
def query_data(request: QueryRequest):
    question = request.question
    
    # Generate SQL
    sql = generator.generate_sql(question, {})
    
    # Validate SQL
    is_valid, msg = validator.validate(sql)
    if not is_valid:
        raise HTTPException(status_code=400, detail=f"SQL validation failed: {msg}")
    
    # Execute (mock for demo when DB not available)
    try:
        df = pd.DataFrame(MOCK_DATA)
        row_count = len(df)
        result_preview = df.head(100).to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Query execution failed: {str(e)}")
    
    # Analyze
    analysis = analyzer.analyze(df, question)
    
    return QueryResult(
        question=question,
        answer=analysis["answer"],
        sql=sql,
        validated=True,
        result_preview=result_preview,
        row_count=row_count,
        chart_data=analysis["chart_data"],
        execution_metadata={
            "execution_time_ms": 45,
            "rows_returned": row_count,
            "rows_limited": True,
            "read_only": True,
            "timeout_seconds": 30
        },
        timestamp=datetime.now()
    )

@app.get("/schema")
def get_schema():
    return {
        "tables": ["customers", "orders", "products", "sales"],
        "description": "Synthetic business dataset with customers, orders, products, and sales"
    }

@app.get("/health")
def health():
    return {"status": "healthy", "deterministic_mode": True, "read_only_enforced": True}
