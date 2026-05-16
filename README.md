# Blog-plateform-project

## Project Overview
* BlogSphere is a full-stack blogging web application built using **Python Flask, SQLite, HTML, CSS, and JavaScript**.
* It allows users to register, log in securely, create and publish blog posts, edit posts, comment on articles, and like posts. The platform includes a responsive modern interface, dark mode support, user profile management, and category-based blog publishing.
* This project demonstrates full-stack web development concepts including authentication, CRUD operations, database integration, session management, and responsive UI design.

## Features
### User Authentication
* User registration
* Secure login system
* Password hashing
* Session management
* Logout functionality
### Blog Post Management
* Create blog posts
* Edit published posts
* View all posts
* Category-based publishing
### Comment System
* Add comments to posts
* View comments under each article
### Like System
* Like blog posts
* Track engagement
### User Profile
* View user profile
* View published posts
### UI Features
* Responsive design
* Dark mode
* Modern interface
  
## Technologies Used
### Frontend
* HTML
* CSS
* JavaScript
### Backend
* Python Flask
### Database
* SQLite

## Project Structure
blog-platform/
│
├── app.py
├── config.py
├── requirements.txt
├── database.sql
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create_post.html
│   ├── edit_post.html
│   ├── view_post.html
│   └── profile.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
    ├── login-page.png
    ├── register-page.png
    ├── dashboard-page.png
    ├── create-post-page.png
    ├── create-post-page..png
    ├── view-post-page.png
    ├── dark-mode-page.p.png
    └── dark-mode-page.png

## Installation
### Clone Repository
git clone <repository-link>
cd blog-platform
### Install Dependencies
pip install -r requirements.txt
### Run Application
python app.py
## Open in Browser
http://127.0.0.1:5000

## Database Tables
* Users
* Posts
* Comments
* Likes
## Learning Outcomes
This project helps in learning:
* Flask routing
* Authentication system
* CRUD operations
* SQLite database integration
* Template rendering
* Responsive web design
* Full-stack application development
* 
## Future Enhancements
* Bookmark system
* Search functionality
* Image upload
* Admin panel
* Notifications
* 
## Author
Developed as a full-stack web development project using Flask and SQLite.
