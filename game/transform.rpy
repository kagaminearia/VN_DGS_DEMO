# QTE setting
# init:
#     $ timer_range = 0
#     $ timer_jump = 0
#     $ time = 0


# screen countdown:
#     timer 0.01 repeat True action If(time>0, 
#         true=SetVariable('time',time-0.01),false=[Hide('countdown'),Jump(timer_jump)])
#     bar value time range timer_range xalign 0.5 yalign 0.07 xmaximum 300 at alpha_dissolve

# screen countdown:
#     frame:
#         xalign 0.5
#         yalign 0.07
#         xmaximum 300
#         has vbox

#         bar value AnimatedValue(value=time, range=timer_range, delay=0.1) at alpha_dissolve

#     timer 0.05 repeat True action If(time > 0.05, 
#         SetVariable("time", time - 0.05),
#         [Hide("countdown"), Jump(timer_jump)])

screen countdown(start_time, total_time, fail_label):

    default active = True
    default time_left = start_time

    frame:
        xalign 0.5
        yalign 0.07
        xmaximum 300
        has vbox

        bar value AnimatedValue(
            value=time_left,
            range=total_time,
            delay=0.1
        )

    timer 0.05 repeat True action If(
        active,
        If(
            time_left > 0.05,
            SetScreenVariable("time_left", time_left - 0.05),
            [
                SetScreenVariable("active", False),
                Hide("countdown"),
                Jump(fail_label)
            ]
        )
    )



# fade the bar in and out
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0


transform char_mid:
    zoom 0.5
    xalign 0.5
    yalign 0.1
    yoffset 80
    xoffset 20

transform char_right:
    zoom 0.5
    xalign 1.0
    yalign 0.1
    yoffset 80
    xoffset 80

transform char_left:
    zoom 0.5
    xalign 0.0
    yalign 0.1
    yoffset 80
    xoffset 200

transform char_c:
    zoom 0.75
    xalign 0.5
    yalign 0.1
    yoffset 90

transform cg0:
    zoom 0.5
    xalign 0.5
    yalign 0.5

transform cg1:
    xalign 0.5
    yalign 0.5

transform clue:
    zoom 0.55
    xalign 0.5
    yalign 0.5
    yoffset -120


transform cg3_1:
    zoom 0.65
    xalign 0.5
    yalign 0.5

transform cg3_2:
    zoom 0.75
    xalign 0.5
    yalign 0.5

transform cg3_3:
    zoom 0.85
    xalign 0.5
    yalign 0.5
    

init python:
    # change punch variable
    hpunch = Move((30, 0), (-30, 0), .50, bounce=True, repeat=True, delay=.275)
    vpunchs = Move((0, 10), (0, -10), 0.3, bounce=True, repeat=True, delay=.275)
    vpunchm = Move((0, 40), (0, -40), 0.2, bounce=True, repeat=True, delay=.275)
    shake = Move((70, 70), (-70, -70), 3, bounce=True, repeat=True, delay=.275)


transform shaking:
    linear 0.1 xoffset -2 yoffset 2 
    linear 0.1 xoffset 3 yoffset -3 
    linear 0.1 xoffset 2 yoffset -2
    linear 0.1 xoffset -3 yoffset 3
    linear 0.1 xoffset 0 yoffset 0
    repeat