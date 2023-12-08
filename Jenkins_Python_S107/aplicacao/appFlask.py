from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import redis
import time
import os

app = Flask(__name__)

# Configuração do PostgreSQL
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'mypassword')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'mydatabase')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'postgres-db')
POSTGRES_PORT = int(os.environ.get('POSTGRES_PORT', 5432))

# Use as variáveis de ambiente para conectar ao PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}'
db = SQLAlchemy(app)

# Configuração do Redis
REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)

# Use as variáveis de ambiente para conectar ao Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'test_results'
cache = Cache(app)

# Configure o cliente Redis
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

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
        # Armazena o resultado do teste no PostgreSQL
        new_result = TestResult(test_name='Teste 1', result=test_result, execution_time=execution_time)
        db.session.add(new_result)
        db.session.commit()

        # Armazena o tempo de execução no Redis
        cache_key = 'execution_time_test_1'
        if cache.get(cache_key) is None:
            cache.set(cache_key, execution_time, timeout=None)

        # Recupera os resultados dos testes do PostgreSQL
        test_results = TestResult.query.all()

        return render_template('index.html', test_results=test_results)
    except Exception as e:
        return f"Erro durante a execução: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

