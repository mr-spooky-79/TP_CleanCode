"""id_controller.py: The endpoint of the api, call function when request are made"""
__author__      = "Girard Alexandre"

from flask import request
from flask_restx import Resource

from ..util.idDto import IDDto
api = IDDto.api

from ..service.id_service import checkID

@api.route('/cle/verification/<id>')
class VerifyID(Resource):
    @api.doc('Verify an id')
    def get(self, id):
        """Verify an id"""
        return checkID(id)