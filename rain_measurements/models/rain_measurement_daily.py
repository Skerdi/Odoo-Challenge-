from odoo import fields, models
from datetime import datetime, timedelta
from odoo import api
from odoo.exceptions import ValidationError


class rainMeasurement(models.Model):
    _name = "rain.measurement.daily"
    _description = "Rain measurements per day"
    _order = 'id'
    _auto = True

    name = fields.Char('Description', required=True, default='Daily record')
    date = fields.Datetime(required=True,  default=fields.Datetime.now())
    height = fields.Integer(required=True, default=0)

    # _sql_constraints = [
    #     ('check_height', 'CHECK(check_height >= 0)',
    #      'Rain height can\'t be negative.'),
    # ]
    
    # I kept getting an ERROR like 'unable to add constraint' and I read 
    # that it might be because problematic data may already exist in db,
    # but even though i dropped the table the error remained. So, I took
    # the other path below

    @api.constrains('height')
    def _check_height(self):
        for record in self:
            if record.height < 0:
                raise ValidationError('Rain height can\'t be negative.')

    @api.constrains('date')
    def _check_date(self):
        for record in self:
            if record.date > fields.Datetime.now():
                raise ValidationError("The date cannot be set in the feature.")