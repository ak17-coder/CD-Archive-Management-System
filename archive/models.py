from django.db import models

class CD(models.Model):
    cd_label = models.CharField(max_length=200)
    folder_name = models.CharField(max_length=255)
    folder_path = models.TextField()
    category = models.CharField(max_length=100)
    year = models.IntegerField()
    number_of_files = models.IntegerField()
    size = models.CharField(max_length=50)
    condition = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cd_label