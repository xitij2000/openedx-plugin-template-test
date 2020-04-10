from __future__ import absolute_import, unicode_literals

from django.template.loader import render_to_string

from six.moves.urllib.parse import unquote


def head_extra_slot(context):
    return render_to_string(
            'test_template_plugin/head-extra.html',
            request=context.get('request'),
            context={
                'slot': 'head-extra',
                'current_url': unquote(context.get('current_url', 'no-curent-url')),
            }
        )

def body_extra_slot(context):
    return render_to_string(
            'test_template_plugin/body-extra.html',
            request=context.get('request'),
            context={
                'slot': 'body-extra',
                'current_url': unquote(context.get('current_url', 'no-curent-url')),
            }
        )

def body_initial_slot(context):
    return render_to_string(
            'test_template_plugin/body-initial.html',
            request=context.get('request'),
            context={
                'slot': 'body-initial',
                'current_url': unquote(context.get('current_url', 'no-curent-url')),
            }
        )
