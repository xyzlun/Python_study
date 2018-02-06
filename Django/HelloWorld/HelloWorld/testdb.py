#coding=utf-8
from django.http import HttpResponse
from TestModel.models import Test

def testdb(request):
    #初始化
    response = ''
    response1 = ''
    # save()相当于SQL中的INSERT
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()
    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)
    # 获取单个对象
    response3 = Test.objects.get(id=1)
    # 限制返回的数据 相当于SQL中的OFFSET 0 LIMIT 2
    Test.objects.order_by('name')[0:2]
    # 数据排序
    Test.objects.order_by('id')
    # 上面的方法可以连锁使用
    Test.objects.filter(name='runoob').order_by('id')
    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse('<p>' + response + '</p>')

# 插入数据
def testdb_add(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse('<p>数据添加成功</p>')
# 更新数据
def testdb_update(request):
    # 修改其中一个id=1的name字段，再save,相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()
    # 另一种方式
    #Test.objects.filter(id=1).update(name='Google')
    #修改所有列
    #Test.objects.all().update(name='Google')
    return HttpResponse('<p>修改成功</p>')

# 删除数据
def testdb_del(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()
    # 另一种方式
    Test.objects.filter(id=1).delete()
    # 删除所有数据
    Test.objects.all().delete()
    return HttpResponse('<p>删除成功</p>')