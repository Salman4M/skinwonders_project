from content.models import ContactUs,CV,Vacancies,Blog

from rest_framework import serializers

from django.utils.html import strip_tags



class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields= ("subject","fullname","email","message")


    def validate_fullname(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("Full name can only contain alphabetic characters and one space between name and surname.")
        
        # Check if there is only one space between name and surname
        parts = value.split(' ')
        if len(parts) != 2:
            raise serializers.ValidationError("Full name should have one space between name and surname.")

        return value


class CVSerializer(serializers.ModelSerializer):
    vacancy = serializers.CharField(read_only=True)
    class Meta:
        model=CV
        fields = "__all__"


    def validate_fullname(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("Full name can only contain alphabetic characters and one space between name and surname.")
        
        parts = value.split(' ')
        print(parts)
        if len(parts) != 2:
            raise serializers.ValidationError("Full name should have exactly one space between name and surname.")

        return value

    # def validate_age(self,value):
    #     for i in value:
    #         if not i.isdigit():
    #             raise serializers.ValidationError({"error":"Only contains numbers"})
        
    #     return value


from services.choices import SUBJECTS,LOCATIONS,DEPARTMENTS,DATE
from django.utils.translation import gettext_lazy as _

class VacanciesSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='get_location_display')
    department = serializers.CharField(source='get_department_display')

    class Meta:
        model = Vacancies
        fields = ("location", "department", "jobtitle")

    def get_location_display(self, obj):
        return _(dict(LOCATIONS).get(obj.location))

    def get_department_display(self, obj):
        return _(dict(DEPARTMENTS).get(obj.department))




class BlogSerializer(serializers.ModelSerializer):
    type=serializers.CharField(source='get_type_display')
    date=serializers.CharField(source='get_date_display')

    class Meta:
        model = Blog
        fields = ("title","image","id","type","date")


from html import unescape
class CustomRichTextField(serializers.Field):

    def to_representation(self, value):
        # Remove HTML tags
        plain_text = strip_tags(value)
        # Convert HTML entities to characters
        plain_text = unescape(plain_text)
        # Remove newline and carriage return characters
        plain_text = plain_text.replace('\n','').replace('\r','')
        # Remove leading and trailing whitespace
        plain_text = plain_text.strip()
        return plain_text

    def get_type_display(self,obj):
        return _(dict(SUBJECTS).get(obj.subject))
    
    def get_date_display(self,obj):
        return _(dict(DATE).get(obj.date))

class BlogDetailSerializer(serializers.ModelSerializer):
    description_ = CustomRichTextField(source="description",read_only=True)
    class Meta:
        model = Blog
        exclude = ("type","date","description")
    