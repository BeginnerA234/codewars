# # https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python

from collections import Counter

ENG_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def top_3_words(text):
    new_dict = Counter()

    '''Удаляем знаки'''
    forbid = tuple(',!?/\.;:_-')
    for i in forbid:
        text = text.replace(i, ' ')  # НУЖНО СТАВИТЬ ПРОБЕЛ, ЧТОБЫ НЕ СКЛЕИВАЛАСЬ СТРОКА!

    '''Разбиваем текст на отдельные слова'''
    text = text.lower().split()

    '''Пробегаемся по строке.
    Используем set чтобы сократить кол-во итераций.'''

    for i in set(text):
        for j in i:  # Доп.цикл для проверки ковычек
            if j in ENG_ALPHABET:  # Если 1 элемент есть в алфавите, то
                new_dict[i] = text.count(i)
                break

    '''most_common([n]) - возвращает n наиболее часто
    встречающихся элементов,в порядке убывания встречаемости.
    Если n не указано, возвращаются все элементы.'''
    #     l_ist = []
    #     for k,v in new_dict.most_common(3):
    #         l_ist.append(k)
    return [k for k, v in new_dict.most_common(3)]

print(top_3_words())

# from collections import Counter
#
#
# def top_3_words(text):
#     print(text)
#     counter = Counter()
#     forbid = tuple(',!?/\.;:_-')
#
#     for i in forbid:
#         text = text.replace(i, ' ')
#
#     text = text.lower().split()
#     for word in text:
#         if not (word.startswith('\'') and len(word.replace('\'', '')) == 0):
#             counter[word] += 1
#
#     lst = []
#     for word, count in counter.most_common(3):
#         lst.append(word)
#
#     return lst
#
# print(top_3_words("kek kek kek wow wow wow lols lols lols eeee eeee eeee"))

# from collections import Counter
# import re
#
#
# def top_3_words(text):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]

# import timeit
#
# code_to_test = """
# from collections import Counter
# import re
#
#
# def top_3_words(text="GsMd:mSeb?ZqFTwIs-!kEvF/:-eroUqcM;VrPFvaIb!-!roPXttO;?/Eu'xBv _;Eu'xBv!  :VrPFvaIb_?!/fwwGlZwwBv/.?GsMd:;? eroUqcM :,'ETgyV!:lkeROkDx!;/VrPFvaIb ._GsMd_!/fwwGlZwwBv Anas!,.GsMd::.Eu'xBv:!,fwwGlZwwBv...roPXttO-ZSPebNuwP!:ZqFTwIs._,,Anas!. ZSPebNuwP/! /:lkeROkDx.Eu'xBv_VGbekmICc',;fwwGlZwwBv_-.ZSPebNuwP;!,GsMd VGbekmICc':-!. ZSPebNuwP,-;/VrPFvaIb,/.:'ETgyV!,eroUqcM_.-:'ETgyV!/;VrPFvaIb-..._VrPFvaIb_!?VGbekmICc'!VGbekmICc';_GsMd:!Anas?,/ZSPebNuwP, _ZqFTwIs!,!VGbekmICc'_kEvF,_, 'ETgyV!?///'ETgyV.VrPFvaIb?-.?GsMd:GsMd-!_.ZSPebNuwP/'ETgyV!;,VrPFvaIb:!_!?kEvF_ ;?VrPFvaIb:Anas_-,Anas.! VGbekmICc'_.:!;'ETgyV  , kEvF_?;:Anas:!kEvF!-?GsMd,-kEvF; :,'ETgyV_?ZSPebNuwP/;/Anas/??//mSeb-/?ZSPebNuwP:.;lkeROkDx! /!GsMd_.kEvF;Eu'xBv _:?,Eu'xBv::? _VGbekmICc',_-?eroUqcM--/,.'ETgyV :::VrPFvaIb..-mSeb/lkeROkDx!..fwwGlZwwBv:ZSPebNuwP_;Anas? ,VrPFvaIb! eroUqcM /!eroUqcM/_;  'ETgyV!?eroUqcM:!VGbekmICc'.VrPFvaIb:/?:GsMd,/-:GsMd-;roPXttO-_ZSPebNuwP:_!.VGbekmICc'-VGbekmICc'?;;Anas::.?_'ETgyV_ .VGbekmICc'; eroUqcM-/ lkeROkDx!-GsMd?Anas:..:lkeROkDx-;kEvF!,VrPFvaIb VrPFvaIb!!;ZqFTwIs GsMd!_?VrPFvaIb;--ZSPebNuwP;,lkeROkDx?-?_Anas? VrPFvaIb/:VGbekmICc'?! GsMd?Anas?://ZSPebNuwP/eroUqcM?? _Anas!,_?!Anas!'ETgyV/ /GsMd!..'ETgyV__;VGbekmICc'./VrPFvaIb_:VGbekmICc':/'ETgyV/.,'ETgyV.Anas_, roPXttO,VGbekmICc';,.eroUqcM/ -:VGbekmICc'?./ZqFTwIs,,?!Anas:: VrPFvaIb_:Eu'xBv:?GsMd!!VGbekmICc':-kEvF;Anas_!-kEvF_-VGbekmICc'//mSeb/'ETgyV GsMd,,/!_roPXttO/:, _kEvF,;,Anas.!/GsMd,_:_GsMd:!,,roPXttO;.kEvF!?!VrPFvaIb!;eroUqcM?'ETgyV;?Anas.; kEvF?-:Anas_?;lkeROkDx:--Anas,VrPFvaIb-kEvF._/VGbekmICc' ,!kEvF?.:.kEvF.VrPFvaIb/-?GsMd?roPXttO/.:.ZSPebNuwP;; /Anas_;;!Eu'xBv;--VGbekmICc'!mSeb /ZqFTwIs/ ?,mSeb-?.eroUqcM  ,:'ETgyV_: !lkeROkDx,Anas;!/:.GsMd-kEvF?.,GsMd!/GsMd!!VGbekmICc'-!roPXttO.mSeb;;/ /roPXttO!;eroUqcM,:?GsMd-.VrPFvaIb:-'ETgyV:/,ZSPebNuwP_;_eroUqcM_!?/_VGbekmICc';kEvF,/_.VGbekmICc',.,GsMd: ,,lkeROkDx,--ZqFTwIs _--fwwGlZwwBv,/GsMd:VrPFvaIb;--, kEvF!_VGbekmICc'.;GsMd-_ VGbekmICc'//!-Anas :fwwGlZwwBv,_?!lkeROkDx;??.'ETgyV:!--GsMd;_roPXttO ?roPXttO//:VrPFvaIb:;GsMd_ ??.fwwGlZwwBv?/! VrPFvaIb?;-/Anas -ZSPebNuwP?!!/VGbekmICc',.,? ZSPebNuwP!Anas!:,?;lkeROkDx!?_::Anas/roPXttO;!::VGbekmICc' eroUqcM?VGbekmICc';ZSPebNuwP,?,/roPXttO:?,Anas:!.VGbekmICc'-;/,eroUqcM?/kEvF/ ;!?ZSPebNuwP_;Eu'xBv_/.-'ETgyV,;VrPFvaIb ?ZSPebNuwP-VrPFvaIb! _./Eu'xBv? VrPFvaIb ::,VrPFvaIb,?roPXttO/:"):
#     c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
#     return [w for w,_ in c.most_common(3)]
# """
#
# elapsed_time = timeit.timeit(code_to_test, number=100)
# print(elapsed_time, 'регулярки')
#
# import timeit
#
# code_to_test = """
# from collections import Counter
#
# ENG_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
#
#
# def top_3_words(text="GsMd:mSeb?ZqFTwIs-!kEvF/:-eroUqcM;VrPFvaIb!-!roPXttO;?/Eu'xBv _;Eu'xBv!  :VrPFvaIb_?!/fwwGlZwwBv/.?GsMd:;? eroUqcM :,'ETgyV!:lkeROkDx!;/VrPFvaIb ._GsMd_!/fwwGlZwwBv Anas!,.GsMd::.Eu'xBv:!,fwwGlZwwBv...roPXttO-ZSPebNuwP!:ZqFTwIs._,,Anas!. ZSPebNuwP/! /:lkeROkDx.Eu'xBv_VGbekmICc',;fwwGlZwwBv_-.ZSPebNuwP;!,GsMd VGbekmICc':-!. ZSPebNuwP,-;/VrPFvaIb,/.:'ETgyV!,eroUqcM_.-:'ETgyV!/;VrPFvaIb-..._VrPFvaIb_!?VGbekmICc'!VGbekmICc';_GsMd:!Anas?,/ZSPebNuwP, _ZqFTwIs!,!VGbekmICc'_kEvF,_, 'ETgyV!?///'ETgyV.VrPFvaIb?-.?GsMd:GsMd-!_.ZSPebNuwP/'ETgyV!;,VrPFvaIb:!_!?kEvF_ ;?VrPFvaIb:Anas_-,Anas.! VGbekmICc'_.:!;'ETgyV  , kEvF_?;:Anas:!kEvF!-?GsMd,-kEvF; :,'ETgyV_?ZSPebNuwP/;/Anas/??//mSeb-/?ZSPebNuwP:.;lkeROkDx! /!GsMd_.kEvF;Eu'xBv _:?,Eu'xBv::? _VGbekmICc',_-?eroUqcM--/,.'ETgyV :::VrPFvaIb..-mSeb/lkeROkDx!..fwwGlZwwBv:ZSPebNuwP_;Anas? ,VrPFvaIb! eroUqcM /!eroUqcM/_;  'ETgyV!?eroUqcM:!VGbekmICc'.VrPFvaIb:/?:GsMd,/-:GsMd-;roPXttO-_ZSPebNuwP:_!.VGbekmICc'-VGbekmICc'?;;Anas::.?_'ETgyV_ .VGbekmICc'; eroUqcM-/ lkeROkDx!-GsMd?Anas:..:lkeROkDx-;kEvF!,VrPFvaIb VrPFvaIb!!;ZqFTwIs GsMd!_?VrPFvaIb;--ZSPebNuwP;,lkeROkDx?-?_Anas? VrPFvaIb/:VGbekmICc'?! GsMd?Anas?://ZSPebNuwP/eroUqcM?? _Anas!,_?!Anas!'ETgyV/ /GsMd!..'ETgyV__;VGbekmICc'./VrPFvaIb_:VGbekmICc':/'ETgyV/.,'ETgyV.Anas_, roPXttO,VGbekmICc';,.eroUqcM/ -:VGbekmICc'?./ZqFTwIs,,?!Anas:: VrPFvaIb_:Eu'xBv:?GsMd!!VGbekmICc':-kEvF;Anas_!-kEvF_-VGbekmICc'//mSeb/'ETgyV GsMd,,/!_roPXttO/:, _kEvF,;,Anas.!/GsMd,_:_GsMd:!,,roPXttO;.kEvF!?!VrPFvaIb!;eroUqcM?'ETgyV;?Anas.; kEvF?-:Anas_?;lkeROkDx:--Anas,VrPFvaIb-kEvF._/VGbekmICc' ,!kEvF?.:.kEvF.VrPFvaIb/-?GsMd?roPXttO/.:.ZSPebNuwP;; /Anas_;;!Eu'xBv;--VGbekmICc'!mSeb /ZqFTwIs/ ?,mSeb-?.eroUqcM  ,:'ETgyV_: !lkeROkDx,Anas;!/:.GsMd-kEvF?.,GsMd!/GsMd!!VGbekmICc'-!roPXttO.mSeb;;/ /roPXttO!;eroUqcM,:?GsMd-.VrPFvaIb:-'ETgyV:/,ZSPebNuwP_;_eroUqcM_!?/_VGbekmICc';kEvF,/_.VGbekmICc',.,GsMd: ,,lkeROkDx,--ZqFTwIs _--fwwGlZwwBv,/GsMd:VrPFvaIb;--, kEvF!_VGbekmICc'.;GsMd-_ VGbekmICc'//!-Anas :fwwGlZwwBv,_?!lkeROkDx;??.'ETgyV:!--GsMd;_roPXttO ?roPXttO//:VrPFvaIb:;GsMd_ ??.fwwGlZwwBv?/! VrPFvaIb?;-/Anas -ZSPebNuwP?!!/VGbekmICc',.,? ZSPebNuwP!Anas!:,?;lkeROkDx!?_::Anas/roPXttO;!::VGbekmICc' eroUqcM?VGbekmICc';ZSPebNuwP,?,/roPXttO:?,Anas:!.VGbekmICc'-;/,eroUqcM?/kEvF/ ;!?ZSPebNuwP_;Eu'xBv_/.-'ETgyV,;VrPFvaIb ?ZSPebNuwP-VrPFvaIb! _./Eu'xBv? VrPFvaIb ::,VrPFvaIb,?roPXttO/:"):
#     new_dict = Counter()
#
#     '''Удаляем знаки'''
#     forbid = tuple(',!?/\.;:_-')
#     for i in forbid:
#         text = text.replace(i, ' ')  # НУЖНО СТАВИТЬ ПРОБЕЛ, ЧТОБЫ НЕ СКЛЕИВАЛАСЬ СТРОКА!
#
#     '''Разбиваем текст на отдельные слова'''
#     text = text.lower().split()
#
#     '''Пробегаемся по строке.
#     Используем set чтобы сократить кол-во итераций.'''
#
#     for i in set(text):
#         for j in i:  # Доп.цикл для проверки ковычек
#             if j in ENG_ALPHABET:  # Если 1 элемент есть в алфавите, то
#                 new_dict[i] = text.count(i)
#                 break
#
#     '''most_common([n]) - возвращает n наиболее часто
#     встречающихся элементов,в порядке убывания встречаемости.
#     Если n не указано, возвращаются все элементы.'''
#     #     l_ist = []
#     #     for k,v in new_dict.most_common(3):
#     #         l_ist.append(k)
#     return [k for k, v in new_dict.most_common(3)]
# """
#
# elapsed_time = timeit.timeit(code_to_test, number=100)
# print(elapsed_time, ' мой код')
#
# import timeit
#
# code_to_test = """
# a = 2+2
# """
#
# elapsed_time = timeit.timeit(code_to_test, number=100)/100
# print(elapsed_time, 'test')