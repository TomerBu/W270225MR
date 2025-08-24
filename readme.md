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
django-admin startproject שם_הפרויקט
cd שם_הפרויקט
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

## נוסיף לקובץ settings.py את שם האפליקציה
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'שם האפליקציה'
]
```


## נערוך את הקובץ views.py בתיקיה של האפליקציה
```bash
from django.http import HttpResponse

def all(request):
    return HttpResponse("all")

def me(request):
    return HttpResponse("me")
```

## ניצור קובץ חדש בשם urls.py בתיקיה של האפליקציה
```bash
from django.urls import path
from students.views import all, me

urlpatterns = [
    path('all/', all, name='all'),
    path('me/', me, name='me'),
]
```

## נערוך את הקובץ בשם urls.py בתיקיה של הפרוייקט הראשי
```bash
from django.contrib import admin
from django.urls import path, include
from students.urls import urlpatterns as students_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include(students_urls)),
]
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


---

## הקפאה ושחזור של ספריות (requirements)

### הקפאת הספריות לקובץ requirements.txt
כדי לשמור את כל הספריות המותקנות בסביבה הוירטואלית, השתמש בפקודה:
```bash
pip freeze > requirements.txt
```

### התקנת הספריות מסביבת requirements.txt
כדי לשחזר את כל הספריות בפרויקט חדש או במחשב אחר:
```bash
pip install -r requirements.txt
```