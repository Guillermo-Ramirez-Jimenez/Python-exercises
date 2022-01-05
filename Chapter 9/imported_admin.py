from imported_admin_module import *

admin=Admin("over", "lord", power=9000)
admin.describe_user()
print(admin.privileges.show_privileges())