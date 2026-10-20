# setup_data.py
# Ye file SQLite database banayegi with 20 employees ka data

import sqlite3
import os
import random

os.makedirs("data", exist_ok=True)

# Database connect/create karo
conn = sqlite3.connect("data/employees.db")
cursor = conn.cursor()

# Table banao
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER NOT NULL,
        department TEXT NOT NULL,
        salary REAL NOT NULL,
        experience INTEGER NOT NULL,
        position TEXT NOT NULL,
        phone TEXT NOT NULL,
        join_date TEXT NOT NULL
    )
""")

# 20 Employees ka data
employees = [
    ("Ahmed Khan", "ahmed.khan@techcorp.com", 32, "Engineering", 85000, 8, "Senior Developer", "+92-300-1234567", "2018-03-15"),
    ("Sara Ali", "sara.ali@techcorp.com", 28, "Engineering", 72000, 5, "Full Stack Developer", "+92-301-2345678", "2021-06-01"),
    ("Usman Malik", "usman.malik@techcorp.com", 35, "Management", 95000, 12, "Project Manager", "+92-302-3456789", "2014-01-10"),
    ("Fatima Zahra", "fatima.zahra@techcorp.com", 26, "HR", 55000, 3, "HR Executive", "+92-303-4567890", "2023-02-20"),
    ("Bilal Ahmed", "bilal.ahmed@techcorp.com", 40, "Finance", 90000, 15, "Finance Manager", "+92-304-5678901", "2011-07-01"),
    ("Ayesha Siddiqui", "ayesha.siddiqui@techcorp.com", 29, "Engineering", 68000, 6, "Backend Developer", "+92-305-6789012", "2020-09-15"),
    ("Hassan Raza", "hassan.raza@techcorp.com", 33, "Marketing", 62000, 9, "Marketing Lead", "+92-306-7890123", "2017-04-22"),
    ("Zainab Hussain", "zainab.hussain@techcorp.com", 27, "Design", 58000, 4, "UI/UX Designer", "+92-307-8901234", "2022-01-10"),
    ("Omar Farooq", "omar.farooq@techcorp.com", 38, "Engineering", 88000, 13, "Tech Lead", "+92-308-9012345", "2013-11-05"),
    ("Mariam Noor", "mariam.noor@techcorp.com", 25, "HR", 48000, 2, "HR Assistant", "+92-309-0123456", "2024-03-01"),
    ("Tariq Mehmood", "tariq.mehmood@techcorp.com", 42, "Management", 105000, 18, "Director of Operations", "+92-310-1234568", "2008-06-15"),
    ("Nadia Parveen", "nadia.parveen@techcorp.com", 31, "Finance", 70000, 7, "Senior Accountant", "+92-311-2345679", "2019-08-20"),
    ("Kamran Shah", "kamran.shah@techcorp.com", 30, "Engineering", 75000, 6, "DevOps Engineer", "+92-312-3456780", "2020-02-14"),
    ("Sana Iqbal", "sana.iqbal@techcorp.com", 24, "Design", 52000, 1, "Junior Designer", "+92-313-4567891", "2025-01-15"),
    ("Faisal Mahmood", "faisal.mahmood@techcorp.com", 36, "Marketing", 65000, 10, "Senior Marketing Manager", "+92-314-5678902", "2016-05-30"),
    ("Rabia Akhtar", "rabia.akhtar@techcorp.com", 29, "Engineering", 71000, 5, "QA Engineer", "+92-315-6789013", "2021-10-01"),
    ("Imran Yousaf", "imran.yousaf@techcorp.com", 45, "Management", 110000, 20, "VP Engineering", "+92-316-7890124", "2006-03-20"),
    ("Hira Mansoor", "hira.mansoor@techcorp.com", 27, "HR", 56000, 4, "HR Specialist", "+92-317-8901235", "2022-07-11"),
    ("Adnan Siddique", "adnan.siddique@techcorp.com", 34, "Finance", 78000, 10, "Financial Analyst", "+92-318-9012346", "2016-12-01"),
    ("Laiba Fatima", "laiba.fatima@techcorp.com", 26, "Engineering", 65000, 3, "Frontend Developer", "+92-319-0123457", "2023-09-05"),
]

# Data insert karo
cursor.executemany("""
    INSERT OR IGNORE INTO employees (name, email, age, department, salary, experience, position, phone, join_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", employees)

conn.commit()

# Verify
cursor.execute("SELECT COUNT(*) FROM employees")
count = cursor.fetchone()[0]
print(f"✅ Database created successfully!")
print(f"   Total employees: {count}")
print(f"   Database location: data/employees.db")

# Sample data dikhao
cursor.execute("SELECT name, department, salary FROM employees LIMIT 5")
print("\n📋 Sample Employees:")
for row in cursor.fetchall():
    print(f"   {row[0]} | {row[1]} | ${row[2]:,.0f}")

conn.close()