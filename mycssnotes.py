""" CSS stands for CASCADING STYLE sheets """

# (refer to csszengarden.com for more information about css.)

# CSS Syntax

# CSS rules are made up of a selector and a declaration block { }.
# The selector is the HTML element(s) you want to style and the declaration
# block contains one or more declarations separated by semicolons (;).
# Each declaration includes a CSS property name and a value, separated by a colon (:).
# The declaration block is enclosed in curly braces.

# CSS Rule Example

# The following CSS rule selects all the <h1> elements and sets four properties:

# the background color of all the <h1> elements to dark blue
# the text color of the content of all the <h1> elements to white
# padding or space around the text content of 16 pixels
# the text is aligned to the center of the <h1> block
h1 {
background-color: darkblue;
color: white;
padding: 16px;
text-align: center;
}
# CSS Key Terms
# Selector — h1
# Declaration Block — { }
# Declaration — background-color: darkblue; (There are four total declarations in this
# .)
# Property — background-color
# Value — darkblue
# CSS Rule — the entire block of code

""" Numeric Values """
# In CSS, property length values are needed to provide layout and presentation control. 
# There are two main types - absolute and relative. The absolute length, like 10px (pixels), 
# is not relative to anything else and is typically the same size on most devices. 
# Relative lengths, like 90%, are dependent on other items including the parent, sibling, 
# or the size of the viewport.

""" Color Values """

# In addition to the numeric units used for sizes, CSS also allows you to specify colors 
# in various ways. CSS color values for text, backgrounds, and wherever applicable can 
# be coded by the following methods:

# keyword: antiquewhite, burlywood, yellow, lightyellow, etc.
# hexadecimal RGB (red, green, blue): #faebd7
# where the first two characters are the red value, the next two are the green value, 
# and the last two are the blue value in hexadecimal (base16) format (0 to F)
# RGB or RGBA: rgb(250, 235, 215) or rgb(250 235 215 / 1)
# where r is a red value ranging from 0 to 255, g is a green value ranging from 0 to 255, 
# b is a blue value ranging from 0 to 255, and the last value is the alpha value ranging 
# from 0 to 1 (0% to 100%)
# HSLA: hsla(34, 78%, 91%, 1)
# where h is the hue (0 to 360), s is the saturation (0% to 100%), l is the lightness 
# (0% to 100%), and a is the alpha value (0 to 1)

""" CSS Box Model """

# The CSS Box Model is a box that wraps around every element. From the inside out, the 
# model defines how the content, padding, border, and margin are rendered.

# Each box has a width and height.
# The default width is 100% (tres large), it can be reduced to the width of the content
# The default height just accommodates te content.
# The padding is the space around the content, inside the border.
# The padding between 20 to 40px seems to look good to me.
# Every box has a border, even it is not showing.
# The border separates the padding and the margin
p {
    border: 5px solid black
}

# Or it can be dotted black for example
# or dashed, doubled...
# we can round the corners using Border-radius.
# or make a circle for an img that was a square: border-radius: 50%;

# If you want spaces between boxes, you give them margin.
p {
    margin: 30px;
}

# When we give only one value to, it applies to the 4 cotes.
# When we give two values, for example margin: 15px 30px, the first applies to the
#     top and bottom, the second to the 2 sides.
# When we give three values, it will be top, right side and bottom.
# We can even give 4 different values. (Same for the padding)

# We can also specify: margin-top, padding-bottom left right etc...

# Because the box has a width, adding padding, border increases this width.
# if the width was 500px for example, we add padding 20px and border 10px,
# the total width will now be 560px.
# we can set this using box-sizing.
# box-sizing: border-box; !!!!! this one makes all the boxes have the same size.
# box-sizing: content-box

# content: This is where the text and images appear.
# padding: This is the area around the content and separates the content from the border.
# border: The border goes around the padding and separates the padding from the margin.
# margin: This is the area outside of the border and can extend beyond the physical 
# characters of the box model.

""" Common Border Shorthand """

# border: 1px solid rgb(0 0 0 / 10%);
# This applies a 1 pixel border around the element with a solid line and a color 
# that match the background of the containing/parent element. The color is set to 10% opacity.

""" HTML Block and Inline Elements """

# Every HTML element exists inside an invisible box, which is either block-level or inline.

# * Block-level elements take up the full available width by default, stretching from left to 
# right. They do not share a line with other elements and always start on a new line (e.g., h1, p).
# * Inline elements only take up as much width as their content needs and can sit side by side as 
# long as there is space (e.g., span, img).

# You can visually confirm this by adding borders: block elements occupy the full line, 
# while inline elements fit tightly around their content. For example, multiple images 
# can appear side by side if there is enough horizontal space.

# Changing Display Behavior

# CSS allows you to override default behaviors using the display property:

# * display: inline; turns a block element into an inline one.
# * display: block; turns an inline element into a block.
# * display: inline-block; combines the best of both: elements flow inline but still 
# respect width, height, and vertical margins.

# Inline-block is often the best choice for aligning items side by side while maintaining 
# layout control.

# Centering Elements

# Centering depends on the element’s display type:

# * text-align: center; centers the content inside a box (text or inline children).
# * margin: 0 auto; centers the box itself horizontally—but only if a width is set.

# If an element already takes up 100% width, margin: 0 auto; will have no visible effect.

# Centering Images

# Images are inline by default, so text-align: center; won’t center them unless:

# * The image is inside a block-level parent with text-align: center;, or
# * The image is changed to display: block;, given a width, and centered using margin: 0 auto;.

# Key takeaway: Understanding block, inline, and inline-block display types is essential 
# for controlling layout and centering elements effectively in CSS.


