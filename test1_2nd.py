import  csv

def search():
    with open('test1.csv', 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            source = line

    word = input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        source.append(word)
        with open('test1.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(source)

if __name__ == "__main__":
    search()
