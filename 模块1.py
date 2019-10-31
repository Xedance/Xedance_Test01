#这是自动制作图片的2.0版本，可以不依赖PS进行批量制作图片
from PIL import Image
import random, glob, os

#from pil import image
#import glob, os, sys

#imagenum = []
#i = 0
#for inpng in glob.glob("*.png"):
#    imagenum.append(inpng)
#    i = i+1
#print('扫描到%d个png图片'%i)
#print(imagenum)
#print('执行图片测试操作')
#im = image.open('test.png')
#print(im.size)
#mysize = (1080, 1440)
#start = (0,0)
#newim = image.new('rgba',mysize)
#print('新建图片成功')
#newim.paste(im)
#print('置入图片成功')
#sucaiim = image.open('1.png')
#newim.paste(sucaiim,start,sucaiim)
#print('修改图片成功')
#newim.save('new.png')
#print('保存图片成功')
#int(int(random.random()*100)%Feet+Feetstart+(minute+(Feetstart+Feet/2)*num))%60
#int(int(random.random()*100)%Feet+Feetstart+(minute+(Feetstart+Feet/2)*num))//60+Hour
#Pic->
#
class MyPic():
    def __init__(self, num, Mylist):
        self.Name = num
        self.Week = Mylist[8]
        self.Moon = Mylist[1]
        self.Sun = Mylist[2]
        self.Loc = Mylist[7]
        self.Hour = int(int(random.random()*100)%Mylist[5]+Mylist[6]+(Mylist[4]+(Mylist[6]+Mylist[5]/2)*self.Name))//60+Mylist[3]
        self.Minute = int(int(random.random()*100)%Mylist[5]+Mylist[6]+(Mylist[4]+(Mylist[6]+Mylist[5]/2)*self.Name))%60
def MyInput():
    a = input('请输入文件范围，格式为YY：')
    d = input('请输入日期和时间 月月日日时时分分：MMDDHHMM：')
    e = input('请输入星期：W：')
    b = input('请输入随机参数(步长)，格式为SSEE，其中SS为步长起始和EE为步长结束：SSEE：')
    c = input('请输入地点代号，格式为X，1.常州新北2.滨湖万达等：')
    return c+d+b+a+e
def NewInput():
    imagename = []
    num = 0
    print('扫描原图片素材文件夹中的图片...')
    for infile in glob.glob("原图片素材\*.jpg"):
        imagename.append(infile)
        num = num + 1
    print('扫描到%d个图片，确认无误后按任意键继续'%num)
    os.system('pause') 
    day = input('请输入日期和时间 月月日日时时分分：MMDDHHMM：')
    week = input('请输入星期：W：')
    feet = input('请输入随机参数(步长)，格式为SSEE，其中SS为步长起始和EE为步长结束：SSEE：')
    loction = input('请输入地点代号，格式为X，1.常州新北2.滨湖万达等：')
    print(imagename)
    return day + week + feet + loction
def MyParse(strdata):   #X MMDDHHMM SSEE YY W
    Filenum = int(strdata[-3:-1])
    Week = int(strdata[-1])
    Moon = int(strdata[1:3])
    Sun = int(strdata[3:5])
    Hour = int(strdata[5:7])
    Minute = int(strdata[7:9])
    Feet = int(strdata[11:13])-int(strdata[9:11])
    Feetstart = int(strdata[9:11])
    Location = int(strdata[0])
    Mylist = [Filenum,Moon,Sun,Hour,Minute,Feet,Feetstart,Location,Week]
    return Mylist
def MyData(Mylist):
    DataList = []
    for num in range(Mylist[0]):
        DataList.append(MyPic(num,Mylist))
    return DataList
def MyWrite(DataList):
    Newfile = 'configv1.txt'
    Myfile = open(Newfile,'w')
    last1 = '.jpg'
    last2 = '.png'
    NamePath = '\原图片素材\\'
    MoonPath = '\月份素材\\'
    SunTPath = '\日期十位素材\\'
    SunSPath = '\日期个位素材\\'
    HourTPath = '\小时十位素材\\'
    HourSPath = '\小时个位素材\\'
    MinTPath = '\分钟十位素材\\'
    MinSPath = '\分钟个位素材\\'
    LocPath = '\位置素材\\'
    WeekPath = '\星期素材\\'
    Myfile.write('原图片\t月份\t日期十位\t日期个位\t星期\t小时十位\t小时个位\t分钟十位\t分钟个位\t位置代号\n')
    for num in range(len(DataList)):
        if DataList[num].Name < 10:
            Filename = '0' + str(DataList[num].Name)
            Myfile.write(NamePath+Filename+last1+'\t')
        else:
            Filename = str(DataList[num].Name)
            Myfile.write(NamePath+Filename+last1+'\t')
        Filemoon = str(DataList[num].Moon)
        Myfile.write(MoonPath+Filemoon+last2+'\t')
        if DataList[num].Hour < 10:
            FileSunT = str(DataList[num].Sun // 10)
            Myfile.write(SunTPath+FileSunT+last2+'\t')
            FileSunS = str(DataList[num].Sun % 10)
            Myfile.write(SunSPath+FileSunS+last2+'\t')
            FileWeek = str(DataList[num].Week)
            Myfile.write(WeekPath + FileWeek + last2 + '\t')
            FileHourT = '0'
            Myfile.write(HourTPath+FileHourT+last2+'\t')
            FileHourS = str(DataList[num].Hour)
            Myfile.write(HourSPath+FileHourS+last2+'\t')
        elif DataList[num].Hour < 24:
            FileSunT = str(DataList[num].Sun // 10)
            Myfile.write(SunTPath+FileSunT+last2+'\t')
            FileSunS = str(DataList[num].Sun % 10)
            Myfile.write(SunSPath+FileSunS+last2+'\t')
            FileWeek = str(DataList[num].Week)
            Myfile.write(WeekPath + FileWeek + last2 + '\t')
            FileHourT = str(DataList[num].Hour // 10)
            Myfile.write(HourTPath+FileHourT+last2+'\t')
            FileHourS = str(DataList[num].Hour % 10)
            Myfile.write(HourSPath+FileHourS+last2+'\t')
        elif DataList[num].Hour < 34:
            Date1 = DataList[num].Sun + 1
            FileSunT = str(Date1 // 10)
            Myfile.write(SunTPath+FileSunT+last2+'\t')
            FileSunS = str(Date1 % 10)
            Myfile.write(SunSPath+FileSunS+last2+'\t')
            FileWeek = str(DataList[num].Week + 1)
            Myfile.write(WeekPath + FileWeek + last2 + '\t')
            FileHourT = '0'
            Myfile.write(HourTPath+FileHourT+last2+'\t')
            FileHourS = str(DataList[num].Hour - 24)
            Myfile.write(HourSPath+FileHourS+last2+'\t')
        else:
            Date2 = DataList[num].Sun + 1
            FileSunT = str(Date2 // 10)
            Myfile.write(SunTPath+FileSunT+last2+'\t')
            FileSunS = str(Date2 % 10)
            Myfile.write(SunSPath+FileSunS+last2+'\t')
            FileWeek = str(DataList[num].Week + 1)
            Myfile.write(WeekPath + FileWeek + last2 + '\t')
            FileHourT = str((DataList[num].Hour - 24) // 10)
            Myfile.write(HourTPath+FileHourT+last2+'\t')
            FileHourS = str((DataList[num].Hour - 24) % 10)
            Myfile.write(HourSPath+FileHourS+last2+'\t')
        FileMinT = str(DataList[num].Minute//10)
        Myfile.write(MinTPath+FileMinT+last2+'\t')
        FileMinS = str(DataList[num].Minute%10)
        Myfile.write(MinSPath+FileMinS+last2+'\t')
        FileLoc = str(DataList[num].Loc)
        Myfile.write(LocPath + FileLoc + last2 + '\n')
    Myfile.close()
def main():
    print('当前版本ver1.0著作人:X\n')
    Mystr = MyInput()
    Mylist = MyParse(Mystr)
    Mydatalist = MyData(Mylist)
    MyWrite(Mydatalist)
def test():
    NewInput();
    #Mystr = MyInput()
    #Mylist = MyParse(Mystr)
    #print(Mylist)
    #print('\n')
    #print(random.random())
if __name__ == '__main__':
    test()
#    main()
