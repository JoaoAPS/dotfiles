from libqtile.config import Key, Screen, Group, Drag, Click, ScratchPad, DropDown, Match
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, extension, hook
from typing import List  # noqa: F401
import os, subprocess

import MyWidgets

#============= Keys =================
mod = "mod4"

keys = [
	#Movement
	Key([mod], "j", lazy.layout.down()),
	Key([mod], "k", lazy.layout.up()),
	Key([mod], "h", lazy.layout.left()),
	Key([mod], "l", lazy.layout.right()),
	Key([mod, "shift"],   "h", lazy.layout.swap_left()),
	Key([mod, "shift"],   "l", lazy.layout.swap_right()),
	Key([mod, "shift"],   "j", lazy.layout.shuffle_down()),
	Key([mod, "shift"],   "k", lazy.layout.shuffle_up()),
	Key([mod, "control"], "l", lazy.layout.grow()),
	Key([mod, "control"], "h", lazy.layout.shrink()),
	Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "f", lazy.window.toggle_floating()),
    Key([mod], 'apostrophe', lazy.next_screen()),

    #Creation/Destruction
    Key([mod], "Return", lazy.spawn("st -e fish")),
    Key([mod], "Tab", lazy.window.kill()),
    Key([mod], "d", lazy.spawn('rofi -show drun -modi drun -config ~/.config/rofi/config')),
    Key([mod, "shift"], "d", lazy.spawn('rofi -show run -modi drun -config ~/.config/rofi/config')),

    #Appearance
    Key([mod], "i", lazy.next_layout()),
    Key([mod], "u", lazy.prev_layout()),
    Key([mod], "b", lazy.hide_show_bar("top")),
    Key([mod, 'shift'], "b", lazy.hide_show_bar("bottom")),
    
    #Change State
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod], "BackSpace", lazy.spawn('prompt "Shutdown?" "sudo shutdown -h now"')),
    Key([mod, "shift"], "BackSpace", lazy.spawn('sysact')),
    Key([mod, "control"], "BackSpace", lazy.spawn('prompt "Exit qtile?" "qtile-cmd -o cmd -f shutdown"')),
    Key([mod], "Pause", lazy.spawn("lockscreen")),

    #Volume control
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('amixer -q -D pulse sset Master 5%+')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('amixer -q -D pulse sset Master 5%-')),
    Key([], 'XF86AudioMute', lazy.spawn('amixer set Master toggle')),
    Key([mod], 'equal', lazy.spawn('amixer -q -D pulse sset Master 5%+')),
    Key([mod], 'minus', lazy.spawn('amixer -q -D pulse sset Master 5%-')),
    Key([mod, "shift"], 'minus', lazy.spawn('amixer set Master toggle')),
    #Music control
    Key([mod], "p", lazy.spawn("playerctl play-pause")),
    Key([mod], "period", lazy.spawn("playerctl next")),
    Key([mod], "comma", lazy.spawn("playerctl previous")),
    
    #Screen Brightness control
    Key([], 'XF86MonBrightnessUp',   lazy.spawn('xbacklight -inc 10')),
    Key([], 'XF86MonBrightnessDown', lazy.spawn('xbacklight -dec 10')),
    
    #External commands
    Key([mod], 'F2', lazy.spawn('dmenumount')),
    Key([mod, 'shift'], 'F2', lazy.spawn('dmenuumount')),
    Key([mod], 'F3', lazy.spawn('screenshot')),
    #Key([], 'SysReq', lazy.spawn('screenshot')),
    Key([mod], 'F4', lazy.spawn('choosedisplay')),
    
    #Lauchers
    Key([mod], 's', lazy.spawn('spotify')),
    Key([mod], 'x', lazy.spawn('brave')),
]


#============= Layouts =================
layouts = [
    layout.MonadTall(
        ratio=0.63,
        border_normal="#000000",
        border_focus="#0000ff",
        margin=5,
        border_width=2,
        single_margin=0,
        single_border_width=0,
        new_at_current=True,
        name="monad"
    ),
    layout.MonadTall(
        ratio=0.63,
        border_normal="#000000",
        border_focus="#0000ff",
        margin=0,
        border_width=2,
        single_margin=0,
        single_border_width=0,
        new_at_current=True,
        name="monad_nogaps"
    ),
    layout.RatioTile(),
    # layout.Tile(),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

#============= Groups =================
group_names  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'q',   'w',  'e', '0']
group_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '', '', '', '']

group_layouts = [
    "monad", "monad", "monad",
    "monad", "monad", "monad",
    "monad", "monad", "monad",
    "max",   "monad", "max",   "max"
]

#Aplicações que devem ser abertas naquele grupo
group_matches = [
    None, None, None,
    None, None, None,
    None, None, None,
    [Match(wm_class=["Subl3", "code-oss", "Atom"])],
    None,
    [Match(wm_class=["Firefox", "Brave-browser", "Google-chrome"], role=["browser"])],
    [Match(wm_class=["Spotify"])]
]

#Comandos a serem executados quando o grupo é criado
group_spawns  = [
    None, None, None,
    None, None, None,
    None, None, None,
    None, 'st -e fish', 'brave', None
]

groups = []
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
            layout=group_layouts[i],
            matches=group_matches[i],
            spawn=group_spawns[i],
        )
    )


for g in groups:
    keys.extend([
        Key([mod], g.name, lazy.group[g.name].toscreen(toggle=False)),
        Key([mod, "shift"], g.name, lazy.window.togroup(g.name)),
    ])


#============= Scratchpad =================
groups.append(
    ScratchPad("scratchpad", [
        DropDown("term", "/usr/local/bin/st -e vim", width=0.8, height=0.7),
        DropDown("calc", "speedcrunch",  width=0.5, height=0.6, x=0.1, y=0.2),
    ]), )

keys.extend([
    Key([mod, 'shift'], 'Return', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod, 'shift'], 'a', lazy.group['scratchpad'].dropdown_toggle('calc')),
])


#============= Bars =================
widget_defaults = dict(
    font='ubuntu',
    fontsize=13,
    foreground="#dddddd",
    padding=10,
)
extension_defaults = widget_defaults.copy()

topBar = bar.Bar(
    [
        widget.GroupBox(
            active="#aaaaaa",
            block_highlight_text_color="#00c8e6",
            borderwidth=0,
            hide_unused=True,
            padding=5,
            fontsize=13
        ),
        widget.Prompt(),
        widget.Spacer(),
        widget.Pomodoro(
            color_inactive='#eeeeee',
            prefix_inactive='<span color="#222222"></span>',
            color_active='#ffffff',
            prefix_active='<span foreground="red"> </span>',
            color_break='#00ff00',
            length_pomodori=20,
        ),
        MyWidgets.Volume(
            update_interval=1,
            step=5,
            low_thresshold=10,
            high_thresshold=50
        ),

        MyWidgets.Memory(
            format='<span foreground="{color}"> {MemFree}G{SwapFree}</span>',
            update_interval=3
        ),
        MyWidgets.CPU(
            format='<span foreground="{color}"> {load_percent}%</span>',
            update_interval=5
        ),
        widget.Battery(
            charge_char='<span color="yellow">\uf0e7</span>',
            discharge_char='\uf240',
            full_char='\uf1e6',
            unknown_char='\uf128',
            empty_char='<span color="red"></span>',
            format='{char} {percent:2.0%} ({hour:d} : {min:02d})',
            low_percentage=0.25,
            hide_threshold=0.99,
            notify_below=0.10
        ),
        MyWidgets.Wifi(
            interface="wlp1s0",
            format='<span foreground="{color}"> {percent:2.0%}</span>',
            update_interval=5,
        ),
        widget.Wlan(
            interface="enp2s0",
            format='<span foreground="#00ff7f"></span>',
            update_interval=5,
        ),
        widget.Clock(
            format='%a %d/%m %H:%M',
            foreground="#ffffff",
            fontsize=15,
            update_interval=15
        ),
    ],
    25,
    background="#151722",
    opacity=0.85
)

bottomBar = bar.Bar(
    [
        widget.CurrentLayout (),
        widget.CapsNumLockIndicator(),
        widget.CheckUpdates(
            colour_no_updates="#909090",
            colour_have_updates="#74d4cd",
            execute="sudo pacman -Syuu",
            update_interval=12*3600
        ),
        widget.Spacer(),
        widget.Clipboard(
            update_interval=1,
        ),
        widget.Systray(),
        widget.QuickExit(),
    ],
    25,
    background="#474a5c",#"#151722",
    opacity=1
)


#============= Screens =================
# Finds how many monitors are connected
from Xlib import display
d = display.Display()
res = d.screen().root.xrandr_get_screen_resources()._data
num_screens = 0
for output in res['outputs']:
    mon = d.xrandr_get_output_info(output, res['config_timestamp'])._data
    if mon['modes']:
        num_screens += 1

screens = [
	Screen(top=topBar, bottom=bottomBar),
]
for i in range(1, num_screens):
	screens.append(Screen())

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]



dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

#============= Startup =================
@hook.subscribe.startup_once
def startup_once():
    from datetime import datetime

    startup_file = os.path.expanduser('~/.config/qtile/startup.sh')
    try:
        subprocess.call([startup_file])
    except Exception as e:
        with open('qtile_log', 'a+') as f:
            f.write(
                datetime.now().strftime('%Y-%m-%dT%H:%M') +
                + ' ' + str(e) + '\n')



@hook.subscribe.startup
def startup():
    bottomBar.show(False)
    groups[-3].toscreen()
