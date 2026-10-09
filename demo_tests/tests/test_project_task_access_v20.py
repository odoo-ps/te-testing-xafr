# -*- coding: utf-8 -*-
from odoo.exceptions import AccessError
from odoo.tests import tagged

from odoo.addons.base.tests.common import BaseCommon


class TestProjectTaskDemoAdmin(BaseCommon):
    _test_user_groups = ("project.group_project_manager",)
    _test_user_name = "Test Project Manager"


    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.project = cls.env["project.project"].create({"name": "Avenger Repairs"})

        cls.partner = cls.env['res.partner'].create({"name": "Thor"})

        cls.task = cls.env["project.task"].create({
            "name": "Repair Mjölnir's handle",
            "project_id": cls.project.id,
            "partner_id": cls.partner.id
        })


    @tagged('post_install', '-at_install', 'v20')
    def test_manager_can_set_task_type(self):
        self.task.write({"task_type": "manual"})

        self.assertEqual(self.task.task_type, "manual")


class TestProjectTaskDemoUser(BaseCommon):
    _test_user_groups = ("base.group_user",)
    _test_user_name = "Test Project User"


    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.project = cls.env["project.project"].create({"name": "Avenger Repairs"})

        cls.partner = cls.env['res.partner'].create({"name": "Hawkeye"})

        cls.task = cls.env["project.task"].create({
            "name": "Refinishing Hawkeye's bow.",
            "project_id": cls.project.id,
            "partner_id": cls.partner.id
        })

    @tagged('post_install', '-at_install', 'v20')
    def test_regular_user_cannot_set_task_type(self):
        with self.assertRaises(AccessError):
            self.task.write({"task_type": "other"})
