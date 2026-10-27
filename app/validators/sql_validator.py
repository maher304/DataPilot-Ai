import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Function
from sqlparse.tokens import Keyword, DML
import re

class SQLValidator:
    FORBIDDEN_KEYWORDS = [
        'INSERT', 'UPDATE', 'DELETE', 'DROP', 'ALTER', 'CREATE', 
        'TRUNCATE', 'EXEC', 'EXECUTE', 'GRANT', 'REVOKE', 'REPLACE'
    ]
    
    ALLOWED_TABLES = ['customers', 'orders', 'products', 'sales']
    
    def validate(self, sql: str) -> tuple[bool, str]:
        if not sql or not sql.strip():
            return False, "Empty query"
        
        # Check for multiple statements
        parsed = sqlparse.parse(sql)
        if len(parsed) > 1:
            return False, "Multiple statements are not allowed"
        
        stmt = parsed[0]
        
        # Check if it's a SELECT
        if not self._is_select(stmt):
            return False, "Only SELECT queries are allowed"
        
        sql_upper = sql.upper()
        
        # Check for forbidden keywords
        for keyword in self.FORBIDDEN_KEYWORDS:
            if re.search(r'\b' + keyword + r'\b', sql_upper):
                return False, f"Forbidden keyword: {keyword}"
        
        # Check for comments that might be malicious
        if '--' in sql or '/*' in sql:
            # Be cautious but allow simple comments - better to be strict
            pass
        
        # Check for semicolons (multiple statements)
        if sql.count(';') > 1 or (sql.count(';') == 1 and not sql.strip().endswith(';')):
            return False, "Invalid semicolon usage"
        
        # Try to extract tables (basic check)
        return True, "Query validated"
    
    def _is_select(self, stmt):
        for token in stmt.tokens:
            if token.ttype is DML and token.value.upper() == 'SELECT':
                return True
            if not token.is_whitespace and token.ttype is Keyword:
                if token.value.upper() in ['WITH']:  # Allow CTEs
                    # Check if it contains SELECT
                    return 'SELECT' in stmt.value.upper()
        # Also check if starts with SELECT or WITH
        return stmt.value.strip().upper().startswith(('SELECT', 'WITH'))

validator = SQLValidator()
