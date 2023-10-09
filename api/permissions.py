from rest_framework.permissions import BasePermission

class CustomUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_authenticated
      
class CustomUserDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_authenticated
        elif request.method == 'PUT':
            return request.user.is_authenticated
        elif request.method == 'DELETE':
            return request.user.is_authenticated

class PostsPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_authenticated
      
class PostsDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'PUT':
            return request.user.is_authenticated
        elif request.method == 'DELETE':
            return request.user.is_authenticated
        
class CategoryPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        if request.method == 'POST':
            return request.user.is_staff
                
class CategoryDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        if request.method == 'PUT':
            return request.user.is_staff
        if request.method == 'DELETE':
            return request.user.is_staff
