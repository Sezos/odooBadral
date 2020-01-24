from odoo import models, fields, api


class registration(models.Model):
    _name = 'model.registration'
    _description = 'registration_model'
    _rec_name = "name"
    name = fields.Char(required=True)
    email = fields.Char(required=True)
    age = fields.Integer(required=True)
    phoneNumber = fields.Text(required=True)


class add(models.Model):
    _name = 'model.add'
    _description = 'add_model'
    name = fields.Many2one('model.registration')
    Calendar_ids = fields.One2many('model.calendar', 'name1')


class Calendar(models.Model):
    _name = 'model.calendar'
    _description = "calendar_model"
    name1 = fields.Many2one('model.add')
    date = fields.Date(default=fields.Date.today, store=True)
    time1 = fields.Float('Duration in hours ')
    time2 = fields.Float('Duration in hours ')
