{
    "name": "Tech Evening - Demo Tests",
    "version": "20.0.1.0.0",
    "summary": "Setup to run some tests as an educational demo.",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": [
        "project",
    ],
    "data": [
        "views/project_task_views.xml",
    ],
    "assets": {
        "web.assets_tests": [
            "demo_tests/static/tests/tours/project_task_tour.js",
        ],
    },
    "demo": [
        "demo/project_task_demo.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
