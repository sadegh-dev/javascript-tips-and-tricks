from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, full_name) :
        if not email :
            raise ValueError('you must Enter email')
        if not full_name :
            raise ValueError('you must Enter full name')
        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password, full_name) :
        user = self.create_user(email, password, full_name)
        user.is_admin = True
        user.save(using=self._db)
        return user