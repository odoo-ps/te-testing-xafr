from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    task_type = fields.Selection(
        [
            ("avenger", "Avengers Assistance"),
            ("technical", "Technical"),
            ("design", "Design"),
            ("manual", "Manual"),
            ("other", "Other"),
        ],
        groups="project.group_project_manager",
        # required=True,
    )

    priority = fields.Selection(compute="_compute_priority", store=True)

    @api.depends('task_type')
    def _compute_priority(self):
        for task in self:
            if task.task_type == "avenger":
                task.priority = "3"
            elif task.task_type == "other":
                task.priority = "0"
            else:
                task.priority = "1"
