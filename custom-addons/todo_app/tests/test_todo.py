from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError


class TestTodo(TransactionCase):


    def test_create(self):
        """comprueba que esté el atributo 'is done' por defecto en False.
        """
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.is_done, False)

    def test_clear_done(self):
        Todo = self.env['todo.task']
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)

    def setUp(self, *args, **kwargs):
        result = super(TestTodo, self).setUp(*args, **kwargs)
        user_demo = self.env.ref('base.user_demo')
        self.env= self.env(user=user_demo)
        return result

    def test_record_rule(self):
        """Test for Record Rules"""
        Todo = self.env('todo.task')
        task = Todo.sudo().create({'name': 'Admin Task'})
        with self.assertRaises(AccessError):
            Todo.browse([task.id]).name







