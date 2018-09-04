from rest_framework import serializers
from .models import Tutorialmenu, Tutorialtopicsmenu

class TutorialMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tutorialmenu
        fields = ('tutorialmenuid', 'tutorialmenuname', 'tutorialmenudesc',)

class TutorialTopicsMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorialtopicsmenu
        fields = ('tutorialtopicsmenuid', 'tutorialtopicsmenuname', 'tutorialtopicsmenudescription',)

