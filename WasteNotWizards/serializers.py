from .models import Receiver, Provider, Post, Reservation, User
from rest_framework import serializers


# Serializer for Provider model to include all fields
class ProviderListSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )
    class Meta:
        model = Provider
        fields = "__all__"


# Serializer for Provider model to include all fields
class ProviderProfileSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )
    class Meta:
        model = Provider
        fields = ['user', 'address', 'Provider_type', 'email',
                   'phone_number', 'username'
        ]


# Serializer for Receiver model to include all fields
class ReceiverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = "__all__"


# Serializer for Receiver model to include all fields
class ReceiverProfileSerializer(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all()
    )
    class Meta:
        model = Receiver
        fields = [
            'user', 'address', 'email', 'phone_number', 'username',
        ]


# Serializer for Post model to include all fields
class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


# Serializer for Reservation model to include all fields
class ReservationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
