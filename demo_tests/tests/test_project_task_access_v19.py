# -*- coding: utf-8 -*-
from odoo import Command
from odoo.exceptions import AccessError
from odoo.tests import TransactionCase, tagged


@tagged("-at_install", "post_install", "v19")
class TestProjectTaskDemo(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.admin = cls.user = cls.env["res.users"].create({
            "name": "Test Project Admin",
            "login": "test_project_admin",
            "group_ids": [
                Command.link(cls.env.ref("base.group_user").id),
                Command.link(cls.env.ref("project.group_project_manager").id),
            ],
        })

        cls.user = cls.env["res.users"].create({
            "name": "Test Project User",
            "login": "test_project_user",
            "group_ids": [
                Command.link(cls.env.ref("base.group_user").id),
                Command.link(cls.env.ref("project.group_project_user").id),
            ],
        })

        cls.project = cls.env["project.project"].create({"name": "Groot's Bodyshop"})

        cls.task = cls.env["project.task"].create({
            "name": "Assemble Groot's battle legs",
            "project_id": cls.project.id,
        })

    def test_admin_can_set_task_type(self):
        task = self.task.with_user(self.admin)

        task.write({"task_type": "avenger"})

        self.assertEqual(task.task_type, "avenger")

    def test_user_cannot_set_task_type(self):
        task = self.task.with_user(self.user)

        with self.assertRaises(AccessError):
            task.write({"task_type": "manual"})
