import pytest
from unittest.mock import MagicMock
from services.report_service import ReportService


def test_export_unknown_type():
    service = ReportService()
    with pytest.raises(ValueError):
        service.export("txt", [])


def test_export_csv_uses_strategy(monkeypatch):
    service = ReportService()
    mock = MagicMock()
    monkeypatch.setattr("services.report_service.CSVExportStrategy", lambda: mock)
    service.export("csv", [{"x": 1}], "out.csv")
    mock.export.assert_called_once()
