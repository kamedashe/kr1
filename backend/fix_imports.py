"""Fix imports in copied files."""
import os
import re

def fix_imports_in_file(filepath, patterns):
    """Fix imports in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    for old_pattern, new_pattern in patterns:
        content = re.sub(old_pattern, new_pattern, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed: {filepath}")
        return True
    return False

def fix_services():
    """Fix imports in services directory."""
    patterns = [
        (r'^from dao\.', 'from ..dao.', re.MULTILINE),
        (r'^from models\.', 'from ..models.', re.MULTILINE),
    ]

    services_dir = 'app/services'
    for filename in os.listdir(services_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(services_dir, filename)
            try:
                for old, new, flags in patterns:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = re.sub(old, new, content, flags=flags)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                print(f"Fixed: {filepath}")
            except Exception as e:
                print(f"Error fixing {filepath}: {e}")

def fix_dao():
    """Fix imports in dao directory."""
    patterns = [
        (r'^from models\.', 'from ..models.', re.MULTILINE),
        (r'^from db\.database', 'from ..db.database', re.MULTILINE),
    ]

    dao_dir = 'app/dao'
    for filename in os.listdir(dao_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            filepath = os.path.join(dao_dir, filename)
            try:
                for old, new, flags in patterns:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    content = re.sub(old, new, content, flags=flags)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                print(f"Fixed: {filepath}")
            except Exception as e:
                print(f"Error fixing {filepath}: {e}")

if __name__ == '__main__':
    print("Fixing imports...")
    fix_services()
    fix_dao()
    print("Done!")
