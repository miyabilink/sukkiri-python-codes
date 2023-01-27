# randomモジュールのrandint関数を取り込む
from random import randint
print('数当てゲームを始めます。3桁の数を当ててください!')

# 正解を作成
answer = list()
for n in range(3):
    answer.append(randint(0, 9))

is_continue = True
while is_continue == True:
    # 予想の入力
    prediction = list()
    for n in range(3):
        data = int(input('{}桁目の予想入力(0~9)>>'.format(n + 1)))
        prediction.append(data)
    
    # 答え合わせ
    hit = 0
    blow = 0
    for n in range(3):
        if prediction[n] == answer[n]:
            hit += 1
        else:
            for m in range(3):
                if prediction[n] == answer[m]:
                    blow += 1
                    break

    # 結果発表
    print('{}ヒット!{}ボール!'.format(hit, blow))
    if hit == 3:
        print('正解です!')
        is_continue = False
    else:
        if int(input('続けますか? 1:続ける 2:終了 >>')) == 2:
            print('正解は{}{}{}でした'.format(answer[0], answer[1], answer[2]))
            is_continue = False