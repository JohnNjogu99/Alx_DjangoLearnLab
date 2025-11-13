# Security Review

## Measures Implemented
- Enforced HTTPS with `SECURE_SSL_REDIRECT` and HSTS headers
- Secured cookies with `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`
- Hardened headers against clickjacking, MIME sniffing, and XSS
- Configured Content Security Policy via `django-csp`
- All forms include `{% csrf_token %}` for CSRF protection
- Views use Django ORM and forms to prevent SQL injection

## Contribution to Security
These measures ensure that all data is transmitted securely, user input is validated, and browser-based attacks are mitigated. They align with OWASP best practices and Django’s security checklist.

## Areas for Improvement
- Add automated security tests (e.g., OWASP ZAP or Bandit)
- Set up HTTPS locally for full simulation
- Monitor headers and cookies in production using browser dev tools

# Nginx HTTPS Configuration (for production deployment)

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/ssl/certs/yourdomain.crt;
    ssl_certificate_key /etc/ssl/private/yourdomain.key;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
