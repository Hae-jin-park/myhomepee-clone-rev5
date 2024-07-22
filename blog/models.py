from django.db import models
from django.conf import settings
from django.urls import reverse

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# Create your models here.
# class Category(BaseModel):
#     parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
#     name = models.CharField(max_length=100) 
#     slug = models.SlugField(null=True)

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse("model_detail", kwargs={"slug": self.slug})
    

#     class Meta:
#         #enforcing that there can not be two categories under a parent with same slug
        
#         # __str__ method elaborated later in post.  use __unicode__ in place of

#         unique_together = ('slug', 'parent',)    
#         verbose_name_plural = "categories"     

#     def __str__(self):                           
#         full_path = [self.name]                  
#         k = self.parent
#         while k is not None:
#             full_path.append(k.name)
#             k = k.parent
#         return ' -> '.join(full_path[::-1])  
    
class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="my_post_set", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    # slug = models.SlugField(null=False, unique=True, allow_unicode=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.pk])
    

class Category(BaseModel):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
    title = models.CharField(max_length=100) 
    slug = models.SlugField(null=False, unique=True, allow_unicode=True)

    def __str__(self):
        return self.title

    class Meta:
        #enforcing that there can not be two categories under a parent with same slug
        
        # __str__ method elaborated later in post.  use __unicode__ in place of

        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"     

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' -> '.join(full_path[::-1])  