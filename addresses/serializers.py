from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from users.models import User
from users.serializers import UpdateUserSerializer

from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    house_no = serializers.CharField(max_length=5)
    street_name = serializers.CharField(max_length=500)
    bus_stop = serializers.CharField(max_length=60)
    lga = serializers.CharField(max_length=60)
    postal_code = serializers.CharField(default=0)
    state = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)
    is_default = serializers.BooleanField(default=False)

    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "house_no",
            "street_name",
            "bus_stop",
            "lga",
            "postal_code",
            "state",
            "country",
            "is_default",
        ]

    # def update(self, instance, validated_data):
    #     instance.house_no = validated_data.get("house_no", instance.house_no)
    #     instance.street_name = validated_data.get(
    #         "street_name", instance.street_name
    #     )
    #     instance.bus_stop = validated_data.get("bus_stop", instance.bus_stop)
    #     instance.lga = validated_data.get("lga", instance.lga)
    #     instance.postal_code = validated_data.get(
    #         "postal_code", instance.postal_code
    #     )
    #     instance.state = validated_data.get("state", instance.state)
    #     instance.country = validated_data.get("country", instance.country)
    #     instance.is_default = validated_data.get(
    #         "is_default", instance.is_default
    #     )

    #     instance.save()

    #     return instance


class UpdateAddressSerializer(serializers.ModelSerializer):
    house_no = serializers.CharField(max_length=5)
    street_name = serializers.CharField(max_length=500)
    bus_stop = serializers.CharField(max_length=60)
    lga = serializers.CharField(max_length=60)
    postal_code = serializers.IntegerField(default=0)
    state = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)
    is_default = serializers.BooleanField(default=False)

    class Meta:
        model = Address
        fields = [
            "user",
            "house_no",
            "street_name",
            "bus_stop",
            "lga",
            "postal_code",
            "state",
            "country",
            "is_default",
        ]

    def update(self, instance, validated_data):
        instance.house_no = validated_data.get("house_no", instance.house_no)
        instance.street_name = validated_data.get(
            "street_name", instance.street_name
        )
        instance.bus_stop = validated_data.get("bus_stop", instance.bus_stop)
        instance.lga = validated_data.get("lga", instance.lga)
        instance.postal_code = validated_data.get(
            "postal_code", instance.postal_code
        )
        instance.state = validated_data.get("state", instance.state)
        instance.country = validated_data.get("country", instance.country)
        instance.is_default = validated_data.get(
            "is_default", instance.is_default
        )

        instance.save()

        return instance
