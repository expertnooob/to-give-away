
---

# **ToGiveAway**

ToGiveAway is a Django-based web application that allows users to give away unused items for free to others. The platform is designed to promote sustainability by encouraging people to share items they no longer need rather than discarding them.

At first, it is specifically developed for students who come to the Capital of Nepal(Kathmandu) from rural parts of the country for education, work, or other opportunities. It could be immensely helpful for them to access items like:

Beds
Tables and chairs
Stoves
Blankets
Kitchenware
Other essential items
However, this technology could be useful for everyone who needs it, including individuals, families, and communities looking for essential items or aiming to reduce waste and share resources.
This system is created to create a positive impact by reducing waste, supporting students, and encouraging a culture of giving and sharing.

## **Features**

1. **User Authentication**  
   - Register, log in, and manage user profiles.
   - Token-based authentication using Django Rest Framework (DRF).

2. **Item Listings**  
   - Users can post items they want to give away, including:  
   - Items can be marked as "Claimed" once taken.

3. **Search & Filters**  
   - Search for items by title or description.  
   - Filter items by category, location, and availability status.

4. **Messaging**  
   - Users can contact the owner of an item via a built-in messaging system.

5. **Admin Panel**  
   - Admins can manage users and listings to ensure appropriate content.

6. **API Documentation**  
   - Integrated Swagger UI for easy API testing and documentation.

---

## **Technologies Used**

- **Backend**: Django, Django Rest Framework (DRF)  
- **Database**: SQLite (can be swapped with PostgreSQL or MySQL)  
- **Storage**: Local storage for media files  
- **API Documentation**: Swagger  
- **Environment Configuration**: `.env` files for sensitive settings  
- **Deployment**: ASGI and WSGI for production-ready apps  

---

## **Project Structure**

```plaintext
TOGIVEAWAY/
│
├── apps/
│   ├── togiveaway/            # Core app for item listings
│   │   ├── models.py          # Item models
│   │   ├── views.py           # Views for item endpoints
│   │   ├── admin.py           # Admin configuration
│   │   ├── apps.py            # App configuration
│   │   ├── tests.py           # Unit tests
│   │   ├── migrations/        # Database migrations
│
│   ├── user/                  # User authentication app
│   │   ├── models.py          # User models
│   │   ├── serializers.py     # DRF serializers
│   │   ├── views.py           # User API views
│   │   ├── urls.py            # User-specific URLs
│
├── main/                      # Project configurations
│   ├── settings/              # Environment-specific settings
│   │   ├── base.py            # Base settings
│   │   ├── local.py           # Local development settings
│   │   ├── production.py      # Production settings
│   │
│   ├── urls.py                # Root URL configuration
│   ├── asgi.py                # ASGI for async support
│   ├── wsgi.py                # WSGI for production
│
├── manage.py                  # Django management commands
├── db.sqlite3                 # Database (local development)
├── requirements.txt           # Project dependencies
├── .gitignore                 # Files ignored by Git
└── .env                       # Environment variables
```

---

## **Setup Instructions**

Follow these steps to set up and run the ToGiveAway application locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/expertnooob/togiveaway.git
   cd togiveaway
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the project root directory:
     ```plaintext
     SECRET_KEY=your_secret_key
     DEBUG=True
     ALLOWED_HOSTS=localhost,127.0.0.1
     ```

5. **Run Database Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - Open your browser and visit: `http://127.0.0.1:8000/`

---

## **API Documentation**

Swagger UI is enabled for easy testing of the APIs.  
Visit `http://127.0.0.1:8000/swagger/` to explore all available endpoints.

---

## **Future Enhancements**

- Add email notifications for new messages or claimed items.
- Implement location-based filtering using maps.
- Deploy to cloud platforms like Heroku or AWS.
- Support social logins (Google, Facebook, etc.).

---

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a Pull Request.

---

## **License**

This project is licensed under the **MIT License**.  

---

**Enjoy giving and sharing! 🎉**  
For any inquiries, feel free to reach out or raise an issue in the repository.

---

What do you think? Let me know if you want me to tweak any part of this!
