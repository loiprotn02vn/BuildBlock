# -*- coding: utf-8 -*-
{
    "name": "Tutorial Snippet",
    "summary": """
        tutorial snippets""",
    "description": """
        ok
    """,
    "author": "vyngt",
    "website": "https://github.com/vyngt",
    "category": "Uncategorized",
    "version": "16.0.1.0.0",
    "depends": ["base", "website"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/snippets/v_block.xml",
        "views/snippets/snippets.xml",
    ],
    "assets": {
        "tutorial_snippet.assets_tutorial_snippet": [
            # bootstrap
            ("include", "web._assets_helpers"),
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            ("include", "web._assets_bootstrap"),
            "web/static/src/libs/fontawesome/css/font-awesome.css",  # required for fa icons
            "web/static/src/legacy/js/promise_extension.js",  # required by boot.js
            "web/static/src/boot.js",  # odoo module system
            "web/static/src/env.js",  # required for services
            "web/static/src/session.js",  # expose __session_info__ containing server information
            "web/static/lib/owl/owl.js",  # owl library
            "web/static/lib/owl/odoo_module.js",  # to be able to import "@odoo/owl"
            "web/static/src/core/utils/functions.js",
            "web/static/src/core/browser/browser.js",
            "web/static/src/core/registry.js",
            "web/static/src/core/assets.js",
            #
            "tutorial_theme/static/src/**/*",
        ],
    },
}
