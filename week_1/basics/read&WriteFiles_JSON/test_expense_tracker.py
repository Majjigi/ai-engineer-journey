import importlib.util
from pathlib import Path


def load_module():
    module_path = Path(__file__).with_name("read&WriteFile.py")
    spec = importlib.util.spec_from_file_location("expense_tracker", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_expense_functions_exist():
    module = load_module()
    assert hasattr(module, "load_expenses")
    assert hasattr(module, "add_expense")
    assert hasattr(module, "delete_expense")
    assert hasattr(module, "show_total")
