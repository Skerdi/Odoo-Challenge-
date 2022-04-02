from odoo import http
from odoo.http import request

class TestRainRecord(http.Controller):

    @http.route('/rain/measure/<int:height>', auth='public',  website= True)
    def test_rain_measure(self, height, **kwargs):
        return "Testing"
