from typing import List, Dict, Any
import pandas as pd


def load_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла."""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict('records')
    except Exception:
        return []


def load_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из Excel-файла."""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict('records')
    except Exception:
        return []
