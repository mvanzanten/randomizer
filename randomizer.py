import random, sys, time#, pygame

#christmas song
###pygame.mixer.init()
###pygame.mixer.music.load("wewishyou.mp3")
###pygame.mixer.music.play()
#christmas song

#preparation
contestants = open("contestants.txt").readlines()
contestants = [s.rstrip() for s in contestants]
spins = random.randint(3632,4712)
counter = random.randint(3,29)
t_count = 0
t_loops = 4

#console colours
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[34m' # orange
W  = '\033[00m' # white
my_color = [R, G, O, W]

#print pretty title
title= """
  ______     _ _   ___           __
 /_  __/____(_) | / (_)___ ___  / /_  __  _______
  / / / ___/ /  |/ / / __ `__ \/ __ \/ / / / ___/
 / / / /  / / /|  / / / / / / / /_/ / /_/ (__  )
/_/ /_/  /_/_/ |_/_/_/ /_/ /_/_.___/\__,_/____/

                                              """

time.sleep(1)
print(title)
time.sleep(0.3)

print 'Picking a winner',

while t_count <= t_loops:
    time.sleep(0.2)
    sys.stdout.write('.')
    sys.stdout.flush()
    t_count = t_count + 1

print '\n\n'
sys.stdout.flush()

while counter <= spins:
    time.sleep(0.003)
    winner = random.choice(contestants)
    sys.stdout.write(" " + winner)
    sys.stdout.write(' ')
    sys.stdout.flush()
    increment = random.randint(1,3)
    counter = counter + increment
sys.stdout.write(' ')
sys.stdout.flush()
print '\n\n'

time.sleep(0.2)
sys.stdout.write('Our Winner is: ')
sys.stdout.write(winner)
print '\n'
f = open("contestants.txt","r+")
d = f.readlines()
f.seek(0)
for i in d:
    if i != winner+"\n":
        f.write(i)
f.truncate()
f.close()
raw_input("Press enter to exit ;)")
