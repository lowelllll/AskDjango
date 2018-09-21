from rest_framework import permissions

class IsAuthorUpdateOrReaonly(permissions.BasePermission):
    # 인증된 유저에 한해, 목록조회/포스팅 등록을 허용.
    def has_permission(self, request, view):
        return request.user.is_authenticated

    # superuser에게는 삭제 권한만 부여하고
    # 작성자에게는 수정권한 부여
    def has_object_permission(self, request, view, obj):
        # 조회요청은 모두 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 삭제요청은 superuser에게만 허용
        if request.method == 'DELETE':
            return request.user.is_superuser

        # put 요청은 작성자일 경우에만 요청 허용
        return obj.author == request.user