#!/usr/bin/env python3
"""
Генератор лістингу коду проекту
"""
import os
from pathlib import Path

# Директорії, які треба ігнорувати
IGNORE_DIRS = {
    'node_modules', '__pycache__', '.git', 'venv', 'env',
    'dist', 'build', '.pytest_cache', '.claude', 'specs'
}

# Розширення файлів, які включаємо
INCLUDE_EXTENSIONS = {
    '.py', '.jsx', '.js', '.json', '.md', '.txt',
    '.html', '.css', '.yml', '.yaml', '.toml', '.ini'
}

# Файли, які треба виключити
EXCLUDE_FILES = {
    'package-lock.json', '.gitignore', 'code_listing.md',
    'generate_code_listing.py'
}

def should_include(path: Path) -> bool:
    """Перевіряє, чи треба включати файл"""
    # Ігноруємо приховані файли
    if path.name.startswith('.') and path.name != '.gitignore':
        return False

    # Перевіряємо розширення
    if path.suffix not in INCLUDE_EXTENSIONS:
        return False

    # Виключаємо конкретні файли
    if path.name in EXCLUDE_FILES:
        return False

    # Перевіряємо шлях на наявність ігнорованих директорій
    for part in path.parts:
        if part in IGNORE_DIRS:
            return False

    return True

def get_file_category(path: Path) -> str:
    """Визначає категорію файлу"""
    path_str = str(path)

    if 'backend' in path_str:
        if 'api' in path_str:
            return 'Backend - API'
        elif 'dao' in path_str:
            return 'Backend - DAO'
        elif 'services' in path_str:
            return 'Backend - Services'
        elif 'models' in path_str:
            return 'Backend - Models'
        elif 'core' in path_str:
            return 'Backend - Core'
        elif 'db' in path_str:
            return 'Backend - Database'
        else:
            return 'Backend - Config'
    elif 'frontend' in path_str:
        if 'components' in path_str:
            return 'Frontend - Components'
        elif 'pages' in path_str:
            return 'Frontend - Pages'
        elif 'services' in path_str:
            return 'Frontend - Services'
        elif 'hooks' in path_str:
            return 'Frontend - Hooks'
        else:
            return 'Frontend - Config'
    elif 'tests' in path_str:
        return 'Tests'
    elif path.suffix == '.md':
        return 'Documentation'
    else:
        return 'Root'

def collect_files(root_dir: Path) -> dict:
    """Збирає файли по категоріях"""
    files_by_category = {}

    for file_path in root_dir.rglob('*'):
        if file_path.is_file() and should_include(file_path):
            relative_path = file_path.relative_to(root_dir)
            category = get_file_category(relative_path)

            if category not in files_by_category:
                files_by_category[category] = []

            files_by_category[category].append(relative_path)

    # Сортуємо файли в кожній категорії
    for category in files_by_category:
        files_by_category[category].sort()

    return files_by_category

def generate_listing(root_dir: Path, output_file: Path):
    """Генерує лістинг коду"""
    files_by_category = collect_files(root_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Лістинг коду проекту КР1\n\n")
        f.write("## Структура проекту\n\n")
        f.write("Веб-додаток для управління поставками комплектуючих\n")
        f.write("- **Backend**: FastAPI + SQLite\n")
        f.write("- **Frontend**: React + Vite + Tailwind CSS\n\n")

        # Категорії у порядку важливості
        category_order = [
            'Documentation',
            'Root',
            'Backend - Config',
            'Backend - Core',
            'Backend - Database',
            'Backend - Models',
            'Backend - DAO',
            'Backend - Services',
            'Backend - API',
            'Frontend - Config',
            'Frontend - Services',
            'Frontend - Hooks',
            'Frontend - Pages',
            'Frontend - Components',
            'Tests',
        ]

        # Виводимо зміст
        f.write("## Зміст\n\n")
        for category in category_order:
            if category in files_by_category:
                file_count = len(files_by_category[category])
                f.write(f"- [{category}](#{''.join(category.lower().split())}) ({file_count} файлів)\n")
        f.write("\n---\n\n")

        # Виводимо файли по категоріях
        for category in category_order:
            if category not in files_by_category:
                continue

            f.write(f"## {category}\n\n")

            for file_path in files_by_category[category]:
                f.write(f"### `{file_path}`\n\n")

                # Читаємо та виводимо вміст файлу
                full_path = root_dir / file_path
                try:
                    with open(full_path, 'r', encoding='utf-8') as file_content:
                        content = file_content.read()

                        # Визначаємо синтаксис для підсвітки
                        extension = file_path.suffix
                        syntax_map = {
                            '.py': 'python',
                            '.js': 'javascript',
                            '.jsx': 'jsx',
                            '.json': 'json',
                            '.md': 'markdown',
                            '.html': 'html',
                            '.css': 'css',
                            '.yml': 'yaml',
                            '.yaml': 'yaml',
                            '.txt': 'text',
                            '.toml': 'toml',
                            '.ini': 'ini',
                        }
                        syntax = syntax_map.get(extension, 'text')

                        f.write(f"```{syntax}\n")
                        f.write(content)
                        if not content.endswith('\n'):
                            f.write('\n')
                        f.write("```\n\n")
                except Exception as e:
                    f.write(f"*Помилка читання файлу: {e}*\n\n")

            f.write("---\n\n")

        # Статистика
        total_files = sum(len(files) for files in files_by_category.values())
        f.write(f"## Статистика\n\n")
        f.write(f"**Всього файлів**: {total_files}\n\n")
        f.write("### Файлів по категоріях:\n\n")
        for category in category_order:
            if category in files_by_category:
                count = len(files_by_category[category])
                f.write(f"- **{category}**: {count}\n")

if __name__ == '__main__':
    root = Path(__file__).parent
    output = root / 'code_listing.md'

    print(f"Генерація лістингу коду...")
    print(f"Корінь проекту: {root}")
    print(f"Вихідний файл: {output}")

    generate_listing(root, output)

    print(f"\nListing created: {output}")
    print(f"Size: {output.stat().st_size / 1024:.1f} KB")
