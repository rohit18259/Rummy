import pygame
import random
import time
import itertools

###  This is an indian rummy game.
# we will have 1 pure sequence of 4 cards, 1 sequence of 3 cards, and 2 sets of 3 cards each.
# you have to arrange the cards in the following sequences and sets in the order as given by the marking on the game screen.
# you have to arrange your cards in the above criteria and in each frame, the program will automatically parse your given card pattern and see if it is in the desired format to win. 
# if you do so , you will win , given that you finish your steps within 10 minutes of the starting of the game.
# if you dont finish it within 10 minutes, you will lose and PC will win.
# the rules of a sequence and set is givem in the readme.txt file.

v1=(32,580)
v2=(144,580)
v3=(256,580)
v4=(368,580)
v5=(480,580) 
v6=(592,580) 
v7=(702,580)
v8=(816,580) 
v9=(928,580)
v10=(1040,580)
v11=(1152,580)
v12=(1264,580)
v13=(1376,580)
decv=(550,200)
disv=(870,200)

def funcsuit(x):
	return x.suit

def differentsuit(l):
	z=sorted(l,key=funcsuit)
	for i in range(len(l)-1):
		if z[i].suit==z[i+1].suit:
			return False
	else:
		return True

def funcvalue(x):
	return x.value

def differentvalue(l):
	z=sorted(l,key=funcvalue)
	for i in range(len(l)-1):
		if z[i].value==z[i+1].value:
			return False
	else:
		return True

def ordervalue(x):
	if x.value=="ace":
		return 1
	elif x.value=="jack":
		return 11
	elif x.value=="queen":
		return 12
	elif x.value=="king":
		return 13
	elif x.value=="red":
		return -1
	elif x.value=="black":
		return -1
	elif x.value=="deck":
		return -1
	else:
		return int(x.value)

class card:
	def __init__(self,name,x=0,y=0,index=0):
		self.name=name
		self.x=x
		self.y=y
		self.index=index
		if '_' in name:
			self.value=name[:name.index('_')]
			self.suit=name[name.rindex('_')+1:]
		else:
			self.value="deck"
			self.suit="deck"


	def show(self,win):
		img=pygame.image.load(r"newcards/"+self.name+".png")
		s=pygame.Surface((80,122))
		s.fill((255,255,255))
		s.blit(img,(0,0))
		win.blit(s,(self.x,self.y))

	def showback(self,win):
		img=pygame.image.load(r"newcards/deck.png")
		s=pygame.Surface((80,122))
		s.fill((255,255,255))
		s.blit(img,(0,0))
		win.blit(s,(self.x,self.y))


background=pygame.image.load(r"background.png")


_2_clubs=card("2_of_clubs")
_2_diamonds=card("2_of_diamonds")
_2_hearts=card("2_of_hearts")
_2_spades=card("2_of_spades")

_3_clubs=card("3_of_clubs")
_3_diamonds=card("3_of_diamonds")
_3_hearts=card("3_of_hearts")
_3_spades=card("3_of_spades")

_4_clubs=card("4_of_clubs")
_4_diamonds=card("4_of_diamonds")
_4_hearts=card("4_of_hearts")
_4_spades=card("4_of_spades")

_5_clubs=card("5_of_clubs")
_5_diamonds=card("5_of_diamonds")
_5_hearts=card("5_of_hearts")
_5_spades=card("5_of_spades")

_6_clubs=card("6_of_clubs")
_6_diamonds=card("6_of_diamonds")
_6_hearts=card("6_of_hearts")
_6_spades=card("6_of_spades")

_7_clubs=card("7_of_clubs")
_7_diamonds=card("7_of_diamonds")
_7_hearts=card("7_of_hearts")
_7_spades=card("7_of_spades")

_8_clubs=card("8_of_clubs")
_8_diamonds=card("8_of_diamonds")
_8_hearts=card("8_of_hearts")
_8_spades=card("8_of_spades")

_9_clubs=card("9_of_clubs")
_9_diamonds=card("9_of_diamonds")
_9_hearts=card("9_of_hearts")
_9_spades=card("9_of_spades")

_10_clubs=card("10_of_clubs")
_10_diamonds=card("10_of_diamonds")
_10_hearts=card("10_of_hearts")
_10_spades=card("10_of_spades")

ace_clubs=card("ace_of_clubs")
ace_diamonds=card("ace_of_diamonds")
ace_hearts=card("ace_of_hearts")
ace_spades=card("ace_of_spades")

jack_clubs=card("jack_of_clubs")
jack_diamonds=card("jack_of_diamonds")
jack_hearts=card("jack_of_hearts")
jack_spades=card("jack_of_spades")

king_clubs=card("king_of_clubs")
king_diamonds=card("king_of_diamonds")
king_hearts=card("king_of_hearts")
king_spades=card("king_of_spades")

queen_clubs=card("queen_of_clubs")
queen_diamonds=card("queen_of_diamonds")
queen_hearts=card("queen_of_hearts")
queen_spades=card("queen_of_spades")

black_joker=card("black_joker")
red_joker=card("red_joker")
deck_=card("deck")


lv=[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]
dv=[decv,disv]
cv=lv+dv
cardlist=[_2_clubs,_2_diamonds,_2_hearts,_2_spades,_3_clubs,_3_diamonds,_3_hearts,_3_spades,_4_clubs,_4_diamonds,_4_hearts,_4_spades,_5_clubs,_5_diamonds,_5_hearts,_5_spades,_6_clubs,_6_diamonds,_6_hearts,_6_spades,_7_clubs,_7_diamonds,_7_hearts,_7_spades,_8_clubs,_8_diamonds,_8_hearts,_8_spades,_9_clubs,_9_diamonds,_9_hearts,_9_spades,_10_clubs,_10_diamonds,_10_hearts,_10_spades,ace_clubs,ace_diamonds,ace_hearts,ace_spades,jack_clubs,jack_diamonds,jack_hearts,jack_spades,king_clubs,king_diamonds,king_hearts,king_spades,queen_clubs,queen_diamonds,queen_hearts,queen_spades,black_joker,red_joker]
print(len(cardlist))

def shuffle(l):
	z=list(l)
	n=len(z)
	for i in range(n):
		j=random.randint(0,n-1)
		z[i],z[j]=z[j],z[i]
	return z

final=shuffle(cardlist)
cardlist=final[:13]
cpcardlist=final[13:26]
deck=final[26:-1]
discard=[final[-1]]

discard[0].x=870
discard[0].y=200
discard[0].index=15

print(len(deck))

for i in range(13):
	cls=cardlist[i]
	cls.x=lv[i][0]
	cls.y=lv[i][1]
	cls.index=i+1

for i in deck:
	cls=i
	cls.x=550
	cls.y=200
	cls.index=14

def transprect(x,y,width,length):
	s=pygame.Surface((width,length))
	s.set_alpha(50)
	s.fill((255,255,0))
	win.blit(s,(x,y))

def oncardtrue(posx,posy):
	for i in cv:
		if i[0]<=posx<=i[0]+80 and i[1]<=posy<=i[1]+122:
			return  True
	else:
		return False

def inplaying_discard(posx,posy):
	for i in lv+[disv]:
		if i[0]<=posx<=i[0]+80 and i[1]<=posy<=i[1]+122:
			return  True
	else:
		return False


def fetchcard(posx,posy):
	global num_deck,num_discard
	if decv[0]<=posx<=decv[0]+80 and decv[1]<=posy<=decv[1]+122:
		if num_deck>=1:
			c=deck[-1]
	#		deck.pop()
			num_deck=len(deck)
			print(num_deck)
			return c
		else:
			return False
	elif disv[0]<=posx<=disv[0]+80 and disv[1]<=posy<=disv[1]+122:
		c=discard[-1]
		return c

	else:
		for i in lv:
			if i[0]<=posx<=i[0]+80 and i[1]<=posy<=i[1]+122:
				c=cardlist[lv.index(i)]
				return c

def reshuffle(deck,discard):
	green=(0,255,0)
	blue=(0,0,255)
	a=time.time()
	pygame.font.init()
	font=pygame.font.Font('freesansbold.ttf',32)
	text=font.render('reshuffling',True,green,blue)
	textrect=text.get_rect()
	textrect.center=(750,400)
	while time.time()-a<=4:
		win.blit(text,textrect)
		pygame.display.update()

def drawtext(string,x,y,colort,colorb):
	pygame.font.init()
	font=pygame.font.Font('freesansbold.ttf',32)
	text=font.render(string,True,colort,colorb)
	textrect=text.get_rect()
	textrect.x,textrect.y=x,y
	win.blit(text,textrect)

def validflife(l):
	winn=1
	flife=l
	if flife[0].suit==flife[1].suit==flife[2].suit==flife[3].suit:
		winn=winn
	else:
		winn=0
	a1,b1,c1,d1=flife[0],flife[1],flife[2],flife[3]
	z1=[ordervalue(a1),ordervalue(b1),ordervalue(c1),ordervalue(d1)]
	if z1[0]==-1 or z1[1]==-1 or z1[2]==-1 or z1[3]==-1:
		winn=0
	else:
		winn=winn
	if z1[0]-z1[1]==-1 and z1[1]-z1[2]==-1 and z1[2]-z1[3]==-1:
		winn=winn
	else:
		winn=0
	if winn==1:
		return True
	else:
		return False

def validllife(l):
	winn=1
	llife=l
	for i in llife:
		if ordervalue(i)==-1:
			llife.remove(i)
	if len(llife)<=1:
		winn=winn
	else:
		for i in range(len(llife)-1):
			if llife[i].suit==llife[i+1].suit:
				winn=winn
			else:
				winn=0
	z2=[ordervalue(i) for i in llife]
	
	for i in range(len(z2)-1):
		if z2[i+1]-z2[i]==1:
			winn=winn
		else:
			winn=0
	if winn==1:
		return True
	else:
		return False

def validset1(l):
	winn=1
	set1=l
	a3,b3,c3=set1[0],set1[1],set1[2]
	if differentsuit([a3,b3,c3]):
		winn=winn
	else:
		winn=0
	z3=[ordervalue(a3),ordervalue(b3),ordervalue(c3)]
	for i in z3:
		if i==-1:
			z3.remove(i)
	if len(set(z3))==1:
		winn=winn
	else:
		winn=0
	if winn==1:
		return True
	else:
		return False

def validset2(l):
	winn=1
	set2=l
	a4,b4,c4=set2[0],set2[1],set2[2]
	if differentsuit([a4,b4,c4]):
		winn=winn
	else:
		winn=0
	z4=[ordervalue(a4),ordervalue(b4),ordervalue(c4)]
	for i in z4:
		if i==-1:
			z4.remove(i)
	if len(set(z4))==1:
		winn=winn
	else:
		winn=0
	if winn==1:
		return True
	else:
		return False


def cparrangecard(l):
	global cpcardlist
	var=False
	n=len(l)
	if not validflife(l[0:4]):
		z=itertools.permutations(l,4)
		for i in z:
			i=list(i)
			i1=i.copy()
			if validflife(i1):
				l.remove(i[0])
				l.remove(i[1])
				l.remove(i[2])
				l.remove(i[3])
				if len(l)==10:
					newc=l.pop()
					newc.x,newc.y=disv[0],disv[1]
					newc.index=15
					discard.append(newc)
				l=i+l
				cpcardlist=l
				var=True
				return var
	elif not validllife(l[4:7]):
		z=itertools.permutations(l[4:],3)
		for i in z:
			i=list(i)
			i1=i.copy()
			if validllife(i1):
				l.remove(i[0])
				l.remove(i[1])
				l.remove(i[2])
				if len(l)==11:
					newc=l.pop()
					newc.x,newc.y=disv[0],disv[1]
					newc.index=15
					discard.append(newc)
				l=l[0:4]+i+l[7:]
				cpcardlist=l
				var=True
				return var
	elif not validset1(l[7:10]):
		z=itertools.permutations(l[7:],3)
		for i in z:
			i=list(i)
			i1=i.copy()
			if validset1(i1):
				l.remove(i[0])
				l.remove(i[1])
				l.remove(i[2])
				if len(l)==11:
					newc=l.pop()
					newc.x,newc.y=disv[0],disv[1]
					newc.index=15
					discard.append(newc)
				l=l[0:7]+i+l[10:]
				cpcardlist=l
				var=True
				return var
	elif not validset2(l[10:13]):
		z=itertools.permutations(l[10:],3)
		for i in z:
			i=list(i)
			i1=i.copy()
			if validset2(i1):
				l.remove(i[0])
				l.remove(i[1])
				l.remove(i[2])
				if len(l)==11:
					newc=l.pop()
					newc.x,newc.y=disv[0],disv[1]
					newc.index=15
					discard.append(newc)
				l=l[0:10]+i+l[13]
				cpcardlist=l
				var=True
				return var
	if len(l)==14:
		l.pop()
	cpcardlist=l
	return var

def playerwin(cardlist):
	winn=1
	flife=cardlist[0:4]
	if flife[0].suit==flife[1].suit==flife[2].suit==flife[3].suit:
		winn=winn
	else:
		winn=0
	a1,b1,c1,d1=flife[0],flife[1],flife[2],flife[3]
	z1=[ordervalue(a1),ordervalue(b1),ordervalue(c1),ordervalue(d1)]
	if z1[0]==-1 or z1[1]==-1 or z1[2]==-1 or z1[3]==-1:
		winn=0
	else:
		winn=winn
	if z1[0]-z1[1]==-1 and z1[1]-z1[2]==-1 and z1[2]-z1[3]==-1:
		winn=winn
	else:
		winn=0
	if winn==1:
		print("flife sequence true")
	llife=cardlist[4:7]
	for i in llife:
		if ordervalue(i)==-1:
			llife.remove(i)
	if len(llife)<=1:
		winn=winn
	else:
		for i in range(len(llife)-1):
			if llife[i].suit==llife[i+1].suit:
				winn=winn
			else:
				winn=0
	z2=[ordervalue(i) for i in llife]

	for i in range(len(z2)-1):
		if z2[i+1]-z2[i]==1:
			winn=winn
		else:
			winn=0
	if winn==1:
		print("llife sequence true")
	set1=cardlist[7:10]
	a3,b3,c3=set1[0],set1[1],set1[2]
	if differentsuit([a3,b3,c3]):
		winn=winn
	else:
		winn=0
	z3=[ordervalue(a3),ordervalue(b3),ordervalue(c3)]
	for i in z3:
		if i==-1:
			z3.remove(i)
	if len(set(z3))==1:
		winn=winn
	else:
		winn=0
	if winn==1:
		print("set1 true")
	set2=cardlist[10:13]
	a4,b4,c4=set2[0],set2[1],set2[2]
	if differentsuit([a4,b4,c4]):
		winn=winn
	else:
		winn=0
	z4=[ordervalue(a4),ordervalue(b4),ordervalue(c4)]
	for i in z4:
		if i==-1:
			z4.remove(i)
	if len(set(z4))==1:
		winn=winn
	else:
		winn=0
	if winn==1:
		print("set2 true")
	if winn==1:
		return True
	else:
		return False

def cpwin(cpcardlist):
	return playerwin(cpcardlist)

def cpplay(cpcardlist):
	if cparrangecard(cpcardlist+[discard[-1]])==True:
		return 
	else:
		cparrangecard(cpcardlist+[deck[-1]])

def displayplayerwin():
	red=(255,0,0)
	yellow=(255,255,0)
	a=time.time()
	pygame.font.init()
	font=pygame.font.Font('freesansbold.ttf',32)
	text=font.render('PLAYER WINS!! :)',True,red,yellow)
	textrect=text.get_rect()
	textrect.center=(750,400)
	while time.time()-a<=4:
		win.blit(text,textrect)
		pygame.display.update()

def displaycpwin():
	red=(255,0,0)
	yellow=(255,255,0)
	a=time.time()
	pygame.font.init()
	font=pygame.font.Font('freesansbold.ttf',32)
	text=font.render('COMPUTER WINS!',True,red,yellow)
	textrect=text.get_rect()
	textrect.center=(750,400)
	while time.time()-a<=4:
		win.blit(text,textrect)
		pygame.display.update()

start=time.time()

re=0

deck_.x=550
deck_.y=200
deck_.index=14
# deck pile index = 14
# discard pile index = 15
num_deck=27
num_discard=1

up=True
Down=False

count=0
fetch=False

win=pygame.display.set_mode((1500,800))
pygame.display.set_caption("Rummy Game")

run=True
while run:
	pygame.time.delay(20)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		pos=pygame.mouse.get_pos()
		posx,posy=pos[0],pos[1]
		if fetch==True and c!=False:
			c.x=posx
			c.y=posy

		if event.type==pygame.MOUSEBUTTONDOWN:

			if oncardtrue(posx,posy) and count%2==0:
				c=fetchcard(posx,posy)
				fetch=True
				count=1
			elif fetch==True:
				count=0
				fetch=False

				if not oncardtrue(posx,posy):
					ind=c.index
					if ind>13:
						c.x,c.y=dv[ind-14][0],dv[ind-14][1]
					else:
						c.x,c.y=lv[ind-1][0],lv[ind-1][1]
				else:
					if inplaying_discard(posx,posy):
						other=fetchcard(posx,posy)
						if c.index<=13 and other.index==15:
							c.x,c.y=lv[c.index-1][0],lv[c.index-1][1]
						elif c.index==15 and other.index==15:
							c.x,c.y=dv[1][0],dv[1][1]
						elif c.index!=14:
							cind=c.index
							othindex=other.index
							c.index,other.index=othindex,cind
							#c.x,c.y,other.x,other.y=other.x,other.y,c.x,c.y
							if c in discard:
								c.x,c.y,other.x,other.y=other.x,other.y,dv[1][0],dv[1][1]
								cardlist[othindex-1],discard[-1]=c,other
							else:
								c.x,c.y,other.x,other.y=other.x,other.y,lv[cind-1][0],lv[cind-1][1]
								cardlist[cind-1],cardlist[othindex-1]=other,c
						elif c.index==14:
							if other.index<=13:
								cind=c.index
								othindex=other.index
								c.index,other.index=othindex,15
								c.x,c.y,other.x,other.y=other.x,other.y,dv[1][0],dv[1][1]
								cardlist[othindex-1]=c
								discard.append(other)
								deck.pop()
							elif other.index==15:
								c.x,c.y=dv[0][0],dv[0][1]
					else:
						other=fetchcard(posx,posy)
						if c.index<=13:
							c.x,c.y=lv[c.index-1][0],lv[c.index-1][1]
						elif c.index==15:
							c.x,c.y=dv[1][0],dv[1][1]
						elif c.index==14:
							c.x,c.y=dv[0][0],dv[0][1]

		if deck==[]:
			re=1
			for i in range(27):
				cls=discard[0]
				cls.index=14
				cls.x,cls.y=dv[0][0],dv[0][1]
				discard.pop(0)
				deck.append(cls)

	win.fill((0,0,0))
	win.blit(background,(0,0))
	transprect(550,200,80,122)
	transprect(870,200,80,122)
	pygame.draw.line(win,(255,0,0),(32,540),(448,540),1)
	pygame.draw.line(win,(0,255,0),(480,540),(782,540),1)
	pygame.draw.line(win,(0,0,255),(816,540),(1120,540),1)
	pygame.draw.line(win,(0,255,255),(1152,540),(1456,540),1)
	drawtext("4 card pure sequence",32,480,(255,255,255),(0,0,0))
	drawtext("3 card sequence",480,480,(255,255,255),(0,0,0))
	drawtext("3 card set",816,480,(255,255,255),(0,0,0))
	drawtext("3 card set",1152,480,(255,255,255),(0,0,0))


	for i in lv:
		transprect(i[0],i[1],80,122)
	for cls in cardlist:
		cls.show(win)
	for cls in discard[-2:]:
		if cls:
			cls.show(win)

	for cls in deck[-2:]:
		if cls:
			cls.showback(win)

	pwins=playerwin(cardlist)
	if pwins==True:
		displayplayerwin()
		break

	if re==1:
		reshuffle(deck,discard)
		re=0
	#cpplay(cpcardlist)
	#cpwins=cpwin(cpcardlist)
	#if cpwins==True:
	#	displaycpwin()
	#	break
	if time.time()-start>=600:
		displaycpwin()
		break

	pygame.display.update()


pygame.quit()