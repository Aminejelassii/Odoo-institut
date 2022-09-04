# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutDepartement(models.Model):
    _name = 'institut.department'
    name = fields.Char()

    # professeur_id = fields.One2many('university.professeur', string='department_id')
    # student_id = fields.One2many('university.student', string='department_id')
    classe_ids = fields.Many2many('institut.classe', string='Class :')
