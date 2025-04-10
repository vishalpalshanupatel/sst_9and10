import csv
import os

# === SETTINGS ===
CLASSES_TO_ANALYZE = [
    "StringUtils",
    "ArrayUtils",
    "BooleanUtils",
    "SystemUtils",
    "RandomUtils",
    "CharSetUtils",
    "ClassUtils",
    "ObjectUtils",
    "Validate",
    "SerializationUtils"
]

INPUT_FILE = "lcom_results/TypeMetrics.csv"
OUTPUT_FILE = "lcom_results/CohesionComparison.csv"

def get_class_code(class_name):
    """Fetch source code for the specified class."""
    if class_name == "AllDisconnected":
        return """package lcom.testsubject;
public class AllDisconnected {
    public int f1, f2, f3;
    public void m1(){}
    public void m2(){}
    public void m3(){}
}"""

    search_paths = [
        f"src/main/java/org/apache/commons/lang3/{class_name}.java",
        f"src/java/org/apache/commons/lang3/{class_name}.java",
        f"org/apache/commons/lang3/{class_name}.java",
        f"{class_name}.java"
    ]

    for path in search_paths:
        try:
            with open(path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            continue

    return f"// Source code unavailable for {class_name}"

def generate_comparison_csv():
    """Extract metrics from CSV and write a formatted output CSV."""
    try:
        with open(INPUT_FILE, 'r') as file:
            sample = file.read(1024)
            file.seek(0)

            dialect = csv.Sniffer().sniff(sample)
            has_header = csv.Sniffer().has_header(sample)

            if not has_header:
                print("Error: Input CSV is missing headers.")
                return

            reader = csv.DictReader(file, dialect=dialect)
            columns = reader.fieldnames

            class_column = next((col for col in ['Type Name', 'Type', 'Class', 'ClassName', 'Name'] if col in columns), None)
            if not class_column:
                print("Error: Could not find class name column.")
                print("Found columns:", columns)
                return

            class_data = {
                row[class_column]: row
                for row in reader if row[class_column] in CLASSES_TO_ANALYZE
            }

    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(['Class Name', 'Java Code', 'LCOM1', 'LCOM2', 'LCOM3', 'LCOM4', 'LCOM5', 'YALCOM'])

        for class_name in CLASSES_TO_ANALYZE:
            code = get_class_code(class_name)

            if class_name in class_data:
                data = class_data[class_name]
                writer.writerow([
                    class_name,
                    code,
                    data.get('LCOM1', data.get('LCOM', 'N/A')),
                    data.get('LCOM2', 'N/A'),
                    data.get('LCOM3', 'N/A'),
                    data.get('LCOM4', 'N/A'),
                    data.get('LCOM5', 'N/A'),
                    data.get('YALCOM', 'N/A')
                ])
            else:
                print(f"Note: Metrics not found for class '{class_name}'.")
                writer.writerow([class_name, code, 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'])

    print(f"\nExport completed. {len(CLASSES_TO_ANALYZE)} classes written to:")
    print(OUTPUT_FILE)

if __name__ == "__main__":
    generate_comparison_csv()
