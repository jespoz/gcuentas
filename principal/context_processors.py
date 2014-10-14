from django.core.urlresolvers import reverse


def menu(request):
    menu = {'menu': [
        {'name': 'Principal', 'url': reverse('home'), 'icon': 'home', 'id': 'id_home'},
        {'name': 'Bases', 'url': reverse('admin:index'), 'icon': 'database', 'id': 'id_admin'},
        {'name': 'Bonos', 'url': reverse('lista_bonos'), 'icon': 'puzzle-piece', 'id': 'id_bonus'},
    ]}
    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu

