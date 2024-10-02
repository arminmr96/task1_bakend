import os
from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)
    
    class Meta:
        model = Post
        fields = "__all__"
        
    def validate_image(self, value):
        ext = os.path.splitext(value.name)[1].lower()
        print("--------------------", ext)
        if ext not in ['.jpg', '.jpeg']:
            raise serializers.ValidationError("The image format must be JPEG (jpg or jpeg)")
        else:
            return value