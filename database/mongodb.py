from pymongo import MongoClient

try:
    MONGO_URI = "mongodb+srv://badolejayanti26_db_user:Shivparvati854@cluster0.w8pkf4y.mongodb.net/?appName=Cluster0"

    client = MongoClient(MONGO_URI)

    client.admin.command("ping")

    db = client["SSUS"]

    students_collection = db["students"]
    marks_collection = db["marks"]
    attendance_collection = db["attendance"]
    bmi_collection = db["bmi_reports"]

    print("MongoDB connected Successfully")

except Exception as e:
    print("MongoDB Error:", e)
