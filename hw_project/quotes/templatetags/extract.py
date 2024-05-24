from bson.objectid import ObjectId

from django import template

from .. utils import get_mongobd

register = template.Library()

def get_author(id_):
    db = get_mongobd()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']


register.filter('author', get_author)