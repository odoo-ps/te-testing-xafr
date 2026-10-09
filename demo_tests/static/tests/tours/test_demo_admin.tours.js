import {_t} from "@web/core/l10n/translation";
import {registry} from '@web/core/registry';

registry.category("web_tour.tours").add("te_demo_admin_tour", {
    steps: () => [
        {
            content: _t("Selecting the app project from the main menu."),
            trigger: ".o_app[data-menu-xmlid='project\\.menu_main_pm']",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_project_kanban_body",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            content: "Adds a delay to let the UI load before proceeding with the next step.",
            trigger: "body",
            run() {
                return new Promise(resolve => setTimeout(resolve, 1000));
            },
        },
        {
            trigger: ".o-kanban-button-new",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_field_widget[name='display_name'] > .o_input",
            run: "edit Test Project Task",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_kanban_edit",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o-dropdown .o_input",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o-dropdown-item:nth-child(2) > div",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_form_button_save",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o-dropdown .o_input",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o-dropdown-item:nth-child(1) > div",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_form_button_save",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            content: "Adds a delay to let the form save and avoid dirty state.",
            trigger: "body",
            run() {
                return new Promise(resolve => setTimeout(resolve, 1000));
            },
        },
    ]
})