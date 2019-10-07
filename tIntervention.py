from odoo import models, fields, api
from datetime import datetime,date
from dateutil.relativedelta import relativedelta

class tintervention(models.Model):
     _name = 't.intervention'
     _order = 'numero'
     _rec_name = 'numero'
     
     numero = fields.Char(string="Numéro",required=True)
     date = fields.Date(string="Date")
     type = fields.Selection(string="Type de document", selection=[('pose', 'Pose'),  ('retrait', 'Retrait')])
     patient_id = fields.Many2one('t.patient', string='Patient')
     nb = fields.Integer(compute='_compute_total')
     num = fields.Char("Numero")
     
    
     _sql_constraints = [
      ('numero_unique','unique(numero)','IPP est affecté à un autre patient !')]
    
     @api.depends('type', 'nb')
     def _compute_total(self):
            for record in self:
                 a=self.env['t.intervention'].search([('type',"=", record.type)])
                 record.nb = len(a)
     @api.model
     def create(self, vals):
         if vals.get('type') == 'pose':
             
             vals['num'] = self.env['ir.sequence'].next_by_code('pose')
             result = super(tintervention, self).create(vals)  
             return result
         else:
             vals['num'] = self.env['ir.sequence'].next_by_code('retrait')
             result = super(tintervention, self).create(vals)  
             return result