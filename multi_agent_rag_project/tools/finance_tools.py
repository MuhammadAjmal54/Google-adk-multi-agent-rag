# tools/finance_tools.py
# Finance Agent ke tools - Single comprehensive tool to prevent tool-calling loops


def calculate_finance(
    salary: float,
    operation: str,
    percentage: float = 0.0,
    performance_rating: str = "",
    expression: str = ""
) -> str:
    """
    Perform any financial or salary calculation in one call.
    Handles salary increments, bonus calculations, and general math.
    Call this tool ONCE and it returns a complete formatted result.

    Args:
        salary      : The salary amount (use 0 if doing pure math only).
        operation   : What to calculate — one of:
                      "increment"   → salary increment by percentage
                      "bonus"       → bonus based on performance_rating
                      "math"        → evaluate the expression string
        percentage  : Increment percentage (e.g. 10 for 10%). Used when operation="increment".
        performance_rating: One of Excellent/Good/Average/Below Average/Poor.
                            Used when operation="bonus".
        expression  : A math expression string (e.g. "85000 * 1.15").
                      Used when operation="math".

    Returns:
        A complete formatted calculation result.
    """
    operation = operation.lower().strip()

    # ── Salary Increment ──────────────────────────────────────────────────────
    if operation == "increment":
        try:
            increment_amount = salary * (percentage / 100)
            new_salary       = salary + increment_amount
            monthly_new      = new_salary / 12
            return (
                f"Salary Increment Calculation:\n"
                f"  Current Salary    : ${salary:,.0f}\n"
                f"  Increment         : {percentage}%\n"
                f"  Increment Amount  : ${increment_amount:,.0f}\n"
                f"  New Annual Salary : ${new_salary:,.0f}\n"
                f"  New Monthly Salary: ${monthly_new:,.0f}"
            )
        except Exception as e:
            return f"Error in increment calculation: {e}"

    # ── Bonus Calculation ─────────────────────────────────────────────────────
    elif operation == "bonus":
        rating_map = {
            "excellent":     0.20,
            "good":          0.15,
            "average":       0.10,
            "below average": 0.05,
            "poor":          0.00,
        }
        rating_lower = performance_rating.lower().strip()
        if rating_lower not in rating_map:
            return (
                f"Invalid rating '{performance_rating}'. "
                f"Use: Excellent, Good, Average, Below Average, or Poor."
            )
        pct    = rating_map[rating_lower]
        bonus  = salary * pct
        total  = salary + bonus
        return (
            f"Bonus Calculation:\n"
            f"  Annual Salary       : ${salary:,.0f}\n"
            f"  Performance Rating  : {performance_rating.title()}\n"
            f"  Bonus Percentage    : {pct * 100:.0f}%\n"
            f"  Bonus Amount        : ${bonus:,.0f}\n"
            f"  Total Compensation  : ${total:,.0f}"
        )

    # ── General Math ──────────────────────────────────────────────────────────
    elif operation == "math":
        try:
            allowed = set("0123456789+-*/.() %")
            if not all(c in allowed for c in expression):
                return "Error: Invalid characters in expression. Only numbers and math operators allowed."
            result = eval(expression)  # noqa: S307 – safe: chars filtered above
            return f"Calculation:\n  {expression} = {result:,.4g}"
        except ZeroDivisionError:
            return "Error: Division by zero."
        except Exception as e:
            return f"Error evaluating '{expression}': {e}"

    else:
        return (
            f"Unknown operation '{operation}'. "
            f"Use 'increment', 'bonus', or 'math'."
        )