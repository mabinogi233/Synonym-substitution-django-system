from myDemo.new_algroithm import bert_encoding,makeSEP
from myDemo.models import Sentence


def run_sim(inputEssayA,simPmax = 0.3):
    #句子列表
    inputEssayAList = makeSEP.make_sep(inputEssayA)
    #从数据库中读入所有句子，加入inputEssayBList
    inputEssayBList = []
    for line in Sentence.objects.all():
        inputEssayBList.append(line.sentence)
    print(inputEssayBList)
    #写入待训练文件

    with open(r"D:\\codes\\codes\\fanChaChong\\BERT_DATA\\lcqmc\\test.tsv",'w',encoding='utf-8')as f:
        f.write('text_a')
        f.write('\t')
        f.write('text_b')
        f.write('\t')
        f.write('label')
        f.write('\n')
        for sentensA in inputEssayAList:
            for sentensB in inputEssayBList:
                f.write(sentensA)
                f.write('\t')
                f.write(sentensB)
                f.write('\t')
                f.write(str(0))
                f.write('\n')

    # 计算每个句子的相似度
    bert_encoding.runSim_byBert()
    #计算整个文章的相似度
    labelP = []
    with open(r"D:\\codes\\codes\\fanChaChong\\BERT_DATA\\output\\test_results.tsv", 'r', encoding='utf-8')as f:
        for line in f.readlines():
            line_list = line.strip('\n').split('\t')
            labelP.append(float(line_list[1]))

    i = 0
    conut = 0
    for sentensA in inputEssayAList:
        boolflag = False
        for sentensB in inputEssayBList:
            if(labelP[i]>=simPmax):
                if(not boolflag):
                    conut+=1
                    boolflag = True
                i+=1
            else:
                i+=1

    #返回最大的相似度
    return conut/(len(inputEssayAList))