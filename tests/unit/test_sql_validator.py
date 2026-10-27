import pytest
from app.validators.sql_validator import validator

def test_select_allowed():
    is_valid, msg = validator.validate("SELECT * FROM customers")
    assert is_valid == True

def test_insert_blocked():
    is_valid, msg = validator.validate("INSERT INTO customers VALUES (1, 'test')")
    assert is_valid == False
    assert "Forbidden" in msg or "SELECT" in msg

def test_delete_blocked():
    is_valid, msg = validator.validate("DELETE FROM customers")
    assert is_valid == False

def test_drop_blocked():
    is_valid, msg = validator.validate("DROP TABLE customers")
    assert is_valid == False

def test_multiple_statements_blocked():
    is_valid, msg = validator.validate("SELECT * FROM customers; DROP TABLE customers;")
    assert is_valid == False
