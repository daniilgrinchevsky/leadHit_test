import re
from tinydb import TinyDB, Query, where

open('db_data.json', 'w').close()
db = TinyDB('db_data.json')
form_table = db.table('form')
form_table.insert({'name': 'SignUp', 'first_name': 'text', 'email': 'email', 'phone_number': 'phone', 'dob': 'date'})
form_table.insert({'name': 'QuickSignUp', 'first_name': 'text', 'email': 'email'})
form_table.insert({'name': 'ContactInfo', 'email': 'email', 'phone_number': 'phone'})
form_table.insert({'name': 'DateOfBirth', 'dob': 'date'})


def get_form(form):
    form_with_types = {}
    for field_name, field_value in form.items():
        field_type = validate(field_value)
        form_with_types[field_name] = field_type
    return search(form_with_types)


def validate(field_value):
    patterns = {
        re.compile(r"^(0?[1-9]|[12]\d|3[01])[.\-](0?[1-9]|1[012])[.\-]\d{4}$"): 'date',
        re.compile(r"^(-]\d{4}/-](0?[1-9]|1[012])[/0?[1-9]|[12]\d|3[01])"): 'date',
        re.compile(r"(\+7)?\s*?(\d{3})\s*?(\d{3})\s*?(\d{2}\s*?(\d{2}))"): 'phone',
        re.compile(r"^[a-z\d]+[._]?[a-z\d]+@\w+[.]\w{2,3}$"): 'email'
    }

    for pattern, field_type in patterns.items():
        if re.search(pattern, field_value):
            return field_type
    return 'text'


def search(form):
    forms = []
    search_result = form_table.search(lambda form_db: search_predicate(form_db, form))
    if not search_result:
        return form
    for result in search_result:
        forms.append(result['name'])
    return forms


def search_predicate(form_db, form):
    for field_name, field_type in form_db.items():
        if field_name != 'name' and (field_name not in form or form[field_name] != field_type):
            return False
    return True


