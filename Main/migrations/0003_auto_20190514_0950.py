# Generated by Django 2.1.7 on 2019-05-14 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20190513_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=128, unique=True, verbose_name='账户类型')),
            ],
            options={
                'verbose_name': '账户类型',
                'verbose_name_plural': '账户类型',
            },
        ),
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('pass_word', models.CharField(max_length=16, verbose_name='密码')),
                ('acc_type', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Main.Account_type', verbose_name='账户类型')),
            ],
            options={
                'verbose_name': '管理员',
                'verbose_name_plural': '管理员',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=128, unique=True, verbose_name='课程名字')),
            ],
            options={
                'verbose_name': '课程表',
                'verbose_name_plural': '课程表',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dep_name', models.CharField(max_length=32, unique=True, verbose_name='部门名称')),
            ],
            options={
                'verbose_name': '部门分类',
                'verbose_name_plural': '部门分类',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('education', models.CharField(max_length=128, unique=True, verbose_name='学历')),
            ],
            options={
                'verbose_name': '学历',
                'verbose_name_plural': '学历',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=128, unique=True, verbose_name='班级名称')),
                ('course', models.ManyToManyField(to='Main.Course', verbose_name='多对多关系')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Department', verbose_name='班级所在系部')),
            ],
            options={
                'verbose_name': '班级表',
                'verbose_name_plural': '班级表',
            },
        ),
        migrations.CreateModel(
            name='Inform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('filed_name', models.CharField(max_length=128, null=True, unique=True, verbose_name='上传文件的文件名')),
                ('local_file', models.CharField(max_length=128, null=True, unique=True, verbose_name='保存到本地的文件名')),
                ('times', models.DateField(auto_now_add=True, verbose_name='发布时间')),
                ('isActive', models.BooleanField(default=True)),
                ('send_from_dpt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='发送教师对应部门', to='Main.Department', verbose_name='来自哪个部门')),
            ],
            options={
                'verbose_name': '消息通知',
                'verbose_name_plural': '消息通知',
            },
        ),
        migrations.CreateModel(
            name='Stu_ate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=128, unique=True, verbose_name='学生状态(/在校/...)')),
            ],
            options={
                'verbose_name': '学生状态(在校...)',
                'verbose_name_plural': '学生状态(在校...)',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('study_num', models.BigIntegerField(verbose_name='学号')),
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('gender', models.BooleanField(default=True, verbose_name='性别男')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('contact', models.CharField(max_length=16, unique=True, verbose_name='联系方式')),
                ('parent_tel', models.CharField(max_length=16, unique=True, verbose_name='监护人联系方式')),
                ('pass_word', models.CharField(max_length=16, verbose_name='密码')),
                ('isactive', models.BooleanField(default=True, verbose_name='是否启用')),
                ('acc_type', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='Main.Account_type', verbose_name='账户类型默认为学生')),
                ('department', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='Main.Department', verbose_name='所在系部')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Grade', verbose_name='学生所在班级')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Stu_ate', verbose_name='学生状态(在校/..)')),
            ],
            options={
                'verbose_name': '学生用户',
                'verbose_name_plural': '学生用户',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=16, verbose_name='用户名')),
                ('gender', models.BooleanField(default=True, verbose_name='性别')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('pass_word', models.CharField(max_length=16, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='邮箱')),
                ('contact', models.CharField(max_length=16, unique=True, verbose_name='联系方式')),
                ('address', models.CharField(max_length=256, verbose_name='家庭地址')),
                ('acc_type', models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='Main.Account_type', verbose_name='账户类型')),
            ],
            options={
                'verbose_name': '教师用户',
                'verbose_name_plural': '教师用户',
            },
        ),
        migrations.CreateModel(
            name='Work_arrange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=512, verbose_name='工作标题')),
                ('content', models.CharField(max_length=4096, verbose_name='工作内容')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('finish', models.DateTimeField(auto_now=True, verbose_name='完成时间记录最后一次修改数据的时间')),
                ('department', models.ForeignKey(max_length=64, on_delete=django.db.models.deletion.CASCADE, to='Main.Department', verbose_name='部门')),
                ('tea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Teacher', verbose_name='对应教师')),
            ],
            options={
                'verbose_name': '工作安排',
                'verbose_name_plural': '工作安排',
            },
        ),
        migrations.CreateModel(
            name='Work_state',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=64, verbose_name='工作状态')),
            ],
            options={
                'verbose_name': '工作状态',
                'verbose_name_plural': '工作状态',
            },
        ),
        migrations.CreateModel(
            name='Work_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=64, verbose_name='工作类型')),
            ],
            options={
                'verbose_name': '工作类型',
                'verbose_name_plural': '工作类型',
            },
        ),
        migrations.CreateModel(
            name='ZhiCheng',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('call', models.CharField(max_length=64, unique=True, verbose_name='职称')),
            ],
            options={
                'verbose_name': '职称',
                'verbose_name_plural': '职称',
            },
        ),
        migrations.AddField(
            model_name='work_arrange',
            name='work_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Work_state', verbose_name='工作状态'),
        ),
        migrations.AddField(
            model_name='work_arrange',
            name='work_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Work_type', verbose_name='工作类型'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='call',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.ZhiCheng', verbose_name='职称'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Department', verbose_name='所属系部'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Education', verbose_name='学历'),
        ),
        migrations.AddField(
            model_name='inform',
            name='send_from_tea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='来自哪个教师', to='Main.Teacher', verbose_name='来自'),
        ),
        migrations.AddField(
            model_name='inform',
            name='send_to_dpt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='接收教师对应部门', to='Main.Department', verbose_name='发送给哪个部门'),
        ),
        migrations.AddField(
            model_name='inform',
            name='send_to_tea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='发送给哪个教师', to='Main.Teacher', verbose_name='发送给哪个教师'),
        ),
        migrations.AddField(
            model_name='grade',
            name='teacher',
            field=models.ManyToManyField(to='Main.Teacher', verbose_name='班级对应教师'),
        ),
        migrations.AddField(
            model_name='admin_user',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.Department', verbose_name='部门'),
        ),
    ]
