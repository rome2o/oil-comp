import pandas as pd
import os

def load_and_process_data():
    dataframes = {}

    # Ahrefs CSVs
    ahrefs_path = "/Users/ali/Sites/business/oil-company/seo/ahrefs/"
    ahrefs_csv_files = [
        "hbnobulk.com-backlinks-subdomains_2025-10-22_19-38-16.csv",
        "hbnobulk.com-organic-keywords-subdomains-al_2025-10-22_19-38-50.csv"
    ]
    for file in ahrefs_csv_files:
        try:
            df = pd.read_csv(os.path.join(ahrefs_path, file), encoding='latin1', sep=r'\s+')
            dataframes[file.replace(".csv", "")] = df
            print(f"Successfully loaded {file} with whitespace delimiter.")
        except Exception as e:
            print(f"Error loading {file} with whitespace delimiter: {e}")
            print(f"Failed to load {file} after trying whitespace delimiter.")

    # Google Analytics XLSX
    ga_path = "/Users/ali/Sites/business/oil-company/seo/google_analytics/"
    ga_xlsx_files = [
        "Pages and screens_ Page path and screen class.xlsx",
        "Traffic acquisition_ Session primary channel group (Default Channel Group).xlsx"
    ]
    for file in ga_xlsx_files:
        try:
            df = pd.read_excel(os.path.join(ga_path, file))
            dataframes[file.replace(".xlsx", "")] = df
            print(f"Successfully loaded {file}")
        except Exception as e:
            print(f"Error loading {file}: {e}")

    # Google Search Console XLSX
    gsc_path = "/Users/ali/Sites/business/oil-company/seo/google_search_console/"
    gsc_xlsx_files = [
        "https___hbno.com_-core-web-vitals-2025-10-22 (1).xlsx",
        "https___hbno.com_-core-web-vitals-2025-10-22.xlsx",
        "https___hbno.com_-Performance-on-Search-2025-10-22.xlsx"
    ]
    for file in gsc_xlsx_files:
        try:
            df = pd.read_excel(os.path.join(gsc_path, file))
            dataframes[file.replace(".xlsx", "")] = df
            print(f"Successfully loaded {file}")
        except Exception as e:
            print(f"Error loading {file}: {e}")

    # Note for PDF files: Manual review or external OCR/PDF parsing tool required.
    print("\nPDF files (Ahrefs Overviews) require manual review or specialized tools for data extraction.")

    return dataframes

if __name__ == "__main__":
    processed_data = load_and_process_data()
    print(f"\nLoaded {len(processed_data)} dataframes.")
    # You can now access individual dataframes, e.g., processed_data["hbnobulk.com-backlinks-subdomains_2025-10-22_19-38-16"]
    # Further processing and analysis would go here.
