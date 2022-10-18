# -*- coding: utf-8 -*-

from odoo import models, fields


class InstitutClasse(models.Model):
    _name = 'institut.classe'
    name = fields.Char()
    code = fields.Char()
    professeur_ids = fields.Many2many('institut.professeur', string='Teacher :')
    matiere_ids = fields.Many2many('institut.matiere', string='Subject :')
    student_ids = fields.Many2many(comodel_name='institut.etudiant', string='Student :')
    date = fields.Date()
    # Field designe le nombre des matières
    num_matiere = fields.Integer(string="Number of subjects", compute="count_mat")

    # Fonction pour compter le nombre des matières

    def count_mat(self):
        self.num_matiere = len(self.matiere_ids)
