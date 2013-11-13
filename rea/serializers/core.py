from rest_framework import serializers


class REASerializer(serializers.ModelSerializer):

    mongoID = serializers.CharField(required=False)
