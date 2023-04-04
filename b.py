from snake import Snake

mysnake=Snake()
mysnake.print_out()
for i in range(100):
    # ['Up','Down','Right','Left']
    try:
        mysnake.move(int(input('Your move: ')))
        mysnake.print_out()
        if mysnake.isgameovered:break
    except:
        print('Game overed!')
        break