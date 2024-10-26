from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email, full_name, password):
        if not phone_number:
            raise ValueError('user muset have phone number')
        if not email:
            raise ValueError('user muset have email')
        if not full_name:
            raise ValueError('user muset have full_name')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email),
                          full_name=full_name, password=password)
        user.set_password(password)
        user.save(using = self._db)
        # user.save()
        return user

    def create_superuser(self, phone_number, email, full_name, password):
        user = self.create_user(phone_number, email, full_name, password)
        user.admin = True
        user.save()
        return user