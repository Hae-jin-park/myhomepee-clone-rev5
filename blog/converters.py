from django.urls.converters import StringConverter

class KoreanSlugConverter(StringConverter):
  regex = '[-\w]+'