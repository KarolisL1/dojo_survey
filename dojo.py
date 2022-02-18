from flask import flash
from mysqlconnection import connectToMySQL
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
    # Other Burger methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @classmethod
    def save(cls, form):
        query = "INSERT INTO dojos ( name , location, language, comment, created_at ) VALUES ( %(your_name)s , %(location)s, %(language)s, %(comment)s, NOW() );"
        # data is a dictionary that will be passed into the save method from server.py

        return connectToMySQL('dojo_survey_schema').query_db( query, form )

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL('dojo_survey_schema').query_db( query, data )

        return cls(results[0])

    @staticmethod
    def validate_dojo(dojo):
        is_valid = True # we assume this is true
        if len(dojo['your_name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        # if len(dojo['location']) < 3:
        #     flash("Bun must be at least 3 characters.")
        #     is_valid = False
        # if len(dojo['language']) < 200:
        #     flash("Calories must be 200 or greater.")
        #     is_valid = False
        if len(dojo['comment']) < 3:
            flash("Bun must be at least 3 characters.")
            is_valid = False
        return is_valid

    