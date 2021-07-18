
# py-face-sample

顔認証ライブラリFace Recognitionの動作確認

https://github.com/ageitgey/face_recognition

下記のブログのプログラムを利用

https://pystyle.info/perform-face-recognition-with-python/


# 利用方法

 - Python3
 - venvの知識を前提とします
   - https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

## 環境構築

```
python -m venv venv
. ./venv/bin/activate
pip install face_recognition
```

パッケージインストールで `CMake must be installed to build dlib` でエラーになる場合は以下を実行

```
brew install cmake
```

## 実行

```
python main.py
```

# FAQ
## 画像に2人以上写っていた場合

各関数、顔の数の長さの配列で返されるので問題なし。ただし、画像中の顔と特徴量を一致させたい場合は、領域抽出を行ってから特徴量抽出を行うなど工夫が必要。

## 処理速度

 - HOGモード(精度中): 4枚で0.4秒
 - CNNモード(精度高): 4枚で5秒
