import html


def make_element(name, value, **attrs):
    keyvals = ['%s=%s' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


print(make_element('item', 'Albatross', size='large', quantity=6))
