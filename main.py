import os

print("Current folder:", os.getcwd())
print("CSV exists:", os.path.exists("students.csv"))
from student_analyzer import StudentAnalyzer


def main():
    analyzer = StudentAnalyzer("students.csv")

    analyzer.load_data()
    analyzer.display_results()
    analyzer.find_topper()
    analyzer.show_high_performers(threshold=80)
    analyzer.save_report()


if __name__ == "__main__":
    main()