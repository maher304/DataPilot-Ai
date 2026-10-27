import pandas as pd
from typing import Dict, Any, List
import json

try:
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except:
    PLOTLY_AVAILABLE = False

class DataAnalyzer:
    def analyze(self, df: pd.DataFrame, question: str) -> Dict[str, Any]:
        answer = self._generate_answer(df, question)
        chart_data = self._generate_chart(df, question)
        return {
            "answer": answer,
            "chart_data": chart_data
        }
    
    def _generate_answer(self, df: pd.DataFrame, question: str) -> str:
        if df.empty:
            return "No results found for the query."
        
        q_lower = question.lower()
        if 'revenue' in q_lower and 'category' in q_lower:
            if len(df) > 0:
                top = df.iloc[0]
                return f"The highest revenue category is {top['category']} with ${top['total_revenue']:.2f} in revenue from {top.get('order_count', 0)} orders."
        elif 'customer' in q_lower:
            if len(df) > 0 and 'customer_name' in df.columns:
                top = df.iloc[0]
                return f"The top customer is {top['customer_name']} with {top.get('order_count', 0)} orders totaling ${top.get('total_spent', 0):.2f}."
        total = df['revenue'].sum() if 'revenue' in df.columns else (df['total_revenue'].sum() if 'total_revenue' in df.columns else 0)
        return f"Analysis shows {len(df)} categories with total revenue of ${total:.2f}."
    
    def _generate_chart(self, df: pd.DataFrame, question: str) -> Dict[str, Any]:
        if df.empty or len(df) == 0:
            return None
        
        if not PLOTLY_AVAILABLE:
            return {"type": "table", "data": df.to_dict('records'), "note": "Plotly not available"}
        
        try:
            q_lower = question.lower()
            if 'category' in df.columns and ('revenue' in df.columns or 'total_revenue' in df.columns):
                col = 'total_revenue' if 'total_revenue' in df.columns else 'revenue'
                fig = px.bar(df, x='category', y=col, title='Revenue by Category')
                return json.loads(fig.to_json())
            elif 'customer_name' in df.columns and 'total_spent' in df.columns:
                fig = px.bar(df.head(5), x='customer_name', y='total_spent', title='Top Customers')
                return json.loads(fig.to_json())
        except Exception as e:
            return {"error": str(e), "data": df.to_dict('records')}
        return {"data": df.to_dict('records')}

analyzer = DataAnalyzer()
