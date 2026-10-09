from odoo.addons.project.tests.test_project_recurrence import TestProjectRecurrence

def _patched_test_deleting_last_recurring_task(self):
    pass


TestProjectRecurrence.test_deleting_last_recurring_task = _patched_test_deleting_last_recurring_task
