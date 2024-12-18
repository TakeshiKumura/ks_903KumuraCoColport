#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy
import cv2 as cv
import numpy as np
import mediapipe as mp


def main():
    # 初期設定：モードと入力番号
    mode = 0
    number = -1

    # Mediapipe のセットアップ
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
    
    mp_face = mp.solutions.face_mesh
    face = mp_face.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    # カメラ準備
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 540)

    # メイン処理ループ
    try:
        while True:
            # キー入力処理 (ESC: 終了)
            key = cv.waitKey(1)
            if key == 27:  # ESCキー
                break
            number, mode = select_mode(key, mode)

            # カメラキャプチャ
            ret, image = cap.read()
            if not ret:
                print("カメラの取得に失敗しました")
                break
            image = cv.flip(image, 1)  # ミラー表示
            debug_image = copy.deepcopy(image)

            # Mediapipe の画像処理
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            face_results = face.process(image)
            image.flags.writeable = True

            # 顔を隠す処理（例として枠を描画）
            if face_results.multi_face_landmarks:
                for face_landmarks in face_results.multi_face_landmarks:
                    face_brect = calc_bounding_rect(image, face_landmarks)
                    cv.rectangle(debug_image, (face_brect[0], face_brect[1]), 
                                 (face_brect[2], face_brect[3]), (0, 255, 0), 2)

            # 手の処理
        if results.multi_hand_landmarks is not None and mode != 9:
            left_fg, right_fg = 0, 0
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                # 外接矩形の計算、ランドマークの計算、相対座標・正規化座標への変換、学習データ保存
                brect = calc_bounding_rect(debug_image, hand_landmarks)
                print(brect)
                # landmark_list = calc_landmark_list(debug_image, hand_landmarks)
                # pre_processed_landmark_list = pre_process_landmark(landmark_list)
                # number, mode, pre_processed_landmark_list

                # 手型分類: 左手は入力文字を1文字削除するフラグとして使用
                if handedness.classification[0].label == "Left":
                    left_fg = 1

                # 手型分類: 右手のみ、ひらがな入力
                else:
                    right_fg = 1
                    
                #     # 手型判定
                #     # （処理を追加する場合、ここに記載）
                #     #  landmark_tips, 
                #     hand_landmarks

                #     # 濁音、半濁音等のために手の動きを判定
                #     # landmarks_ave = calc_landmarks_ave(hand_landmarks)
                #     hand_landmarks

                # # 手型の判定結果描画
                # # brect_center = calc_brect_center(brect)
                # round(brect[0])

            # 両手を検出しているときは入力文字を1文字ずつ削除
            if left_fg == 1 and right_fg == 1:
                pass
                # out_no -= 1

        # 手を認識していないときの処理
        # 手を認識していないときは入力した文字を全削除
        else:
            # 入力文字列を管理する変数
            input_letters = ""  # 仮の文字列管理変数（実際はこの変数がどこで定義されるかにより適切に処理）
            input_letters = ""  # 手が認識されていない場合、リセット
            print("手が認識されていないため、入力文字を全削除しました")


            # 結果を画面に表示
            cv.imshow('Hand Gesture Recognition', debug_image)
    finally:
        # 終了処理
        cap.release()
        hands.close()
        face.close()
        cv.destroyAllWindows()


def select_mode(key, mode):
    """キー入力でモードを選択"""
    number = -1
    if 48 <= key <= 57:  # 数字キー 0 ~ 9
        number = key - 48
    if key == ord("n"):  # nキーで通常モード
        mode = 0
    if key == ord("k"):  # kキーで別モード
        mode = 1
    if key == ord("s"):  # sキーで特別モード
        mode = 9
    return number, mode


def calc_bounding_rect(image, landmarks):
    """ランドマークから外接矩形を計算"""
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_array = np.array([[int(landmark.x * image_width), int(landmark.y * image_height)]
                               for landmark in landmarks.landmark])
    x, y, w, h = cv.boundingRect(landmark_array)
    return [x, y, x + w, y + h]


def calc_landmark_list(image, landmarks):
    """ランドマーク座標リストを取得"""
    image_width, image_height = image.shape[1], image.shape[0]
    return [[int(landmark.x * image_width), int(landmark.y * image_height)]
            for landmark in landmarks.landmark]


def pre_process_landmark(landmark_list):
    """ランドマーク座標を正規化"""
    temp_landmark_list = copy.deepcopy(landmark_list)
    base_x, base_y = temp_landmark_list[0][0], temp_landmark_list[0][1]
    temp_landmark_list = [[x - base_x, y - base_y] for x, y in temp_landmark_list]
    max_value = max(max(abs(x), abs(y)) for x, y in temp_landmark_list)
    return [[x / max_value, y / max_value] for x, y in temp_landmark_list]


if __name__ == '__main__':
    main()
