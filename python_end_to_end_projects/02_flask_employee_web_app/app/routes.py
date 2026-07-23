from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint("main", __name__)

employees = [
    {"id": 1, "name": "Anita", "department": "Engineering", "location": "Hyderabad"},
    {"id": 2, "name": "Rahul", "department": "Finance", "location": "Bengaluru"},
    {"id": 3, "name": "Meera", "department": "HR", "location": "Pune"},
]

@main.route("/")
def home():
    return render_template("index.html", employees=employees)

@main.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        department = request.form.get("department", "").strip()
        location = request.form.get("location", "").strip()

        if name and department and location:
            next_id = max((employee["id"] for employee in employees), default=0) + 1
            employees.append({
                "id": next_id,
                "name": name,
                "department": department,
                "location": location
            })
            return redirect(url_for("main.home"))

    return render_template("add_employee.html")

@main.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):
    employee = next((item for item in employees if item["id"] == employee_id), None)
    if employee:
        employees.remove(employee)
    return redirect(url_for("main.home"))
