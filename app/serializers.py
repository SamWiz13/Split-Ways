from rest_framework.serializers import Serializer,ModelSerializer
from .models import Table, Order, OrderItem, MenuItem, Category

from .models import CustomUser

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):

        if CustomUser.objects.check_user(validated_data):
            validated_data['is_active'] = True
            user = super().create(validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return {"message":"user created"}
        else:
            return {"message":"user already exists"}

class LoginSerializer(Serializer):
    username = CharField()
    password = CharField() 
