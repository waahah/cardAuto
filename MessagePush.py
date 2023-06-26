# encoding:utf-8
# PushPlus
import requests
import json

def pushMessage(title, status, token,username,address,time):
    html = '''
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title></title>
    </head>
    <body>
        <div id="app" style="height:100%">
            <div id="all">
                <div class="wrapper">
                    <div class="main">
                        <div class="content">
                            <div class="content-top">
<h2>
    <a href="javascript:void(0)" class="smoothScroll btn btn-lg">
        <span style="color:#ffffff;">今日自动打卡通知
    </a>
</h2>
</p>
<h6>
    <a style="color:green">Tip：请确认打卡信息</a>
</h6>
<ul>
    <li>
    <div class="link"></div>
    </li>
    <li>
        <div class="link">
            <div style="color:#02a982">用户：</div>
            <div class="go" style="color:#999">
                    '''+username+'''
            </div>
        </div>
    </li>
    <li>
        <div class="link">
            <div style="color:#02a982">状态：</div>
            <div class="go" style="color:#999">
                    '''+status+'''
            </div>
        </div>
    </li>
    <li>
        <div class="link">
            <div style="color:#02a982">地址：</div>
            <div class="go" style="color:#999">
                    '''+address+'''
            </div>
        </div>
    </li>
    <li>
        <div class="link">
            <div style="color:#02a982">时间：</div>
            <div class="go" style="color:#999"> 
                    '''+time+'''
            </div>
        </div>
    </li>
</ul>
</div></div>
</div></div></div></div>

<style>
            html,body {
                height: 100%;
                margin: 0;
            }
            body {
                height: 100%;
                overflow: hidden;
                overflow-y: auto;
                background: #01a982;
            }
            .main {
                z-index: 999;
                position: relative;
                top: -240px;
            }
            .main h1 {
                font-size: 40px;
                text-align: center;
                color: #fff;
                margin-bottom: 30px;
                text-transform: uppercase
            }
            .link {
                display: flex;
                align-items: center;
                position: relative;
            }
            .content {
                margin: 0 auto;
                width: 100%;
                background: #fff;
                border-radius: 5px
            }

            .content-top h2 {
                font-size: 22px;
                color: #fff;
                text-align: center;
                background-color: #01a982;
                padding: 12px 0;
                border-radius: 5px
            }

            .content-top p {
                text-align: center;
                font-size: 16px;
                color: #000;
                margin-top: 15px
            }

            .content-top ul li {
                display: block;
                font-size: 16px;
                line-height: 1.8em;
                padding: 1em 0 1em 1em;
                border-bottom: 1px solid #e2e0de
            }

            .content-top ul li a {
                font-weight: 400
            }

            .content-top ul li a i {
                color: #02a982;
                font-style: normal;
                display: block;
                margin: 2px 0
            }

            .content-top ul li span {
                display: block;
                color: #999
            }

            .content-top {
                padding: 1.5em
            }

            .content-top p a {
                color: #55acee;
                margin-left: 5px
            }
            ul {
                margin-top: 0;
                padding:0;
            }
        </style>

</body></html>

'''
    url = 'http://www.pushplus.plus/send'
    data = {
        "token":token,
        "title":title,
        "content":html,
        "template":"html"
    }
    body=json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    resp = requests.post(url,data=body,headers=headers)
    if resp.json()["code"] == 200:
        print('推送消息提醒成功！')
        sendMessage = f"{username} 推送消息提醒成功！</br>"
    else:
        print(resp)
        print('推送消息提醒失败！')
        sendMessage = f"{username} 推送消息提醒失败！</br>"
    return sendMessage

def pushAllMessage(allMessage, persionToken):
    persionTitle = '所有用户打卡情况统计'
    templateType = 'html'
    url = f'http://www.pushplus.plus/send?token={persionToken}&title={persionTitle}&content={allMessage}&template={templateType}'
    resp = requests.post(url)
    if resp.json()["code"] == 200:
        print('所有用户打卡情况统计推送成功！')
    else:
        print('所有用户打卡情况统计推送失败！')
