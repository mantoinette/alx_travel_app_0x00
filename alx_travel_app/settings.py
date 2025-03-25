INSTALLED_APPS = [
    ...
    'corsheaders',
    'rest_framework',
    'listings',
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Example for React frontend
    # Add other origins as needed
]
