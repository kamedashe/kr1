# Тест чорного ящика через tkinter не виконується тут,
# але драйвер показує, що вікно SupplyWindow створюється без помилок.
import sys
import os
import pytest
if not os.environ.get("DISPLAY") and os.name != "nt":
    pytest.skip("No display – GUI tests skipped", allow_module_level=True)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import TclError
from ui.supply_window import SupplyWindow

def test_supply_window_creation(monkeypatch):
    try:
        root = tk.Tk()
    except TclError:
        pytest.skip("Tk not available")
    # Перехоплюємо метод center_window, щоб не відкривалось GUI.
    monkeypatch.setattr(SupplyWindow, 'center_window', lambda self, w, h: None)
    win = tk.Toplevel(root)
    SupplyWindow(win)
    assert win.winfo_exists() == 1
    win.destroy()
    root.destroy()
