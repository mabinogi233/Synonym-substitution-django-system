
#分割字符列表
DIV_LIST = ['.','。','？','！','?','!']
#将文章分为句子列表
def make_sep(inputEssay):
    reInputEssayList = []
    str=''
    for i in range(len(inputEssay)):
        if(inputEssay[i] not in DIV_LIST):
            str+=inputEssay[i]
        else:
            str += inputEssay[i]
            reInputEssayList.append(str)
            str = ''
    if(len(str)!=0):
        reInputEssayList.append(str)
    print(reInputEssayList)
    return reInputEssayList

#将句子列表拼装为字符串
def fan_make_sep(inputEssayList):
    str=""
    for line in inputEssayList:
        str+=line
    return str