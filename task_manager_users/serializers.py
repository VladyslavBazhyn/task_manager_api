from rest_framework import serializers

from django.contrib.auth import get_user_model

from task_manager_users.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    """Base user serializer for all basic needs"""
    class Meta:
        model = User
        fields = [
            "email", "first_name", "last_name", "nickname", "image"
        ]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        """Create new user with encrypted password and return it."""
        return get_user_model().objecta.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update user: set password and return this user."""
        password = validated_data.get("password", None)
        validated_data.pop("password2", None)
        validated_data.pop("old_password", None)

        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

