import  csv

# ３．２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう
with open('test1.csv','r') as f:
    reader = csv.reader(f)
    for line in reader:
        source = line
　　　　　# 初期source = ["ねずこ", "たんじろう", "きょうじゅろう", "ぎゆう", "げんや", "かなお", "ぜんいつ"]

### 検索ツール
def search():
    word = input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        source.append(word)

if __name__ == "__main__":
    search()

# ４．３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう
with open('test1.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(source)
