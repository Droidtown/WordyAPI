# Wordy 中文仿作生成系統
## [力求保留原文篇章架構，最像人的仿作生成系統]

### [Wordy Website](https://api.droidtown.co/)
### [Document](https://api.droidtown.co/document/#Wordy)

# WordyAPI

## 安裝方法
```sh
pip3 install -U WordyAPI
```

## 使用方法

### Wordy
```
from WordyAPI import Wordy
inputSTR = "" 		#這邊填入您想仿寫的內容，需要是 string 格式。
username = "" 		#這裡填入您在 https://api.droidtown.co 使用的帳號 email。不得為空字串
wordy_key = "" 		#這裡填入您在 https://api.droidtown.co 登入後取得的 api Key。不得為空字串
max_num = 72 		#這邊輸入您想要的仿寫的篇數，預設為72篇
user_defined = {} 	#這邊輸入使用者自定替換詞典，必須是 dictionary 格式。非必要參數。
fixed_term = [] 	#這邊輸入禁止替換的詞組列表，必須是 list 格式。非必要參數。

wd = Wordy(username, wordy_key)
wd.rewrite(inputSTR, max_num=16, user_defined, fixed_term) 

```


### 回傳結果
```
您的 16 篇文章改寫正在準備中，等改寫完成後，我們會再寄通知到 {您的信箱}
```

**環境需求**

Python 3.6+ 


