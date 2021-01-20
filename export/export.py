import pandas as pd

def to_excel(report_data, filename):
    """Exports data to Excel file"""
    df_report = pd.DataFrame.from_dict(report_data)
    df_report.to_excel(filename)
