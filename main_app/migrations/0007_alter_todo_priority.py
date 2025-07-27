from django.db import migrations,models

def convert_priority_to_int(apps, schema_editor):
    Todo = apps.get_model('main_app', 'Todo')
    mapping = {'High': 1, 'Medium': 2, 'Low': 3, 'None': 4}
    for todo in Todo.objects.all():
        if todo.priority in mapping:
            todo.priority = mapping[todo.priority]
            todo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_todo_priority'),
    ]

    operations = [
        migrations.RunPython(convert_priority_to_int),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(
                choices=[(1, 'High'), (2, 'Medium'), (3, 'Low'), (4, 'None')],
                default=4,
            ),
        ),
    ]
