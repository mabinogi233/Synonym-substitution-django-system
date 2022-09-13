import myDemo.models
import random
import os

#选择需要替换的句子，写入文件
def write_input(inputEssayList):
    list_select_i = [random.randint(0,len(inputEssayList)-1) for i in range(len(inputEssayList)//2)]
    #list_select_i = [0,1]
    with open(r"D:\\codes\\codes\\fanChaChong\\BERT_DATA\\lcqmc\\test.tsv",'w',encoding='utf-8')as f:
        f.write('text_a')
        f.write('\t')
        f.write('text_b')
        f.write('\t')
        f.write('label')
        f.write('\n')
        for i in list_select_i:
            for line in myDemo.models.Replacesentence.objects.all().order_by('id'):
                f.write(inputEssayList[i])
                f.write('\t')
                f.write(line.sentencereplace)
                f.write('\t')
                f.write(str(0))
                f.write('\n')
    #返回选择的句子的下标
    return list_select_i

#运行模型计算相似度
def run_bert():
    os.system("python D:\\codes\\codes\\fanChaChong\\bert-master\\run_classifier.py")

#读入输出数据，选择句子替换
def read_output(inputEssayList,list_select_i,maxP):
    outputEssayList = inputEssayList[:]
    with open(r"D:\\codes\\codes\\fanChaChong\\BERT_DATA\\output\\test_results.tsv", 'r', encoding='utf-8')as f:
        for i in list_select_i:
            simPmax = 0
            str = ""
            for line in myDemo.models.Replacesentence.objects.all().order_by('id'):
                resultList = f.readline().strip('\n').split('\t')
                simP = float(resultList[1])
                #相似的概率为simP
                if(simP>simPmax):
                    simPmax = simP
                    str = line.sentencereplace
            #大于阈值则替换
            if(simPmax>maxP):
                outputEssayList[i] = str
    return outputEssayList


#主函数
def main(inputEssayList):
    list_select_i = write_input(inputEssayList)
    run_bert()
    outputEssayList = read_output(inputEssayList,list_select_i,maxP=0.9)
    return outputEssayList