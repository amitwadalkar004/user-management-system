ROLE_PERMISSIONS = {
    "OWNER": {
        "view_project",
        "update_project",
        "delete_project",
        "add_user",
        "view_user",
        "remove_user",
    },
    "ADMIN": {
        "view_project",
        "update_project",
        "add_user",
        "view_user",
        "remove_user",
    },
    "MEMBER": {
        "view_project",
        "view_user",
    },
    "VIEWER": {
        "view_project",
        "view_user",
    },
}
