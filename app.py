from website import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('apache2/ssl/server.crt', 'apache2/ssl/server.key'))

