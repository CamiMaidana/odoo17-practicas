# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class mod_prueba(models.Model):
    _name = 'mod.prueba'
    _description = 'mod_prueba.mod_prueba'

    name = fields.Char(string="Agregue un nombre")
    description = fields.Char(string="Agregue una descripcion")
    value = fields.Integer(string="Agregue el valor estimado")

    fecha_lanzamiento = fields.Date(string="Fecha de lanzamiento")

    tipo = fields.Selection(
        selection=[
            ('idea', 'Idea'),
            ('prototipo', 'Prototipo'),
            ('final', 'Producto Final')
        ],
        string="Tipo de proyecto"
    )

    responsable_id = fields.Many2one('res.partner', string="Responsable")
    def action_confirmar(self):
        for record in self:
            if not record.name:
                raise ValidationError("⚠️ Debes completar el campo 'Nombre de la idea'.")

            if not record.tipo:
                raise ValidationError("⚠️ Debes seleccionar el tipo de proyecto.")

            if not record.fecha_lanzamiento:
                raise ValidationError("⚠️ Debes ingresar la fecha de lanzamiento.")

            if not record.responsable_id:
                raise ValidationError("⚠️ Debes asignar un responsable.")

        return {
            'type': 'ir.actions.act_window',
            'name': 'Lista de Pruebas',
            'res_model': 'mod.prueba',
            'view_mode': 'tree',
            'target': 'current',
        }
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

