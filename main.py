import face_recognition
from time import time

FILES = ["known-face_01.jpg", "known-face_02.jpg", "known-face_03.jpg"]
MODEL = "hog"  # hog / cnn

# 経過時間計測
start = time()

# 保存されている人物の顔の画像を読み込む。
known_face_imgs = []
for path in FILES:
    img = face_recognition.load_image_file(path)
    known_face_imgs.append(img)

# 認証する人物の顔の画像を読み込む。
face_img_to_check = face_recognition.load_image_file("face_to_check.jpg")

# 顔の画像から顔の領域を検出する。
known_face_locs = []
for img in known_face_imgs:
    loc = face_recognition.face_locations(img, model=MODEL)
    assert len(loc) == 1, "画像から顔の検出に失敗したか、2人以上の顔が検出されました"
    known_face_locs.append(loc)

face_loc_to_check = face_recognition.face_locations(face_img_to_check, model=MODEL)
assert len(face_loc_to_check) == 1, "画像から顔の検出に失敗したか、2人以上の顔が検出されました"

# 顔の領域から特徴量を抽出する。
known_face_encodings = []
for img, loc in zip(known_face_imgs, known_face_locs):
    (encoding,) = face_recognition.face_encodings(img, loc)
    known_face_encodings.append(encoding)

(face_encoding_to_check,) = face_recognition.face_encodings(
    face_img_to_check, face_loc_to_check
)

matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check)
for f, match in zip(FILES, matches):
    print(f"{f}: {match}")

period = time() - start
print(f"経過時間: {period}")
