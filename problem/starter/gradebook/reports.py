"""gradebook.reports — build a printable report from grade records."""
from .stats import (
    average_per_student,
    subjects_offered,
    top_scorer,
    passing_students,
)
def format_report(records: list[dict]) -> str:
    report_lines = []
    report_lines.append(f"Total records: {len(records)}")
    subjects = sorted(list(subjects_offered(records)))
    report_lines.append(f"Subjects offered: {', '.join(subjects)}")
    report_lines.append("Average scores per student:")
    avg_scores = average_per_student(records)
    for student_name in sorted(avg_scores.keys()):
        report_lines.append(f"  {student_name}: {avg_scores[student_name]:.2f}")
    top_student_name, top_student_score = top_scorer(records)
    report_lines.append(f"Top scorer: {top_student_name} ({top_student_score:.2f})")
    passing = passing_students(records)
    report_lines.append(
        f"Passing students (threshold 60.0): {', '.join(passing) if passing else 'None'}"
    )
    return "\n".join(report_lines)