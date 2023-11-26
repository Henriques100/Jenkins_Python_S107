from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import redis

app = Flask(__name__)

# Configuração do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://myuser:mypassword@mysql-db/mydatabase'
db = SQLAlchemy(app)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'my_cache_prefix'
cache = Cache(app)

@app.route('/')
def index():
    # Exemplo de uso do MySQL
    result = db.session.execute("SELECT 1")
    mysql_data = result.fetchone()[0]

    # Exemplo de uso do Redis
    cached_data = cache.get('my_cached_data')
    if not cached_data:
        cached_data = 'Data não encontrado no cache. Salvando no cache.'
        cache.set('my_cached_data', cached_data, timeout=600) # Expira após 600 segundos

    return f'MySQL Data: {mysql_data}, Redis Cached Data: {cached_data}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
