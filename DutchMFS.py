!pip install pdfplumber pandas openpyxl


import os
import pdfplumber
import pandas as pd

input_pdf = r"C:\Users\Admin\Downloads\inputDutchMFS.pdf"
output_folder = r"C:\Users\Admin\Downloads"

def process_pdf(input_path, output_folder):
    try:
        output_rows = []

        with pdfplumber.open(input_path) as pdf:
            total_pages = len(pdf.pages)
            print(f"📄 Total Pages Found: {total_pages}")

            for page_num, page in enumerate(pdf.pages, start=1):
                try:
                    table = page.extract_table()
                    if not table:
                        continue
                    
                    for row in table:
                        if not row or "Dutch-Bangla Bank Limited" in row[0] or "Page" in row[0] or "End of Report" in row[0]:
                            continue
                        row = [cell.replace("\n", "").strip() if cell else "" for cell in row]
                        if len(row) >= 11:
                            output_rows.append(row[:11])

                except Exception as page_err:
                    print(f"Error processing page {page_num}: {page_err}")
                    continue

        if not output_rows:
            print("No valid data found in the PDF.")
            return None
        columns = [
            "SL", "Date", "Time", "Txn ID", "Br. Code",
            "Txn Type", "Ref Number/Bill No",
            "Initiator A/C", "A/C Title",
            "Txn Amount", "Fee Amount"
        ]

        df = pd.DataFrame(output_rows, columns=columns)
        input_name = os.path.splitext(os.path.basename(input_path))[0]
        output_filename = f"{input_name}_output.xlsx"
        save_path = os.path.join(output_folder, output_filename)

        df.to_excel(save_path, index=False)
        print(f"File saved at: {save_path}")

        return df

    except Exception as e:
        print(f"Error: {e}")
        return None
