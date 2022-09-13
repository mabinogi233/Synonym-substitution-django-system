import myDemo.new_algroithm.googleRun
import myDemo.new_algroithm.makeSEP
import myDemo.new_algroithm.replace_sentence
#反查重修正
def fanChaChong(inputEssay):
    #翻译
    list1 = myDemo.new_algroithm.googleRun.main(inputEssay,'de')
    str1 = myDemo.new_algroithm.makeSEP.fan_make_sep(list1)
    list2 =myDemo.new_algroithm.googleRun.main(str1,'zh-CN')
    #随机替换
    list3 = myDemo.new_algroithm.replace_sentence.main(list2)
    str2 = myDemo.new_algroithm.makeSEP.fan_make_sep(list3)
    return str2
