"""
Pytest: Test API Table1
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app

# สร้าง TestClient เพื่อเรียก API
client = TestClient(app)


@pytest.fixture
def sample_record():
    """
    Sample data for creating a record.
    """
    return {
        "c_text": "Sample Text",
        "c_double": 123.45
    }


def test_create_table1_record(sample_record):
    """
    Test creating a new record in Table1.
    """
    response = client.post("/table1/create/", json=sample_record)
    assert response.status_code == 200
    data = response.json()
    assert data["c_text"] == sample_record["c_text"]
    assert data["c_double"] == sample_record["c_double"]
    assert "id" in data


def test_get_all_table1_records():
    """
    Test retrieving all records from Table1.
    """
    response = client.get("/table1/get_all/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_table1_record(sample_record):
    """
    Test retrieving a specific record by ID.
    """
    # สร้าง record ใหม่
    create_response = client.post("/table1/create/", json=sample_record)
    assert create_response.status_code == 200
    record_id = create_response.json()["id"]

    # ดึง record ที่สร้างมา
    response = client.get(f"/table1/get_by_id/{record_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == record_id
    assert data["c_text"] == sample_record["c_text"]
    assert data["c_double"] == sample_record["c_double"]


def test_update_table1_record(sample_record):
    """
    Test updating a specific record by ID.
    """
    # สร้าง record ใหม่
    create_response = client.post("/table1/create/", json=sample_record)
    assert create_response.status_code == 200
    record_id = create_response.json()["id"]

    # อัปเดต record
    updated_data = {
        "c_text": "Updated Text",
        "c_double": 987.65
    }
    update_response = client.put(f"/table1/update_by_id/{record_id}", json=updated_data)
    assert update_response.status_code == 200
    assert update_response.json() is True

    # ตรวจสอบ record ที่อัปเดต
    response = client.get(f"/table1/get_by_id/{record_id}")
    data = response.json()
    assert data["c_text"] == updated_data["c_text"]
    assert data["c_double"] == updated_data["c_double"]


def test_delete_table1_record(sample_record):
    """
    Test deleting a specific record by ID.
    """
    # สร้าง record ใหม่
    create_response = client.post("/table1/create/", json=sample_record)
    assert create_response.status_code == 200
    record_id = create_response.json()["id"]

    # ลบ record
    delete_response = client.delete(f"/table1/delete/{record_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() is True

    # ตรวจสอบว่า record ถูกลบแล้ว
    response = client.get(f"/table1/get_by_id/{record_id}")
    assert response.status_code == 404
