# tools/hr_tools.py
# HR Agent ke tools - Single comprehensive tool to prevent tool-calling loops

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "employees.db")


def query_employee_database(query: str) -> str:
    """
    Search the employee database for any HR question in one call.
    Handles: employee lookups by name/email, department summaries,
    salary range queries, and department head-counts.
    Call this tool ONCE with the user's question and it returns a complete answer.

    Args:
        query: The search term — an employee name, department name, salary range
               description, or any HR-related keyword (e.g. "Ahmed Khan",
               "Engineering", "salary above 80000").

    Returns:
        A complete formatted answer with all matching employee or department data.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        query_lower = query.lower()

        # ── Salary range queries ──────────────────────────────────────────────
        import re
        salary_match = re.search(r"(\d[\d,]*)\s*(?:to|-)\s*(\d[\d,]*)", query_lower)
        above_match  = re.search(r"above\s+(\d[\d,]*)|more\s+than\s+(\d[\d,]*)|greater\s+than\s+(\d[\d,]*)", query_lower)
        below_match  = re.search(r"below\s+(\d[\d,]*)|less\s+than\s+(\d[\d,]*)", query_lower)

        if salary_match:
            lo = int(salary_match.group(1).replace(",", ""))
            hi = int(salary_match.group(2).replace(",", ""))
            cursor.execute(
                "SELECT name, department, position, salary FROM employees "
                "WHERE salary BETWEEN ? AND ? ORDER BY salary DESC",
                (lo, hi)
            )
            rows = cursor.fetchall()
            conn.close()
            if not rows:
                return f"No employees found with salary between ${lo:,.0f} and ${hi:,.0f}."
            lines = [f"Employees with salary ${lo:,.0f} – ${hi:,.0f}:\n"]
            for r in rows:
                lines.append(f"  - {r[0]} | {r[2]} | {r[1]} | ${r[3]:,.0f}")
            return "\n".join(lines)

        if above_match:
            threshold = int((above_match.group(1) or above_match.group(2) or above_match.group(3)).replace(",", ""))
            cursor.execute(
                "SELECT name, department, position, salary FROM employees "
                "WHERE salary > ? ORDER BY salary DESC",
                (threshold,)
            )
            rows = cursor.fetchall()
            conn.close()
            if not rows:
                return f"No employees found with salary above ${threshold:,.0f}."
            lines = [f"Employees earning above ${threshold:,.0f}:\n"]
            for r in rows:
                lines.append(f"  - {r[0]} | {r[2]} | {r[1]} | ${r[3]:,.0f}")
            return "\n".join(lines)

        if below_match:
            threshold = int((below_match.group(1) or below_match.group(2)).replace(",", ""))
            cursor.execute(
                "SELECT name, department, position, salary FROM employees "
                "WHERE salary < ? ORDER BY salary ASC",
                (threshold,)
            )
            rows = cursor.fetchall()
            conn.close()
            if not rows:
                return f"No employees found with salary below ${threshold:,.0f}."
            lines = [f"Employees earning below ${threshold:,.0f}:\n"]
            for r in rows:
                lines.append(f"  - {r[0]} | {r[2]} | {r[1]} | ${r[3]:,.0f}")
            return "\n".join(lines)

        # ── Department summary (when query is a department name) ──────────────
        dept_keywords = ["engineering", "hr", "human resource", "finance", "marketing",
                         "sales", "operations", "management", "it ", "department"]
        is_dept_query = any(kw in query_lower for kw in dept_keywords)

        if is_dept_query:
            cursor.execute(
                "SELECT COUNT(*), AVG(salary), AVG(experience) FROM employees "
                "WHERE LOWER(department) LIKE ?",
                (f"%{query_lower}%",)
            )
            summary = cursor.fetchone()

            cursor.execute(
                "SELECT name, position, salary, experience FROM employees "
                "WHERE LOWER(department) LIKE ? ORDER BY salary DESC",
                (f"%{query_lower}%",)
            )
            members = cursor.fetchall()
            conn.close()

            if not members:
                # Fall through to name/general search below
                pass
            else:
                count, avg_sal, avg_exp = summary
                lines = [
                    f"Department Query: '{query}'\n",
                    f"Total Employees  : {count}",
                    f"Average Salary   : ${avg_sal:,.0f}",
                    f"Average Experience: {avg_exp:.1f} years\n",
                    "Employees:"
                ]
                for m in members:
                    lines.append(f"  - {m[0]} | {m[1]} | ${m[2]:,.0f} | {m[3]} yrs exp")
                return "\n".join(lines)

        # ── Employee search by name / email / position ────────────────────────
        cursor.execute("""
            SELECT name, email, age, department, position, salary, experience, phone, join_date
            FROM employees
            WHERE LOWER(name)       LIKE ?
               OR LOWER(email)      LIKE ?
               OR LOWER(department) LIKE ?
               OR LOWER(position)   LIKE ?
        """, (f"%{query_lower}%",) * 4)
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return f"No employee or department found matching '{query}'."

        output = []
        for emp in rows:
            output.append(
                f"Name       : {emp[0]}\n"
                f"Email      : {emp[1]}\n"
                f"Age        : {emp[2]}\n"
                f"Department : {emp[3]}\n"
                f"Position   : {emp[4]}\n"
                f"Salary     : ${emp[5]:,.0f}\n"
                f"Experience : {emp[6]} years\n"
                f"Phone      : {emp[7]}\n"
                f"Join Date  : {emp[8]}\n"
                "---"
            )
        return "\n".join(output)

    except Exception as e:
        return f"Error querying employee database: {str(e)}"