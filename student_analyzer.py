import csv


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @property
    def total(self):
        return sum(self.marks)

    @property
    def percentage(self):
        return self.total / len(self.marks)

    @property
    def result(self):
        if all(mark >= 40 for mark in self.marks):
            return "Pass"
        return "Fail"


class StudentAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load_data(self):
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    name = row["name"]
                    marks = [
                        float(row["python"]),
                        float(row["math"]),
                        float(row["computer_science"])
                    ]

                    if not all(0 <= mark <= 100 for mark in marks):
                        raise ValueError(
                            f"Invalid marks found for {name}"
                        )

                    student = Student(name, marks)
                    self.students.append(student)

        except FileNotFoundError:
            print("Error: Student data file not found.")

        except (ValueError, KeyError) as error:
            self.students.clear()
            print(f"Error: Invalid student data: {error}")

    def display_results(self):
        if not self.students:
            print("No student records available.")
            return

        print("\nSTUDENT PERFORMANCE REPORT")
        print("-" * 65)
        print(
            f"{'Name':<12}{'Total':<10}"
            f"{'Percentage':<15}{'Result':<10}"
        )
        print("-" * 65)

        for student in self.students:
            print(
                f"{student.name:<12}"
                f"{student.total:<10.1f}"
                f"{student.percentage:<15.2f}"
                f"{student.result:<10}"
            )

    def find_topper(self):
        if not self.students:
            print("No student records available.")
            return

        topper = max(
            self.students,
            key=lambda student: student.percentage
        )

        print(
            f"\nTopper: {topper.name} "
            f"({topper.percentage:.2f}%)"
        )

    def show_high_performers(self, threshold=80):
        print(f"\nStudents scoring at least {threshold}%:")

        found = False

        for student in self.students:
            if student.percentage >= threshold:
                print(
                    f"{student.name}: "
                    f"{student.percentage:.2f}%"
                )
                found = True

        if not found:
            print("No students meet this threshold.")

    def save_report(self, output_file="report.csv"):
        try:
            with open(
                output_file, "w", newline=""
            ) as file:
                fieldnames = [
                    "name",
                    "total",
                    "percentage",
                    "result"
                ]

                writer = csv.DictWriter(
                    file, fieldnames=fieldnames
                )

                writer.writeheader()

                for student in self.students:
                    writer.writerow({
                        "name": student.name,
                        "total": student.total,
                        "percentage": round(
                            student.percentage, 2
                        ),
                        "result": student.result
                    })

            print(f"\nReport saved to {output_file}")

        except OSError as error:
            print(f"Could not save report: {error}")