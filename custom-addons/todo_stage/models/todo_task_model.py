from odoo import api, fields, models


class TodoTask(models.Model):
    _inherit = "todo.task"

    name = fields.Char(help='What needs to be done?')
    effort_estimate = fields.Integer()

    stage_id = fields.Many2one('todo.task.stage', string='Stage')


    """
    Dos formas de crear relaciones Many2many: 
    tag_ids = fields.Many2many('todo.task.tag',  # model
                               'todo_task_tag_rel',    # Nombre de la tabla
                               'task_id',         # columna para este registro
                               'tag_id',          # columna para EL OTRO registro
                               'Tags')            # string                           """

    tag_ids = fields.Many2many(comodel_name='todo.task.tag',
                               relation='todo_task_tag_rel',
                               column1='task_id',
                               column2='tag_id',
                               string='Tags')           # comentarios anteriores validos para aqui.









