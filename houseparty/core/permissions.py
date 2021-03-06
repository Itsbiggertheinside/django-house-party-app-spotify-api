from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class ListCreateOrIsOwner(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        return super(ListCreateOrIsOwner, self).has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or request.user.is_staff or request.user 
            and request.user.profile == obj.host)