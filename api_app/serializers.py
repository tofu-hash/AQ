from rest_framework import serializers
from api_app.models import Question, Theme
from django.core.validators import *
from django.contrib.auth import get_user_model  # If used custom user model
import string

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    def validate_username(self, username):
        if len(username) >= 5:
            valid_characters = string.ascii_lowercase + string.ascii_uppercase + ''.join(
                [str(i) for i in range(10)]) + '._'

            for character in username:
                if str(character) not in valid_characters:
                    raise ValidationError(
                        'Имя пользователя должно состоять только из букв, цифр, нижнего подчеркивания ("_") и точки')
            return username
        raise ValidationError(
            'Минимальная длинна имени пользователя - 5 символов')

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("username", "password",)


class ThemesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('name',)


class GetQuestionSerializer(serializers.ModelSerializer):
    themes = ThemesSerializer(many=Theme)

    class Meta:
        model = Question
        fields = ("title", "description", "themes",)
        depth = 1


class CreateQuestionSerializer(serializers.ModelSerializer):
    themes = serializers.CharField(max_length=200)

    def create(self, validated_data):
        question = Question()
        question.author = self.context['request'].user
        question.title = validated_data['title']
        question.description = validated_data['description']

        themes = []
        for theme_name in validated_data['themes'].split(', '):
            theme_name = theme_name.lower().strip()
            if not Theme.objects.filter(name=theme_name):
                theme = Theme()
                theme.name = theme_name
                theme.save()
        for theme in themes:
            question.themes.add(theme)
        question.save()

        return question

    class Meta:
        model = Question
        fields = ("title", "description", "themes",)
