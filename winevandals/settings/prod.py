# winevandals/settings/prod.py
import os
from .base import *

DEBUG = False

# Make sure SECRET_KEY is provided in prod
if SECRET_KEY == "dev-insecure-secret-key":
    raise RuntimeError("SECRET_KEY must be set in production")

# Always provide ALLOWED_HOSTS in prod (Railway domain)
if not ALLOWED_HOSTS or ALLOWED_HOSTS == ["localhost", "127.0.0.1"]:
    # You can still set ALLOWED_HOSTS="your-app.up.railway.app"
    raise RuntimeError("ALLOWED_HOSTS must be set in production")

# Security headers (good defaults)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True").lower() == "true"

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "3600"))
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# If you later add a frontend on another domain, configure:
# CSRF_TRUSTED_ORIGINS = ["https://your-frontend.com"]
