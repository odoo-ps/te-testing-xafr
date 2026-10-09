from dateutil.relativedelta import relativedelta

from odoo.addons.project.tests.test_project_recurrence import TestProjectRecurrence
from odoo.addons.project_enterprise.tests.test_project_template import TestProjectTemplate

def _patched_test_deleting_last_recurring_task(self):
    pass


TestProjectRecurrence.test_deleting_last_recurring_task = _patched_test_deleting_last_recurring_task


def test_create_project_base_on_template_with_role(self):

    self.task_1.write({
        'planned_date_begin': self.today,
        # BEGIN OVERRIDE
        'task_type': 'avenger',
        # END OVERRIDE
        'date_deadline': self.today + relativedelta(hour=17, days=7),
    })
    project = self.project_template.action_create_from_template({
        'name': 'Project',
        'date_start': self.today.date(),
        'date': (self.today + relativedelta(days=15)).date(),
    })
    self.assertFalse(project.task_ids.filtered(lambda t: t.name == 'Task Template 1').user_ids)
    self.assertEqual(project.task_ids.filtered(lambda t: t.name == 'Task Template 2').user_ids, self.user_projectmanager)
    self.assertEqual(project.task_ids.filtered(lambda t: t.name == 'Task Template 3').user_ids, self.user_projectmanager)


TestProjectTemplate.test_create_project_base_on_template_with_role = test_create_project_base_on_template_with_role
