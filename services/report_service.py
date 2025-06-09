from strategy.csv_export_strategy import CSVExportStrategy
from strategy.pdf_export_strategy import PDFExportStrategy

class ReportService:
    def export(self, kind: str, rows, out_path="report.out"):
        if kind == "csv":
            strategy = CSVExportStrategy()
        elif kind == "pdf":
            strategy = PDFExportStrategy()
        else:
            raise ValueError("Unsupported export type")
        return strategy.export(rows, out_path)
