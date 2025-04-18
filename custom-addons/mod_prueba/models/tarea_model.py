from odoo import models, fields

class TareaPrueba(models.Model):
    _name = 'tarea.prueba'
    _description = 'Tarea relacionada a una idea'

    name = fields.Char(string="Título de la tarea")
    descripcion = fields.Text(string="Descripción")
    idea_id = fields.Many2one('mod.prueba', string="Idea relacionada")
