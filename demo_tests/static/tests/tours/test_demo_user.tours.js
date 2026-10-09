import {registry} from '@web/core/registry';

registry.category("web_tour.tours").add("te_demo_user_tour", {
    steps: () => [
        {
            trigger: ".o_card_record:nth-child(5) div[name='action_view_tasks']",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_technical_modal footer > button:nth-child(2)",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_kanban_group",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            trigger: ".o_record_main > div:nth-child(2) > span",
            run: "click",
            tooltipPosition: "bottom"
        },
        {
            content: "Raises an error if the element is not found. Allows us to check access rights.",
            trigger: ".o-dropdown .o_input",
            run() {
                if (document.querySelector(".o-dropdown .o_input")) {
                    throw new Error("The dropdown input should not be visible");
                }
            }
        },
    ]
})