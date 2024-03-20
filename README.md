# Jun's Resume API
REST API that displays information found in my resume.

## Purpose
Leveraging the Django framework, this API offers multiple endpoints for retrieving detailed information about my work experience, skills and projects. Now hosted on http://jun-see-resume.onrender.com/api/routes/.

## Usage
Can be used with a curl command like such:
```
curl -L http://jun-see-resume.onrender.com/api/routes/
```
or can also be used via [Postman](postman.com). This API uses a PostgreSQL database and can be used with other databases as well by changing the environment variables. To do this, simply clone this repository, create a PostgreSQL database and create a .env file with variables found in settings.py. Then, run

```
python3 manage.py migrate
python3 manage.py runserver
```

## What's Next
- Create a frontend for this API
- Build detailed documentation using Swagger
