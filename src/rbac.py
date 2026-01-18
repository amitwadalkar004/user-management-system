from fastapi import HTTPException, status
from constants.role_permissions import ROLE_PERMISSIONS
from src.project_user.schema import project_user


def check_project_permission(
    db,
    user_id: int,
    project_id: int,
    required_permission: str
):
    mapping = (
        db.query(project_user)
        .filter(
            project_user.user_id == user_id,
            project_user.project_id == project_id,
            project_user.is_deleted == False
        )
        .first()
    )

    if not mapping:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User not part of this project"
        )

    permissions = ROLE_PERMISSIONS.get(mapping.role, set())

    if required_permission not in permissions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied"
        )

    return True
