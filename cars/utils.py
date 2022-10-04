menu = [
    {'title': 'Home', 'url_name': 'home'},
    {'title': 'Catalog', 'url_name': 'cars'},
]

class DataMixin:
    
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context