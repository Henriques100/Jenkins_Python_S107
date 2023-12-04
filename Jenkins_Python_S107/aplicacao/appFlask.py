from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import redis

app = Flask(__name__)

# Configuração do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://seu_usuario:sua_senha@localhost:3306/shopping_list'
db = SQLAlchemy(app)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'shopping_list'
cache = Cache(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

@app.route('/')
def index():
    # Exemplo de uso do MySQL
    result = db.session.execute("SELECT 1")
    mysql_data = result.fetchone()[0]

    # Exemplo de uso do Redis
    cached_data = cache.get('my_cached_data')
    if not cached_data:
        cached_data = 'Data não encontrado no cache. Salvando no cache.'
        cache.set('my_cached_data', cached_data, timeout=600)  # Expira após 600 segundos

    # Exemplo de uso do Flask-SQLAlchemy
    items = Item.query.all()

    return render_template('index.html', mysql_data=mysql_data, cached_data=cached_data, items=items)

if __name__ == '__main__':
    app.run(debug=True)
