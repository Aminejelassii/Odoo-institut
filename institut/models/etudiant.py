# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re


class InstitutEtudiant(models.Model):
    _name = 'institut.etudiant'
    f_name = fields.Char('Full name : ', required=True )

    sex = fields.Selection([('female', 'Female'), ('male', 'Male')])
    image = fields.Image()
    startdate = fields.Char("Registration code : ", size=10)
    identity = fields.Char('Identity : ', size=8)
    adress = fields.Text('Address :')
    birthday = fields.Date('Date of Birth :')
    email = fields.Char('E-mail:')
    phone = fields.Char('Phone number :', size=8, required=True)

    classe_id = fields.Many2one('institut.classe', string='Class:', required=True)
    department_id = fields.Many2one('institut.department', string='Departement:', required=True)
    matiere_ids = fields.Many2many(related='classe_id.matiere_ids')
    classe_ids = fields.Many2one('institut.classe', string='Class :')

    def name_get(self):
        result = []
        for etudiant in self:
            nom = etudiant.f_name
        result.append((etudiant.id, nom))
        return result

 #   @api.constrains('birthday', 'startdate')
  #  def chek_date(self):
   #     if self.birthday > self.startdate:
    #        raise ValueError('date de naissance doit etre inferieur a date dinscription')

    def send_message(self):
        if not self.phone:
            raise ValueError('Incorrect phone number')
        message = 'Hi %s' % self.f_name
        whatapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatapp_api_url
        }



# @api.onchange('department_id')
# def _onchange_department(self):
#   for i in self:
#      return {'domain': {'classe_id': [('department_id', '=', i.department_id.id)]}}
#   @api.depends('is_student')
#   def _compute_person_type(self):
#      for institut in self:
#           institut.type = 'etud' if institut.is_student else 'Prof'

#  def _write_person_type(self):
#      for institut in self:
#         institut.is_student = institut.type == 'etud'
