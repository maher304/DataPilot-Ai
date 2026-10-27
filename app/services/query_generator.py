from typing import Dict, Any, List
from app.core.config import settings

class QueryGenerator:
    def __init__(self):
        self.deterministic = settings.deterministic_mode
    
    def generate_sql(self, question: str, schema_info: Dict[str, Any]) -> str:
        if not self.deterministic:
            # Would use LLM here
            pass
        
        q_lower = question.lower()
        if 'revenue' in q_lower and 'category' in q_lower:
            return """SELECT 
    p.category,
    SUM(s.quantity * s.unit_price) as total_revenue,
    COUNT(DISTINCT o.order_id) as order_count
FROM products p
JOIN sales s ON p.product_id = s.product_id
JOIN orders o ON s.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY total_revenue DESC"""
        elif 'customer' in q_lower and 'order' in q_lower:
            return """SELECT 
    c.first_name || ' ' || c.last_name as customer_name,
    COUNT(o.order_id) as order_count,
    SUM(s.quantity * s.unit_price) as total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN sales s ON o.order_id = s.order_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC"""
        else:
            return """SELECT p.category, SUM(s.quantity * s.unit_price) as revenue
FROM products p
JOIN sales s ON p.product_id = s.product_id
JOIN orders o ON s.order_id = o.order_id
WHERE o.status = 'completed' AND o.order_date >= '2026-09-01'
GROUP BY p.category
ORDER BY revenue DESC
LIMIT 10"""

generator = QueryGenerator()
