# План очищення проекту

## 📦 Файли/папки ДЛЯ ВИДАЛЕННЯ (старий Tkinter код)

### UI (Tkinter - більше не потрібен)
- [ ] `ui/` - весь каталог з Tkinter інтерфейсом
  - component_tab.py
  - main_window.py
  - orders_tab.py
  - reports_tab.py
  - storekeeper_tab.py
  - supplier_tab.py
  - supplier_window.py
  - suppliers_tab.py
  - supply_tab.py
  - warehouse_tab.py
  - warehouse_window.py

### Controllers (старі - тепер в backend/app/api/)
- [ ] `controllers/` - весь каталог
  - component_controller.py
  - orders_controller.py
  - report_controller.py
  - storekeeper_controller.py
  - supplier_controller.py
  - supply_controller.py
  - warehouse_controller.py

### Старі модулі в корені (дублікати - тепер в backend/app/)
- [ ] `models/` - перенесено в backend/app/models/
- [ ] `services/` - перенесено в backend/app/services/
- [ ] `dao/` - перенесено в backend/app/dao/

### Інші старі файли
- [ ] `main.py` - старий Tkinter entry point
- [ ] `logging_config.py` - якщо не використовується
- [ ] `contextcodex.md` - схоже видалено
- [ ] `code_listing.md` - застарілий лістинг

### Builder/Strategy (якщо не використовуються в API)
- [ ] `builder/` - перевірити чи використовується
- [ ] `strategy/` - перевірити чи використовується

### Тести старого коду
- [ ] `tests/controller/` - тести старих контролерів
- [ ] `tests/service/` - можливо залишити
- [ ] `tests/dao/` - можливо залишити

---

## ✅ Файли/папки ДЛЯ ЗБЕРЕЖЕННЯ

### Новий веб-додаток
- ✅ `backend/` - FastAPI backend
- ✅ `frontend/` - React frontend
- ✅ `db/` - база даних (спільна)

### Документація
- ✅ `README_WEB.md` - головна документація
- ✅ `QUICK_START.md` - швидкий старт
- ✅ `WEB_MIGRATION_GUIDE.md` - посібник з міграції
- ✅ `.claude/` - Claude Code конфігурація
- ✅ `specs/` - специфікації (якщо є)

### Git
- ✅ `.git/`
- ✅ `.gitignore`

---

## 🎯 Рекомендації

1. **Створити архів старого коду** перед видаленням (на всяк випадок)
2. **Видалити старі файли** поетапно
3. **Перевірити чи все працює** після кожного видалення
4. **Оновити .gitignore** для нової структури

---

## 📊 Нова структура проекту (після очищення)

```
kr1/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── core/        # Config, auth
│   │   ├── models/      # Data models
│   │   ├── services/    # Business logic
│   │   ├── dao/         # Database access
│   │   ├── db/          # Database
│   │   └── main.py
│   ├── venv/
│   ├── requirements.txt
│   └── run.py
│
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── ...
│   ├── node_modules/
│   ├── package.json
│   └── ...
│
├── db/                  # Спільна база даних
│   └── supply.db
│
├── .claude/             # Claude Code config
├── specs/               # Документація
├── README_WEB.md
├── QUICK_START.md
└── WEB_MIGRATION_GUIDE.md
```

Набагато чистіше! 🎉
