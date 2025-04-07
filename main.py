# Mad Libs ゲーム(this program creates a Mad Libs game)
          #Python で作成した入力型の物語ゲームです.
          #ユーザーの入力によって、ストーリーが変化します。

# Python



print("Please enter the following:")

adjective = input("adjective:")      #happy
animal = input("animal:")            #zebra
verb1 = input("verb")                #sneeze
exclamation = input("exclamation:")  #hooray
verb2 = input("verb:")               #read
verb3 = input("verb:")               #drive

place = input("a place:")
food = input("a type of food:")

print("your story is:")

story = f"""The other day, I was really in trouble.It all started when I saw a very {adjective} {animal} {verb1} down the hallway at {place}. "{exclamation}!" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tired to {verb3} right in front of my family. Later, we celebrated by eating some delicious {food}."""

print(story)



