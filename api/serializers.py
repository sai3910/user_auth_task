from rest_framework import serializers
from api.models import User, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('photo',)

class UserUpdateSerializer(serializers.HyperlinkedModelSerializer):
    """
    Upadate seralizer
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email','username' ,'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True},'email':{'read_only': True},'username':{'read_only': True}}

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile
        instance.email = validated_data.get('email', instance.email)
        instance.last_name = validated_data.get('last_name')
        instance.first_name = validated_data.get('first_name')

        instance.save()

        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    create serializer
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email','username', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    