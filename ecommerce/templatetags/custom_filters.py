from django import template

register = template.Library()

@register.filter
def format_brl(value):
    try:
        # teste2 = value[0:6].replace('.', ',')
        # teste1 = value[5:].replace(',', '.')
        # return teste1 + teste2

        novo = ''
        cont = 0
        for i in value[::-1].replace('.', ''):
            if cont == 2:
                novo += ','
            
            if cont == 5:
                novo += '.'

            novo += i
            cont += 1
        
        return novo[::-1]
        
    except (ValueError, TypeError):
        return value
    

#5.000,00