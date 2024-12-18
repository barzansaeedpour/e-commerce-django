

## session 1:

- creating the project and apps
- creating urls
- creating templates
- creating views

## session 2:

- Custom User

    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#substituting-a-custom-user-model
    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example

- User Manager

    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model

- User Creation & Changing Forms
    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example


- User Register
    - UserRegistrationForm
    - UserRegisterView
    - urlpatterns
    - accounts/templates/register.html

## session 3:

    - Generate and send random code to user for registration
      - Otp Model
      - OtpCodeAdmin
    
    - Register & Sessions
      - https://docs.djangoproject.com/en/5.1/topics/http/sessions/
      - When the sessions are saved?
      - utils (send otp code by sms)
      - accounts.views (UserRegisterView.post)
      - accounts.forms (VerifyCodeForm)
      - accounts.views (UserRegisterVerifyCodeView)
      - accounts.templates (verify.html)
      - utils (kavenegar)
    
    - Static & Media files
      - What is the difference?
      - home/static/home/css -> base.html, home.html
      - Static files directory -> for all of the apps -> base.html

## Session 4:
    - Models (home/models)
        - Category
            - verbose_name, verbose_name_plural
        - Product (Image Field, Pillow) -> Python data time field
    
    - Register Models in admin

    - Media Files (https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-MEDIA_ROOT)
        - MEDIA_ROOT -> Absolute filesystem path to the directory that will hold user-uploaded fiels
        - MEDIA_URL -> Url that handles the media served from MEDIA_ROOT

    - Product Detail
        - home/HomeView
        - home/templates/home/home.html
        - Bootstrap Card (https://getbootstrap.com/docs/4.0/components/card/)
        - Image is not showing -> serving files uploaded by a user during development (https://docs.djangoproject.com/en/5.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development)
        - add static to urlpattern (A/urls.py) 
        - add a tag to redirect the user to detail page
        - home/views (ProductDetailView)

## Session 5:
    - Django-storages (Bucket)
        - pip install django-storages
    - settings
        - add 'storages' to installed apps
        - docs: https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html
    - Add Variables to the settings
    - pip install boto3

## Session 6:
    - user passes test
        - https://docs.djangoproject.com/en/5.1/topics/auth/default/#limiting-access-to-logged-in-users
    - Login, Logout
        - accounts/forms -> UserLoginForm
        - accounts/view -> UserLogoutView, UserLoginView
        - accounts/urls -> login, logout
        - templates/navbar -> login, logout
        - templates/accounts -> login
    -