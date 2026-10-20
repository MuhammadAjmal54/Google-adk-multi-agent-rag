# create_documents.py
# Ye file company policies aur FAQs documents banayegi

import os

# ============================================
# COMPANY POLICIES DOCUMENT
# ============================================
company_policies = """
COMPANY POLICIES - TechCorp Solutions Pvt Ltd
================================================

1. WORKING HOURS POLICY
- Office hours: Monday to Friday, 9:00 AM to 6:00 PM
- Lunch break: 1:00 PM to 2:00 PM (1 hour)
- Flexible working hours available with manager approval
- Remote work allowed up to 2 days per week for eligible employees
- Late arrival beyond 30 minutes requires manager notification

2. LEAVE POLICY
- Annual leave: 20 days per year for employees with 1+ year experience
- Annual leave: 15 days per year for new employees (first year)
- Sick leave: 12 days per year with medical certificate for 3+ days
- Maternity leave: 90 days paid leave
- Paternity leave: 7 days paid leave
- Casual leave: 5 days per year
- Leave must be applied 3 days in advance (except emergencies)
- Leave balance carries forward up to 10 days only

3. SALARY & COMPENSATION POLICY
- Salary disbursed on 1st of every month via bank transfer
- Annual performance bonus: 5% to 20% based on rating
- Overtime pay: 1.5x hourly rate for approved overtime
- Salary increments reviewed annually in April
- Provident fund: 12% employee + 12% employer contribution
- Health insurance provided for employee and family

4. CODE OF CONDUCT
- Professional behavior expected at all times
- No harassment or discrimination tolerated
- Confidentiality of company data is mandatory
- Social media policy: No posting company info without approval
- Dress code: Business casual on regular days, formal on client days

5. IT & SECURITY POLICY
- Company laptops must not be used for personal business
- Password must be changed every 90 days
- Two-factor authentication mandatory for all systems
- No unauthorized software installation
- Data backup required daily for project files
- VPN required for remote access to company systems

6. PERFORMANCE REVIEW POLICY
- Quarterly performance reviews conducted
- Annual appraisal in April
- Performance ratings: Excellent, Good, Average, Below Average, Poor
- PIP (Performance Improvement Plan) for Below Average ratings
- Promotion criteria: 2 consecutive years of Good or Excellent rating

7. TERMINATION POLICY
- Notice period: 30 days for employees, 60 days for managers
- Resignation must be submitted in writing
- Exit interview mandatory
- Final settlement within 15 days of last working day
- Company property must be returned before final settlement

8. TRAINING & DEVELOPMENT
- Annual training budget: $500 per employee
- Mandatory compliance training every year
- Technical skill development encouraged
- Conference attendance with manager approval
- Internal mentorship program available

9. EXPENSE REIMBURSEMENT POLICY
- Travel expenses reimbursed within 15 days of submission
- Meal allowance: $25 per day for business travel
- Internet reimbursement: $30/month for remote workers
- Original receipts required for all claims
- Claims above $500 require director approval

10. HEALTH & SAFETY POLICY
- Emergency exits must remain unobstructed
- Fire drill conducted quarterly
- First aid kits available on each floor
- Report any workplace hazard immediately
- Ergonomic workstation setup available on request
"""

# ============================================
# COMPANY FAQs DOCUMENT
# ============================================
company_faqs = """
FREQUENTLY ASKED QUESTIONS - TechCorp Solutions Pvt Ltd
========================================================

Q1: How do I apply for leave?
A1: You can apply for leave through the HR portal or by emailing hr@techcorp.com. 
    Leave applications must be submitted at least 3 days in advance. 
    For sick leave, a medical certificate is required for leaves exceeding 3 days.

Q2: What is the office dress code?
A2: Business casual is required on regular working days. 
    Formal attire is required on client meeting days and official events. 
    Casual Fridays are allowed with manager approval.

Q3: How is salary calculated for new joiners?
A3: Salary is calculated on a pro-rata basis for the first month. 
    If you join mid-month, you will receive salary for the actual days worked. 
    Full salary starts from the next month.

Q4: What are the working hours?
A4: Standard working hours are 9:00 AM to 6:00 PM, Monday through Friday. 
    There is a 1-hour lunch break from 1:00 PM to 2:00 PM. 
    Flexible hours can be arranged with your manager's approval.

Q5: How do I request remote work?
A5: Submit a remote work request through the HR portal at least 2 days in advance. 
    Remote work is allowed up to 2 days per week. 
    You must be available during core hours (10 AM - 4 PM) while working remotely.

Q6: What is the performance review process?
A6: Performance reviews are conducted quarterly. 
    Your manager will schedule a one-on-one meeting to discuss your performance. 
    Annual appraisals happen in April, where salary increments and bonuses are decided.

Q7: How do I claim expense reimbursement?
A7: Submit your expense claim through the finance portal with original receipts. 
    Claims are processed within 15 business days. 
    Claims above $500 require director approval.

Q8: What training opportunities are available?
A8: Each employee has an annual training budget of $500. 
    You can use this for online courses, certifications, or conferences. 
    Submit training requests through the L&D portal with manager approval.

Q9: What is the notice period for resignation?
A9: The notice period is 30 days for regular employees and 60 days for managers. 
    Resignation must be submitted in writing to your manager and HR. 
    An exit interview is mandatory before your last working day.

Q10: How do I get IT support?
A10: For IT issues, raise a ticket on the IT support portal or email it@techcorp.com. 
    Urgent issues can be reported by calling the IT helpline at ext. 1234. 
    Response time is within 4 hours for critical issues.

Q11: What is the company's health insurance coverage?
A11: The company provides health insurance for the employee and their immediate family 
    (spouse and up to 2 children). Coverage includes hospitalization, outpatient care, 
    and dental. The insurance card is issued within 30 days of joining.

Q12: How are overtime hours compensated?
A12: Approved overtime is paid at 1.5 times the hourly rate. 
    Overtime must be pre-approved by your manager. 
    Maximum overtime allowed is 10 hours per week.

Q13: What is the provident fund contribution?
A13: Both employee and employer contribute 12% of the basic salary to the provident fund. 
    The PF account is managed by the company's PF administrator. 
    You can check your PF balance through the HR portal.

Q14: Can I transfer to another department?
A14: Internal transfers are possible after completing 1 year in your current department. 
    You need to apply through the internal job posting system. 
    Both current and receiving department managers must approve the transfer.

Q15: What is the company's policy on social media?
A15: Employees should not post confidential company information on social media. 
    Personal opinions should be clearly stated as personal views. 
    Official company social media accounts are managed by the marketing team only.

Q16: How do I update my personal information?
A16: You can update your personal information (address, phone, emergency contact) 
    through the HR self-service portal. Changes to bank details require HR verification.

Q17: What happens if I'm late to office?
A17: If you're going to be late by more than 30 minutes, notify your manager immediately. 
    Frequent late arrivals may affect your performance rating. 
    Three unnotified late arrivals in a month result in a formal warning.

Q18: Is there a probation period for new employees?
A18: Yes, new employees have a 3-month probation period. 
    During probation, performance is closely monitored. 
    Upon successful completion, employment is confirmed with full benefits.

Q19: What is the company's holiday calendar?
A19: The company observes 12 public holidays per year, including national holidays 
    and company-specific holidays. The holiday calendar is shared at the start of each year. 
    Working on a holiday is compensated with double pay or a compensatory off.

Q20: How do I report a workplace issue or harassment?
A20: Report any workplace issue to HR immediately. You can also use the anonymous 
    reporting system on the company intranet. All complaints are investigated confidentially. 
    The company has a zero-tolerance policy for harassment and discrimination.
"""

# Save documents
os.makedirs("data", exist_ok=True)

with open("data/company_policies.txt", "w", encoding="utf-8") as f:
    f.write(company_policies.strip())

with open("data/company_faqs.txt", "w", encoding="utf-8") as f:
    f.write(company_faqs.strip())

print("✅ Documents created successfully!")
print("   - data/company_policies.txt")
print("   - data/company_faqs.txt")