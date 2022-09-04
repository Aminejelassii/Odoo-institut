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
    #num_prof = fields.Integer(string="Nombre des professeurs", compute="count_prof")




    #num_student = fields.Integer(string="nombre des étudiants", compute="count_etude")
    num_matiere = fields.Integer(string="Number of subjects", compute="count_mat")

   # def count_prof(self):
     #  self.num_prof = len(self.professeur_ids)

   # def count_etude(self):
    #    self.num_student = len(self.student_ids)

    def count_mat(self):
        self.num_matiere = len(self.matiere_ids)
