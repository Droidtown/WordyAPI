#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from requests import post

class Wordy:
    def __init__(self, username="", wordy_key=""):
        '''
        username = ""    # 你註冊時的 email。若留空，則會使用每小時更新 2000 字的公用帳號。
        apikey = ""      # 您完成付費後取得的 apikey 值。若留空，則會使用每小時更新 2000 字的公用帳號。
        '''

        if username == "" :
            print("請先在卓騰網站 (https://api.droidtown.co) 申請帳號，再來完整使用 Wordy 的強大改寫功能")

        if wordy_key == "":
            print("在卓騰網站 (https://api.droidtown.co)登入後，填入 Wordy API key ，再來完整使用 Wordy 的強大改寫功能")

        self.url = "https://api.droidtown.co/Wordy/API/"
        self.username = username
        self.wordy_key = wordy_key
        self.max_num = 72

    def rewrite(self, inputSTR, max_num=72, user_defined={}, fixed_term=[]):
        payload = {
            "username": self.username,
            "wordy_key": self.wordy_key,
            "max_num": self.max_num,
            "input_str": inputSTR,
            "user_defined" : {},
            "fixed_term" : []}

        if isinstance(inputSTR, str):
            if inputSTR == "":
                print("inputSTR 不得為空字串")
                return False
        else:
            print("inputSTR 需要為字串 string")
            return False

        if isinstance(max_num, int):
            if abs(max_num) > self.max_num:
                print("我們一次最多可以改寫的是 72 篇喔")
                max_num = self.max_num
            payload["max_num"] = max_num
        else:
            print("max_num 需要是整數")
            return False

        if user_defined !=None:
            if isinstance(user_defined, dict):
                payload["user_defined"] = user_defined
            else:
                print("user_defined 一定要是 dict")
                return False

        if fixed_term != None:
            if isinstance(fixed_term, list):
                payload["fixed_term"] = fixed_term
            else:
                print("fixed_term 一定要是 list")
                return False

        try:
            response = post(url=self.url, json=payload)
            if response.status_code == 200:
                result = response.json()
                if result['status']:
                    print("您的 {} 篇文章改寫正在準備中，等改寫完成後，我們會再寄通知到 {}。等收到通知時，再請您至 Wordy 頁面 (https://api.droidtown.co/wordy/) 登入後下載。".format(max_num, self.username))
                    return True
                else:
                    print(result['msg'])
                    return False
            else:
                print(response)
                return False
        except Exception as e:
            print(e)
            return False


if __name__ == "__main__":
    inputSTR = "今年10戶勤奮自強家庭，獲選者都是對抗逆境的堅韌母親，其中來自越南的黎夢琴被稱「超人媽媽」，懷孕時一邊照顧女兒跟病夫一邊上班，還教導孩子回饋社會。北高雄家扶中心今天發布新聞稿指出，今年度10戶勤奮自強家庭獲選者清一色都是女性，有的曾被配偶不當對待，或是歷經喪偶，有的則是撫養照顧生病的家人，但她們身為母親，都憑藉著這股力量不被逆境所打倒，勇敢面對生命難關。"

    from WordyAPI import Wordy

    wd = Wordy(username="", wordy_key="")
    userDICT = {"懷孕":["有小孩"]}
    fixLIST = ['照顧']

    test = wd.rewrite(inputSTR, max_num= 15, user_defined=userDICT, fixed_term=fixLIST)
