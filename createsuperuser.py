from django.contrib.auth.models import User

superuser = User.objects.create_superuser(username=НИКНЕЙМ, email=ПОЧТА, password=ПАРОЛЬ)
superuser.save()
