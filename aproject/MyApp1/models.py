from django.db import models



# Create your models here.
class GradesmanaGrade(models.Manager):
    def get_queryset(self):
        return super(GradesmanaGrade,self).get_queryset().filter(ggnumber=23)

    def CreatStundent(self,name,gender,age,time,grade,Delete=False,):
        stu = self.model()
        stu.sname = name
        stu.sgender = gender
        stu.sage = age
        stu.stime = time
        stu.sgrade = grade
        return stu




class Grades (models.Model):
    graobj = models.Manager()
    graobj2 = GradesmanaGrade()
    gname = models.CharField(max_length=20, verbose_name="班级名")
    gtime = models.DateTimeField()
    ggnumber = models.IntegerField()
    gnnumber = models.IntegerField()
    gDelete = models.BooleanField(default=False)

    #class Meta:
        #verbose_name = "班级表班级表班级表"

    @classmethod
    def creatgrade (cls,name,time,gnumber,nnumber,Delete=False ):

        grass =cls( gname = name,gtime = time,
                    ggnumber =gnumber,gnnumber=nnumber )
        return grass

    def __str__(self):
        return "%s" % self.gname


class Students(models.Model):
    graobj = models.Manager()
    graobj2 = GradesmanaGrade()
    sname = models.CharField(max_length=20,default="",verbose_name=u'主键')
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=40)
    sDelete = models.BooleanField(default=False)
    # 定义外键，关联主键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE)

   # def __str__(self):

       # return "%s" % self.name