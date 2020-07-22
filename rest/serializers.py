from rest_framework import serializers
from .models import Info


class AddTwoNumberSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()


class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        print("context on serializer", self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance


class InfoModelSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['name', 'address', 'message', 'id']
        read_only_fields = ['id']

    @staticmethod
    def get_message(obj):
        name = obj.name
        return f"Hi, My name is {name}"

    @staticmethod
    def validate_name(name):
        if len(name) <= 1:
            raise serializers.ValidationError("Length of name should be greater than 1")
        return name

    def validate(self, data):
        name = data['name']
        address = data['address']
        if name == address:
            raise serializers.ValidationError("name and address cannot be same")
        return data
