# Generated by Django 3.1 on 2020-12-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student_id',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='subject_assignment_marks',
            new_name='cie_1',
        ),
        migrations.RenameField(
            model_name='studentresult',
            old_name='subject_exam_marks',
            new_name='cie_2',
        ),
        migrations.AddField(
            model_name='studentresult',
            name='cie_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='lab_Marks',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='quiz_1',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='quiz_2',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='quiz_3',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='studentresult',
            name='selfstudy_marks',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
    ]
