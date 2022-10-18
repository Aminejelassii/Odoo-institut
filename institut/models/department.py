# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutDepartement(models.Model):
    _name = 'institut.department'
    name = fields.Char()

    classe_ids = fields.Many2many('institut.classe', string='Class :')
