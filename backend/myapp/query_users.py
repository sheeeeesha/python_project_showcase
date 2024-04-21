# query_users.py

from myapp.models import User  # Replace 'myapp' with the name of your Django app

# Query all users
all_users = User.objects.all()

# Print all users
for user in all_users:
    print(user.name, user.email)
