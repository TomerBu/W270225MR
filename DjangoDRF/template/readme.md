# Create the project directory
mkdir lec4
cd lec4

code .

# Create a virtual environment to isolate our package dependencies locally
# mac <br>
`python3 -m venv .venv`
`source .venv/bin/activate` 
 # Windows
 `.venv\Scripts\activate`

# Install Django and Django REST framework into the virtual environment
pip install djangorestframework

# Set up a new project with a single application
django-admin startproject lec4 .    # Note the trailing '.' character
 
django-admin startapp api