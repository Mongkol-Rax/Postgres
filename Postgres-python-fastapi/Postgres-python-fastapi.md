# คู่มือการใช้งาน Postgres, Python และ FastAPI

## ไฟล์และหน้าที่

### 1. `requirements.txt`
ไฟล์นี้ระบุไลบรารีที่จำเป็นสำหรับโปรเจกต์ เช่น:
- `psycopg2`: ใช้สำหรับเชื่อมต่อกับ Postgres
- `fastapi`: สำหรับสร้าง API
- `uvicorn`: สำหรับรันเซิร์ฟเวอร์ FastAPI
- `pytest` และ `httpx`: สำหรับการทดสอบ

### 2. `table1_schemas.py`
กำหนดโครงสร้างของข้อมูลที่ใช้ใน API:
- ใช้ Pydantic สร้าง schema สำหรับ `Table1` เช่น `Table1Create`, `Table1Update` และ `Table1Response`
- รองรับการตรวจสอบข้อมูลและเพิ่มคำอธิบาย

### 3. `table1_services.py`
ไฟล์นี้ประกอบด้วย endpoint สำหรับ API:
- `/create/`: สร้างข้อมูลใหม่
- `/get_all/`: ดึงข้อมูลทั้งหมด
- `/get_by_id/{record_id}`: ดึงข้อมูลตาม ID
- `/update_by_id/{record_id}`: อัปเดตข้อมูลตาม ID
- `/delete/{record_id}`: ลบข้อมูลตาม ID

### 4. `.env`
ไฟล์นี้เก็บข้อมูลการตั้งค่าฐานข้อมูล เช่น:
- `POSTGRES_USER`: ชื่อผู้ใช้
- `POSTGRES_PASSWORD`: รหัสผ่าน
- `POSTGRES_DB`: ชื่อฐานข้อมูล
- `POSTGRES_HOST`: ที่อยู่เซิร์ฟเวอร์
- `POSTGRES_PORT`: พอร์ต

### 5. `table1_utilitys.py`
จัดการ CRUD สำหรับฐานข้อมูล Postgres:
- ใช้ `psycopg2` สร้างการเชื่อมต่อ
- มีฟังก์ชัน เช่น `create`, `read`, `read_by_id`, `update`, และ `delete`

### 6. `call_table1_api.py`
ไฟล์นี้สำหรับเรียก API ผ่าน HTTP:
- รองรับฟังก์ชัน เช่น `create_record`, `get_all_records`, `get_record_by_id`, `update_record`, และ `delete_record`

### 7. `crud_table1_test.py`
ทดสอบการทำงาน CRUD กับฐานข้อมูลโดยตรง:
- ทดสอบการสร้าง อ่าน อัปเดต และลบข้อมูลใน `Table1`

### 8. `pytest_table1_api.py`
ทดสอบ API ด้วย Pytest:
- รวมถึงการทดสอบ endpoint เช่น `/create/`, `/get_all/`, `/get_by_id/`, `/update_by_id/` และ `/delete/`

## คำสั่งที่ใช้ในโปรเจกต์

### Directory ที่ใช้:
```
..\Postgres\Postgres-python-fastapi
```

### สร้าง Virtual Environment ใหม่:
```
python -m venv .venv
```

### เปิดใช้งาน Virtual Environment:
```
.venv\Scripts\activate
```

### ปิดใช้งาน Virtual Environment:
```
deactivate
```

### ลบ Virtual Environment ปัจจุบัน:
```
rmdir /s /q .venv
```

### อัปเดต `pip` และติดตั้งแพ็กเกจใหม่:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### รันเซิร์ฟเวอร์ Uvicorn
- ไม่มีการ reload เมื่อแก้โค้ด:
```
uvicorn app.main:app
```
- มีการ reload เมื่อแก้โค้ด:
```
uvicorn app.main:app --reload
```

### การทดสอบ
- ทดสอบ CRUD ของไฟล์ `crud_table1_test.py`:
```
python -m tests.crud_table1_test
```
- ทดสอบการเรียก API ของไฟล์ `call_table1_api.py`:
```
python -m tests.call_table1_api
```
- รัน Pytest แบบไม่สน warnings:
```
pytest tests/pytest_table1_api1.py --disable-warnings
```
- รัน Pytest:
```
pytest tests/pytest_table1_api1.py
```

