from django.db import models
import bcrypt, re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[^\W_]+(-[^\W_]+)?$', re.U)
PW_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')

# Create your models here.

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = []
        # check name and last name length
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 3:
            errors.append("First and Last name should be more than 2 characters.")

        if len(postData['gender']) < 3:
            errors.append("Gender fields required.")
        # check password
        if not PW_REGEX.match(postData['password']):
            errors.append('Password is invalid. Cannot be fewer than 8 characters.')
        #check name for character
        if not re.match(NAME_REGEX, postData['first_name']) or not re.match(NAME_REGEX, postData['last_name']):
            errors.append("User name/last name should contains only letters, no capitals!")
        # check email
        if not re.match(EMAIL_REGEX, postData['email']):
            errors.append("Invalid email format.")
        #search for the email
        if len(User.objects.filter(email=postData['email'])) > 0:
            errors.append("email already in use")
        # check password
        if postData['password'] != postData['conf_password']:
            errors.append("Password doesn't match.")
        return errors

    def create_user(self, postData):
        hashed_pw = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = User.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],gender=postData['gender'],age=postData['age'],email=postData['email'],hashed_pw=hashed_pw)
        return new_user.id

    def login_validator(self, postData):
        errors = []
        if len(self.filter(email=postData['email'])) > 0:
             # check this user's password
             user = self.filter(email=postData['email'])[0]
             print(user)
             if not bcrypt.checkpw(postData['password'].encode(), user.hashed_pw.encode()):
                  errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect.')
        if errors:
            return errors
        return user
class User(models.Model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    gender = models.CharField(max_length=225)
    age = models.IntegerField(default=0)
    email = models.TextField(max_length=225)
    hashed_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.first_name
