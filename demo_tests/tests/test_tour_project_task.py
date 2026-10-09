# -*- coding: utf-8 -*-
from odoo import Command
from odoo.tests import HttpCase

class HttpCaseDemo(HttpCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = cls.env["res.users"].create({
            "name": "Test Project User",
            "login": "test_project_user",
            "group_ids": [
                Command.link(cls.env.ref("base.group_user").id),
                Command.link(cls.env.ref("project.group_project_user").id),
            ],
        })

        cls.admin = cls.user = cls.env["res.users"].create({
            "name": "Test Project Admin",
            "login": "test_project_admin",
            "group_ids": [
                Command.link(cls.env.ref("base.group_user").id),
                Command.link(cls.env.ref("project.group_project_manager").id),
            ],
        })

        cls.project = cls.user = cls.env["project.project"].create({"name": "Tech Evening Project"})

    def test_01_user_cannot_access_task_type(self):
        with self.assertRaises(AssertionError):
            self.start_tour(
                "/odoo/project",
                'te_demo_user_tour',
                login='test_project_user',
                timeout=1,
            )

    @classmethod
    def tearDownClass(cls):
        project = cls.env["project.project"].sudo().search([("name", "=", "Tech Evening Project")], limit=1)

        if project:
            project.unlink()
