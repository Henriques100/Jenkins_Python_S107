import unittest
from flask_testing import TestCase
from app import app, db, Item

class TestShoppingListApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['CACHE_TYPE'] = 'null'
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        # Adicionar item à lista
        item = Item(name='Maçãs', quantity=5)
        db.session.add(item)
        db.session.commit()

        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('index.html')

        # Verificar se os dados do MySQL e do Redis estão presentes na resposta
        self.assert_context('mysql_data' in response.context)
        self.assert_context('cached_data' in response.context)

        # Verificar se os dados do item estão presentes na resposta
        self.assertIn('Maçãs', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
