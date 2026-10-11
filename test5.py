import math

#林粒粒呀零基础入门教程——打印字符串
# print("Hello Dad")
# print("hellow" + " world" + "!")

#f字符串
sucess=0.9
print(f"f字符串测试结果为：{sucess}")
print("'单双引号 \n换行\n转义\" '")
#三引号——跨行打印
str1='''沁园春·雪
北国风光，千里冰封，万里雪飘。望长城内外，惟余莽莽；
大河上下，顿失滔滔。山舞银蛇，原驰蜡象，欲与天公试比高。须晴日，看红装素裹，分外妖娆。
江山如此多娇，引无数英雄竞折腰。惜秦皇汉武，略输文采；
唐宗宋祖，稍逊风骚。一代天骄，成吉思汗，只识弯弓射大雕。俱往矣，数风流人物，
还看今朝。'''
#print(str1)

greet="hello"
print(greet)

#引入math库 然后执行数学运算
a,b,c=-1,-2,3
rusult1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
rusult2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)

print("x1=", rusult1," x2=", rusult2)

print("沁园春.雪的长度为:\n",len(str1))
print(str1[len(str1)-1])

#布尔类型、空值类型
b1 = True
b2 = False
b3 = None
#type函数查看类型
print(type(b1), type(b2), type(b3))