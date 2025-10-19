"""Fix all imports in backend app."""
import os
import re

def fix_file(filepath, replacements):
    """Fix imports in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for old, new in replacements:
            content = re.sub(old, new, content, flags=re.MULTILINE)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[OK] Fixed: {filepath}")
            return True
        return False
    except Exception as e:
        print(f"[ERROR] in {filepath}: {e}")
        return False

def fix_all():
    """Fix all imports."""
    # DAO files - fix base_dao imports
    dao_replacements = [
        (r'^from dao\.base_dao import', 'from .base_dao import'),
        (r'^from dao\.', 'from .'),
        (r'^from models\.', 'from ..models.'),
        (r'^from db\.database', 'from ..db.database'),
    ]

    dao_dir = 'app/dao'
    if os.path.exists(dao_dir):
        print("\n=== Fixing DAO files ===")
        for filename in os.listdir(dao_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                fix_file(os.path.join(dao_dir, filename), dao_replacements)

    # Services files
    services_replacements = [
        (r'^from dao\.', 'from ..dao.'),
        (r'^from models\.', 'from ..models.'),
        (r'^from services\.', 'from .'),
    ]

    services_dir = 'app/services'
    if os.path.exists(services_dir):
        print("\n=== Fixing Services files ===")
        for filename in os.listdir(services_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                fix_file(os.path.join(services_dir, filename), services_replacements)

if __name__ == '__main__':
    print("Fixing all imports in backend app...")
    fix_all()
    print("\n[DONE] All imports fixed!")
