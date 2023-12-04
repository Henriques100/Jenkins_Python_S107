import unittest
from flask_testing import TestCase
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app import app, db
import time

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class TestShoppingListApp(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['CACHE_TYPE'] = 'null'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index_successful(self):
        # Adicionar item à lista
        item = Item(name='Sucesso', quantity=1)
        db.session.add(item)
        db.session.commit()

        start_time = time.time()
        response = self.client.get('/')
        end_time = time.time()
        execution_time = end_time - start_time

        self.assert200(response)
        self.assert_template_used('index.html')

        # Verificar se os dados do MySQL e do Redis estão presentes na resposta
        self.assert_context('mysql_data' in response.context)
        self.assert_context('cached_data' in response.context)

        # Verificar se os dados do item estão presentes na resposta
        self.assertIn('Sucesso', response.get_data(as_text=True))

        # Armazenar os resultados no MySQL
        new_result = Item(name='Sucesso', quantity=1)
        db.session.add(new_result)
        db.session.commit()

        # Armazenar o tempo de resposta no Redis
        cache_key = 'execution_time_successful'
        cached_execution_time = cache.get(cache_key)
        if not cached_execution_time:
            cache.set(cache_key, execution_time, timeout=None)  # Sem expiração

if __name__ == '__main__':
    unittest.main()
