from django.db import models
from django.contrib.auth.models import User

# User Profile model
class UserProfile(models.Model):
    PRONOUN_CHOICES = [
        ('he/him', 'He/Him'),
        ('she/her', 'She/Her'),
        ('they/them', 'They/Them'),
        ('he/they', 'He/They'),
        ('she/they', 'She/They'),
        ('custom', 'Custom'),
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="User"
    )
    name = models.CharField(max_length=100, verbose_name="Full Name")
    pronouns = models.CharField(
        max_length=10, 
        choices=PRONOUN_CHOICES,
        blank=True, 
        verbose_name="Preferred Pronouns"
        )
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    district = models.CharField(max_length=100, blank=True, verbose_name="District")
    state = models.CharField(max_length=100, blank=True, verbose_name="State")
    zip_code = models.CharField(max_length=10, blank=True, verbose_name="Zip Code")
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True, verbose_name="Profile Picture"
    )
    open_to_work = models.BooleanField(default=True, verbose_name="Open to Work")
    resume = models.FileField(
        upload_to='resumes/', blank=True, null=True, verbose_name="Resume"
    )
    bio = models.TextField(blank=True, verbose_name="Biography")

    def __str__(self):
        return self.user.username
    
# About model
class About(models.Model):
    user_profile = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="about_me",
        verbose_name="User Profile"
    )
    title = models.CharField(max_length=100, verbose_name="Title")
    about_me = models.TextField(verbose_name="About Me")

    def __str__(self):
        return f"About {self.user_profile.user.username}"

# Experience model
class Experience(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="experiences",
        verbose_name="User Profile"
    )
    title = models.CharField(max_length=150, verbose_name="Job Title")
    company = models.CharField(max_length=100, verbose_name="Company Name")
    description = models.TextField(verbose_name="Job Description")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")

    def __str__(self):
        return f"{self.title} at {self.company}"

# Education model
class Education(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="educations",
        verbose_name="User Profile"
    )
    degree = models.CharField(max_length=100, verbose_name="Degree")
    school_name = models.CharField(max_length=200, verbose_name="School/University")
    grade = models.CharField(max_length=50, verbose_name="Grade or CGPA")
    course = models.CharField(max_length=100, verbose_name="Course")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")

    def __str__(self):
        return f"{self.degree} from {self.school_name}"

# Certificate model
class Certificate(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="certificates",
        verbose_name="User Profile"
    )
    title = models.CharField(max_length=200, verbose_name="Certificate Title")
    issued_by = models.CharField(max_length=200, verbose_name="Issued By")
    issued_on = models.DateField(verbose_name="Issued On")
    certificate_url = models.URLField(blank=True, null=True, verbose_name="Certificate URL")

    def __str__(self):
        return f"{self.title} issued by {self.issued_by}"

# Project model
class Project(models.Model):
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="projects",
        verbose_name="User Profile"
    )
    title = models.CharField(max_length=200, verbose_name="Project Title")
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(null=True, blank=True, verbose_name="End Date")
    description = models.TextField(verbose_name="Project Description")
    project_url = models.URLField(blank=True, null=True, verbose_name="Project URL")

    def __str__(self):
        return self.title

# Skill model
class Skill(models.Model):
    PROFICIENCY_LEVELS = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert"),
    ]
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="skills",
        verbose_name="User Profile"
    )
    skill = models.CharField(max_length=100, verbose_name="Skill")
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_LEVELS,
        default="Beginner",
        verbose_name="Proficiency Level"
    )

    def __str__(self):
        return f"{self.skill} ({self.proficiency})"

# Language model
class Language(models.Model):
    PROFICIENCY_LEVEL = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Expert", "Expert"),
    ]
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name="languages",
        verbose_name="User Profile"
    )
    language = models.CharField(max_length=100, verbose_name="Language")
    proficiency = models.CharField(
        max_length=100,
        choices=PROFICIENCY_LEVEL,
        default="Beginner",
        verbose_name="Proficiency Level"
    )

    def __str__(self):
        return f"{self.language} ({self.proficiency})"
