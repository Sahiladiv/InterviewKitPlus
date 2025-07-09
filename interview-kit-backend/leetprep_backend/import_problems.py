import csv
import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leetprep_backend.settings")  # Replace with your actual project name
django.setup()

from problems.models import Problem  # Replace 'your_app' with the actual app name

def import_problems_from_csv(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            problem, created = Problem.objects.get_or_create(
                title=row['Title'].strip(),
                defaults={
                    'description': row['Description'].strip(),
                    'difficulty': row['Difficulty'].strip(),
                    'category': row['Category'].strip(),
                    'input_format': row['Input'].strip(),
                    'output_format': row['Output'].strip(),
                    'example_input': row['Example Input'].strip(),
                    'example_output': row['Example Output'].strip(),
                }
            )
            if created:
                count += 1
                print(f"[+] Added: {problem.title}")
            else:
                print(f"[-] Skipped (already exists): {problem.title}")
        print(f"\n✅ Total new problems added: {count}")

if __name__ == '__main__':
    csv_file_path = 'algorithm_questions_dataset.csv'  # Update path if needed
    import_problems_from_csv(csv_file_path)
