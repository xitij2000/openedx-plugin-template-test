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
                'instructor_dashboard_2': {
                    'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                    'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                    'body-extra': 'test_template_plugin.plugin.body_extra_slot',
                },
                'student.views.dashboard': {
                    'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                    'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                    'body-extra': 'test_template_plugin.plugin.body_extra_slot',
                }
            },
            'studio.djangoapp': {
                'course_listing': {
                    'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                    'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                    'body-extra': 'test_template_plugin.plugin.body_extra_slot',
                },
                'settings_handler': {
                    'head-extra': 'test_template_plugin.plugin.head_extra_slot',
                    'body-initial': 'test_template_plugin.plugin.body_initial_slot',
                    'body-extra': 'test_template_plugin.plugin.body_extra_slot',
                },
            }
        }
    }
