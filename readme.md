<hr>

# מדריך הקמת פרויקט Django חדש

## התקנה ראשונית (פעם אחת במחשב)

### 1. התקנת Django גלובלית
```bash
pip install django
```

או עם pip3 אם יש לך Mac:
```bash
pip3 install django
```

### 2. וידוא שההתקנה הצליחה
```bash
django-admin --version
```

---

## יצירת פרויקט חדש (לכל פרויקט)

### 1. יצירת הפרויקט
```bash
django-admin startproject שם_הפרויקט
cd שם_הפרויקט
```

**דוגמה:**
```bash
django-admin startproject my_blog
cd my_blog
```

### 2. יצירת סביבה וירטואלית (venv)
```bash
python -m venv myenv
```

או עם מאק:
```bash
python3 -m venv myenv
```

### 3. הפעלת הסביבה הוירטואלית

**ב-Windows:**
```bash
myenv\Scripts\activate
```

**ב-macOS/Linux:**
```bash
source myenv/bin/activate
```

### 4. התקנת Django בסביבה הוירטואלית
```bash
pip install django
```

### 5. הרצת השרת לבדיקה
```bash
python manage.py runserver
```

פתח את הדפדפן בכתובת: http://127.0.0.1:8000

---

## מבנה הפרויקט שנוצר
```
שם_הפרויקט/
├── manage.py
├── שם_הפרויקט/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── myenv/
```

---

## פקודות שימושיות

### יצירת אפליקציה חדשה
```bash
python manage.py startapp שם_האפליקציה
```

### הרצת מיגרציות
```bash
python manage.py makemigrations
python manage.py migrate
```

### יצירת משתמש מנהל
```bash
python manage.py createsuperuser
```

### כיבוי הסביבה הוירטואלית
```bash
deactivate
```

---

## טיפים חשובים

1. **תמיד הקפד להפעיל את הסביבה הוירטואלית** לפני עבודה על הפרויקט
2. **שמור את הדרישות** בקובץ requirements.txt:
   ```bash
   pip freeze > requirements.txt
   ```
3. **התקנת דרישות** מקובץ requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
4. **הוסף את תיקיית myenv ל-.gitignore** כדי לא להעלות אותה ל-Git

---

## דוגמה מלאה
```bash
# יצירת פרויקט חדש
django-admin startproject blog_project
cd blog_project

# יצירת סביבה וירטואלית
python -m venv myenv

# הפעלת הסביבה (Windows)
myenv\Scripts\activate

# התקנת Django
pip install django

# הרצת השרת
python manage.py runserver
```