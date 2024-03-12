from django.db import models

# Create your models here.

class offer(models.Model):
    tittle_offer = models.CharField(max_length=200)
    description_offer = models.TextField()
    group_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    instruments = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    years = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    applicants = models.CharField(max_length=1000, blank=True, null=True)

    def add_applicant(self, applicant):
        if self.applicants:
            applicants_list = self.applicants.split(',')
            if applicant not in applicants_list:
                applicants_list.append(applicant)
        else:
            applicants_list = [applicant]

        self.applicants = ','.join(applicants_list)
        self.save()