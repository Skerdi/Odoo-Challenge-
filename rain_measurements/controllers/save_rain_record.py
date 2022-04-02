from odoo import http
from odoo.http import request

class SaveRainRecord(http.Controller):
   @http.route('/rain/measure/<int:height>', type = 'http', auth='public',  website= True)
   def save_record(self, height, **kwargs):
      value = {'height': height}
      request.env['rain.measurement.daily'].create(value)
      # return "Record added to database"
      return request.render("rain_measurements.rain_record_saved", {})