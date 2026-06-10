from flask import Flask, render_template, request, redirect, flash
from database import (get_all_appointments, insert_appointment,update_appointment, delete_appointment, get_appointment_by_id, search_appointments)


app = Flask(__name__)
app.secret_key = "secret-key"

@app.route("/")
def home():
    appointments = get_all_appointments()
    return render_template("index.html", appointments=appointments)


@app.route("/create", methods= ["GET", "POST"])
def create():
    if request.method == "POST":
        name = request.form["name"]
        mobile = request.form["mobile"]
        service = request.form["service"]
        time = request.form["time"]

        insert_appointment(name, mobile, service, time)
        flash("Appointment create successfully" , "success")

        return redirect("/")
    return render_template("create.html")


@app.route("/delete/<int:id>")
def delete(id):
    delete_appointment(id)
    flash("Appointment deleted 🗑", "danger")

    return redirect("/")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        name = request.form["name"]
        mobile = request.form["mobile"]
        service = request.form["service"]
        time = request.form["time"]

        update_appointment(id, name, mobile, service, time)
        flash("Appointment updated ✏️", "info")
        return redirect("/")

    appointment = get_appointment_by_id(id)
    return render_template("edit.html", appointment = appointment)


@app.route("/search")
def search():
    keyword = request.args.get("q")
    if keyword:
        appoinitments = search_appointments(keyword)
    else:
        appoinitments = get_all_appointments()

    return render_template("index.html", appoinitments = appoinitments)


if __name__ == "__main__":
   app.run(debug=True)

