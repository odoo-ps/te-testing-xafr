# -*- coding: utf-8 -*-
from odoo.addons.base.tests.common import BaseCommon


class TestProjectTaskDemoAdmin(BaseCommon):
    _test_user_groups = ("project.group_project_manager",)
    _test_user_name = "Test Project Manager"

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.project = cls.env["project.project"].create({"name": "Avenger Repairs"})

        cls.partner = cls.env["res.partner"].create({"name": "Groot"})

        cls.task = cls.env["project.task"].create({
            "name": "Sharpen groot's Axe arm",
            "project_id": cls.project.id,
            "partner_id": cls.partner.id
        })

        cls.partner = cls.env['res.partner'].create({"name": "Sharpen groot's Axe arm"})

    def test_01_manager_can_set_task_type(self):
        self.task.write({"task_type": "manual"})

        self.assertEqual(self.task.task_type, "manual")

    def test_02_priority_computed_after_type_change(self):
        self.task.write({"task_type": "avenger"})
        self.assertEqual(self.task.priority, "3")

        self.task.write({"task_type": "other"})
        self.assertEqual(self.task.priority, "0")

        self.task.write({"task_type": "technical"})
        self.assertEqual(self.task.priority, "1")
