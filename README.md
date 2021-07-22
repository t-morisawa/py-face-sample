
# summary

https://github.com/ageitgey/face_recognition

# インプット情報

https://pystyle.info/perform-face-recognition-with-python/


# 利用方法

venvの知識を前提とします。

https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

```
python -m venv venv
. ./venv/bin/activate
pip install face_recognition
```

パッケージインストールで `CMake must be installed to build dlib` でエラーになる場合は以下を実行

```
brew install cmake
```

# FAQ
## 画像に2人以上写っていた場合

各関数、顔の数の長さの配列で返されるので問題なし。ただし、画像中の顔と特徴量を一致させたい場合は、領域抽出を行ってから特徴量抽出を行うなど工夫が必要。

## 処理速度

 - HOGモード: 4枚で0.4秒
 - CNNモード: 4枚で5秒

```
% python main.py
画像読み込み完了 経過時間: 0.01854681968688965
特徴量抽出完了 経過時間: 0.341400146484375
判定完了 経過時間: 9.799003601074219e-05
known-face_01.jpg: True
known-face_02.jpg: False
known-face_03.jpg: False
```
