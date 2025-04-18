# -*- coding: utf-8 -*-

from odoo import models, fields, api


class mod_prueba(models.Model):
    _name = 'mod.prueba'
    _description = 'mod_prueba.mod_prueba'

    name = fields.Char()
    description = fields.Char()
    value = fields.Integer()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

