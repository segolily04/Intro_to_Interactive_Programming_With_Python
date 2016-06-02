# template for "Stopwatch: The Game"

import simplegui

# define global variables
tick_interval = 0 
stop_count = 0
win_count = 0 
stopwatch_running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    tenths = t % 10
    t = t // 10
    seconds = t % 60
    t = t//60
    minutes = t
    
    if seconds < 10:
        return str(minutes) + ":0"+str(seconds)+"."+str(tenths) 
    else:
        return str(minutes) + ":"+str(seconds)+"."+str(tenths) 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global stopwatch_running
    timer.start()
    stopwatch_running = True

def stop_handler():
    global stop_count, win_count, stopwatch_running
    timer.stop()
    
    if stopwatch_running:
        stop_count += 1
        stopwatch_running = False
    
    if tick_interval % 10 == 0:
        win_count += 1
     
    frame.set_draw_handler(draw)
    

def reset_handler():
    global tick_interval, stop_count, win_count
    tick_interval = 0
    stop_count = 0 
    win_count = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global tick_interval
    tick_interval += 1
    frame.set_draw_handler(draw)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(tick_interval), [40, 110], 50, "White")
    canvas.draw_text(str(win_count)+"/"+str(stop_count), [125, 40], 40, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch Game", 200, 200) 


# register event handlers
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)
timer = simplegui.create_timer(100, tick) 

# start frame
frame.start()

# Please remember to review the grading rubric
