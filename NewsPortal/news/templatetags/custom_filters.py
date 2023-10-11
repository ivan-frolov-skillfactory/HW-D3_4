from django import template
register = template.Library()

stop_words = [
    'Дискредитация',
    'плохое_слово2',
    'плохое_слово3',
]


# Теперь каждый раз, когда мы захотим пользоваться нашими фильтрами, в шаблоне нужно будет прописывать следующий тег:
# {% load custom_filters %}

@register.filter(name='censor')
def censor(value):
    # фильтр заменяет слова из стоп-листа на '...'
    for sw in stop_words:
        value = value.lower().replace(sw.lower(), '...')
    return value

@register.filter(name='preview')

def preview(value):
    if len(value) > 10:
        return value[:51] + '...'
    else:
        return value


if __name__ == '__main__':
    print(censor("""Слово1 слово2 плохое_слово1 плохое_слово2
плохое_слово3 плохое_слово4 слово3"""))