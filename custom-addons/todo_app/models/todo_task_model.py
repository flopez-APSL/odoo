from odoo import models, fields


class TodoTask(models.Model):
    _name = 'todo.task' # identificador del modelo para Odoo.
    _description = 'Aplicación de prueba'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=False)
    user_id = fields.Many2one(
        'res.users',
        string='Responsible',
        default=lambda self: self.env.user)
    team_ids = fields.Many2many('res.partner', string='Team')



