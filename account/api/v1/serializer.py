from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:

        model = User
        fields = ['username','password','password_confirm','email','date_of_birth']
        extra_kwargs={
            'password' : {'write_only':True},
            'email': {'required': True},
            'date_of_birth' : {'required':True}
        }

    def validate_email(self, value):
         print('value')
         if (not value):

            raise serializers.ValidationError({'details': 'you must enter a valid email'})

         return value

    def save(self,**kwargs):
        print(self.validated_data['username'])
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            date_of_birth=self.validated_data['date_of_birth']
        )


        if(self.validated_data['password'] != self.validated_data['password_confirm']):
          raise  serializers.ValidationError({'details':'passwords didnt match'})


        user.set_password(self.validated_data['password'])
        user.save()
        return user




