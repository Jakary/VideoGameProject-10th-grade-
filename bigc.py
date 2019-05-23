from libgame import*
game = Game(1100,600,"BIG CHUNGUS")

bk1 =Image("forrest.jpg",game)
bk1.resizeTo(1100,600)
bk2 = Image("kitchen.jpg",game)
bk2.resizeTo(1100,600)
bk3 = Image("hell.png",game)
bk3.resizeTo(1100,600)
bk4 = Image("hell333.jpg",game)
bk4.resizeTo(1100,600)
bk5 = Image("swamp.png",game)
game.setBackground(bk5)
bk5.resizeTo(1100,600)
bk6 = Image("wildland.jpg",game)
game.setBackground(bk6)
bk6.resizeTo(1100,600)
bk7 = Image("space.png",game)
game.setBackground(bk7)
bk7.resizeTo(1100,600)
bk8 = Image("jungle.jpg",game)
deadscreen =Image("deadchung.png",game)
victoryscreen = Image("chung1.png",game)
storyscreen = Image("story screen.png",game)


squid = Image("squid.png",game)
squid.resizeBy(-20)
squidr = Image("squidr.png",game)
guy =Image("guy.png",game)
chef = Image("chef.png",game)
chef.resizeBy(-40)
chefr = Image("chefr.png",game)
chefr.resizeBy(-40)
big = Image("bigc.png",game)
big.resizeBy(-75)
bigr =Image("bigcr.png",game)
bigr.resizeBy(-75)
bag = Image("thebag.png",game)
bag.resizeBy(-70)
storychung = Image("storychung.png",game)
storychung.resizeBy(-80)
storychef = Image("chefstory.png",game)
storychef.resizeBy(-50)
storyguy = Image("guystory.png",game)
storyguy.resizeBy(-50)
storysquid = Image("squidstory.png",game)
storysquid.resizeBy(-40)
title = Image("chungustext.png",game)
title.y =140
text = Image("texbox.png",game)
razorwire = Image("razorwire.png",game)
razorwire.y =200
play = Image("playbutton.png",game)
play.y=360
story = Image("storybutton.png",game)
story.y=480
storys= Image("story screen.png",game)
easteregg = Image("easteregg.jpg",game)
easteregg.resizeTo(1100,600)
chungtext1 = Image ("chungtext1.png",game)
chungtext2 = Image("chungtext2.png",game)
chungtext3 = Image("chungtext3.png",game)
chungtext4 = Image("chungustext4.png",game)
chungtext4.resizeBy(-54)
chungtext5 = Image("chungtext4.png",game)
chungtext6 = Image("chungtext6.png",game)
chungtext6.resizeBy(-30)
chungtext7 = Image("chungtext7.png",game)
chungtext8 = Image("chungtext8.png",game)
chungtext8.resizeBy(-40)
food =[]
for index in range(150):
    food.append(Image("carrots.png",game))
for index in range(150):
    food[index].resizeBy(-80)
    x=randint(100,700)
    y=randint(100,10000)
    s=randint(5,7)
    food[index].moveTo(x,y)
    food[index].setSpeed(s,0)
#Title
while not game.over:
    game.processInput()
    bk2.draw()
    chef.draw()
    chef.moveTo(350,345)
    big.draw()
    big.moveTo(810,350)
    guy.draw()
    guy.moveTo(100,345)
    title.draw()
    play.draw()
    story.draw()
    razorwire.draw()
    if play.collidedWith(mouse)and mouse.LeftClick:
        game.over = True
    game.update(60)
game.over = True
#Level1
while not game.over:
    game.processInput()
    bk2.draw()
    big.moveTo(260,390)
    text.draw()
    text.moveTo(810,497)
    chungtext1.draw()
    chungtext1.moveTo(788,475)
    storychung.draw()
    storychung.moveTo(975,425)
    game.update(60)
game.over = False
#Level1.1
while not game.over:
    game.processInput()
    bk2.draw()
    big.moveTo(300,390)
    chef.draw()
    chef.moveTo(115,399)
    text.draw()
    text.moveTo(810,497)
    chungtext2.draw()
    chungtext2.moveTo(788,497)
    storychef.draw()
    storychef.moveTo(975,465)
    game.update(60)
game.over = False
#Level1.2
while not game.over:
    game.processInput()
    bk2.draw()
    big.moveTo(300,390)
    chef.draw()
    chef.moveTo(115,399)
    text.draw()
    text.moveTo(810,497)
    chungtext3.draw()
    chungtext3.moveTo(788,497)
    storychung.draw()
    storychung.moveTo(975,425)
    game.update(60)
game.over = False
#Level2
while not game.over:
    game.processInput()
    bk6.draw()
    big.moveTo(mouse.x,mouse.y)
    for index in range(len(food)):
        food[index].move()
    if food[index].isOffScreen("bottom")and food[index].visible:
        game.score+=10
        game.update(60)
game.over = False

#Level3
while not game.over:
    game.processInput()
    bk5.draw()
    guy.draw()
    guy.moveTo(260,340)
    bag.draw()
    bag.moveTo(730,300)
    text.draw()
    text.moveTo(810,497)
    storyguy.draw()
    storyguy.moveTo(975,450)
    chungtext4.draw()
    chungtext4.moveTo(730,455)
    game.update(60)
game.over = False

    
#Level3.1
while not game.over:
    game.processInput()
    game.scrollBackground("down",7)
    chungtext5.draw()
    game.update(60)
game.over = False

#Level3.2
while not game.over:
    game.processInput()
    bk2.draw()
    big.draw()
    big.moveTo(810,340)
    text.draw()
    text.moveTo(300,510)
    chungtext6.draw()
    chungtext6.moveTo(210,510)
    storychung.draw()
    storychung.moveTo(450,440)
    game.update(60)
game.over = False
#Level4
while not game.over:
    game.processInput()
    bk2.draw()
    chefr.draw()
    chefr.moveTo(810,340)
    text.draw()
    text.moveTo(300,510)
    chungtext7.draw()
    chungtext7.moveTo(232,460)
    storychef.draw()
    storychef.moveTo(430,477)
    game.update(60)
game.over= False
#Level4.1
while not game.over:
    game.processInput()
    game.scrollBackground("down",7)
    big.draw()
    if keys.Pressed[K_RIGHT]:
        big.x+=12
    if keys.Pressed[K_LEFT]:
        big.x-=12
    if keys.Pressed[K_UP]:
        big.y-=5
        big.rotateTo(10)
    else:
            big.rotateTo(-10)
            big.y+=2
    for index in range(len(food)):
        food[index].move()
    if food[index].isOffScreen("bottom")and food[index].visible:
        game.update(60)
    game.update(60)
game.over = False
#Level 5
while not game.over:
    game.processInput()
    game.scrollBackground("down",6)
    text.draw()
    storysquid.draw()
    storysquid.moveTo(500,495)
    squid.draw()
    squid.moveTo(740,300)
    chungtext8.draw()
    chungtext8.moveTo(244,470)
    for index in range(len(food)):
        food[index].move()
    if food[index].isOffScreen("bottom")and food[index].visible:
        game.update(60)
    game.update(60)
game.over= False
#Level 5.1
while not game.over:
    game.processInput()
    game.scrollBackground("down",6)
    text.draw()
    storysquid.draw()
    storysquid.moveTo(500,495)
    squid.draw()
    squid.moveTo(740,300)
    #chungtextgoeshere
    game.update(60)
game.over= False
#Level5.2
while not game.over:
    game.processInput()
    game.scrollBackground("down",6)
    big.moveTo(mouse.x,mouse.y)
    game.update(60)
game.over= False

    
