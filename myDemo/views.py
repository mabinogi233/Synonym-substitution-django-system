from django.shortcuts import render
from myDemo.new_algroithm import run_sim,addToMySql,updateSim


from django.http import HttpResponse
# Create your views here.

#计算两篇文章相似度
def runSim(request):
    simP = run_sim.run_sim("我就是一个句子。我是第二个句子")
    print(simP)
    return HttpResponse(str(simP))

def addData(request):
    addToMySql.addToMySQL("我是第二个句子。",'第二个作者',"第二篇论文")
    return HttpResponse("True")

def index(request):
    return render(request,'index.html')

def fanChaChong(request):
    str = updateSim.fanChaChong("测试一句话。我是第二句话啊")
    print(str)
    return HttpResponse("成功")