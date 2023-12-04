from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import redis
import time

app = Flask(__name__)

# Configuração do MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://myuser:mypassword@mysql-db:3306/mydatabase'
db = SQLAlchemy(app)

# Configuração do Redis
app.config['CACHE_TYPE'] = 'redis'
app.config['CACHE_KEY_PREFIX'] = 'test_results'
cache = Cache(app)
redis_client = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_name = db.Column(db.String(255), nullable=False)
    result = db.Column(db.String(255), nullable=False)
    execution_time = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    # Exemplo de teste (substitua isso por seus próprios testes)
    start_time = time.time()
    test_result = "Resultado do teste"
    end_time = time.time()
    execution_time = end_time - start_time

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
