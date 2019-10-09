from __future__ import absolute_import, unicode_literals

from django.template.loader import render_to_string

from six.moves.urllib.parse import unquote

class TestPlugin(object):

    def get_include(self, slot, context):
        if slot in ['head-extra', 'body-initial', 'body-extra']:
            return render_to_string(
                'test_template_plugin/{}.html'.format(slot),
                request=context.get('request'),
                context={
                    'slot': slot,
                    'current_url': unquote(context.get('current_url', 'no-curent-url')),
                }
            )
