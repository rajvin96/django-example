from django import template

register = template.Library()


def omit(value,arg):
    """
    this cuts out all values of "arg" from the string!
    """

    return value.replace(arg,'')

register.filter('slice',omit)
