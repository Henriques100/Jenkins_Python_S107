from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import redis
import time
import os

app = Flask(__name__)

# Configuração do MySQL
mysql_user = os.environ.get('MYSQL_USER', 'myuser')
mysql_password = os.environ.get('MYSQL_PASSWORD', 'mypassword')
mysql_database = os.environ.get('MYSQL_DATABASE', 'mydatabase')
mysql_host = os.environ.get('MYSQL_HOST', 'mysql-db')
mysql_port = int(os.environ.get('MYSQL_PORT', 3306))

# Configuração do Redis
redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
redis_password = os.environ.get('REDIS_PASSWORD', None)

# Use as variáveis de ambiente para conectar ao MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}'
db = SQLAlchemy(app)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'test_results'
cache = Cache(app)

# Configure o cliente Redis
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(255), nullable=False)
    result = db.Column(db.String(255), nullable=False)
    execution_time = db.Column(db.Float, nullable=False)

# Criação do banco de dados e das tabelas
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    # Exemplo de teste (substitua isso por seus próprios testes)
    start_time = time.time()
    test_result = "Resultado do teste"
    end_time = time.time()
    execution_time = end_time - start_time

    try:
        # Armazena o resultado do teste no MySQL
        new_result = TestResult(test_name='Teste 1', result=test_result, execution_time=execution_time)
        db.session.add(new_result)
        db.session.commit()

        # Armazena o tempo de execução no Redis
        cache_key = 'execution_time_test_1'
        cached_execution_time = cache.get(cache_key)
        if not cached_execution_time:
            cache.set(cache_key, execution_time, timeout=None)  # Sem expiração

        # Recupera os resultados dos testes do MySQL
        test_results = TestResult.query.all()

        return render_template('index.html', test_results=test_results)
    except Exception as e:
        return f"Erro durante a execução: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
 