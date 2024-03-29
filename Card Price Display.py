#text file you want to display
openfile='File you want to read, should be the same name as the file you saved data in'

#variables for pygame
import pygame
pygame.init()
set=f'{openfile}'
(width,height)=(300,1000)
background_color= (0,0,0)
screen=pygame.display.set_mode((width,height))
screen.fill(background_color)
pygame.display.set_caption(f'{set}')
f= open(f'{openfile}.txt', 'r')
raw_data=[]
data=[]



#takes txt file and converts it into a list of strings
for i in f:
    if i=='\n':continue
    lastchar=i[-1:]
    i=i[:-1]
    raw_data.append(i)
raw_data[-1]= raw_data[-1] + lastchar
#takes the string and turns it into a list seperated by commas
for i in raw_data:
    i=i.split('@')
    data.append(i)
print(raw_data)
print(data)
adjuster=int(len(data) / 3)
baseadjuster=int(adjuster)



def display(data, adjuster, baseadjuster):
    #resets screen
    screen.fill(background_color)
    # sets font for header (set/date)
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('', True, (0, 0, 0), (0, 0, 0))
    text=font.render(f'{data[adjuster * 3 - 3][0]}', True, (255, 255, 255), (0, 0, 0))
    screen.blit(text, (10, 10))
    if adjuster>1:
        text=font.render('Back', True, (255,255,255),(0,0,0))
        screen.blit(text, (135, 10))
    if adjuster!=baseadjuster:
        text = font.render('Forward', True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (195, 10))
    #sets font for body/prices
    font = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render('', True, (0, 0, 0), (0, 0, 0))
    for i in range(len(data[adjuster * 3 - 2])):
        text = font.render (f'{data[adjuster * 3 - 2][i]}' + '  ' + f'{data[adjuster * 3 - 1][i]}', True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, (10, 40+i*20))
    pygame.display.update()



def button(mouse,adjuster,baseadjuster):
    #back button
    if 135 <=mouse[0]<=181 and 10<=mouse[1]<=25 and adjuster !=1:
        adjuster-=1
        display(data, adjuster, baseadjuster)
    #forward button
    if 195 <= mouse[0] <= 275 and 10 <= mouse[1] <= 25 and adjuster != baseadjuster:
        adjuster+=1
        display(data, adjuster, baseadjuster)
    return adjuster



display(data, adjuster, baseadjuster)
pygame.display.flip()
running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running= False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            adjuster=button(mouse,adjuster,baseadjuster)
            print(mouse)
        pygame.display.update()
        mouse = pygame.mouse.get_pos()

