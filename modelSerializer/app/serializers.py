from rest_framework import serializers
from .models import *


# 1. it will automatically generate a set of fields for you, based on the model
# 2. It will automatically generate validators for the serializer, such as unique_together validators.
# 3. it includes simple default implementations of create() and update()

# class StudentSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(read_only=True)
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']
#         # fields = '__all__'
#         # exclude = ['id']

# METHOD 2
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = ['id', 'name', 'roll', 'city']
#         read_only_fields = ['name', 'roll']
# class StudentSerializer(serializers.ModelSerializer):

# METHOD 3
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        extra_kwargs = {
                'name': {
                    'read_only': True,
                    'required': True,
                    # 'write_only': True,
                }
            }


    # FIELD LEVEL VALIDATION
    # This method is called when serializer.is_valid() method is called
    def validate_roll(self, value):
        if value > 200:
            raise serializers.ValidationError("Seats Full")
        return value

    # OBJECT LEVEL VALIDATION
    def validate(self, data):
        n = data.get('name')
        c = data.get('city')
        if n.lower() == "vaibhav" and c.lower() == "chittorgarh":
            raise serializers.ValidationError("City Must Be chittorgarh")
        return data