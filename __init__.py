#创建一个python包
print('启动中，请稍等...')
def help():
    info = '''
[
  {
    "enable": true,
    "alias": "王萌萌",
    "phone": "19888678xxx",
    "password": "1234....",
    "deviceType": "Honor|COL-AL10|10",//手机品牌英文名称\|手机代号\|安卓系统版本
    "deviceId": "设备ID",//36位字母+数字组合,从此获取随机ID http://did.sxba.xuanran.cc
    "randomLocation": true,//打卡位置浮动，启用后每次打卡系统将会在你原有的经纬度的基础之上删掉最后一位数字并随机加入一位数字，使每次打卡经纬度不同
    "address": "打卡地址",
    "longitude": "位置经度", //通过坐标拾取来完成,从此获取 https://jingweidu.bmcx.com/
    "latitude": "位置纬度", //通过坐标拾取来完成,从此获取 https://jingweidu.bmcx.com/
    "pushKey": "推送token" //打卡结果微信推送,微信推送使用的是pushPlus,请到官网绑定微信(https://www.pushplus.plus/)发送token复制出来粘贴
  }
]
'''
    return info