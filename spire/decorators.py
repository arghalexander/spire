from django.core.exceptions import PermissionDenied
from members.models import Member
from functools import wraps

def member_access(level=1):
    def decorator(view):
        @wraps(view)
        def wrapper(request, *args, **kwargs):
           	#staff can do anything
	    	#if request.user.is_staff:
	    	#	return view(request, *args, **kwargs)

	    	member = Member.objects.get(user=request.user)
	    	access_level = member.membership_level.access_level

	    	if access_level >= level:
	    		return view(request, *args, **kwargs)
	    	else:
	    		raise PermissionDenied
        return wrapper
    return decorator