"""
Call API
"""

import httpx
import json

BASE_URL = "http://127.0.0.1:8000/table1"

def create_record(c_text: str, c_double: float):
    """Call API to create a new record."""
    payload = {"c_text": c_text, "c_double": c_double}
    response = httpx.post(f"{BASE_URL}/create/", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def get_all_records():
    """Call API to retrieve all records."""
    response = httpx.get(f"{BASE_URL}/get_all/")
    if response.status_code == 200:
        # return response.json()
        return "\n".join(json.dumps(record, indent=2) for record in response.json())
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def get_record_by_id(record_id: int):
    """Call API to retrieve a record by ID."""
    response = httpx.get(f"{BASE_URL}/get_by_id/{record_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Record not found"}
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def update_record(record_id: int, c_text: str, c_double: float):
    """Call API to update a record by ID."""
    payload = {"c_text": c_text, "c_double": c_double}
    response = httpx.put(f"{BASE_URL}/update_by_id/{record_id}", json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def delete_record(record_id: int):
    """Call API to delete a record by ID."""
    response = httpx.delete(f"{BASE_URL}/delete/{record_id}")
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Record not found"}
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


# Example Usage
if __name__ == "__main__":
    # Create a new record
    new_record = create_record("Sample Text", 123.45)
    print("Created Record:", new_record)

    # Get all records
    all_records = get_all_records()
    print("All Records:", all_records)

    # Get a record by ID
    record_id = new_record["id"]
    record = get_record_by_id(record_id)
    print("Record by ID:", record)

    # Update the record
    updated_record = update_record(record_id, "Updated Text", 987.65)
    print("Updated Record:", updated_record)

    # Delete the record
    delete_status = delete_record(record_id)
    print("Delete Status:", delete_status)
