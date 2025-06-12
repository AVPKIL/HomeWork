from unittest.mock import patch, Mock
import pandas as pd
from src.pandas_utils import load_csv_transactions, load_excel_transactions


@patch('src.pandas_utils.pd.read_csv')
def test_load_csv_transactions_success(mock_read_csv):
    """Тест корректного CSV"""
    test_data = [{'id': 1, 'amount': 100}]
    mock_df = Mock()
    mock_df.to_dict.return_value = test_data
    mock_read_csv.return_value = mock_df

    result = load_csv_transactions('test.csv')
    assert result == test_data


@patch('src.pandas_utils.pd.read_csv')
def test_load_csv_transactions_failure(mock_read_csv):
    """Тест битого CSV"""
    mock_read_csv.side_effect = pd.errors.EmptyDataError("Error")
    result = load_csv_transactions('bad.csv')
    assert result == []


@patch('src.pandas_utils.pd.read_excel')
def test_load_excel_transactions_success(mock_read_excel):
    """Тест корректного Excel"""
    test_data = [{'id': 2, 'amount': 200}]
    mock_df = Mock()
    mock_df.to_dict.return_value = test_data
    mock_read_excel.return_value = mock_df

    result = load_excel_transactions('test.xlsx')
    assert result == test_data


@patch('src.pandas_utils.pd.read_excel')
def test_load_excel_transactions_failure(mock_read_excel):
    """Тест битого Excel"""
    mock_read_excel.side_effect = Exception("Error")
    result = load_excel_transactions('bad.xlsx')
    assert result == []
