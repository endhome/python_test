"""
eg: 单例使用场景
打印机
回收站
音乐播放器

单例模式
目的 让类创建的对象 在系统中只有唯一的一个实例
每一次执行 类名() 放回的对象 内存地址是相同的
"""


class musicplayer(object):

#创建对象时候 该方法自动调用
    def __new__(cls, *args, **kwargs):
        print("创建对象时候默认使用的函数 进行内存空间的分配 必须要returne 返回")
#为对象分配空间
        instance = super().__new__(cls)
#返回对象的引用
        return instance

    def __init__(self):
        print("播放器开始播放音乐....")



kugou = musicplayer()
print(kugou)
qq_music = musicplayer()
print(qq_music)









