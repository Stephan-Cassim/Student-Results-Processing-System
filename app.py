from flask import Flask, render_template, request

app = Flask(__name__)

students = []

def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 65:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

@app.route("/", methods=["GET", "POST"])
def index():
    global students

    if request.method == "POST":
        name = request.form["name"]
        m1 = int(request.form["course1"])
        m2 = int(request.form["course2"])
        m3 = int(request.form["course3"])

        average = round((m1 + m2 + m3) / 3, 2)
        grade = calculate_grade(average)

        students.append({
            "name": name,
            "marks": [m1, m2, m3],
            "average": average,
            "grade": grade
        })

    return render_template("index.html", students=students)

@app.route("/results")
def results():
    top_student = max(students, key=lambda s: s["average"]) if students else None
    return render_template("results.html", students=students, top_student=top_student)

if __name__ == "__main__":
    app.run(debug=True)
