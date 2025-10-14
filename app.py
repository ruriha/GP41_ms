from flask import Flask, render_template, session, redirect, url_for, request, jsonify
import firebase_admin
from firebase_admin import credentials, storage, firestore
from io import BytesIO
import requests


app = Flask(__name__)

#######################################################
# Firebase
#######################################################
cred = credentials.Certificate("gp41-ms-firebase-adminsdk-fbsvc-ea0acd7078.json")
firebase_admin.initialize_app(cred, {
    'storageBucket': 'gp41-ms.firebasestorage.app'  # FirebaseStorage
})

# FirebaseStorageのバケット
bucket = storage.bucket()

# FireStoreのクライアント
db = firestore.client()


#######################################################
# FireStoreサンプル
#######################################################
# 全件取得サンプル
# @app.route('/getSpecies')
# def GetSpecies():
#     species_ref = db.collection("species") # コレクション名を指定
#     docs = species_ref.stream() # 全件取得

#     result = []
#     for doc in docs:
#         data = doc.to_dict()
#         data["id"] = doc.id
#         result.append(data)

#     return jsonify(result)

# # ドキュメント名を指定した取得サンプル
# @app.route('/getSpeciesId')
# def GetSpeciesId():
#     species_ref = db.collection("species").document("Fx1O1k8AKyYWlX8K1ivP") # コレクション名とドキュメント名を指定
#     doc = species_ref.get() # ドキュメント名を指定して取得
    
#     data = doc.to_dict()
#     data["id"] = doc.id
    
#     return jsonify(data)

# # ドキュメントを追加するサンプル
# @app.route("/addSpecies")
# def AddSpecies():
#     name = "abc"
#     age = 22
#     data = {"name": name, "age": age} # 任意の値を設定してJSONへ

#     doc_ref = db.collection("species").document() # コレクション名を指定
#     doc_ref.set(data) # ドキュメントを追加

#     return jsonify({"message": "User added", "id": doc_ref.id})


#######################################################
# FirebaseStorageサンプル
#######################################################
# 公開URLからアップロード
# @app.route("/upload")
# def upload_model():
    
#     # ファイル取得元の公開URL
#     animation_model_url = "https://storage.googleapis.com/gp41-ms.firebasestorage.app/animation_model.glb"
    
#     # ファイルを用意
#     response = requests.get(animation_model_url)

#     # バイトデータをBytesIOにラップ
#     file_data = BytesIO(response.content)

#     # FirebaseStorageにアップロード
#     blob = bucket.blob("animation_model.glb")  # ファイル名を指定
#     blob.upload_from_file(file_data, content_type="model/gltf-binary")
#     blob.make_public()  # 公開URL取得

#     return jsonify({"url": blob.public_url})

# # ローカルからアップロード
# @app.route("/upload2")
# def upload_model2():
    
#     # FirebaseStorageにアップロード
#     with open("animation_model.glb", "rb") as f:
#         blob = bucket.blob("animation_model.glb")
#         blob.upload_from_file(f, content_type="model/gltf-binary")
#         blob.make_public()  # 公開URL取得

#     return jsonify({"url": blob.public_url})

# @app.route("/download")
# def download_model():
#     # 公開URL
#     glb_url = "https://storage.googleapis.com/gp41-ms.firebasestorage.app/animation_model.glb"

#     # ファイルを取得
#     response = requests.get(glb_url)
#     # エラーチェック
#     response.raise_for_status()
    
#     # ダウンロードしたファイルをローカルに保管
#     with open("downloaded_model.glb", "wb") as f:
#         f.write(response.content)

#     return jsonify({"status": "downloaded_model.glb"})

#######################################################
# MARK: トップ画面 (01_top.html)
#######################################################
@app.route('/')
def Top():
    return render_template('01_top.html')