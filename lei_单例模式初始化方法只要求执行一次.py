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

    #记录第一个被创建的对象的引用
    instance = None

    #记录是否被初始化过的标志
    init_flag = False

    #创建对象时候 该方法自动调用 重写该方法
    def __new__(cls, *args, **kwargs):
        #print("创建对象时候默认使用的函数 进行内存空间的分配 必须要returne 返回")

        #判断类属性是否是空对象
        if cls.instance is None:
            #调用父类方法 为对象分配空间
            cls.instance = super().__new__(cls)

        #返回对象的引用
        return cls.instance

    def __init__(self):

        #判断标志检查
        if musicplayer.init_flag :
            return
        else:
            print("播放器开始播放音乐....")
            #修改标志
            musicplayer.init_flag = True

print("**********************************")
print("单例模式多个创建的对象的地址是相同的")
print("**********************************")
kugou = musicplayer()
print(kugou)
qq_music = musicplayer()
print(qq_music)









