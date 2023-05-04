from rest_framework import serializers


# PRIORITY = Validators > Field level validation > object level validation

class StudentSerializer():
    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

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


# # VALIDATORS
# def start_with_v(value):
#     if value[0].lower() != 'v':
#         raise serializers.ValidationError("First Character must start with V")

# class StudentSerializer():
#     name = serializers.CharField(max_length=50, validators=[start_with_v])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=50)
