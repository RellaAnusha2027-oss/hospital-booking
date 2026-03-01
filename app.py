from flask import Flask, render_template, request

app = Flask(__name__)

# Doctor data based on department
doctor_data = {
    "Cardiology": ["Dr. Sharma", "Dr. Reddy"],
    "Neurology": ["Dr. Mehta", "Dr. Priya"],
    "Orthopedics": ["Dr. Kumar", "Dr. Singh"],
    "physician":["Dr.rupa","Dr.siri"],
    "opthalmologist":["Dr.sandeep","Dr.nandu"],
    "General": ["Dr. Rao", "Dr. Anjali"]
}


# Home Page
@app.route("/")
def home():
    return render_template("form.html")


# Show doctors based on department
@app.route("/doctors", methods=["POST"])
def doctors():
    name = request.form["name"]
    department = request.form["department"]

    doctors_list = doctor_data.get(department, [])

    return render_template("doctors.html",
                           name=name,
                           department=department,
                           doctors=doctors_list)


# Appointment confirmation
@app.route("/appointment", methods=["POST"])
def appointment():
    selected_doctor = request.form["doctor"]
    date = request.form["date"]
    time = request.form["time"]

    # Save appointment in file
    with open("appointments.txt", "a") as file:
        file.write(f"Doctor: {selected_doctor}, Date: {date}, Time: {time}\n")

    return render_template("appointment.html",
                           doctor=selected_doctor,
                           date=date,
                           time=time)


if __name__ == "__main__":
    app.run(debug=True)