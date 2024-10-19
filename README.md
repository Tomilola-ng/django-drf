# Django DRF Template


![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white)
![Django](https://img.shields.io/badge/-Django-092E20?style=flat-square&logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=plastic&logo=jsonwebtokens&logoColor=%232CB9F1)
![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=Docker&logoColor=white)

🚀 A ready-to-use Django + Django REST Framework (DRF) template for building scalable RESTful APIs.

Pre-configured with essential features like authentication, permissions, pagination, and more, so you can jumpstart your next project with ease. Perfect for rapid API development and clean architecture.

## Features

- 🔐 JWT Authentication
- 🛡️ Role-based permissions
- 📄 Customizable pagination
- 🌐 CORS configuration
- 📊 Swagger/OpenAPI documentation
- 🐳 Docker support
- 🧪 Pre-configured testing setup

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/Tomilola-ng/django-drf-template.git
   cd django-drf-template
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

Visit `http://localhost:8000/api/` to access the API.

## Configuration

- Environment variables: Copy `.env.example` to `.env` and update the values.
- Database: Configure your database in `settings.py` or use the default SQLite.
- Custom user model: Located in `users/models.py`.

## Testing

Run the test suite:

```
python manage.py test
```

## Deployment

Dockerfile and docker-compose.yml are provided for easy deployment. Adjust as needed for your production environment.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Follow Me

- Twitter: [https://x.com/tomilola_ng](https://x.com/tomilola_ng)
- LinkedIn: [https://www.linkedin.com/in/tomilola-oluwafemi/](https://www.linkedin.com/in/tomilola-oluwafemi/)
- Hashnode: [https://hashnode.com/@tomilolang](https://hashnode.com/@tomilolang)

Happy coding! 🎉
