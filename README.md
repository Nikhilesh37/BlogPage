DJANGO BLOG PAGE

This is a blog application built with Django. It features a clean, responsive design that works well on mobile devices, tablets, and desktop computers. You can use it to publish posts, manage tags, and interact with readers through comments.

FEATURES

- Responsive Design: Fits any screen size, from mobile phones to large monitors.
- Blog Management: Easily create, edit, and delete posts using the Django Admin panel.
- Comments: Readers can leave comments on your posts.
- Read Later: Users can bookmark posts to read them later.
- API Support: Includes a REST API to fetch blog posts programmatically.
- Optimization: Uses database indexing and caching for better performance.

GETTING STARTED

Here is how you can set up the project on your local machine.

Prerequisites

You will need Python 3.8 or higher installed.

Installation

1. Clone the repository
   git clone https://github.com/Nikhilesh37/Django-BlogPage.git
   cd Django-BlogPage

2. Set up a virtual environment
   
   On Windows:
   python -m venv venv
   venv\Scripts\activate
   
   On macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Prepare the database
   Run the migrations to set up your database tables.
   python manage.py makemigrations
   python manage.py migrate

5. Create an Admin user
   You need an admin account to log in and create blog posts.
   python manage.py createsuperuser

6. Run the server
   python manage.py runserver

   You can now view the site at http://127.0.0.1:8000/
   To manage posts, go to http://127.0.0.1:8000/admin/

API ENDPOINTS

We have added a REST API if you want to consume the blog data from another application (like a mobile app).

- List all posts: GET /api/posts/
- Get a single post: GET /api/posts/<slug>/

PRODUCTION CONFIGURATION

If you are deploying this to a production environment, you should use PostgreSQL and Redis instead of the default SQLite.

Set these environment variables in your production environment:

- DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT (for PostgreSQL)
- REDIS_URL (for Caching)
- SECRET_KEY (Generates a secure key for Django)
- DEBUG (Set to False)

If you don't feature these variables, the app will automatically fall back to using SQLite and local memory, which is fine for development.

PROJECT STRUCTURE

- blog/: Contains the main logic, views, models, and API endpoints.
- webpage1/: The main project configuration (settings.py, urls.py).
- templates/: HTML files for the layout.
- static/: CSS and images.
- uploads/: Where user-uploaded images are stored.

USAGE

To add a new post, go to the Admin panel. You can upload images, set tags, and assign an author. The "Read Later" feature uses sessions, so it works per browser.

If you find any bugs, feel free to open an issue on the GitHub repository.

Happy coding!
