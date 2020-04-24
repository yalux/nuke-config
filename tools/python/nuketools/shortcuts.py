import nuke

#--------------------------------------------------------------------------------------------
#
#   Customize Nuke Shortcuts
#
#--------------------------------------------------------------------------------------------

# In Nuke 9 there are now 3 different shortcut contexts: 
#    Window Context = 0 (default), Application Context = 1, DAG Context = 2


# Misc
nuke.menu('Nuke').findItem('File').addCommand('Start Performance Timers', 'nuke.startPerformanceTimers()', '', index=20)
nuke.menu('Nuke').findItem('File').addCommand('Stop Performance Timers', 'nuke.stopPerformanceTimers()', '', index=21)
nuke.menu('Nuke').findItem('File').findItem('Clear').setShortcut('ctrl+shift+w')
nuke.menu('Nuke').findItem('&Cache').findItem('Clear All').setShortcut('ctrl+alt+meta+shift+w')
nuke.menu('Nuke').findItem('Workspace').addCommand("Toggle Fullscreen", 'nuke.toggleFullscreen()', 'ctrl+alt+shift+f')

# Show or hide Nuke statusbar
nuke.menu('Nuke').addCommand('File/Show Status Bar', 'import hiero; hiero.ui.mainStatusBar.show()')
nuke.menu('Nuke').addCommand('File/Hide Status Bar', 'import hiero; hiero.ui.mainStatusBar.hide()')


# nuke.menu('Nuke').findItem("Render").addCommand("Render Selected", 'terminal_render.render(nuke.selectedNodes())', 'F7', index=5)
# nuke.menu('Nuke').addCommand('Edit/Node/Label Dot', 'createBackdrop.create_dot()', 'ctrl+meta+shift+d', shortcutContext=2)
# nuke.menu('Nuke').addCommand('Edit/Node/Create Backdrop', 'createBackdrop.create()', 'shift+b')
# python_scripts.addCommand('Cornerpin To Matrix', 'cornerpin_matrix.create()', '')

# Viewer Shortcuts
nuke.menu('Viewer').addCommand('Next Frame', 'nuke.activeViewer().frameControl(1)', 'shift+f')
nuke.menu('Viewer').addCommand('Previous Frame', 'nuke.activeViewer().frameControl(-1)', 'shift+d')
nuke.menu('Viewer').addCommand('Next Keyframe', 'nuke.activeViewer().frameControl(2)', 'alt+shift+f')
nuke.menu('Viewer').addCommand('Previous Keyframe', 'nuke.activeViewer().frameControl(-2)', 'alt+shift+d')
nuke.menu('Viewer').addCommand('Next Frame', 'nuke.activeViewer().frameControl(1)', 'shift+f')
nuke.menu('Viewer').addCommand('Play Forward', 'nuke.activeViewer().frameControl(5)', 'ctrl+alt+f')
nuke.menu('Viewer').addCommand('Play Backward', 'nuke.activeViewer().frameControl(-5)', 'ctrl+alt+d')
nuke.menu('Viewer').findItem('Show Overscan').setShortcut('alt+shift+o')


# Nodes
nuke.toolbar('Nodes').addCommand('Merge/Merge', 'nuke.createNode("Merge2", "bbox B", inpanel=False)', 'm', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/MergeUnion', 'nuke.createNode("Merge2", "bbox union", inpanel=False)', 'alt+meta+m', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Plus', 'nuke.createNode("Merge2", "operation plus output rgb", inpanel=False)', 'alt+meta+p', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/From', 'nuke.createNode("Merge2", "operation from output rgb", inpanel=False)', 'alt+meta+f', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Mask', 'nuke.createNode("Merge2", "operation mask bbox intersection", inpanel=False)', 'alt+meta+a', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B", inpanel=False)', 'alt+meta+s', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Under', 'nuke.createNode("Merge2", "operation under bbox B", inpanel=False)', 'alt+meta+u', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Divide', 'nuke.createNode("Merge2", "operation divide", inpanel=False)', 'alt+meta+d', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Multiply', 'nuke.createNode("Merge2", "operation multiply output rgb", inpanel=False)', 'alt+meta+t', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/MultiplyAlpha', 'nuke.createNode("Merge2", "operation multiply", inpanel=False)', 'alt+shift+meta+t', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/MergeAlpha', 'nuke.createNode("Merge2", "operation screen bbox union Achannels alpha Bchannels alpha output alpha", inpanel=False)', 'alt+meta+shift+e', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Merges/Screen', 'nuke.createNode("Merge2", "operation screen bbox union", inpanel=False)', 'alt+meta+e', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Premult', 'nuke.createNode("Premult", inpanel=False)', '\\', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Keymix', 'nuke.createNode("Keymix", "channels rgba", inpanel=False)', 'alt+meta+k', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Merge/Unpremult', 'nuke.createNode("Unpremult", inpanel=False)', 'alt+\\', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Channel/ChannelMerge', 'nuke.createNode("ChannelMerge", "operation union", inpanel=False)', 'alt+meta+c', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Filter/Blur', "nuke.createNode('Blur')", 'b', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/ColorLookup', 'nuke.createNode("ColorLookup")', 'meta+alt+shift+c', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/Exposure', lambda: nuke.nodePaste(os.path.expanduser("~/.nuke/ToolSets/Color/Exposure.nk")), 'meta+e', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/Mult', lambda: nuke.nodePaste(os.path.expanduser("~/.nuke/ToolSets/Color/Mult.nk")), 'alt+meta+g', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Filter/BlurPercent', lambda: nuke.nodePaste(os.path.expanduser("~/.nuke/ToolSets/Filter/BlurPercent.nk")), 'alt+meta+b', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Channel/Shuffle_', 'nuke.createNode("Shuffle")', 'h', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Channel/ShuffleCopy_', 'nuke.createNode("ShuffleCopy", "label [value\ in]\ |\ [value\ in2]\ ->\ [value\ out]")', 'alt+meta+h', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/CCorrect', 'nuke.createNode("CCorrect", "channels rgb")', 'alt+meta+c', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/Fill', 'nuke.createNode("Fill")', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/ClampMin', 'nuke.createNode("Clamp", "name ClampMin maximum_enable 0")', index=5, shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/GradeAlpha', 'nuke.createNode("Grade", "name Grade channels a white_clamp 1 black_clamp 1")', 'alt+shift+g', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/HueCorrect', 'nuke.createNode("HueCorrect", "")', 'alt+shift+h', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Color/Math/Multiply', 'nuke.createNode("Multiply", "channels rgba")', 'alt+m', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Filter/FilterErode', 'nuke.createNode("FilterErode")', 'meta+shift+e', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Filter/Dilate', 'nuke.createNode("Dilate")', 'alt+shift+e', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Time/FrameHold', 'nuke.createNode("FrameHold", "first_frame {0}".format(nuke.frame()), inpanel=False)', 'meta+alt+shift+f', icon="FrameHold.png", shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Other/StickyNote', 'nuke.createNode("StickyNote", "tile_color 0x40454aff note_font_size 14 label <left>")', 'meta+n', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Other/Dot_', 'nuke.createNode("Dot")', 'alt+d', shortcutContext=2)
nuke.toolbar('Nodes').addCommand('Other/Label Dot', 'nuke.createNode("Dot", "hide_input 1 note_font_size 96 tile_color 0xff")', 'ctrl+meta+alt+shift+d', shortcutContext=2)
