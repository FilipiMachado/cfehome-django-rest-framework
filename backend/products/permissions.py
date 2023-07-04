from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("products.add_product"):  # Ex: "app_name.verb_model_name"
                return True
            if user.has_perm("products.delete_product"):
                return True
            if user.has_perm("products.change_product"):
                return True
            if user.has_perm("products.view_product"):
                return True
            return False
        return False

    """ def has_object_permission(self, request, view, obj):
        return obj.owner == request.user """
