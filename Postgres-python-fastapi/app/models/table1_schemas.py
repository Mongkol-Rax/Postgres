"""
Table1 Schema
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Table1Base(BaseModel):
    """
    Base schema for Table1 with common fields.
    """
    c_text: str = Field(..., max_length=100, description="Text field with a maximum of 100 characters.")
    c_double: Optional[float] = Field(None, description="Optional double precision field.")


class Table1Create(Table1Base):
    """
    Schema for creating a new record in Table1.
    """
    pass


class Table1Update(BaseModel):
    """
    Schema for updating a record in Table1.
    """
    c_text: Optional[str] = Field(None, max_length=100, description="Updated text field.")
    c_double: Optional[float] = Field(None, description="Updated double precision field.")


class Table1Response(Table1Base):
    """
    Schema for retrieving a record from Table1.
    """
    id: int = Field(..., description="Unique identifier for the record.")
    c_datetime: datetime = Field(..., description="Timestamp when the record was created.")

    class Config:
        orm_mode = True
