from app.utility.table1_utility import DatabaseService

if __name__ == "__main__":
    db_service = DatabaseService()
    try:
        # Create
        new_id = db_service.create(c_text="Sample Text", c_double=123.45)
        print(f"Inserted record with ID: {new_id}")

        # Read by id
        record = db_service.read_by_id(new_id)
        print("Record fetched:", record)
        # print(record['id'])
        # print(record['c_text'])
        # print(record['c_double'])
        # print(record['c_datetime'])

        # Read all
        all_records = db_service.read()
        print("All records:")
        for record in all_records:
            print(record)

        # Update
        updated = db_service.update(new_id, c_text="Updated Text", c_double=678.90)
        print("Record updated:", updated)

        # Delete
        deleted = db_service.delete(new_id)
        print("Record deleted:", deleted)
    finally:
        db_service.close()
