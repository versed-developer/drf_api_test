from rest_framework import serializers
from ...core.loading import get_model

TABLE = get_model('timelog', 'TimeLog')
PROJECT_TABLE = get_model('project', 'Project')
APP = 'timelog_api'
fields = ('project', 'description', 'start_time', 'end_time')


class TimeLogSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name=APP + ':update')
    delete_url = serializers.HyperlinkedIdentityField(view_name=APP + ':delete')

    class Meta:
        model = TABLE

        fields = fields + ('update_url', 'delete_url')

    def update(self, instance, validated_data):
        project_name = validated_data.get('project', instance.project.name)
        instance.project = PROJECT_TABLE.objects.get(name=project_name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


class TimeLogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TABLE

        fields = fields

    def create(self, validated_data):
        TABLE.objects.create(**validated_data)
        return validated_data

