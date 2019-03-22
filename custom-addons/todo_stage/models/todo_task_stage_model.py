from odoo import fields, models


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'secuence, name'
    
    # String fields. 
    name = fields.Char('Name', translate=True)
    desc = fields.Text('Description')
    state = fields.Selection([
        ('draft', 'New'),
        ('open', 'Started'),
        ('done', 'Closed')], string='State')
    docs = fields.Html('Documentation')
    
    # Numeric fields
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    
    # Data fields
    data_effective = fields.Date('Effective Date')
    date_created = fields.Datetime(
        'Create Data a Time',
        default=lambda self: fields.Datetime.now() # genera la fecha actual en el momento del registro
    )
    
    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    task_ids = fields.One2many('todo.task',         # modelo al cual se relaciona
                               'stage_id',          # fields for "this" on related model
                               'Tasks in this Stage')
    
    


