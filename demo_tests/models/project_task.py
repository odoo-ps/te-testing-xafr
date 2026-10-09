from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_type = fields.Selection(
        [
            ("technical", "Technical"),
            ("design", "Design"),
            ("manual", "Manual"),
            ("other", "Other"),
        ],
        string="Task Type",
    )
    # task_warning_type = fields.Char(string="Task Type")
