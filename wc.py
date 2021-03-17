import wordcloud
import jieba
txt = """
时长奖励功能
提高效率，目的性，应付学校要求，加强平台学生互动，提供讨论时间，压力，学习氛围
提升监督水平
调整每节课，长度，放松头脑
面部表情识别ai，技术
保持好心情
不要Ecredit，别卷了，chill
老师检验和询问，学习效果，询问帮助
统一网课平台授课方式
学习氛围，加强
summative，简单
布置作业，严格，鬼混
跳过已掌握内容，想学、该学、难学
plog形式记录
网课前布置作业，讲更多内容
减短网课时间，高效授课
连线晚自习，提高效率
减少课时
老师加强管理，穿插提问
提高，自律性，学习意识
关掉手机
师生互动
自由交流时间，上课限制软件
学习小组，互相帮助
回学校上课，氛围，环境
打开摄像头
离开手机"""
w = wordcloud.WordCloud(width=1000,font_path="CN.ttf",height=700,max_words=35)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("q17.png")
