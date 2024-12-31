"""
API endpoints for managing Table1 resources.
"""

from fastapi import APIRouter, HTTPException
from typing import List
from app.utility.table1_utilitys import DatabaseService  # Import your DatabaseService class
from app.models.table1_schemas import Table1Create, Table1Response, Table1Update  # Import schema class

# Initialize router
router = APIRouter()

# Database service instance
DB_SERVICE = DatabaseService()


@router.post("/create/", response_model=Table1Response)
async def create_table1_record(record: Table1Create):
    """
    Create a new record in Table1.

    Args:
        record (Table1Create): Data for the new record.

    Returns:
        Table1Response: The created record with its ID.
    """
    record_id = DB_SERVICE.create(c_text=record.c_text, c_double=record.c_double)
    return DB_SERVICE.read_by_id(record_id)


@router.get("/get_all/", response_model=List[Table1Response])
async def get_all_table1_records():
    """
    Retrieve all records from Table1.

    Returns:
        List[Table1Response]: A list of all records.
    """
    return DB_SERVICE.read()


@router.get("/get_by_id/{record_id}", response_model=Table1Response)
async def get_table1_record(record_id: int):
    """
    Retrieve a specific record from Table1 by its ID.

    Args:
        record_id (int): The ID of the record to retrieve.

    Returns:
        Table1Response: The record corresponding to the given ID.

    Raises:
        HTTPException: If the record is not found.
    """
    record = DB_SERVICE.read_by_id(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record


@router.put("/update_by_id/{record_id}", response_model=bool)
async def update_table1_record(record_id: int, record: Table1Update):
    """
    Update a specific record in Table1 by its ID.

    Args:
        record_id (int): The ID of the record to update.
        record (Table1Update): Data for updating the record.

    Returns:
        bool: True if the record was updated, False otherwise.

    Raises:
        HTTPException: If the record is not found or update fails.
    """
    updated = DB_SERVICE.update(record_id, c_text=record.c_text, c_double=record.c_double)
    if not updated:
        raise HTTPException(status_code=404, detail="Record not found or update failed")
    return updated


@router.delete("/delete/{record_id}", response_model=bool)
async def delete_table1_record(record_id: int):
    """
    Delete a specific record from Table1 by its ID.

    Args:
        record_id (int): The ID of the record to delete.

    Returns:
        bool: True if the record was deleted, False otherwise.

    Raises:
        HTTPException: If the record is not found or deletion fails.
    """
    deleted = DB_SERVICE.delete(record_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Record not found or delete failed")
    return deleted
