from odoo import fields, models
from odoo import _


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'secuence, name'
    
    # String fields. 
    name = fields.Char('Name', translate=True)
    desc = fields.Text(_('Description'))
    state = fields.Selection(
        (_('draft', 'New')),
        (_('open', 'Started')),
        (_('done', 'Closed')),
    )
    docs = fields.Html(_('Documentation'))
    
    # Numeric fields
    sequence = fields.Integer(_('Sequence'))
    perc_complete = fields.Float(_('% Complete', (3, 2)))
    
    # Data fields
    data_effective = fields.Date(_('Effective Date'))
    date_created = fields.Datetime(
        _('Create Data a Time'),
        default=lambda self: fields.Datetime.now() # genera la fecha actual en el momento del registro
    )
    
    # Other fields:
    fold = fields.Boolean(_('Folded?'))
    image = fields.Binary(_('Image'))
    
    


