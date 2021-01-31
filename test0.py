# 5.関数の使い方
name = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]
def character(name1 = 'ねずこ', name2 = 'ぜんいつ'):
    # 1.変数の使い方
    print(name1 + 'と' + name2 + 'は仲間です')
    # 2.if文の使い方
    if name2 == 'むざん':
        print(name1 + 'と' + name2 + 'は仲間ではありません')
    # 3.配列の使い方
    name.append('ぜんいつ')
    # 4.for文の使い方
    for n in name:
        print(n)

character(name1 = 'ぎゆう')

# 6.関数
def index(character_name):
    if character_name in name:
        print(character_name + 'は含まれてます')
    else:
        print(character_name + 'は含まれてません')

index('れんごく')
