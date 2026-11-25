# -*- coding: utf-8 -*-
{
    'license': 'LGPL-3',
    'name': "Web Window Title",
    'summary': "The custom web window title",
    'description': """
Web Window Title
================

The custom web window title.

Changelog
---------
14.0.1.2.1 (24 Nov 2026): deskripsi gaya baru bilingual (EN default + ID) + screenshot testbed.
""",
    'author': 'Ahmad Ghozali',
    'category': 'Extra Tools',
    'version': '14.0.1.2.8',
    'depends': ['base_setup'],
    'demo': [
        'data/demo.xml',
    ],
    'data': [
        'views/webclient_templates.xml',
        'views/res_config.xml',
    ],
    'images': [
        'static/description/Web_Window_Title_Video.gif',
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}