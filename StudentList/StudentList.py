import pdfplumber
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

COLUMNS = [
    "SL.No.", "Candidate's Name", "Father's Name", "Mother's Name",
    "Section", "Roll", "Gender", "Group", "Shift", "Version",
    "Subjects", "Opt. Sub", "Pass Year", "Roll No",
    "Board", "RegNo"
]

def extract_students(text_lines):
    students = []
    current = []

    for line in text_lines:

        line = line.strip()
        if not line:
            continue

        # Start of new student (SL.No.)
        if line.isdigit() and len(line) <= 3:
            if current:
                students.append(current)
            current = [line]
            continue

        if current is not None:
            current.append(line)

    if current:
        students.append(current)

    return students


def parse_student(block):
    """
    Convert raw block into structured fields
    """

    try:
        # flatten all text into words
        words = []

        for b in block:
            words.extend(b.split())

        # Now manual mapping based on your structure
        data = []

        # SL.No
        data.append(words[0])

        # Name (take next 3 lines merged)
        data.append(" ".join(block[1].split()))
        data.append(" ".join(block[2].split()))
        data.append(" ".join(block[3].split()))

        # Remaining fixed fields
        remaining = words[4:]

        # Safe fill
        for i in range(len(COLUMNS) - 4):
            if i < len(remaining):
                data.append(remaining[i])
            else:
                data.append("")

        return data[:len(COLUMNS)]

    except:
        return None


def convert(pdf_path, excel_path):
    all_rows = []

    with pdfplumber.open(pdf_path) as pdf:
        full_text = []

        for page in pdf.pages:
            text = page.extract_text()
            if text:
                full_text.extend(text.split("\n"))

    students = extract_students(full_text)

    for s in students:
        row = parse_student(s)
        if row:
            all_rows.append(row)

    df = pd.DataFrame(all_rows, columns=COLUMNS)
    df.to_excel(excel_path, index=False)


def main():
    root = tk.Tk()
    root.withdraw()

    pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not pdf_path:
        return

    excel_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if not excel_path:
        return

    try:
        convert(pdf_path, excel_path)
        messagebox.showinfo("Success", "Converted Successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    main()