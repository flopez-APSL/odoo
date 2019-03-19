from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):


    def test_create(self):
        """comprueba que esté el atributo 'is done' por defecto en False.
        """
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):  # comprueba que esté el atributo 'is done' por defecto en False.
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertEqual(task.active)



