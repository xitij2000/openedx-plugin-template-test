# -*- coding: utf-8 -*-
"""
test_template_plugin Django application initialization.
"""

from __future__ import absolute_import, unicode_literals

from django.apps import AppConfig


class TestTemplatePluginConfig(AppConfig):
    """
    Configuration for the test_template_plugin Django application.
    """

    name = 'test_template_plugin'

    plugin_app = {
        'slots_config': {
            'lms.djangoapp': {
                'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                'body-extra': 'test_template_plugin.plugin.body_extra_slot',
            },
            'studio.djangoapp': {
                'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                'body-extra': 'test_template_plugin.plugin.body_extra_slot',
            }
        }
    }
