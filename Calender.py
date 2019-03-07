import sqlite3

#公元元年是猴年, 1984年为甲子鼠年
#animals = ['\N{Mouse}', '\N{Ox}', '\N{Tiger}','\N{Rabbit}',
#		'\N{Dragon}','\N{Snake}', '\N{Horse}','\N{Sheep}',
#		'\N{Monkey}','\N{Chicken}','\N{Dog}','\N{Pig}']

conn = sqlite3.connect('lunar_calendar.db')
db = conn.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS calendar
	(year INTEGER PRIMARY KEY,
	ytg TEXT,
	ydz TEXT,
	sx TEXT)''')
Zodiac='鼠牛虎兔龙蛇马羊猴鸡狗猪'
tiangan = '甲乙丙丁戊己庚辛壬癸'
dizhi = '子丑寅卯辰巳午未申酉戌亥'

#Sexagenary_cycle=	['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉',  
#				'甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未',  
#				'甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳',  
#				'甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯',  
#				'甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑',  
#				'甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

for year in range(-1000, 2050, 1):
	ytg = tiangan[(year-4)%10]
	ydz = dizhi[(year-4)%12]
	sx = Zodiac[(year-4)%12]
	#ganzhi = Sexagenary_cycle[(year-4)%60]
	db.execute('''INSERT INTO calendar(year, ytg, ydz, sx) values(?, ?, ?, ?)''', (year, ytg, ydz, sx))

conn.commit()
conn.close() 
