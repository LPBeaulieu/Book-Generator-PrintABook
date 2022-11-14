import glob
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
import re
import sys


numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13',
'14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
'27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
'40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
'53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65',
'66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78',
'79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
'92', '93', '94', '95', '96', '97', '98', '99', '100']

numbers_dots = ['1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.',
'11.', '12.', '13.', '14.', '15.', '16.', '17.', '18.', '19.', '20.', '21.',
'22.', '23.', '24.', '25.', '26.', '27.', '28.', '29.', '30.', '31.', '32.',
'33.', '34.', '35.', '36.', '37.', '38.', '39.', '40.', '41.', '42.', '43.',
'44.', '45.', '46.', '47.', '48.', '49.', '50.', '51.', '52.', '53.', '54.',
'55.', '56.', '57.', '58.', '59.', '60.', '61.', '62.', '63.', '64.', '65.',
'66.', '67.', '68.', '69.', '70.', '71.', '72.', '73.', '74.', '75.', '76.',
'77.', '78.', '79.', '80.', '81.', '82.', '83.', '84.', '85.', '86.', '87.',
'88.', '89.', '90.', '91.', '92.', '93.', '94.', '95.', '96.', '97.', '98.',
'99.', '100.']

roman_numerals = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII',
'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV',
'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXIII', 'XXXIV', 'XXXV',
'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII', 'XLIV', 'XLV', 'XLVI',
'XLVII', 'XLVIII', 'XLIX', 'L', 'LI', 'LII', 'LIII', 'LIV', 'LV', 'LVI', 'LVII', 'LVIII',
'LIX', 'LX', 'LXI', 'LXII', 'LXIII', 'LXIV', 'LXV', 'LXVI', 'LXVII', 'LXVIII', 'LXIX',
'LXX', 'LXXI', 'LXXII', 'LXXIII', 'LXXIV', 'LXXV', 'LXXVI', 'LXXVII', 'LXXVIII', 'LXXIX',
'LXXX', 'LXXXI', 'LXXXII', 'LXXXIII', 'LXXXIV', 'LXXXV', 'LXXXVI', 'LXXXVII', 'LXXXVIII',
'LXXXIX', 'XC', 'XCI', 'XCII', 'XCIII', 'XCIV', 'XCV', 'XCVI', 'XCVII', 'XCVIII', 'XCIX', 'C']

roman_numerals_dots = ['I.', 'II.', 'III.', 'IV.', 'V.', 'VI.', 'VII.', 'VIII.', 'IX.', 'X.',
'XI.', 'XII.', 'XIII.', 'XIV.', 'XV.', 'XVI.', 'XVII.', 'XVIII.', 'XIX.', 'XX.', 'XXI.', 'XXII.',
'XXIII.', 'XXIV.', 'XXV.', 'XXVI.', 'XXVII.', 'XXVIII.', 'XXIX.', 'XXX.', 'XXXI.', 'XXXII.',
'XXXIII.', 'XXXIV.', 'XXXV.', 'XXXVI.', 'XXXVII.', 'XXXVIII.', 'XXXIX.', 'XL.', 'XLI.', 'XLII.',
'XLIII.', 'XLIV.', 'XLV.', 'XLVI.', 'XLVII.', 'XLVIII.', 'XLIX.', 'L.', 'LI.', 'LII.', 'LIII.',
'LIV.', 'LV.', 'LVI.', 'LVII.', 'LVIII.', 'LIX.', 'LX.', 'LXI.', 'LXII.', 'LXIII.', 'LXIV.',
'LXV.', 'LXVI.', 'LXVII.', 'LXVIII.', 'LXIX.', 'LXX.', 'LXXI.', 'LXXII.', 'LXXIII.', 'LXXIV.',
'LXXV.', 'LXXVI.', 'LXXVII.', 'LXXVIII.', 'LXXIX.', 'LXXX.', 'LXXXI.', 'LXXXII.', 'LXXXIII.',
'LXXXIV.', 'LXXXV.', 'LXXXVI.', 'LXXXVII.', 'LXXXVIII.', 'LXXXIX.', 'XC.', 'XCI.', 'XCII.',
'XCIII.', 'XCIV.', 'XCV.', 'XCVI.', 'XCVII.', 'XCVIII.', 'XCIX.', 'C.']

numbers_letters_lower = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two',
'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven',
'twenty-eight', 'twenty-nine', 'thirty', 'thirty-one', 'thirty-two', 'thirty-three',
'thirty-four', 'thirty-five', 'thirty-six', 'thirty-seven', 'thirty-eight', 'thirty-nine',
'forty', 'forty-one', 'forty-two', 'forty-three', 'forty-four', 'forty-five', 'forty-six',
'forty-seven', 'forty-eight', 'forty-nine', 'fifty', 'fifty-one', 'fifty-two', 'fifty-three',
'fifty-four', 'fifty-five', 'fifty-six', 'fifty-seven', 'fifty-eight', 'fifty-nine', 'sixty',
'sixty-one', 'sixty-two', 'sixty-three', 'sixty-four', 'sixty-five', 'sixty-six', 'sixty-seven',
'sixty-eight', 'sixty-nine', 'seventy', 'seventy-one', 'seventy-two', 'seventy-three',
'seventy-four', 'seventy-five', 'seventy-six', 'seventy-seven', 'seventy-eight', 'seventy-nine',
'eighty', 'eighty-one', 'eighty-two', 'eighty-three', 'eighty-four', 'eighty-five', 'eighty-six',
'eighty-seven', 'eighty-eight', 'eighty-nine', 'ninety', 'ninety-one', 'ninety-two', 'ninety-three',
'ninety-four', 'ninety-five', 'ninety-six', 'ninety-seven', 'ninety-eight', 'ninety-nine', 'hundred']

numbers_letters_lower_dots = ['one.', 'two.', 'three.', 'four.', 'five.', 'six.', 'seven.',
'eight.', 'nine.', 'ten.', 'eleven.', 'twelve.', 'thirteen.', 'fourteen.', 'fifteen.',
'sixteen.', 'seventeen.', 'eighteen.', 'nineteen.', 'twenty.', 'twenty-one.', 'twenty-two.',
'twenty-three.', 'twenty-four.', 'twenty-five.', 'twenty-six.', 'twenty-seven.', 'twenty-eight.',
'twenty-nine.', 'thirty.', 'thirty-one.', 'thirty-two.', 'thirty-three.', 'thirty-four.',
'thirty-five.', 'thirty-six.', 'thirty-seven.', 'thirty-eight.', 'thirty-nine.', 'forty.',
'forty-one.', 'forty-two.', 'forty-three.', 'forty-four.', 'forty-five.', 'forty-six.',
'forty-seven.', 'forty-eight.', 'forty-nine.', 'fifty.', 'fifty-one.', 'fifty-two.', 'fifty-three.',
'fifty-four.', 'fifty-five.', 'fifty-six.', 'fifty-seven.', 'fifty-eight.', 'fifty-nine.', 'sixty.',
'sixty-one.', 'sixty-two.', 'sixty-three.', 'sixty-four.', 'sixty-five.', 'sixty-six.', 'sixty-seven.',
'sixty-eight.', 'sixty-nine.', 'seventy.', 'seventy-one.', 'seventy-two.', 'seventy-three.',
'seventy-four.', 'seventy-five.', 'seventy-six.', 'seventy-seven.', 'seventy-eight.', 'seventy-nine.',
'eighty.', 'eighty-one.', 'eighty-two.', 'eighty-three.', 'eighty-four.', 'eighty-five.', 'eighty-six.',
'eighty-seven.', 'eighty-eight.', 'eighty-nine.', 'ninety.', 'ninety-one.', 'ninety-two.',
'ninety-three.', 'ninety-four.', 'ninety-five.', 'ninety-six.', 'ninety-seven.', 'ninety-eight.',
'ninety-nine.', 'hundred.']

cwd = os.getcwd()

#The "problem" variable is initialized to "False"
#and will be set to "True" should the code encounter
#any problems, in order to give the user relevant error
#messages along the  way.
problem = False

path_txt = os.path.join(cwd, "*.txt")
txt_files = glob.glob(path_txt)
if txt_files == []:
    print('\nPlease include a TXT file containing the book that you wish to print in the working folder.')
    problem = True
elif len(txt_files) > 1:
    print("\nPlease include only one TXT file containing the book that you wish to print in the working folder.")
else:
    txt_file_name = txt_files[0]

#The demonstration image entitled "Floral Pattern Background 843" was taken from the following source
#and is licenced for public domain use ("CC0 Public Domain"):
#https://www.publicdomainpictures.net/en/view-image.php?image=214080&picture=floral-pattern-background-843
#The user can select their own background image as well and the text box fill color on the cover page will
#be determined from the complementary color to one of the darkest pixels in the image. The text color on
#the cover page will be taken from the lightest pixel on the canvas.
path_jpeg = os.path.join(cwd, "*.jpg")
jpeg_files = glob.glob(path_jpeg)
if jpeg_files == []:
    print('\nPlease include a JPEG file containing the image that you ' +
    'wish to use as a background for the book cover in the working folder. Also, please ' +
    'make sure that the provided background image is in JPEG format, ' +
    "with a resolution of 300 ppi and a canvas size of US Legal dimensions in " +
    "landscape mode (width of 4200 pixels and height of 2550 pixels).")
    problem = True
elif len(jpeg_files) > 1:
    print("\nPlease include only one JPEG file containing the image that you " +
    "wish to use as a background for the book cover in the working folder.")
else:
    background_img = jpeg_files[0]

path_ttf = os.path.join(cwd, "*.ttf")
ttf_files = glob.glob(path_ttf)
if ttf_files == []:
    print("\nPlease include a True Type Font (.ttf) file containing " +
    "the font you wish to use on the cover page in the working folder.")
elif len(ttf_files) > 1:
    print("\nPlease include only one True Type Font (.ttf) file containing " +
    "the font you wish to use on the cover page in the working folder.")
else:
    cover_font = ttf_files[0]


title = None
author = None
#If the title needs to be split
#in order to fit in the title page,
#the value of "asjusted_title_rtf"
#will be set to the string containing
#a "\line" linebreak RTF command and
#will be updated in text[title_index].
#A similar approach is taken for the
#title and author name on the cover.
adjusted_title_rtf = None
adjusted_title_cover = None
adjusted_author_rtf = None
adjusted_author_cover = None
#Should the cover title need to be split,
#the default line spacing in-between title lines
#is initialized at 5 pixels, and may be altered
#by the user.
cover_title_line_spacing = 5
cover_author_line_spacing = 4
cover_box_color = None
cover_text_color = None
cover_trim_width = 0.25

number_of_pages = None
inches_per_ream_500_pages = None
cm_per_ream_500_pages = None

grayscale = False

#The font sizes are in points and
#not half-points. This means that
#a title size of r"fs\112" is really
#in size 56.
title_size = r"\fs112"
#The "cover_title_size" is initialized
#at 200 and the code will determine the largest
#font size that fits within the title page.
cover_title_size = 200
subtitle_size = None
#The spacing on the cover in-between
#the title and the author name will be
#a certain proportion of the cover title
#height and is set to 20% by default.
cover_spacing_title_height_ratio = 0.20
#The "max_author_title_font_ratio" variables
#determines the max ratio between the title
#headings font size and that of the author name,
#to provide a starting font size while automatically
#adjusting the font size to the available space.
max_author_title_font_ratio = 0.75
max_subtitle_title_font_ratio = 0.75
#The "cover_author_size" is initialized
#at 200 and the code will determine the largest
#font size that fits within the title page.
cover_author_size = 150
#The font size of the divider
#separating the title and the
#subtitle and author name.
divider_size = r"\fs72"
#To ensure that the spacing between
#Title, Subtitle and Author are the
#same, "title_page_spacing" is set as
#the font size before "\line" RTF commands.
title_page_spacing = r"\fs36"
body_font_size = r"\fs34"
header_font_size = r"\fs32"
chapter_heading_font_size = r"\fs51"
#The "max_longest_chapter_heading_body_font_ratio"
#variable determines the maximum ratio between the
#chapter headings font size and that of the body text,
#to provide a starting font size while automatically
#adjusting the font size to the available space.
max_longest_chapter_heading_body_font_ratio = 1.5
#By default, the chapter headings will not be in bold,
#but the user can pass in the argument "bold_chapter_headings"
#to make them bold.
bold_chapter_headings = False
#The default tab width of 360 twips
#corresponds to the width of four
#spaces written in size 14 Baskerville
#(r"\fs28") and may be adjusted.
tab_width = r"\deftab360"
font = "Baskerville"
#"title_page_posy" determines
#the starting vertical distance (in twips), from
#the top left of the page, where the title page
#paragraph starts.
title_page_posy = r"\posy4040"
#The top and bottom margins
#are set to 0, given that these are
#the lowest possible top and
#bottom margins when printing 2 pages
#on a sheet of letter paper, due to the
#different proportions of the resulting
#sheets (8.5x11" vs 5.5x8.5" for the
#individual pages).
header_top_margin = r"\headery0"
top_margin = r"\margt720"
bottom_margin = r"\margb0"
#The default values in twips for
#the left and right margins is of
#1600, which equates to about 0.75 inches.
#According to the following link
#https://kdp.amazon.com/en_US/help/topic/GVBQ3CMEQW3W2VL6
#these specifications would be suitable
#for books up to 700 pages in length,
#which should cover most books.
left_margin = r"\margl1600"
left_margin_twips = 1600
right_margin = r"\margr1600"
right_margin_twips = 1600

#The default left and right
#margins on the cover page are set to 0.75 inches
#from the edges of the half-letter page (5.5 inches wide).

#The left margin can be determined by subtracting the space
#in-between the margins (4.75 inches) from the right edge
#pixel count: (4200 - 4.75*4200/14) = 2775 px
left_margin_cover_textbox = 2775

#The space between the left edge of the textbox
#and the start of the text on the x axis is set to 100 pixels,
#so the text will start drawing at "left_margin_cover_textbox + 100" pixels
left_margin_cover_text = 2875
#The left margin can simply be calculated given the pixel
#width of the canvas: 4220-(0.75*4200/14) = 3995 px
right_margin_cover_textbox = 3995

#The space between the right edge of the textbox
#and the end of the text on the x axis is set to 100 pixels,
#so the text will start drawing at "right_margin_cover_textbox - 100" pixels
right_margin_cover_text = 3895

#The top margin of the text box on the cover page can
#be determined by adding a 25% of the vertical
#pixels to the starting y corrdinate of 0. (0+(2550/4)).
top_margin_cover_textbox = 640


#The bottom margin of the text box on the cover page
#can be determined by adding

#A line spacing of 276 twips (r"\sl276\slmult1")
#is equivalent to 1.15 line spacing. Here is
#a list of common line spacing, but anything
#in-between may be specified:
# 240 twips single spacing by default
# 360 twips (1.5 spacing)
# 480 twips (double spacing)
# 720 twips (triple spacing)
line_spacing = r"\sl276\slmult1 "
#The "points_between_paragraphs" variable equates
#to the number of twips after a paragraph and will
#be concatenated to the "\saN" RTF command to provide
#The spacing in-between paragraphs. It is set to zero
#by default, as novels typically do not have spacing
#in-between paragraphs, but may be modified by the user,
#where they input the distance in terms of number of points
#(as those used to measure font sizes).
points_between_paragraphs = "0"

#The number of carriage returns before
#the section headings (prologue, chapters,
#epilogue, etc.) is set to 5 and may be
#adjusted.
number_of_lines_above_chapter_headings = 6

if len(sys.argv) > 1:
    #The "try/except" statement will
    #intercept any "ValueErrors" and
    #ask the users to correctly enter
    #the desired values for the variables
    #directly after the colon separating
    #the variable name from the value.
    try:
        for i in range(1, len(sys.argv)):
            if len(sys.argv[i]) > 1 and sys.argv[i][:6] == "title:":
                title = sys.argv[i][6:].strip()
            elif len(sys.argv[i]) > 1 and sys.argv[i][:7] == "author:":
                if len(sys.argv[i][7:]) > 3 and sys.argv[i][7:10].lower() == "by ":
                    author = sys.argv[i][10:]
                    author_names = author.split(" ")
                    for i in range(len(author_names)):
                        if author_names[i].lower() != "by":
                            author_names[i] == author_names[i].capitalize()
                    #"by" will not be included in the "author" variable, so
                    #index 0 in "author_names" is skipped over.
                    author = " ".join(author_names[1:]).strip()
                elif len(sys.argv[i][7:]) > 3 and sys.argv[i][7:10] != "by ":
                    author = sys.argv[i][7:].strip()
                    author_names = author.split(" ")
                    for i in range(len(author_names)):
                        author_names[i] == author_names[i].capitalize()
                    author = " ".join(author_names).strip()
                else:
                    author = sys.argv[i][7:].strip()
            #The font sizes are automatically multiplied by two, so that
            #should a user enter "10.5" points, it would be registered as
            #21 half-points by the code. The "round" method rounds the
            #half-point value should it not be an integer.
            elif sys.argv[i].lower()[:11] == "title_size:":
                title_size = r"\fs" + str(round(float(sys.argv[i][11:].strip())*2))
            elif sys.argv[i].lower()[:14] == "subtitle_size:":
                subtitle_size = r"\fs" + str(round(float(sys.argv[i][14:].strip())*2))
            elif sys.argv[i].lower()[:13] == "divider_size:":
                divider_size = r"\fs" + str(round(float(sys.argv[i][13:].strip())*2))
            elif sys.argv[i].lower()[:19] == "title_page_spacing:":
                title_page_spacing = r"\fs" + str(round(float(sys.argv[i][19:].strip())*2))
            elif sys.argv[i].lower()[:28] == "max_title_author_font_ratio:":
                 max_title_author_font_ratio = float(sys.argv[i].lower()[28:].strip())
            elif sys.argv[i].lower()[:28] == "max_author_title_font_ratio:":
                max_author_title_font_ratio = float(sys.argv[i][28:].strip())
            elif sys.argv[i].lower()[:30] == "max_subtitle_title_font_ratio:":
                max_subtitle_title_font_ratio = float(sys.argv[i][30:].strip())
            elif sys.argv[i].lower()[:28] == "max_chapter_body_font_ratio:":
                 max_longest_chapter_heading_body_font_ratio = float(sys.argv[i].lower()[28:].strip())
            elif sys.argv[i].lower()[:21] == "bold_chapter_headings":
                bold_chapter_headings = True
            elif sys.argv[i].lower()[:15] == "body_font_size:":
                body_font_size = r"\fs" + str(round(float(sys.argv[i][15:].strip())*2))
            elif sys.argv[i].lower()[:17] == "header_font_size:":
                header_font_size = r"\fs" + str(round(float(sys.argv[i][17:].strip())*2))
            elif sys.argv[i].lower()[:26] == "chapter_heading_font_size:":
                chapter_heading_font_size = r"\fs" + str(round(float(sys.argv[i][26:].strip())*2))
            #The margins are entered by the user in inches, which
            #are converted into twips (1/1440th of an inch)
            elif sys.argv[i].lower()[:10] == "tab_width:":
                inches = float(sys.argv[i][10:].strip())
                twips = round(inches*1440)
                tab_width = r"\deftab" + str(twips)
            elif sys.argv[i].lower()[:13] == "tab_width_cm:":
                cm = float(sys.argv[i][13:].strip())
                twips = round(cm/2.54*1440)
                tab_width = r"\deftab" + str(twips)
            elif sys.argv[i].lower()[:5] == "font:":
                font = sys.argv[i][5:]
            elif sys.argv[i].lower()[:22] == "title_page_top_margin:":
                inches = float(sys.argv[i][22:].strip())
                twips = round(inches*1440)
                title_page_posy = r"\title_page_posy" + str(twips)
            elif sys.argv[i].lower()[:25] == "title_page_top_margin_cm:":
                cm = float(sys.argv[i][25:].strip())
                twips = round(cm/2.54*1440)
                title_page_posy = r"\title_page_posy" + str(twips)
            elif sys.argv[i].lower()[:12] == "left_margin:":
                inches = float(sys.argv[i][12:].strip())
                left_margin_twips = round(inches*1440)
                left_margin = r"\margl" + str(left_margin_twips)
            elif sys.argv[i].lower()[:15] == "left_margin_cm:":
                cm = float(sys.argv[i][15:].strip())
                left_margin_twips = round(cm/2.54*1440)
                left_margin = r"\margl" + str(left_margin_twips)
            elif sys.argv[i].lower()[:13] == "right_margin:":
                inches = float(sys.argv[i][13:].strip())
                right_margin_twips = round(inches*1440)
                right_margin = r"\margr" + str(right_margin_twips)
            elif sys.argv[i].lower()[:16] == "right_margin_cm:":
                cm = float(sys.argv[i][16:].strip())
                right_margin_twips = round(cm/2.54*1440)
                right_margin = r"\margr" + str(right_margin_twips)
            elif sys.argv[i].lower()[:11] == "top_margin:":
                inches = float(sys.argv[i][11:].strip())
                twips = round(inches*1440)
                top_margin = r"\margt" + str(twips)
            elif sys.argv[i].lower()[:14] == "top_margin_cm:":
                cm = float(sys.argv[i][14:].strip())
                twips = round(cm/2.54*1440)
                top_margin = r"\margt" + str(twips)
            elif sys.argv[i].lower()[:14] == "bottom_margin:":
                inches = float(sys.argv[i][14:].strip())
                twips = round(inches*1440)
                bottom_margin = r"\margb" + str(twips)
            elif sys.argv[i].lower()[:17] == "bottom_margin_cm:":
                cm = float(sys.argv[i][17:].strip())
                twips = round(cm/2.54*1440)
                bottom_margin = r"\margb" + str(twips)
            elif sys.argv[i].lower()[:18] == "header_top_margin:":
                inches = float(sys.argv[i][18:].strip())
                twips = round(inches*1440)
                header_top_margin = r"\headery" + str(twips)
            elif sys.argv[i].lower()[:21] == "header_top_margin_cm:":
                cm = float(sys.argv[i][21:].strip())
                twips = round(cm/2.54*1440)
                header_top_margin = r"\headery" + str(twips)
            elif sys.argv[i].lower()[:13] == "line_spacing:":
                lines = float(sys.argv[i][13:].strip())
                twips = round(lines*240)
                line_spacing = r"\sl" + str(twips) + "\slmult1 "
            elif sys.argv[i].lower()[:26] == "points_between_paragraphs:":
                points = float(sys.argv[i][26:].strip())
                points_between_paragraphs = str(round(points*1440/72))
            elif sys.argv[i].lower()[:39] == "number_of_lines_above_chapter_headings:":
                number_of_lines_above_chapter_headings = int(sys.argv[i][39:].strip())
            elif sys.argv[i].lower()[:16] == "number_of_pages:":
                number_of_pages = int(sys.argv[i].lower()[16:].strip())
            elif sys.argv[i].lower()[:26] == "inches_per_ream_500_pages:":
                make_cover = True
                inches_per_ream_500_pages = float(sys.argv[i][26:].strip())
            elif sys.argv[i].lower()[:22] == "cm_per_ream_500_pages:":
                make_cover = True
                cm_per_ream_500_pages = float(sys.argv[i][22:].strip())
                inches_per_ream_500_pages = cm_per_ream_500_pages/2.54
            elif sys.argv[i].strip().lower() == "grayscale" or sys.argv[i].strip().lower() == "greyscale":
                grayscale = True
            elif sys.argv[i].lower()[:16] == "cover_box_color:":
                cover_box_color = sys.argv[i].lower()[16:].strip()
            elif sys.argv[i].lower()[:17] == "cover_text_color:":
                cover_text_color =  sys.argv[i].lower()[17:].strip()
            elif sys.argv[i].lower()[:33] == "cover_spacing_title_height_ratio:":
                cover_spacing_title_height_ratio = float(sys.argv[i][33:].strip())
            elif sys.argv[i].strip().lower()[:17] == "cover_trim_width:":
                cover_trim_width = float(sys.argv[i][17:].strip())
            elif sys.argv[i].strip().lower()[:20] == "cover_trim_width_cm:":
                cover_trim_width = float(sys.argv[i][20:].strip())/2.54

    except:
        problem = True
        print("\nPlease enter the name of the parameter you wish to alter, followed " +
        "by a colon, and the desired setting directly after the colon. For example, " +
        'to set the title, you would enter: "title:Your Title Here" as an additional argument.')

#The code below only runs if the user has at least
#provided a title, author and valid file name.
if (problem == False and title != None and author != None and txt_file_name != None and
txt_file_name[-4:].lower() == ".txt"):

    #The space between the top margin of the textbox
    #and where the top edge of the text on the y axis
    #is set to 50 pixels: "top_margin_cover_textbox+100"
    vertical_margin_cover_text = top_margin_cover_textbox + 100

    #According to the following source,
    #https://www.pacificu.edu/sites/default/files/documents/Individualcharacterlegibility.pdf
    #the average width to height ratio of six different serif fonts
    #(Rockwell, Georgia, Garamond, Centaur, Bodoni and Baskerville) is of 1.10
    #To allow for a certain margin of error, a width to height ratio of 1.1
    #will be used in this code.

    #The title font size in points is determined by dividing the
    #floating number extracted from "title_size" (in half_points)
    #by two.
    title_size_float = float(title_size.strip()[3:])/2
    #The character height in twips is determined by using the conversion
    #factor of 1440 twips for every 72 points.
    title_character_height_twips = round(title_size_float*1440/72)
    #The character width in twips is calculated by multiplying
    #the "title_character_height_twips" by the average width to height
    #ratio for serif fonts of "1.1" mentioned above.
    title_character_width_twips = round(1.1*title_character_height_twips)

    #The total width of the title (in twips) is determined by multiplying
    #the number of characters by the individual character width.
    title_width_twips = len(title)*title_character_width_twips

    #If the title width in twips ("title_width_twips") is greater than the
    #total width of the page in twips (5.5 inches times 1440 twips per inch)
    #minus the sum of the left and right margins in twips, then the title is
    #split and will span over two lines.

    #A correction factor is applied to the page width, as conversion of font
    #width in points into twips results in much too large character dimensions
    #relative to the space available on the width of the page. The "correction_factor"
    #should work similarly with other fonts, assuming that their width to height ratio
    #is in line with the average value of 1.1 mentioned above.
    correction_factor = 4.0

    width_threshold =  int((5.5*1440 - (left_margin_twips + right_margin_twips)) * correction_factor)

    if title_width_twips > width_threshold:
        #If the title width in twips is too high to fit
        #on one line, then the title string is split into
        #individual words, which are assessed for length
        #in the while loop below. The "title_size" is
        #decremented until both fragments of the title
        #can fit onto their own line or a font size of
        #27 is reached.
        title_words = title.split()
        number_of_title_words = len(title_words)
        #The middle index in the title will be the threshold
        #for including a carriage return in the title.
        middle_index_in_title = len(title)//2
        #For every word in the title, a check will be made
        #to see whether it could fit on the first line (along
        #with the space after it, hence the "+1" below) and
        #still be within the "middle_index_in_title" threshold.
        #if so, the word will be added to the line and
        #"character_count" will be incremented accordingly.
        character_count = 0
        word_delimitor = None
        for i in range(len(title_words)):
            if character_count <= middle_index_in_title - (len(title_words[i])+1):
                character_count += len(title_words[i])
            #If there isn't room on the current line for
            #the word and its following space, then it will
            #be the forst word on the next line and the
            #index of that word in "title_words" will be
            #the point where the carriage return "\line" will be added.
            else:
                word_delimitor = i
                break
        first_half_words = title_words[:word_delimitor]
        first_half_words_string = " ".join(first_half_words)
        second_half_words = title_words[word_delimitor:]
        second_half_words_string = " ".join(second_half_words)

        adjusted_title_rtf = first_half_words_string + "\line " + second_half_words_string
        title_width_set = False
        while title_width_set == False and title_size_float > 27:
            title_character_height_twips = round(title_size_float*1440/72)
            title_character_width_twips = round(1.1*title_character_height_twips)
            title_width_twips = len(title)*title_character_width_twips

            first_half_words_width = 0
            for word in first_half_words:
                #The width of every word (with a space, hence the +1) is determined
                #in twips and added to "first_half_words_width".
                first_half_words_width += (len(word)+1)*title_character_width_twips

            second_half_words_width = 0
            for word in second_half_words:
                #The width of every word (with a space, hence the +1) is determined
                #in twips and added to "first_half_words_width".
                second_half_words_width += (len(word)+1)*title_character_width_twips

            #If the two halves of the title are still too wide to fit into their
            #own lines, the "title_size" is decremented until both fragments of
            #the title can fit onto their own line or a font size of 27 is reached.
            if first_half_words_width > width_threshold or second_half_words_width > width_threshold:
                title_size_float -= 0.5
            else:
                title_size = r"\fs" + str(round(2*title_size_float))
                title_width_set = True

        #If "author_size_float" is 27, then the "while" loop was broken
        #before anything else could take place. The "if" statement below
        #then updates the value of "author_size_float".
        if title_size_float == 27:
            title_size = r"\fs54"


    #A similar automatic font scaling is applied to the
    #author name string "author".
    author_size_float = title_size_float * max_author_title_font_ratio
    author_size = r"\fs" + str(round(2*author_size_float))
    author_character_height_twips = round(author_size_float*1440/72)
    author_character_width_twips = round(1.1*author_character_height_twips)
    author_width_twips = len(author)*author_character_width_twips

    correction_factor = 4.0

    width_threshold =  int((5.5*1440 - (left_margin_twips + right_margin_twips)) * correction_factor)

    if author_width_twips > width_threshold:
        author_words = author.split()
        number_of_author_words = len(author_words)
        middle_index_in_author = len(author)//2
        character_count = 0
        word_delimitor = None
        for i in range(len(author_words)):
            if character_count <= middle_index_in_author - (len(author_words[i])+1):
                character_count += len(author_words[i])
            else:
                word_delimitor = i
                break
        first_half_words = author_words[:word_delimitor]
        first_half_words_string = " ".join(first_half_words)
        second_half_words = author_words[word_delimitor:]
        second_half_words_string = " ".join(second_half_words)
        adjusted_author_rtf = first_half_words_string + "\line " + second_half_words_string

        author_width_set = False
        while author_width_set == False and author_size_float > 27:
            author_character_height_twips = round(author_size_float*1440/72)
            author_character_width_twips = round(1.1*author_character_height_twips)
            author_width_twips = len(author)*author_character_width_twips

            first_half_words_width = 0
            for word in first_half_words:
                first_half_words_width += (len(word)+1)*author_character_width_twips

            second_half_words_width = 0
            for word in second_half_words:
                second_half_words_width += (len(word)+1)*author_character_width_twips

            #As the author name font size should be at most 75% of that of the title,
            #"author_size_float" is scaled down to 75% of "title_size_float" if it is
            #equal or above 75% of "title_size_float".
            if first_half_words_width > width_threshold or second_half_words_width > width_threshold:
                author_size_float -= 0.5
            elif author_size_float > title_size_float*0.75:
                author_size_float = title_size_float*0.75
                author_size = r"\fs" + str(round(2*author_size_float))
                author_width_set = True
            else:
                author_size = r"\fs" + str(round(2*author_size_float))
                author_width_set = True

        #If "author_size_float" is 27, then the "while" loop was broken
        #before anything else could take place. The "if" statement below
        #then updates the value of "author_size_float".
        if author_size_float == 27:
            author_size = r"\fs54"

    with open(txt_file_name, "r", encoding="utf-8") as f:
        text = f.readlines()
    #First, any occurences of more than one successive space are
    #changed to a single space. This needs to be done before introducing
    #RTF commands, which are followed by an optional space, the removal
    #of which would result in merged words.
    #Then, backslashes and curly brackets (if present in the TXT file)
    #are changed to their corresponding RTF escapes, so as to avoid
    #any issues when parsing the RTF code.
    for i in range(len(text)):
        #Instances of three or more successive spaces would typically
        #designate tabs and will be removed. Afterwards, any instances
        #of two or more successive space will be changed for a signe space,
        #as there could have been a typo with an additional space.
        text[i] = (re.sub('[" "]{3,}', "", text[i]).replace("  ", " ")
        .replace("[Illustration]", "").replace('\\', r"\'5c")
        .replace('{', "\\'7b").replace('}', "\\'7d"))

    #The "title_index" variable (defaulted to None), will serve as line
    #reference to locate the "contents" section (if present)
    #and remove it from the manuscript, as the page numbers would not be
    #accurate anymore, given the change in line length, line spacing,
    #font size and margins.
    title_index = None

    contents_index_start = None
    contents_index_end = None

    first_line_index = 0
    last_line_index = len(text)-1

    for i in range(len(text)):
        if title_index == None and text[i].lower().strip() == title.lower():
            title_index = i
        elif (contents_index_start == None and title_index != None and
        i < title_index + 15 and (text[i].lower().strip() == "contents" or
        text[i].lower().strip() == "content" or text[i].lower().strip() == "table of contents" or
        text[i].lower().strip() == "toc")):
            #The index at which the table of contents starts (the header)
            #is stored within "contents_index_start" to allow for slicing
            #it out of the "text" list later on in the code.
            contents_index_start = i
            #The code below will locate the line index at which the table of
            #contents ends, insofar as there is at most one space in-between
            #the elements of the table of contents. However, there can be any
            #number of empty lines between the "Contents" header and the first
            #element of the table of contents.
            contents_text = None
            contents_text_before = None
            first_line_empty = None
            no_empty_lines_contents = None
            contents_index_end = None
            #The "index_modifier" is set to one in case there are
            #no spaces between the "Contents" header and the first
            #element of the table of contents, in which case the
            #first element is found at text[i+1].
            index_modifier = 1
            for j in range(1,len(text)-i):
                #If the line following the "Contents" header is an empty line,
                #the line index at which the first element is found will be
                #stored in "index_modifier", and will be found at the
                #"text[i+index_modifier]" index.
                if text[i+1].strip(" ") == "\n" and text[i+j].strip(" ") != "\n":
                    index_modifier = j
                    break
            #The following "for" loop will cycle through the lines of the
            #"text" list and determine the line index "contents_index_end",
            #where the table of contents ends
            for j in range(index_modifier+1,len(text)-(i+index_modifier+1)):
                if contents_index_end != None:
                    break
                #If the line right after the first element of the table
                #of contents is not an empty line, then "no_empty_lines_contents",
                #is set to True.
                elif j == index_modifier + 1 and text[i+j].strip(" ") != "\n":
                    no_empty_lines_contents = True
                #If the line right after the first element of the table
                #of contents is an empty line, then "no_empty_lines_contents",
                #is set to False.
                elif j == index_modifier + 1 and text[i+j].strip(" ") == "\n":
                    no_empty_lines_contents = False
                #If "no_empty_lines_contents" is "True", meaning that there are
                #no empty lines in-between the elements of the table of contents,
                #then "contents_index_end" is set as the index of the first empty
                #line.
                elif j > index_modifier + 1 and no_empty_lines_contents == True:
                    if text[i+j].strip(" ") == "\n":
                        contents_index_end = i+j
                        break
                #If "no_empty_lines_contents" is "False", then one cannot assume
                #that the table of contents ends upon reaching the  next empty
                #line. Instead, "contents_index_end" is set as the index of the
                #first sequence of two empty lines or non-empty lines, as these
                #should normally alternate within a table of contents with alternating
                #elements and empty lines.
                elif j > index_modifier + 1 and no_empty_lines_contents == False:
                    if text[i+j].strip(" ") != "\n" and text[i+j+1].strip(" ") != "\n":
                        contents_index_end = i+j
                        break
                    elif text[i+j].strip(" ") == "\n" and text[i+j+1].strip(" ") == "\n":
                        contents_index_end = i+j
                        break
            #If "contents_text_end" is still not set, it means that the table of contents
            #either doesn't have a "Contents" heading, or the line spacing is irregular
            #(more than one empty line in-between elements) and the user should remove
            #it by hand. The variable "Problem" is set to "True", which will prevent
            #the code after this "for" loop to proceed.
            if contents_index_end == None:
                print("\nPlease manually remove the table of contents from the TXT file, " +
                "save the file and run the code again.")
                problem = True
                break

        #The line indices at which the opening and closing tags of the manuscript are located
        #within the "text" list are stored in "first_line_index" and "last_line_index" and
        #will enable to slice out the Project Gutenberg information and license.
        elif text[i].strip(" ") != "\n" and text[i][:40] == "*** START OF THE PROJECT GUTENBERG EBOOK":
            #If there are "***" in the line (after the opening stars),
            #then the "first_line_index" is set to the next line ("i+1").
            if text[i][3:].find("***") != -1:
                first_line_index = i+1
            #Otherwise, the next lines are screened for the presence of
            #the closing stars and the first line encountered that
            #contains "***" will be used to determine the index of
            #"first_line_index" ("j+1")
            else:
                for j in range(i+1, len(text)-1):
                    if "***" in text[j]:
                        first_line_index = j+1
                        break
        elif text[i].strip(" ") != "\n" and text[i][:38] == "*** END OF THE PROJECT GUTENBERG EBOOK":
            last_line_index = i-1

    if problem == False and contents_index_start != None and contents_index_end != None:
        #The list of lines is sliced to remove both the "Project Gutenberg"
        #information and the table of contents (if present), as the page
        #numbers wouldn't line up with the original table of contents and
        #table of contents aren't strictly required for novels at least.
        text = text[first_line_index:contents_index_start] + text[contents_index_end:last_line_index+1]

    elif problem == False:
        #The list of lines text is sliced to exclude the "Project Gutenberg"
        #information. This needs to be done after dealing with the tabs, as
        #the indices "contents_index", "author_index" and "title_index" are
        #used in that code and map to the unabridged list of lines.
        text = text[first_line_index:last_line_index+1]

    if problem == False:
        title_index = None
        author_index = None
        line_skipping_first_word = None
        #The variable "page_break_ok" is initialized to "True" and
        #allows for inclusion of a page break and carriage returns before
        #the chapter headings. After writing the heading, the variable
        #will be set to "False" and only set to "True" again once a
        #regular line of text will be encountered.
        page_break_ok = True
        chapter_indices = []
        slash_n_line_indices = []
        for i in range(len(text)):
            #In case the author name is preceded by "by" (or an equivalent in another language),
            #the first word of the line is skipped over and stored in "line_skipping_first_word",
            #for comparison with "author" in the first "elif" statement.
            line_words = text[i].split()
            if len(line_words) > 1:
                line_skipping_first_word = (" ".join(line_words[1:]).lower().strip())

            #The title page is assembled if the "text" list element at index "i"
            #corresponds to the title of the work.
            if title_index == None and text[i].lower().strip() == title.lower():
                title_index = i
                title_string = text[i].lower().strip()
                #If the title needs to be split
                #in order to fit in the title page,
                #the value of "asjusted_title_rtf"
                #will be set to the string containing
                #a "\line" linebreak RTF command and
                #will be updated in text[title_index].
                if adjusted_title_rtf != None:
                    text[i] = (title_size + adjusted_title_rtf + r"\par}{\pard\pvmrg\phmrg\posxc" +
                    title_page_spacing + title_page_posy + "\qc\line" + divider_size + 3*r"\'87" +
                     r"\par}{\pard\hyphpar0\pvmrg\phmrg\posxc" + title_page_spacing + title_page_posy + "\qc\line")
                #Otherwise, the RTF formatting is added to the line.
                else:
                    text[i] = (title_size + text[i].strip(" ") + r"\par}{\pard\pvmrg\phmrg\posxc" +
                    title_page_spacing + title_page_posy + "\qc\line" + divider_size + 3*r"\'87" +
                     r"\par}{\pard\hyphpar0\pvmrg\phmrg\posxc" + title_page_spacing + title_page_posy + "\qc\line")
            #If the element at index "i" of the "text" list corresponds to the author name
            #(either or not while skipping over the first word such as "by") and is located
            #within 5 elements of the title, it is added to the title page.
            elif (author_index == None and title_index != None and (text[i].lower().strip() == author.lower() or
            line_skipping_first_word == author.lower()) and i < title_index + 5):
                author_index = i
                text[i] = author_size + author + r"\par}{\pard \qj\line"
                #If there are lines between the title and author name,
                #the subtitle formatting is applied to those lines.
                if author_index - title_index > 1:
                    #If the user hasn't provided a font size for the subtitle,
                    #it is set as 60% of "title_size_float", multiplied by
                    #two to give points instead of half points, hence it being
                    #equal to "1.2*title_size_float".
                    if subtitle_size == None:
                        subtitle_size = r"\fs" + str(round(1.2*title_size_float))

                    #As there could be empty lines ("\n") in-between
                    #The title and the line where the subtitle begins,
                    #the index where the subtitle starts is stored
                    #in "line_index_subtitle_start" by skipping over
                    #empty lines.
                    line_index_subtitle_start = None
                    for j in range(title_index + 1, author_index):
                        if text[j].strip(" ") != "\n":
                            line_index_subtitle_start = j
                            break
                    #If the line following "line_index_subtitle_start" isn't
                    #empty ("\n"), all of the lines of following it, down to the
                    #"author_index" will be appended to the stripped version
                    #of the first line of the subtitle text[title_index+1],
                    #so that there will not be random carriage returns within
                    #the subtitle. All of the subsequent lines after text[title_index+1],
                    #down to the next carriage return will be changed for "\n",
                    #and extraneous "\n" will be removed later in the code.
                    if (line_index_subtitle_start != None and
                    text[line_index_subtitle_start+1].strip(" ") != "\n"):
                        complete_subtitle = text[line_index_subtitle_start].strip() + " "
                        for k in range(line_index_subtitle_start, author_index):
                            if text[k].strip(" ") == "\n":
                                break
                            else:
                                complete_subtitle += text[k].strip() + " "
                                text[k] = "\n"
                        #As a space is added after every line up to the
                        #end of "next_carriage_return", the final space
                        #needs to be removed using the strip() method.
                        text[line_index_subtitle_start] = (subtitle_size + r"\hyphpar0 " +
                        complete_subtitle.strip() + r"\par}{\pard\pvmrg\phmrg\posxc" +
                        title_page_spacing + title_page_posy + r"\qc\line")
                    #If the subtitle only spans one line, then it is
                    #formatted using the subtitle settings.
                    elif line_index_subtitle_start != None:
                        text[line_index_subtitle_start] = (subtitle_size + r"\hyphpar0 " +
                        text[line_index_subtitle_start].strip() + r"\par}{\pard\pvmrg\phmrg\posxc" +
                        title_page_spacing + title_page_posy + r"\qc\line")

            #If the line contains either a number in written form,  a digit or roman
            #numeral, followed by a period or not, or if it is comprised of "chapter"
            #(irrespective of case), followed by a character (presumably a space)
            #and then a number in written form, a digit or roman numeral, folllowed
            #by a period or not, and if the line index is zero or the previous line
            #is empty, then the chapter heading is further investigated below.
            #Examples: Chapter 1. / CHAPTER II / 1 / II. / Chapter One. / Three
            if ((text[i].strip() in numbers or text[i].strip() in numbers_dots or
            text[i].strip() in roman_numerals or text[i].strip() in roman_numerals_dots or
            text[i].strip().lower() in numbers_letters_lower or
            (text[i].strip()[:7].lower() == "chapter" and (text[i].strip()[8:] in numbers or
            text[i].strip()[8:] in numbers_dots or text[i].strip()[8:] in roman_numerals or
            text[i].strip()[8:] in roman_numerals_dots or text[i].strip()[8:].lower() in numbers_letters_lower or
            text[i].strip()[8:].lower() in numbers_letters_lower_dots))) and (i == 0 or i > 0 and
            text[i-1].strip(" ") == "\n")):
                #If the line after the chapter heading isn't empty, it means
                #that a subheading follows the chapter heading. All of the
                #lines of following the chapter heading (ex: Chapter I.), down
                #to the next carriage return "\n" will be appended to the
                #stripped version of line text[i+1], so that there will not
                #be random carriage returns within the subheading. All of the
                #subsequent lines after text[i+1], down to the next carriage
                #return will be changed to "\n", and extraneous "\n" will
                #be removed later in the code.
                if i < len(text)-1 and text[i+1].strip(" ") != "\n":
                    complete_subheading = text[i+1].strip() + " "
                    loop_done = False
                    #The lines after index "i+1" are appended to line "i+1",
                    #down to "len(text)-3", as the "elif" statement needs to
                    #start screening three lines ahead.
                    for j in range(i+2, len(text)-3):
                        if loop_done == True:
                            break
                        #If the line is empty "\n", then the lines after it
                        #are screened to determine where a non-empty
                        #line is encountered next (!= "\n"). Upon reaching
                        #that non-empty line, the variable "loop_done" is
                        #set to "True" and the nested "for" loops are broken.
                        elif text[j].strip(" ") == "\n":
                            for k in range(i+3, len(text)-3):
                                if text[k].strip(" ") != "\n":
                                    loop_done = True
                                    break
                                #If the line is empty "\n", then its index
                                #is appended to the list "slash_n_line_indices".
                                #This will remove all the empty lines in-between
                                #the heading and the next line of body text.
                                else:
                                    if k not in slash_n_line_indices:
                                        slash_n_line_indices.append(k)
                        #If the line at index "j" isn't empty (!= "\n"),
                        #then it will be appended to the first line of the
                        #subtitle at index "i+1". The indices of the non-empty
                        #lines after "i+2" will be appended to the list
                        #"slash_n_line_indices" and removed later in the code.
                        #The line at index "i+2" will be overwritten with two
                        #empty paragraph RTF commands to have two carriage
                        #returns after every heading (text[i+2] = (r"\par}{\pard\sa" +
                        #points_between_paragraphs + line_spacing + r"\qj" +
                        #r"\par}{\pard\sa" + points_between_paragraphs +
                        #line_spacing + r"\qj ")).
                        else:
                            complete_subheading += text[j].strip() + " "
                            text[j] = "\n"
                            if j not in slash_n_line_indices and j > i+2:
                                slash_n_line_indices.append(j)
                    #As a space is added after every line down to the
                    #end of "next_carriage_return", the final space
                    #needs to be removed and a carriage return needs
                    #to be placed at the end of the line "\n" so that
                    #the automatic removal of extraneous "\n" proceeds
                    #as usual later in the code.
                    text[i+1] = complete_subheading.strip() + "\n"

                    if bold_chapter_headings:
                        #As there could be a subsection under chapter heading (for example,
                        #'Chapter One "\n" I. "\n" Body text'), then the page break and
                        #carriage returns should only be added before a chapter heading
                        #if at least one line of regular text was encountered ("page_break_ok == True").
                        if page_break_ok == True:
                            text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing +  r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                            chapter_heading_font_size + r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}")
                            text[i+1] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing + r"\qc"  + chapter_heading_font_size + r"\b " +
                            text[i+1].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                            r" " + line_spacing + r"\qj")
                            text[i+2] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                            r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                            #"page_break_ok" is set to "False" and will be reset to "True" once
                            #a regular line of text will be reached in the final "else" statement
                            #of this "for" loop.
                            page_break_ok = False
                        else:
                            text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing + r"\qc" + chapter_heading_font_size + r"\b " +
                            text[i].strip(" ")[:-1] + r"\b0\par}")
                            text[i+1] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing + r"\qc"  + chapter_heading_font_size + r"\b " +
                            text[i+1].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                            r" " + line_spacing + r"\qj")
                            text[i+2] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                            r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                            page_break_ok = False
                    else:
                        #As there could be a subsection under chapter heading (for example,
                        #'Chapter One "\n" I. "\n" Body text'), then the page break and
                        #carriage returns should only be added before a chapter heading
                        #if at least one line of regular text was encountered ("page_break_ok == True").
                        if page_break_ok == True:
                            text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing +  r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                            chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}")
                            text[i+1] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing + r"\qc"  + chapter_heading_font_size + text[i+1].strip(" ")[:-1] +
                            r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                            text[i+2] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                            r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                            #"page_break_ok" is set to "False" and will be reset to "True" once
                            #a regular line of text will be reached in the final "else" statement
                            #of this "for" loop.
                            page_break_ok = False
                        else:
                            text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                            line_spacing + r"\qc" + chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}")
                            text[i+1] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                            r"\qc"  + chapter_heading_font_size + text[i+1].strip(" ")[:-1] + r"\par}{\pard\sa" +
                            points_between_paragraphs + line_spacing + r"\qj")
                            text[i+2] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                            r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                            page_break_ok = False

                #If there is an empty line in-between the chapter heading
                #(ex:Chapter I.) and the subheading, it is removed in the
                #RTF document using a similar approach to the code in the
                #"if" statement.
                elif i < len(text)-3 and text[i+1].strip(" ") == "\n":
                    #The "for" loop below reviews the lines after
                    #the first line of the subheading at index "text[i+2]",
                    #and breaks upon reaching the first non-empty line
                    #after the end of the subheading. If there were two
                    #or more empty lines after the subheading, it can be
                    #concluded that it cannot consist of body text and
                    #must then be a subheading. The "if" statement below
                    #can then proceed. Otherwise, the "else" statement
                    #runs in case the subheading only spans one line (ex: I.).
                    loop_done = False
                    empty_lines_after_heading = 0
                    for j in range(i+3, len(text)-3):
                        if empty_lines_after_heading > 0 and text[j].strip(" ") != "\n":
                            break
                        elif text[j].strip(" ") == "\n":
                            empty_lines_after_heading += 1

                    #The "if" statement will only run if the subheader is more than
                    #one line in length (it begins on text[i+1] and the next non-empty
                    #line should meet the condition 'text[i+2].strip(" ") != "\n"'),
                    #and if there are two empty lines after it "empty_lines_after_heading >= 2"
                    if text[i+2].strip(" ") != "\n" and empty_lines_after_heading >= 2:
                        #The lines after index "i+2" are appended to line "i+2",
                        #down to "len(text)-3", as the "elif" statement needs to
                        #start screening three lines ahead.
                        complete_subheading = text[i+2].strip() + " "
                        loop_done = False
                        for j in range(i+3, len(text)-3):
                            if loop_done == True:
                                break
                            #If the line is empty "\n", then the lines after it
                            #are screened to determine where a non-empty
                            #line is encountered next (!= "\n"). Upon reaching
                            #that non-empty line, the variable "loop_done" is
                            #set to "True" and the nested "for" loops are broken.
                            elif text[j].strip(" ") == "\n":
                                for k in range(i+4, len(text)-3):
                                    if text[k].strip(" ") != "\n":
                                        loop_done = True
                                        break
                                    #If the line is empty "\n", then its index
                                    #is appended to the list "slash_n_line_indices".
                                    #This will remove all the empty lines in-between
                                    #the heading and the next line of body text.
                                    else:
                                        if k not in slash_n_line_indices:
                                            slash_n_line_indices.append(k)
                            #If the line at index "j" isn't empty (!= "\n"),
                            #then it will be appended to the first line of the
                            #subtitle at index "i+2". The indices of the non-empty
                            #lines after "i+3" will be appended to the list
                            #"slash_n_line_indices" and removed later in the code.
                            #The line at index "i+3" will be overwritten with two
                            #empty paragraph RTF commands to have two carriage
                            #returns after every heading (text[i+3] = (r"\par}{\pard\sa" +
                            #points_between_paragraphs + line_spacing + r"\qj" +
                            #r"\par}{\pard\sa" + points_between_paragraphs +
                            #line_spacing + r"\qj ")).
                            else:
                                complete_subheading += text[j].strip() + " "
                                text[j] = "\n"
                                if j not in slash_n_line_indices and j > i+3:
                                    slash_n_line_indices.append(j)
                        #As a space is added after every line down to the
                        #end of "next_carriage_return", the final space
                        #needs to be removed and a carriage return needs
                        #to be placed at the end of the line "\n" so that
                        #the automatic removal of extraneous "\n" proceeds
                        #as usual later in the code.
                        text[i+2] = complete_subheading.strip() + "\n"

                        if bold_chapter_headings:
                            #As there could be a subsection under chapter heading (for example,
                            #'Chapter One "\n" I. "\n" Body text'), then the page break and
                            #carriage returns should only be added before a chapter heading
                            #if at least one line of regular text was encountered ("page_break_ok == True").
                            if page_break_ok == True:
                                text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing +  r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                                chapter_heading_font_size + r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}")
                                text[i+2] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc"  + chapter_heading_font_size + r"\b " +
                                text[i+2].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                                r" " + line_spacing + r"\qj")
                                text[i+3] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                #"page_break_ok" is set to "False" and will be reset to "True" once
                                #a regular line of text will be reached in the final "else" statement
                                #of this "for" loop.
                                page_break_ok = False
                            else:
                                text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc" + chapter_heading_font_size + r"\b " +
                                text[i].strip(" ")[:-1] + r"\b0\par}")
                                text[i+2] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc"  + chapter_heading_font_size + r"\b " +
                                text[i+2].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                                r" " + line_spacing + r"\qj")
                                text[i+3] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False
                        else:
                            #As there could be a subsection under chapter heading (for example,
                            #'Chapter One "\n" I. "\n" Body text'), then the page break and
                            #carriage returns should only be added before a chapter heading
                            #if at least one line of regular text was encountered ("page_break_ok == True").
                            if page_break_ok == True:
                                text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing +  r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                                chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}")
                                text[i+2] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc"  + chapter_heading_font_size + text[i+2].strip(" ")[:-1] +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                                text[i+3] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                #"page_break_ok" is set to "False" and will be reset to "True" once
                                #a regular line of text will be reached in the final "else" statement
                                #of this "for" loop.
                                page_break_ok = False
                            else:
                                text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc" + chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}")
                                text[i+2] = (r"{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                                r"\qc"  + chapter_heading_font_size + text[i+2].strip(" ")[:-1] + r"\par}{\pard\sa" +
                                points_between_paragraphs + line_spacing + r"\qj")
                                text[i+3] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False

                    #If the line following the title heading is empty, then the
                    #chapter title formatting elements are only applied to the
                    #chapter heading line (ex: Chapter I.).
                    else:
                        if bold_chapter_headings:
                            if page_break_ok == True:
                                text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                                chapter_heading_font_size + r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" +
                                points_between_paragraphs + line_spacing + r"\qj")
                                text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False
                            else:
                                text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc" + chapter_heading_font_size + r"\b " + text[i].strip(" ")[:-1] +
                                r"\b0\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                                text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False
                        else:
                            if page_break_ok == True:
                                text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" +
                                line_spacing + r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                                chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}{\pard\sa" +
                                points_between_paragraphs + line_spacing + r"\qj")
                                text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False
                            else:
                                text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                                r"\qc" + chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}{\pard\sa" +
                                points_between_paragraphs + line_spacing + r"\qj")
                                text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                                page_break_ok = False

            #If the chapter subtitle is found on the same line as the chapter heading and
            #that the chapter heading is comprised of either a digit, roman numeral or number
            #in written form, followed by either a period or colon and if the line index is
            #zero or the previous line is empty then the chapter heading is further investigated
            #below. (Examples: 1. Chapter Title / II: CHAPTER TITLE)
            elif (text[i].strip(" ") != "\n" and (text[i].strip(" ").split()[0][:-1] in roman_numerals or
            text[i].strip(" ").split()[0][:-1] in numbers or text[i].strip(" ").split()[0][:-1] in
            numbers_letters_lower) and text[i].strip(" ").split()[0][-1] in [".",":"] and
            (i == 0 or i > 0 and text[i-1].strip(" ") == "\n")):
                #If the line after the chapter heading isn't empty, it means
                #that the chapter heading spans multiple lines. All of the
                #lines following the start of chapter heading, down
                #to the next carriage return "\n" will be appended to the
                #stripped version of line text[i], so that there will not
                #be random carriage returns within the subheading. All of the
                #subsequent lines after text[i], down to the next carriage
                #return will be changed to "\n", and extraneous "\n" will
                #be removed later in the code.
                if text[i+1].strip(" ") != "\n":
                    complete_subheading = text[i].strip() + " "
                    loop_done = False
                    #The lines after index "i" are appended to line "i",
                    #down to "len(text)-2", as the "elif" statement needs to
                    #start screening two lines ahead.
                    for j in range(i+1, len(text)-2):
                        if loop_done == True:
                            break
                        #If the line is empty "\n", then the lines after it
                        #are screened to determine where a non-empty
                        #line is encountered next (!= "\n"). Upon reaching
                        #that non-empty line, the variable "loop_done" is
                        #set to "True" and the nested "for" loops are broken.
                        elif text[j].strip(" ") == "\n":
                            for k in range(i+2, len(text)-2):
                                if text[k].strip(" ") != "\n":
                                    loop_done = True
                                    break
                                #If the line is empty "\n", then its index
                                #is appended to the list "slash_n_line_indices".
                                #This will remove all the empty lines in-between
                                #the heading and the next line of body text.
                                else:
                                    if k not in slash_n_line_indices:
                                        slash_n_line_indices.append(k)
                        #If the line at index "j" isn't empty (!= "\n"),
                        #then it will be appended to the first line of the
                        #subtitle at index "i". The indices of the non-empty
                        #lines after "i+1" will be appended to the list
                        #"slash_n_line_indices" and removed later in the code.
                        #The line at index "i+1" will be overwritten with two
                        #empty paragraph RTF commands to have two carriage
                        #returns after every heading (text[i+1] = (r"\par}{\pard
                        #\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                        #r"\par}{\pard\sa" + points_between_paragraphs  +
                        #line_spacing + r"\qj ")).
                        else:
                            complete_subheading += text[j].strip() + " "
                            text[j] = "\n"
                            if j not in slash_n_line_indices and j > i+1:
                                slash_n_line_indices.append(j)

                    #As a space is added after every line down to the
                    #end of "next_carriage_return", the final space
                    #needs to be removed and a carriage return needs
                    #to be placed at the end of the line "\n" so that
                    #the automatic removal of extraneous "\n" proceeds
                    #as usual later in the code.
                    text[i] = complete_subheading.strip() + "\n"

                if bold_chapter_headings:
                    if page_break_ok == True:
                        text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                        r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                        r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                        line_spacing + r"\qj")
                        text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                        r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                        page_break_ok = False
                    else:
                        text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                        r"\qc" + r"\b " + chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" +
                        points_between_paragraphs + line_spacing + r"\qj")
                        text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                        r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                        page_break_ok = False
                else:
                    if page_break_ok == True:
                        text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                        r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                        text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                        text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                        r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                        page_break_ok = False
                    else:
                        text[i] = (r"\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing + r"\qc" +
                        chapter_heading_font_size + text[i].strip(" ")[:-1] + r"\par}{\pard\sa" +
                        points_between_paragraphs + line_spacing + r"\qj")
                        text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                        r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                        page_break_ok = False

            #If the chapter subtitle is found on the same line as the chapter heading and
            #that the chapter heading is comprised of the word "chapter" followed by a space
            #and then either a digit, roman numeral or number in written form, themselves followed
            #by either a period or colon, and if the line index is zero or the previous line
            #is empty then the chapter heading is further investigated below.
            #Examples: Chapter 1: Chapter Title / CHAPTER TWO. Chapter Title / Chapter Three: CHAPTER TITLE
            elif ((text[i].strip(" ") != "\n" and len(text[i].strip(" ").split()) > 0 and
            text[i].strip(" ").split()[0].lower() == "chapter") and (text[i].strip(" ").split()[1][:-1] in
            roman_numerals or text[i].strip(" ").split()[1][:-1] in numbers or
            text[i].strip(" ").split()[1][:-1].lower() in numbers_letters_lower) and
            text[i].strip(" ").split()[1][-1] in [".",":"] and
            (i == 0 or i > 0 and text[i-1].strip(" ") == "\n")):
                #If the line after the chapter heading isn't empty, it means
                #that the chapter heading spans multiple lines. All of the
                #lines of following the start of chapter heading, down
                #to the next carriage return "\n" will be appended to the
                #stripped version of line text[i], so that there will not
                #be random carriage returns within the subheading. All of the
                #subsequent lines after text[i], down to the next carriage
                #return will be changed to "\n", and extraneous "\n" will
                #be removed later in the code.
                if text[i+1].strip(" ") != "\n":
                    complete_subheading = text[i].strip() + " "
                    loop_done = False
                    #The lines after index "i" are appended to line "i",
                    #down to "len(text)-2", as the "elif" statement needs to
                    #start screening two lines ahead.
                    for j in range(i+1, len(text)-2):
                        if loop_done == True:
                            break
                        #If the line is empty "\n", then the lines after it
                        #are screened to determine where a non-empty
                        #line is encountered next (!= "\n"). Upon reaching
                        #that non-empty line, the variable "loop_done" is
                        #set to "True" and the nested "for" loops are broken.
                        elif text[j].strip(" ") == "\n":
                            for k in range(i+2, len(text)-2):
                                if text[k].strip(" ") != "\n":
                                    loop_done = True
                                    break
                                #If the line is empty "\n", then its index
                                #is appended to the list "slash_n_line_indices".
                                #This will remove all the empty lines in-between
                                #the heading and the next line of body text.
                                else:
                                    if k not in slash_n_line_indices:
                                        slash_n_line_indices.append(k)
                        #If the line at index "j" isn't empty (!= "\n"),
                        #then it will be appended to the first line of the
                        #subtitle at index "i". The indices of the non-empty
                        #lines after "i+1" will be appended to the list
                        #"slash_n_line_indices" and removed later in the code.
                        #The line at index "i+1" will be overwritten with two
                        #empty paragraph RTF commands to have two carriage
                        #returns after every heading (text[i+1] = (r"\par}{\pard
                        #\sa" + points_between_paragraphs + line_spacing + r"\qj"
                        #+ r"\par}{\pard\sa" + points_between_paragraphs +
                        #line_spacing + r"\qj ")).
                        else:
                            complete_subheading += text[j].strip() + " "
                            text[j] = "\n"
                            if j not in slash_n_line_indices and j > i+1:
                                slash_n_line_indices.append(j)

                    #As a space is added after every line down to the
                    #end of "next_carriage_return", the final space
                    #needs to be removed and a carriage return needs
                    #to be placed at the end of the line "\n" so that
                    #the automatic removal of extraneous "\n" proceeds
                    #as usual later in the code.
                    text[i] = complete_subheading.strip() + "\n"

                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs +
                    r"\hyphpar0" + line_spacing + r"\qc" + number_of_lines_above_chapter_headings*r"\line" +
                    chapter_heading_font_size + r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" +
                    points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                    #As a subsection within a chapter wouldn't typically begin with the word "chapter",
                    #we only need to set "page_break_ok" to "False" after updating this chapter heading.
                    page_break_ok = False
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                    #As a subsection within a chapter wouldn't typically begin with the word "chapter",
                    #we only need to set "page_break_ok" to "False" after updating this chapter heading.
                    page_break_ok = False

            #If the element at index "i" of the list "text" corresponds to "foreword" or "afterword" (irrespective
            #of case and followed or not by a period or colon), then the line is formatted according to the
            #chapter formatting settings. The same applies to all the "elif" statements following this one.
            elif ((text[i].strip().lower() == "foreword" or  text[i].strip().lower() == "foreword." or
            text[i].strip().lower() == "foreword:" or text[i].strip().lower() == "afterword" or
            text[i].strip().lower() == "afterword." or text[i].strip().lower() == "afterword:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "acknowledgements" or  text[i].strip().lower() == "acknowledgements." or
            text[i].strip().lower() == "acknowledgements:") and i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "preface" or  text[i].strip().lower() == "preface." or
            text[i].strip().lower() == "preface:") and i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "prologue" or  text[i].strip().lower() == "prologue." or
            text[i].strip().lower() == "prologue:" or text[i].strip().lower() == "epilogue" or
            text[i].strip().lower() == "epilogue." or text[i].strip().lower() == "epilogue:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "synopsis" or  text[i].strip().lower() == "synopsis." or
            text[i].strip().lower() == "synopsis:") and i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "introduction" or  text[i].strip().lower() == "introduction." or
            text[i].strip().lower() == "introduction:" or text[i].strip().lower() == "conclusion" or
            text[i].strip().lower() == "conclusion." or text[i].strip().lower() == "conclusion:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower()[:8] == "appendix" or  text[i].strip().lower()[:9] == "appendix." or
            text[i].strip().lower()[:9] == "appendix:" or text[i].strip().lower()[:8] == "addendum" or
            text[i].strip().lower()[:9] == "addendum." or text[i].strip().lower()[:9] == "addendum:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + "\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "glossary" or  text[i].strip().lower() == "glossary." or
            text[i].strip().lower() == "glossary:") and i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "bibliography" or  text[i].strip().lower() == "bibliography." or
            text[i].strip().lower() == "bibliography:" or text[i].strip().lower() == "endnotes" or
            text[i].strip().lower() == "endnotes." or text[i].strip().lower() == "endnotes:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing + r"\qc" +
                    number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "index" or  text[i].strip().lower() == "index." or
            text[i].strip().lower() == "index:") and i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")

            elif ((text[i].strip().lower() == "author biography" or  text[i].strip().lower() == "author biography." or
            text[i].strip().lower() == "author biography:" or text[i].strip().lower() == "author bio" or
            text[i].strip().lower() == "author bio." or text[i].strip().lower() == "author bio:") and
            i < len(text)-1 and text[i+1].strip(" ") == "\n"):
                if bold_chapter_headings:
                    text[i] = (r"\par}{\page \pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    r"\b " + text[i].strip(" ")[:-1] + r"\b0\par}{\pard\sa" + points_between_paragraphs +
                    line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
                else:
                    text[i] = (r"\par}{\page \pard\sa" + points_between_paragraphs + r"\hyphpar0" + line_spacing +
                    r"\qc" + number_of_lines_above_chapter_headings*r"\line" + chapter_heading_font_size +
                    text[i].strip(" ")[:-1] + r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")
                    text[i+1] = (r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                    r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj ")
            #The variable "page_break_ok" is initialized to "True" and
            #allows for inclusion of a page break and carriage returns (\line)
            #before the chapter headings. After writing the heading, the variable
            #will be set to "False" and only set to "True" again once a
            #regular line of text will be encountered. That is to say,
            #if the line under investigation isn't a carriage return ("\n")
            #nor the empty paragraphs after a heading (r"\par}{\pard\sa" +
            #points_between_paragraphs + line_spacing + r"\qj" + r"\par}{\pard\sa"
            #+ points_between_paragraphs + line_spacing + r"\qj"),"page_break_ok"
            #will be reset to "True".
            elif (text[i].strip(" ") != "\n" and text[i].strip(" ") != r"\par}{\pard\sa" +
            points_between_paragraphs + line_spacing + r"\qj" + r"\par}{\pard\sa" +
            points_between_paragraphs + line_spacing + r"\qj"):
                page_break_ok = True

        #The "text" list elements at the indices found within the
        #"slash_n_line_indices" list will be removed in reverse
        #order, in order to avoid indexing issues when deleting
        #elements. The list "slash_n_line_indices" is then
        #sorted beforehand. This step needs to be done before
        #changing any carriage returns "\n" into RTF commands
        #for new paragraphs, in order to avoid introducing
        #superfluous RTF commands.
        slash_n_line_indices.sort()
        for i in range(len(slash_n_line_indices)-1, -1, -1):
            text.pop(slash_n_line_indices[i])

        #As numerous empty lines were removed from the "text" list,
        #the indices "author_index" and "title_index" need to be
        #determined once again.
        for i in range(len(text)):
            #In case the author name is preceded by "by" (or an equivalent in another language),
            #the first word of the line is skipped over and stored in "line_skipping_first_word",
            #for comparison with "author" in the first "elif" statement.
            line_words = text[i].split()
            if len(line_words) > 1:
                line_skipping_first_word = (" ".join(line_words[1:]).lower().strip())

            if title_index == None and text[i].lower().strip() == title.lower():
                title_index = i
                title_string = text[i].lower().strip()

            #If the element at index "i" of the "text" list corresponds to the author name
            #(either or not while skipping over the first word such as "by") and is located
            #within 5 elements of the title, its index will be stored in "author_index".
            elif (author_index == None and title_index != None and (text[i].lower().strip() == author.lower() or
            line_skipping_first_word == author.lower()) and i < title_index + 5):
                author_index = i

        #Cycling though the "text" list of lines and removing
        #carriage returns "\n" if they are not preceded by a
        #line ending with a carriage return. This will effectively
        #remove carriage returns within paragraphs.
        #The line index at which the extroneous line carriages "\n"
        #will stop being removed will depend on whether or not
        #there is a table of contents, or author name at the
        #beginning of the text file, precedence being given to
        #the former.
        space_removal_end = 0
        if author_index != None:
            space_removal_end = author_index
        elif title_index != None:
            space_removal_end = title_index

        #The presence of empty lines in-between paragraphs is examined in the
        #"for" loop below, where any instances of empty lines ('text[i].strip(" ") == "\n"')
        #preceded by a line ending with a carriage return ('text[i-1].strip(" ")[-1] == "\n"'),
        #and followed by another empty line ('text[i+1].strip(" ") == "\n"') will result
        #in the inclusion of two new empty paragraph RTF commands ('r"\par}{\pard \sa" +
        #points_between_paragraphs + line_spacing + r"\qj "', with a space after "\pard " in
        #order to distinguish them from other empty paragraphs, as these ones need to remain
        #and not be automatically removed by the code later on in the script), insofar
        #as the line at index "i+2" isn't empty nor isn't the start of a heading, which would
        #contain the "\hyphpar0" RTF command that deactivates automatic hyphenation for the heading
        #paragraph ('text[i+2].strip(" ")[:len(r"\page\par}{\pard\sa" +
        #points_between_paragraphs + r"\hyphpar0")] not in ["\n", "\page\par}{\pard\sa" +
        #points_between_paragraphs + r"\hyphpar0"]').
        line_index_next_heading = None
        line_index_next_body_text = None
        for i in range(len(text)-1, space_removal_end, -1):
            if (i > space_removal_end and i < len(text)-2 and
            text[i].strip(" ") == "\n" and text[i-1].strip(" ")[-1] == "\n" and
            text[i+1].strip(" ") == "\n" and text[i+2].strip(" ")[:len(r"\page\par}{\pard\sa" +
            points_between_paragraphs + r"\hyphpar0")] not in
            ["\n", r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0"]):
                text[i] = r"\par}{\pard \sa" + points_between_paragraphs + line_spacing + r"\qj "
                text[i+1] = r"\par}{\pard \sa" + points_between_paragraphs + line_spacing + r"\qj "

        for i in range(len(text)-1, space_removal_end, -1):
            #The current instance of "\n" will be converted into a new RTF paragraph
            #"r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + "\qj\line ",
            #as the previous instance of "\n" ("text[i-1].strip(" ")[-1]")
            #will be removed in the next iteration of the "for" loop (elif statement).
            #The substitution of the new RTF paragraph for "\n" will only take place
            #if the current line is empty ('text[i].strip(" ") == "\n"'), the previous line
            #ends with a carriage return ('text[i-1].strip(" ")[-1] == "\n"') and the
            #following line is not the start of a new paragraph, which contains the "\hyphpar0"
            #RTF command to disable the automatic hyphenation ('text[i+1].strip(" ")[:len(r"\page\par}{\pard\sa" +
            #points_between_paragraphs + r"\hyphpar0")] != "\page\par}{\pard\sa" +
            #points_between_paragraphs + r"\hyphpar0")')
            if (i > space_removal_end and text[i].strip(" ") == "\n" and text[i-1].strip(" ")[-1] == "\n" and
            i < len(text)-1 and len(text[i+1].strip(" ")) > 24 and text[i+1].strip(" ")[:len(r"\page\par}{\pard\sa" +
            points_between_paragraphs + r"\hyphpar0")] != r"\page\par}{\pard\sa" + points_between_paragraphs +
            r"\hyphpar0"):
                text[i] = r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj "
            elif (i > space_removal_end and i < len(text)-1 and text[i].strip(" ") != "\n" and
            text[i][-1] == "\n" and text[i+1] != r"\par}{\pard\sa" + points_between_paragraphs +
            line_spacing + r"\qj "):
                text[i] = text[i][:-1] + " "

        #The index at which the "\tab" RTF commands begin to be added
        #is set to the latest between "author_index" and "title_index",
        #so as to avoid adding tabs to the title page.
        if author_index != None:
            tabs_index_start = author_index
        elif title_index != None:
            tabs_index_start = title_index
        else:
            problem == True
            print('\n\nPlease ensure that your TXT file has a book title and author name (preceded by "by") in it, ' +
            "directly following the Project Gutenbergs start label, as in the following example:")
            print("\n*** START OF THE PROJECT GUTENBERG EBOOK THE TIME MACHINE ***")
            print("\nThe Time Machine")
            print("An Invention")
            print("by H. G. Wells")


        if problem == False:
            for i in range(len(text)-1, tabs_index_start, -1):
                #If the current line isn't an empty line ("\n" that was later changed
                #to "r"\par}{\pard\sa" + points_between_paragraphs + line_spacing +
                #"\qj\line") and if the current line isn't a chapter heading (which
                #would contain a page break and start with the following: "\page\par}{\pard\sa" +
                #points_between_paragraphs + r"\hyphpar0"), and the previous line
                #is either an empty line ("r"\par}{\pard\sa" + points_between_paragraphs +
                #line_spacing + "\qj\line", with or without a space after "\pard",
                #the space being added to distinguish new empty paragraphs inserted after
                #empty lines in-between paragraphs) or the line right after a chapter heading
                #('r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                #r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj"'),
                #then add a "\tab " RTF command at the beginning of the line (with optional
                #space to prevent mixups when the software parses the RTF commands)
                if (text[i].strip(" ") != r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" and
                text[i].strip(" ")[:len(r"\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0")] !=
                "\page\par}{\pard\sa" + points_between_paragraphs + r"\hyphpar0" and
                (text[i-1].strip(" ") == r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" or
                text[i-1].strip(" ") == r"\par}{\pard \sa" + points_between_paragraphs + line_spacing + r"\qj" or
                text[i-1].strip(" ") == r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" +
                r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj")):
                    #The line "re.search(r"([' ']{0})", text[i])"
                    #searches for the first occurence of a non-space
                    #character in the line "text[i]".
                    non_space_match = re.search(r"([' ']{0})", text[i])
                    if non_space_match != None:
                        non_space_index = non_space_match.start()
                        if non_space_index == 0:
                            text[i] = r"\tab " + text[i]
                        elif non_space_index > 0:
                            non_space_start_index = non_space_index - 4
                            text[i] = r"\tab " + text[i][non_space_start_index:]

            #The following code removes successive carriage returns in the "if" statement
            #("\n" that were later changed to r"\par}{\pard\sa" + points_between_paragraphs +
            #line_spacing + "\qj\line "), insofar as the previous line is another such carriage return.
            for i in range(len(text)-1, tabs_index_start, -1):
                if (text[i].strip(" ") == r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj" and
                text[i-1].strip(" ") == r"\par}{\pard\sa" + points_between_paragraphs + line_spacing + r"\qj"):
                    text.pop(i)

            #Joining the list items of "text" with empty strings, as there are
            #already "\n\n" dividers in-between paragraphs.
            text_string = ("".join(text).replace("\n", "").replace("--", r"\'97"))

            #If there is at least one instance of a non-directional single "'" or
            #double '"' quote in the "text_string" string, then the following "if"
            #statement will run. First, all of the directional quotes are switched
            #to their non-directional counterparts.
            if text_string.find("'") != -1 or text_string.find('"') != -1:
                text_string = (text_string.replace("‘", "'").replace("’", "'")
                .replace('“', '"').replace('”', '"'))

            #The nested quotes and single or double quotes followed by a space (and thus mapping
            #to closing directional quotes) are changed to their RTF escape equivalents.
            quote_substitutions = [['"' + "'", r"\'93" + r"\'91"], ["'" + '"', r"\'92" + r"\'94"],
            ["' ", r"\'92" + ' '], ['" ', r"\'94" + ' ']]
            for quote in quote_substitutions:
                text_string = re.sub(quote[0], quote[1], text_string)

            #If the first character of the "text_string" string
            #is a quote, it is then changed for the corresponding
            #opening directional quote.
            if text_string[0] == "'":
                text_string = r"\'91" + text_string[1:]
            elif text_string[0] == '"':
                text_string = r"\'93" + text_string[1:]

            #If the last character of the "text_string" string
            #is a quote, it is then changed for the corresponding
            #closing directional quote.
            if text_string[-1] == "'":
                text_string = text_string[:-1] + r"\'92"
            elif text_string[-1] == '"':
                text_string = text_string[:-1] + r"\'94"

            #The indices of any remaining symmetrical double quotes ('"') are stored in
            #the list "double_quote_indices" and cycled through using a "for" loop.
            #If the index is above zero and smaller than the last index of the "double_quote_indices"
            #list, and if the preceding character is not a space, then the closing directional quote
            #is substituted for the symmetrical one. The "text_string" string is updated by
            #slicing it while skipping over what was the symmetrical double quote ('"') at index
            #"double_quote_indices[i]" in "text_string". The "for" loop proceeds in reverse order
            #to avoid indexing issues when substituting quotes for multi-character RTF escapes.
            double_quote_matches = re.finditer('"', text_string)
            double_quote_indices = [match.start() for match in double_quote_matches]
            for i in range(len(double_quote_indices)-1, -1, -1):
                if (double_quote_indices[i] > 0 and double_quote_indices[i] < len(text_string)-1 and
                text_string[double_quote_indices[i]-1] != " "):
                    text_string = (text_string[:double_quote_indices[i]] + r"\'94" +
                    text_string[double_quote_indices[i]+1:])

                #If the index is above zero and smaller than the last index of the "double_quote_indices"
                #list, and if the previous character is not a letter and the following character is either
                #a letter or "¡", "¿" (which would start an exclamation or question, respectively, in Spanish)
                #a backslash (if the quote is followed by an RTF command or escape such as "\i"),
                #or an underscore (the italics will be dealt with after this step), then the double quote
                #is changed to the opening directional quote.
                elif (double_quote_indices[i] > 0 and double_quote_indices[i] < len(text_string)-1 and
                (text_string[double_quote_indices[i]-1].isalpha() == False and
                (text_string[double_quote_indices[i]+1].isalpha() or
                text_string[double_quote_indices[i]+1] in ["¡", "¿", "\\", "_"]))):
                    text_string = (text_string[:double_quote_indices[i]] + r"\'93" +
                    text_string[double_quote_indices[i]+1:])

            single_quote_matches = re.finditer("'", text_string)
            single_quote_indices = [match.start() for match in single_quote_matches]
            for i in range(len(single_quote_indices)-1, -1, -1):
                #The "if" statement will also change the symmetrical single quote to the closing
                #directional single quote in contractions such as "don't", as only the preceding character
                #is considered. In this case, the preceding character must not be a space nor a backslash
                #so that the single quote in the RTF escapes (such as r"\'92") are not confused for actual
                #single quotes.
                if (single_quote_indices[i] > 0  and single_quote_indices[i] < len(text_string)-1 and
                text_string[single_quote_indices[i]-1] != "\\" and text_string[single_quote_indices[i]-1] != " "):
                    text_string = (text_string[:single_quote_indices[i]] + r"\'92" +
                    text_string[single_quote_indices[i]+1:])

                elif (single_quote_indices[i] > 0 and single_quote_indices[i] < len(text_string)-1 and
                (text_string[single_quote_indices[i]-1] != "\\" and
                text_string[single_quote_indices[i]-1].isalpha() == False and
                (text_string[single_quote_indices[i]+1].isalpha() or
                text_string[single_quote_indices[i]+1] in ["¡", "¿", "\\", "_"]))):
                    text_string = (text_string[:single_quote_indices[i]] + r"\'91" +
                    text_string[single_quote_indices[i]+1:])


            #A copy of "text_string" is made in case there are formatting errors in the
            #manuscript and unmatched underscores. This way, the "text_string" will only
            #be updated if all of the underscores can be assigned to italics RTF commands.
            text_string_copy = text_string
            #If there is at least one instance of an underscore in
            #"text_string_copy", indicating the presence of italics
            #formatting, the "if" statement will run.
            if text_string_copy.find("_") != -1:
                underscore_matches = re.finditer("_", text_string_copy)
                underscore_indices = [match.start() for match in underscore_matches]
                #The variable "italics_opening_tag" is initialized to false and
                #designates whether or not the next italics tag to be assigned
                #is an opening tag. As the "for" loop proceeds in reverse order
                #to avoid indexing issues related tu the substitution of an underscore
                #for a multi-character RTF command, the first italics tag to
                #be assigned will be a closing one (r"\i0"). Every time an
                #italics tag is assigned, the value of "italics_opening_tag"
                #is changed to its opposite.
                italics_opening_tag = False
                for i in range(len(underscore_indices)-1, -1, -1):
                    if italics_opening_tag == True and underscore_indices[i] < len(text_string_copy)-1:
                        #The "text_string_copy" string is sliced while skipping over the index at
                        #which the underscore was found, introducing the RTF italics tag in its place.
                        text_string_copy = (text_string_copy[:underscore_indices[i]] + r"\i " +
                        text_string_copy[underscore_indices[i]+1:])
                        italics_opening_tag = False
                    elif italics_opening_tag == False and underscore_indices[i] < len(text_string_copy)-1:
                        text_string_copy = (text_string_copy[:underscore_indices[i]] + r"\i0 " +
                        text_string_copy[underscore_indices[i]+1:])
                        italics_opening_tag = True
                    elif italics_opening_tag == False and underscore_indices[i] == len(text_string_copy)-1:
                        text_string_copy = text_string_copy[:underscore_indices[i]] + r"\i0 "
                        italics_opening_tag = True

                #As the initial value of "italics_opening_tag" was set
                #to "False", it should end up at "False" if all underscores
                #were matched to their respective italics RTF commands. If
                #The value ends up being "True", it means that there are
                #some missing underscores in the text file to fully pair up.
                if italics_opening_tag == False:
                    text_string = text_string_copy
                #If the underscores don't match up, the user is informed that
                #the italics formatting has not been applied to the file and
                #the underscores will remained unchanged. The code below will
                #continue on with the "text_string", which was not updated
                #as in the "if" statement above.
                else:
                    print("\nThere appears to be formatting errors in the submitted text file, " +
                    "in that there are some unmatched underscores that prevent the code from " +
                    "applying intalics formating to the text. All the underscores were therefore " +
                    "left unchanged and designate words or passages in italics.")

            #The RTF escapes are substituted for the symbols to allow for adequate representation within
            #the RTF file.
            rtf_escapes = [['…', r"\'85"], ['†', r"\'86"], ['‡', r"\'87"],  ['✕', r"\'d7"], ['\+', r"\'2b"],
            ['⋅', r"\'b7"], ['÷', r"\'f7"], ['/', r"\'2f"], ['>', r"\'3e"], ['<', r"\'3c"], ['=', r"\'3d"],
            ['¢', r"\'a2"], ['\$', r"\'24"], ['€', r"\'80"], ['¤', r"\'a4"], ['¥', r"\'a5"],  [r'\[', r"\'5b"],
            ['\]', r"\'5d"], ['\^', r"\'5e"], ['ˆ', r"\'88"], ['`', r"\'60"], ['´', r"\'b4"], ['”', r"\'94"],
            ['\|', r"\'7c"], ['¦', r"\'a6"], ['£', r"\'a3"], ['″', r"\'22"], ['%', r"\'25"], ['‰', r"\'89"],
            ['Š', r"\'8a"], ['š', r"\'9a"], ['‹', r"\'8b"], ['›', r"\'9b"], ['Œ', r"\'8c"], ['œ', r"\'9c"],
            ['Ÿ', r"\'9f"], ['Ž', r"\'8e"], ['ž', r"\'9e"], ['°', r"\'b0"], ['#', r"\'23"], ['&', r"\'26"],
            ['©', r"\'a9"], ['™', r"\'99"], ['•', r"\'95"], ['@', r"\'40"], [r'\*', r"\'2a"], ['∼', r"\'98"],
            ['±', r"\'b1"], ['€', r"\'80"], ['͵', r"\'80"], ['ƒ', r"\'83"], ['„', r"\'84"], ['〃', r"\'22"],
            ['¶', r"\'b6"], ['®', r"\'ae"], ['§', r"\'a7"], ['«', r"\'ab"], ['»', r"\'bb"], ['¡', r"\'a1"],
            ['¿', r"\'bf"], ['¨', r"\'a8"], ['ª', r"\'aa"], ['º', r"\'ba"], ['¬', r"\'ac"], ['¯', r"\'af"],
            ['¼', r"\'bc"], ['½', r"\'bd"], ['¾', r"\'be"], ['¹', r"\'b9"], ['²', r"\'b2"], ['³', r"\'b3"],
            ['µ', r"\'b5"], ['¸', r"\'b8"], ['À', r"\'c0"], ['Á', r"\'c1"], ['Â', r"\'c2"], ['Ã', r"\'c3"],
            ['Ä', r"\'c4"], ['Å', r"\'c5"], ['Æ', r"\'c6"], ['Ç', r"\'c7"], ['È', r"\'c8"], ['É', r"\'c9"],
            ['Ê', r"\'ca"], ['Ë', r"\'cb"], ['Ì', r"\'cc"], ['Í', r"\'cd"], ['Î', r"\'ce"], ['Ï', r"\'cf"],
            ['Ð', r"\'d0"], ['Ñ', r"\'d1"], ['Ò', r"\'d2"], ['Ó', r"\'d3"], ['Ô', r"\'d4"], ['Õ', r"\'d5"],
            ['Ö', r"\'d6"], ['Ø', r"\'d8"], ['Ù', r"\'d9"], ['Ú', r"\'da"], ['Û', r"\'db"], ['Ü', r"\'dc"],
            ['Ý', r"\'dd"], ['Þ', r"\'de"], ['ß', r"\'df"], ['à', r"\'e0"], ['á', r"\'e1"], ['â', r"\'e2"],
            ['ã', r"\'e3"], ['ä', r"\'e4"], ['å', r"\'e5"], ['æ', r"\'e6"], ['ç', r"\'e7"], ['è', r"\'e8"],
            ['é', r"\'e9"], ['ê', r"\'ea"], ['ë', r"\'eb"], ['ì', r"\'ec"], ['í', r"\'ed"], ['î', r"\'ee"],
            ['ï', r"\'ef"], ['ð', r"\'f0"], ['ñ', r"\'f1"], ['ò', r"\'f2"], ['ó', r"\'f3"], ['ô', r"\'f4"],
            ['õ', r"\'f5"], ['ö', r"\'f6"], ['ø', r"\'f8"], ['ù', r"\'f9"], ['ú', r"\'fa"], ['û', r"\'fb"],
            ['ü', r"\'fc"], ['ý', r"\'fd"], ['þ', r"\'fe"], ['ÿ', r"\'ff"], ["\-", r"\'2d"], ["—", r"\'97"],
            ['—', r"\'96"], ['_', r"\'5f"], ["‘", r"\'91"], ["’", r"\'92"], ['“', r"\'93"]]
            for escape in rtf_escapes:
                text_string = re.sub(escape[0], escape[1], text_string)

            #Please consult the following reference for an in-depth explanation of RTF commands:
            #(https://www.oreilly.com/library/view/rtf-pocket-guide/9781449302047/ch01.html)
            with open(txt_file_name[:-4] + ".rtf", "w", encoding="utf-8") as g:
                g.write(r"{\rtf1\ansi\deff0{\fonttbl{\f0" + font + ";}}\plain\sl100" +
                body_font_size + header_top_margin + top_margin +
                bottom_margin + left_margin + right_margin + tab_width + r"\hyphauto\hyphconsec1"
                r"\widowctrl" + r"{\header\pard\qc\plain" + header_font_size +
                r"\chpgn\par}{\pard\hyphpar0\pvmrg\phmrg\posxc" + title_page_posy + r"\qc")
                g.write(text_string + r"\par}}")

            #If the "inches_per_ream_500_pages" or "cm_per_ream_500_pages" and "number_of_pages"
            #were passed in as additional arguments, it means that the user has reviewed the
            #RTF document and deemed it suitable, and now wants to generate a cover. The number
            #of pages and thickness of a ream of paper of 500 pages will allow to determine
            #the dimensions of the rectangle that will mark the location of the spine of the book
            #on a US Legal canvas in Landscape mode and with a resolution of 300 ppi.
            spine_thickness_pixels = None
            if number_of_pages != None and inches_per_ream_500_pages != None:
                spine_thickness_inches = inches_per_ream_500_pages*number_of_pages/500
                spine_thickness_pixels = int(inches_per_ream_500_pages*4200/14)
            if problem == False and number_of_pages != None and spine_thickness_pixels != None:
                #The "ImageDraw" module will load the default background image (which
                #the user can change by selecting another image in the working folder and
                #passing in its name as an additional argument, when calling the Python code.
                font_title = ImageFont.truetype(cover_font, cover_title_size)
                image = Image.open(background_img)
                #If the user hasn't provided a color for the cover text box
                #nor for the cover text, the colors will be assigned automatically
                #based on the darkest and lightest pixels on the canvas. In order to
                #facilitate this process, the image the image is first converted to
                #grayscale in order to be able to extract the darkest and lightest
                #pixels from the background.

                #If the user hasn't povided a color for the cover text box
                #nor for the cover text, then the code needs to check if
                #the submitted image is grayscale or not, in the case that
                #the "grayscale" argument wasn't passed in when running the code.
                #If the submitted image turns out to already be in grayscale format,
                #then the default color for the cover boxes is set to "Black" and
                #the color of the cover text is set to "LightGrey", as these give more
                #esthetically pleasing results in terms of contrast with the
                #background.
                #The first pixel "x,y" coordinate at index "[0][0]" in the numpy
                #array "image_array" (before the image is converted to "RGBA" mode)
                #will be checked to see if it is of type "np.ndarray", indicating that
                #it has RGB channels, instead of being an integer as in a
                #grayscale image. If the "isinstance()" method is "False",
                #then it means that the image is grayscale.
                if cover_box_color == None and cover_text_color == None:
                    image_array = np.array(image)
                    if isinstance(image_array[0][0], np.ndarray) == False or grayscale == True:
                        cover_box_color = "Black"
                        cover_text_color = "LightGrey"
                        #If the provided image was in grayscale format to start with,
                        #or if the user has passed in the "grayscale" argument when
                        #running the code, then the "image" instance is overwritten with
                        #its grayscale version and the "grayscale" variable is set to "True",
                        #in order to avoid creating another grayscale image in the "elif"
                        #statement below: "cover_box_color == None and cover_text_color ==
                        #None and grayscale == False".
                        image = ImageOps.grayscale(image)
                        grayscale = True

                #If the provided image isn't in grayscale format, then the colors for the
                #cover text box fill and text need to be determined. The value of the variable
                #"grayscale" will determine if the original image will be overwritten with its
                #grayscale version or if a new instance of the "ImageOps" class will be created,
                #in order to preserve the color information from the original "image".

                #If the "grayscale" variable is set to "True", it means that the user
                #wants to output the cover in grayscale format, and the original image
                #is overwritten with the grayscale image ("image = ImageOps.grayscale(image)").
                if cover_box_color == None and cover_text_color == None and grayscale == True:
                    image_array = np.array(image)
                    #The "x,y" coordinates for the lightest pixels (having the highest grayscale
                    #value, as white is 255) are found using the np.where() method, where the
                    #pixels's grayscale value is equal to the maximal grayscale value
                    #(np.max(image_array)).
                    max_pixels = np.where(image_array == np.max(image_array))
                    #One of the pixel "x,y" coordinates matching the highest grayscale value will
                    #be selected and stored in "max_pixel". If there were more than one pixel with
                    #that grayscale value ("len(max_pixels) > 1"), then the first one is selected.
                    if len(max_pixels) > 1:
                        max_pixel = [max_pixels[0][0], max_pixels[1][0]]
                    #If there is only one pixel with that grayscale value, then its coordinates
                    #are stored in "max_pixel".
                    else:
                        max_pixel = [max_pixels[0], max_pixels[1]]
                    #A similar approach is taken for the darkest pixels, which have the lowest
                    #grayscale value (black being 0).
                    min_pixels = np.where(image_array == np.min(image_array))
                    if len(min_pixels) > 1:
                        min_pixel = [min_pixels[0][0], min_pixels[1][0]]
                    else:
                        min_pixel = [min_pixels[0], min_pixels[1]]
                #If the user didn't pass in "grayscale" as an additional argument,
                #then the grayscale image is stored in "image_grayscale", to preserve
                #the color information of the original "image".
                elif cover_box_color == None and cover_text_color == None and grayscale == False:
                    image_grayscale = ImageOps.grayscale(image)
                    image_array_grayscale = np.array(image_grayscale)

                    #The "x,y" coordinates for the lightest pixels (having the highest grayscale
                    #value, as white is 255) are found using the np.where() method, where the
                    #pixels's grayscale value is equal to the maximal grayscale value
                    #(np.max(image_array_grayscale)).
                    max_pixels = np.where(image_array_grayscale == np.max(image_array_grayscale))
                    #One of the pixel "x,y" coordinates matching the highest grayscale value will
                    #be selected and stored in "max_pixel". If there were more than one pixel with
                    #that grayscale value ("len(max_pixels) > 1"), then the first one is selected.
                    if len(max_pixels) > 1:
                        max_pixel = [max_pixels[0][0], max_pixels[1][0]]
                    #If there is only one pixel with that grayscale value, then its coordinates
                    #are stored in "max_pixel".
                    else:
                        max_pixel = [max_pixels[0], max_pixels[1]]
                    #A similar approach is taken for the darkest pixels, which have the lowest
                    #grayscale value (black being 0).
                    min_pixels = np.where(image_array_grayscale == np.min(image_array_grayscale))
                    if len(min_pixels) > 1:
                        min_pixel = [min_pixels[0][0], min_pixels[1][0]]
                    else:
                        min_pixel = [min_pixels[0], min_pixels[1]]

                #The "image" is then converted to "RGBA" mode in case
                #the user has specified some colors to use in "RGBA" mode.
                #The "image_array" is overwritten with the multi-channel
                #"RGBA" numpy array.
                image = image.convert("RGBA")
                image_array = np.array(image)
                #The "image_editable" instantiation of the "Draw" class will allow
                #to modify the background image by overlaying it with the text boxes.)
                image_editable = ImageDraw.Draw(image)

                #If no colors have been specified by the user for the boxes and text containing
                #the title and author name, then the code will automatically extract the darkest
                #color from the image, which it will apply to the filled-out boxes on the cover and spine,
                #and the lightest color on the canvas, which it will assign to the text and light rectangles.
                #It will also apply lightness corrections to these colors if needed in order for the text to
                #be readily legible.
                if cover_box_color == None and cover_text_color == None:
                    #Knowing the pixel "x,y" coordinates for the pixel with the lowest
                    #grayscale value ("min_pixel"), it is possible to find it within the
                    #colored image, by indexing the "image_array" numpy array derived from it.
                    dark_color = (image_array[min_pixel[0], min_pixel[1]]).tolist()[:-1]

                    #The complementary color is determined by subtracting the RGB
                    #values from those of white (255,255,255). This tends to give
                    #more interesting color combinations for the boxes.
                    for i in range(3):
                        dark_color[i] = 255 - dark_color[i]

                    #In order to compare the darkness of different colors quantitatively, the colors are
                    #converted into their grayscale equivalents by doing the average of the three RGB values.
                    dark_color_grayscale = round(dark_color[0]/3 + dark_color[1]/3 + dark_color[2]/3)
                    #The same process as above is repeated for the lightest color on the background image,
                    #except that its complementary color is not determined.
                    light_color = (image_array[max_pixel[0], max_pixel[1]]).tolist()[:-1]

                    light_color_grayscale = round(light_color[0]/3 + light_color[1]/3 + light_color[2]/3)

                    #The "too_high" variable initialized as "False" and will be set to "True" if
                    #a R, G or B value exceeding 255 is obtained when correcting the lightness of
                    #"light_color". A normalization will then take place to bring the highest channel
                    #value to 250, while keeping the relative proportion between channel values.
                    too_high = False
                    #If the "light_color" is either white (255,255,255) or the grayscale
                    #equivalence of the RGB for "light_color" is very pale ("light_color_grayscale">250),
                    #or if "light_color_grayscale" is too dark ("light_color_grayscale" < 225) and
                    #the "dark_color_grayscale" is dark enough ("dark_color_grayscale < 125"), then
                    #every channel of "light_color" will be set to the corresponding channel of
                    #"dark_color" multiplied by two. If the highest channel of the resulting
                    #"light_color" is over 255, it will be normalized so that it equals 250, and
                    #the other channels will be decreased proportionally.
                    if ((light_color == [255,255,255] or light_color_grayscale > 250 or
                    light_color_grayscale < 225) and dark_color_grayscale < 125):
                        multiplier_light = 250/light_color_grayscale
                        for i in range(3):
                            light_color[i] = round(light_color[i] * multiplier_light)
                            if light_color[i] > 255:
                                too_high = True
                        if too_high == True:
                            normalization_factor = 250/max(light_color)
                            for i in range(len(light_color)):
                                light_color[i] = round(light_color[i] * normalization_factor)
                    #If the "light_color" is either white (255,255,255) or the grayscale
                    #equivalence of the RGB for "light_color" is very pale ("light_color_grayscale">250),
                    #or if "light_color_grayscale" is too dark ("light_color_grayscale" < 225) and
                    #the "dark_color_grayscale" is too light ("dark_color_grayscale >= 125"), then
                    #a correction factor will be applied to every channel of "dark_color", such that
                    #its grayscale equivalence reaches 125. Then, every channel of "light_color" will
                    #be set to the corresponding channel of the corrected "dark_color", multiplied by two.
                    #If the highest channel of the resulting "light_color" is over 255, it will be
                    #normalized so that it equals 250, and the other channels will be decreased proportionally.
                    elif ((light_color == [255,255,255] or light_color_grayscale > 250 or
                    light_color_grayscale < 225) and dark_color_grayscale >= 125):
                        multiplier_dark = 125/dark_color_grayscale
                        for i in range(3):
                            dark_color[i] = round(dark_color[i] * multiplier_dark)
                            light_color[i] = round(dark_color[i] * 2)
                            if light_color[i] > 255:
                                too_high = True
                        if too_high == True:
                            normalization_factor = 250/max(light_color)
                            for i in range(len(light_color)):
                                light_color[i] = round(light_color[i] * normalization_factor)
                    #If the only issue is that the grayscale equivalence of "dark_color" is too
                    #light ("dark_color_grayscale >= 125"), then a correction factor will be
                    #applied to every channel of "dark_color", such that its grayscale equivalence
                    #reaches 125.
                    elif dark_color_grayscale >= 150:
                        multiplier_dark = 125/dark_color_grayscale
                        for i in range(len(dark_color)):
                            dark_color[i] = round(dark_color[i] * multiplier_dark)

                    #The lists "light_color" and "dark_color" are
                    #converted into tuple form in order to be passed in
                    #as parameters when drawing the rectangles and writing
                    #the text onto the cover page.
                    cover_text_color = "rgb" + str(tuple(light_color))
                    cover_box_color = "rgb" + str(tuple(dark_color))

                else:
                    if cover_box_color[0] == "(":
                        cover_box_color = "rgb" + cover_box_color
                    if cover_text_color[0] == "(":
                        cover_text_color = "rgb" + cover_text_color

                #The length (in pixels) taken up by the title is determined using the
                #"textlength()" method, using the "font_title" with the default font size
                #"cover_title_size".
                title_length_pixels = image_editable.textlength(title, font_title)
                #The "cover_title_offset" variable stores the offset length in pixels required on the x axis so that the
                #title is centered within the black rectangle. The offset is calculated as the difference between the
                #middle points of the total available horizontal space and the length of the title.
                cover_title_offset = round((right_margin_cover_text-left_margin_cover_text)/2 - title_length_pixels/2)
                #The "available_horizontal_space_pixels" that is available within the
                #black rectangle is determined as the difference between
                #"right_margin_cover_text" and "left_margin_cover_text". These margins
                #are 100 pixels farther inside from the edges of the black rectangle
                #and will prevent the text from being too close to them.
                available_horizontal_space_pixels = round((right_margin_cover_text-left_margin_cover_text))
                #If the "title_length_pixels" (written using the formatting parameters specified in
                #"font_title") is above the "available_horizontal_space_pixels", then the title text
                #will be split in the same way as for the title page, and the font size will be
                #decremented by one unit in the "while" loop below until each of the split lines
                #of the title can fit within the black rectangle, down to a minimum font size of 50.
                cover_title_height = cover_title_size
                if title_length_pixels > available_horizontal_space_pixels:
                    title_words = title.split()
                    number_of_title_words = len(title_words)
                    middle_index_in_title = len(title)//2
                    character_count = 0
                    word_delimitor = None
                    for i in range(len(title_words)):
                        if character_count <= middle_index_in_title - (len(title_words[i])+1):
                            character_count += len(title_words[i])
                        else:
                            word_delimitor = i
                            break
                    first_half_words = title_words[:word_delimitor]
                    first_half_words_string = " ".join(first_half_words)
                    second_half_words = title_words[word_delimitor:]
                    second_half_words_string = " ".join(second_half_words)
                    adjusted_title_cover = first_half_words_string + "\n" + second_half_words_string

                    while cover_title_size > 50:
                        if (image_editable.textlength(first_half_words_string, font_title) >
                        available_horizontal_space_pixels or
                        image_editable.textlength(second_half_words_string, font_title) >
                        available_horizontal_space_pixels):
                            cover_title_size-=1
                            font_title = ImageFont.truetype(cover_font, cover_title_size)
                        else:
                            break
                    #If the title was split, the "cover_title_height" variable is updated to
                    #reflect that the text now spans two lines, including the spacing
                    #in-between the lines ("cover_title_line_spacing").
                    cover_title_height = 2*cover_title_size + cover_title_line_spacing

                    #The "cover_title_offset" variable stores the offset length in pixels required on
                    #the x axis so that the title is centered within the black rectangle. The carriage
                    #returns ("\n") are removed if present, as the "textlength()" method does not allow
                    #for them within the passed in string. The offset is calculated as the difference
                    #between the middle points of the total available horizontal space and the length of the
                    #longest of the two lines of the split title. Since the title has been split, the
                    #original offset is overwritten with the one reflecting the length of the split title.
                    first_half_words_string_length = (image_editable.textlength(first_half_words_string
                    .replace("\n", ""), font_title))
                    second_half_words_string_length = (image_editable.textlength(second_half_words_string
                    .replace("\n", ""), font_title))
                    cover_title_offset = (round((right_margin_cover_text-left_margin_cover_text)/2-
                    max([first_half_words_string_length, second_half_words_string_length])/2))

                #As the author name font size should be at most 75% of that of the title,
                #the initial font size is set to 75% of "cover_title_size".
                cover_author_size = round(0.75*cover_title_size)
                font_author = ImageFont.truetype(cover_font, cover_author_size)
                cover_author_height = cover_author_size
                author_length_pixels = image_editable.textlength(author, font_author)
                #The "cover_author_offset" variable stores the offset length in pixels required on the
                #x axis so that the author name (which should be smaller than the title, in principle)
                #is centered within the black rectangle. The offset is calculated as the difference
                #between the middle points of the total available horizontal space and the length of
                #the author name.
                cover_author_offset = (round((right_margin_cover_text-left_margin_cover_text)/2 -
                author_length_pixels/2))
                available_horizontal_space_pixels = round((right_margin_cover_text-left_margin_cover_text))
                if author_length_pixels > available_horizontal_space_pixels:
                    author_words = author.split()
                    number_of_author_words = len(author_words)
                    middle_index_in_author = len(author)//2
                    character_count = 0
                    word_delimitor = None
                    for i in range(len(author_words)):
                        if character_count <= middle_index_in_author - (len(author_words[i])+1):
                            character_count += len(author_words[i])
                        else:
                            word_delimitor = i
                            break
                    first_half_words = author_words[:word_delimitor]
                    first_half_words_string = " ".join(first_half_words)
                    second_half_words = author_words[word_delimitor:]
                    second_half_words_string = " ".join(second_half_words)
                    adjusted_author_cover = first_half_words_string + "\n" + second_half_words_string
                    adjusted_author = first_half_words_string + "\n" + second_half_words_string

                    while cover_author_size > 50*max_author_title_font_ratio:
                        if (image_editable.textlength(first_half_words_string, font_author) >
                        available_horizontal_space_pixels or
                        image_editable.textlength(second_half_words_string, font_author) >
                        available_horizontal_space_pixels):
                            cover_author_size-=1
                            font_author = ImageFont.truetype(cover_font, cover_author_size)
                        else:
                            break
                    cover_author_height = 2*cover_author_size + cover_author_line_spacing

                    #The "cover_author_offset" variable stores the offset length in pixels required on
                    #the x axis so that the author name (which should be smaller than the title, in
                    #principle) is centered within the black rectangle. The carriage returns ("\n") are
                    #removed if present, as the "textlength()" method does not allow for them within the
                    #passed in string. The offset is calculated as the difference between the middle points
                    #of the total available horizontal space and the length of the longest of the two lines
                    #of the split author name.
                    first_half_words_string_length = (image_editable.textlength(first_half_words_string
                    .replace("\n", ""), font_author))
                    second_half_words_string_length = (image_editable.textlength(second_half_words_string
                    .replace("\n", ""), font_author))
                    cover_author_offset = (round((right_margin_cover_text-left_margin_cover_text)/2-
                    max([first_half_words_string_length, second_half_words_string_length])/2))

                #The lowest y coordinates of the black and light rectangles are determined below by
                #adding the vertical distances of the elements above it. They add the y coordinate
                #at which the text starts to be written ("vertical_margin_cover_text") to the height
                #of the title ("cover_title_height"), the vertical spacing in-between title and author
                #name ("round(cover_spacing_title_height_ratio*cover_title_height)"), the height of
                #the author name ("cover_author_height") and finally the number of pixels matching
                #the spacing above the text on top of the rectangle (125 px).
                cover_dark_rectangle_end_y = (vertical_margin_cover_text + cover_title_height +
                round(cover_spacing_title_height_ratio*cover_title_height) + cover_author_height + 125)

                #A filled-in rectangle with rounded is drawn on the background using the
                #"rounded_rectangle()" method from the Pillow module. It's top left "x,y"
                #coordinates are "left_margin_cover_textbox", "top_margin_cover_textbox"
                #and it s bottom right "x,y" coordinates are "right_margin_cover_textbox",
                #"cover_dark_rectangle_end_y". The radius of the corners are set to 50
                #pixels for the darker and larger rectangle and 48 pixels for the smaller
                #lighter rectangle (proportional radius to the decrease in size of the rectangle).

                #The "cover_trim_width_pixels" is calculated from the variable "cover_trim_width"
                #and the know ratio of 4200 pixels per 14 inches at 300 ppi resolution. The
                #"cover_trim_width_pixels" will be used to draw a white trim around the canvas
                #to account for the non-printable area. As such, the rectangle and text containing
                #the title and author information on the front cover will be offset by that amount
                #(split evenly on either side of the rectangle), to keep the margins on either side
                #of the rectangle even despite the presence of such a white trim.

                cover_trim_width_pixels = round(cover_trim_width*4200/14)
                image_editable.rounded_rectangle([(left_margin_cover_textbox-
                round(cover_trim_width_pixels/2),top_margin_cover_textbox),
                (right_margin_cover_textbox-round(cover_trim_width_pixels/2),
                cover_dark_rectangle_end_y)], radius=50, fill=cover_box_color)
                #The lighter rectangle has vertical and horizontal dimensions
                #50 pixels smaller than the larger darker rectangle.
                image_editable.rounded_rectangle([(left_margin_cover_textbox+25-
                round(cover_trim_width_pixels/2), top_margin_cover_textbox+25),
                (right_margin_cover_textbox-25-round(cover_trim_width_pixels/2),
                cover_dark_rectangle_end_y-25)], radius=48, outline=cover_text_color, width=10)
                #If the title was too large to fit within the "available_horizontal_space_pixels",
                #it was split into two lines and will be written in light font (fill = light_text_color)
                #with centered alignment and starting at the "x,y" coordinate "left_margin_cover_text",
                #"vertical_margin_cover_text", using the "multiline_text()" method of the Pillow module
                #with the "adjusted_title_cover" string containing a carriage return "\n" after the
                #"first_half_words_string".
                if adjusted_title_cover != None:
                    image_editable.multiline_text((left_margin_cover_text +
                    cover_title_offset-round(cover_trim_width_pixels/2), vertical_margin_cover_text),
                    adjusted_title_cover, fill=cover_text_color, font=font_title, align="center",
                    spacing=cover_title_line_spacing)
                #If the title wasn't split, it will be written using the "text"() method of the Pillow module
                else:
                    image_editable.text((left_margin_cover_text + cover_title_offset
                    -round(cover_trim_width_pixels/2), vertical_margin_cover_text),
                    title, fill=cover_text_color, font=font_title, align="center")
                #A similar approach is taken for the author name, except that since it is written in smaller sized font,
                #it needs a horizontal offset ("cover_author_offset") in order to be centered. Also, the text begins at
                #a lower point in the dark rectangle, which is the "vertical_margin_cover_text" y coordinate plus the
                #height of the title "cover_title_height" and the vertical spacing in-between the title and the author
                #name ("round(cover_spacing_title_height_ratio*cover_title_height)")
                if adjusted_author_cover != None:
                    image_editable.multiline_text((left_margin_cover_text +
                    cover_author_offset-round(cover_trim_width_pixels/2),
                    vertical_margin_cover_text + cover_title_height +
                    round(cover_spacing_title_height_ratio*cover_title_height)),
                    adjusted_author_cover, fill=cover_text_color, font=font_author,
                    align="center", spacing=cover_author_line_spacing)
                else:
                    image_editable.text((left_margin_cover_text +
                    cover_author_offset-round(cover_trim_width_pixels/2),
                    vertical_margin_cover_text + cover_title_height +
                    round(cover_spacing_title_height_ratio*cover_title_height)),
                    author, fill=cover_text_color, font=font_author, align="center")

                #The rectangles for the spine are drawn in a similar way as for the title and author name,
                #except that the width depends on the number of pages in the book and the thickness of a
                #ream of paper of 500 pages, which are both provided as additional arguments by the user
                #when running the code. The width of the spine in pixels "width_of_spine_pixels" is
                #determined by multiplying the "inches_per_ream_500_pages" by the number of pages in the
                #book ("number_of_pages"), and then dividing by two (as every sheet of 8.5x11" paper will
                #result in two leaves of the book (each containing two pages) pages in the book) and then
                #by 500 to get the number of inches of thickness for the book. The number of inches is
                #then multiplied by the pixel count for the width of the Legal page in landscape mode
                #(4200 pixels at 300 ppi) and then divided by the corresponding inch measurement for
                #that width (14").
                width_of_spine_pixels = inches_per_ream_500_pages*number_of_pages/2/500*4200/14

                #A white trim of "cover_trim_width" inches in width (which is converted into pixels
                #(cover_trim_width*4200/14)) will be drawn on the outer edges of the canvas, except
                #the left side, where another similar trim will be drawn where the back cover ends,
                #enabling the user to easily cut out the excess paper from the Legal cardstock after printing.
                image_editable.rectangle([(0,0),(4200, cover_trim_width_pixels)], fill="white")
                image_editable.rectangle([(round(4200-cover_trim_width*4200/14),0),(4200, 2550)], fill="white")
                image_editable.rectangle([(0,2550-cover_trim_width_pixels),(4200, 2550)], fill="white")
                #An extra pixel (equivalent to about 1 mm) is added to the width of the white rectangle
                #on the left vertical side, to allow to cut the line while excluding the pattern on the
                #excess cardstock.
                image_editable.rectangle([(4200-round(11*4200/14+width_of_spine_pixels)-1,0),
                ((4200-round(11*4200/14+width_of_spine_pixels))+cover_trim_width_pixels, 2550)], fill="white")
                #A dark trim of color "dark_color" is drawn directly within the white border, so as to
                #harmonize the white border with the rest of the contents of the cover.
                image_editable.rectangle([((4200-round(11*4200/14+width_of_spine_pixels))+
                cover_trim_width_pixels,cover_trim_width_pixels),(4200-cover_trim_width_pixels,
                2550-cover_trim_width_pixels)], outline=cover_box_color, width = 25)

                #The "x,y" coordinates of the top left corner of the rectangle are calculated based on the
                #width of the covers of the book (14"-5.5"=8.5") and the pixel count is given using the known
                #pixel numbers for the width of a Legal page in landscape mode (4200 pixels at 300 ppi).
                #The width of the spine is then subracted in order to reach the left "x" coordinate with
                #the addition of 3 pixels to account for the space needed to fold the spine. The top "y"
                #coordinate is set at one inch from the top of the page, and the bottom "y" coordinate of
                #the bottom right corner is set at one inche from the bottom of the page (8.5"-1"=7.5").
                #The bottom right corner "x" coordinate is calculated based on the width of the covers of
                #the book (14"-5.5"=8.5") and the pixel count is determined using the Legal proportions
                #as above, with 3 pixels being subtracted to avoid spillover of the black spine onto the
                #cover page when folding the cover paper.
                image_editable.rounded_rectangle([(8.5*4200/14-width_of_spine_pixels+3,1.0*4200/14),
                (8.5*4200/14-3,7.5*4200/14)], radius=50, fill=cover_box_color)

                #The author name is initialized to take up less space on the spine. First, the name is
                #split at every space or hyphen, with inclusion of those characters as separate elements
                #in the "author_name_split" list (given the use of parentheses). Then, the names are
                #cycled through in the "for" loop and if the element isn't the last one in the list,
                #meaning that it is not the last name, and if it isn't a space or a hyphen and if its
                #length is more than 1 and the second character isn't a period, then that name is
                #initialized.
                author_name_split = re.split(r"([' '-])", author)
                for i in range(len(author_name_split)):
                    if (author_name_split[i] not in [" ", "-"] and (len(author_name_split[i]) > 1 and
                    author_name_split[i][1] != ".") and i < len(author_name_split)-1):
                        author_name_split[i] = author_name_split[i][0] + "."
                author_spine = "".join(author_name_split) + " — "

                #The "spine_string" containing the text written on the spine is assembled.
                spine_string = author_spine + title.strip()

                #Similar to what was done above, the font size of the spine
                #initialized to 100 pixels, will be optimized to the available
                #space. However, in this case both the horizontal and vertical
                #space need to be considered, as only one line of text can fit
                #onto the spine (so the string will not be split into two lines
                #as for the title and author box).
                spine_font_size = 100
                font_spine = ImageFont.truetype(cover_font, spine_font_size)

                spine_string_length_pixels = image_editable.textlength(spine_string, font_spine)

                #Similarly to the title and author box, a white rectangle 25 pixels distant from the edge
                #of the black rectangle is drawn only if the number of pages is over 300, as its presence
                #decreases the available space for the spine text.
                if number_of_pages >= 300:
                    image_editable.rounded_rectangle([(8.5*4200/14-width_of_spine_pixels+25+3,1.0*4200/14+25),
                    (8.5*4200/14-25-3,7.5*4200/14-25)], radius=round((width_of_spine_pixels
                    -50)/width_of_spine_pixels*50), outline=cover_text_color, width=10)

                    #The available space on the horizontal axis is determined by subtracting the
                    #"x" coordinate of the bottom right corner of the spine dark rectangle from
                    #that of the top left corner. 70 pixels are subtracted from that amount to
                    #account for the space between the pale rectangle vertical edges and the text.
                    available_horizontal_space_pixels = (round((8.5*4200/14-25-3)-
                    (8.5*4200/14-width_of_spine_pixels+25+3))-70)
                    #As there is one inch above and below the dark rectangle, the height of the
                    #dark rectangle is equal to the height of the Legal page in landscape mode
                    #minus two inches (8.5"-2"=6.5"). 50 pixels are subtracted to account for the
                    #margins between the edges of the dark rectangle and the lighter line, and
                    #another 70 pixels are subtracted from that amount to allow for space between
                    #the pale rectangle horizontal edges and the text.
                    available_vertical_space_pixels = 6.5*4200/14-50-70

                    #If either the length of the "spine_string" in pixels ("spine_string_length_pixels")
                    #exceeds the "available_vertical_space_pixels" or if the height of the spine font
                    #"spine_font_size" is above the "available_horizontal_space_pixels", the "spine_font_size"
                    #will be decremented until both dimensions are within range of the available space.
                    if (spine_string_length_pixels > available_vertical_space_pixels or
                    spine_font_size > available_horizontal_space_pixels):
                        while cover_title_size > 25:
                            if (image_editable.textlength(spine_string, font_spine) > available_vertical_space_pixels or
                            spine_font_size > available_horizontal_space_pixels):
                                spine_font_size-=1
                                font_spine = ImageFont.truetype(cover_font, spine_font_size)
                            else:
                                spine_string_length_pixels = image_editable.textlength(spine_string, font_spine)
                                break

                    #The offset on the x and y axis are determined by subtracting the halfpoint of
                    #either dimension of the "spine_string" from the that of the available space in
                    #the corresponding dimension of the rectangle.
                    offset_x = round(available_vertical_space_pixels/2 - spine_string_length_pixels/2)
                    offset_y = round(available_horizontal_space_pixels/2 - spine_font_size/2)

                    #The image is outputted in PNG format.
                    image.save(txt_file_name[:-4] + "(cover).png", "PNG")

                    #As text can only be written horizontally in Pillow, the image is reloaded and
                    #rotated 90 degrees clockwise in order to write the text on the spine.
                    image_rotated = (Image.open(txt_file_name[:-4] +
                    "(cover).png").convert("RGBA").rotate(90, expand = True))
                    image_rotated_editable = ImageDraw.Draw(image_rotated)

                    #The starting x and y coordinates mirror the measurements in the unrotated image.
                    #The left side of the dark rectangle is then one inch from the top of the canvas
                    #in the rotated image, with 25 pixels added to reach the light line and another 35
                    #pixels to reach the point where the text will start to be written, with the addition
                    #of the "offset_x".
                    #The top of the dark rectangle now stands 5.5 inches from the top of the canvas
                    #(the origin 0,0 being in the top left corner), with 25 pixels added to reach the
                    #lighter line, and 28 pixels to reach the point where the text will start to be
                    #written, with the addition of the "offset_y"
                    spine_text_starting_x = round(1.0*4200/14+25 + 35 + offset_x)
                    spine_text_starting_y = round(5.5*4200/14+25+3+28 + offset_y)

                    image_rotated_editable.text((spine_text_starting_x, spine_text_starting_y),
                    spine_string, fill=cover_text_color, font=font_spine, align="center")

                #If the "number_of_pages" is below 300, the white rectangle will not be drawn to allow
                #for more space for the text on a smaller spine. The margins are adjusted in consequence.
                else:
                    #The "space_offset" was determined by linear regression between a number of pages
                    #of 299 and 200, and represents the combined number of pixels on either side of the
                    #spine text, between the edges of the long sides of the spine and the spine text. That
                    #margin decreases linearly down to zero at a page count of 200, below which the
                    #"space_offset" is set to 12 pixels.
                    space_offset = round(0.71*number_of_pages-142)
                    if number_of_pages < 200:
                        space_offset = 12
                    #The available space on the horizontal axis is determined by subtracting the
                    #"x" coordinate of the bottom right corner of the spine dark rectangle from
                    #that of the top left corner. "space_offset" pixels are subtracted from that amount to
                    #account for the space between the pale rectangle vertical edges and the text.
                    #As "space_offset" effectively acts as a margin, it is subtracted from the
                    #available horizontal pixels.
                    available_horizontal_space_pixels = (round((8.5*4200/14-3)-
                    (8.5*4200/14-width_of_spine_pixels+3))-space_offset)

                    #As there is one inch above and below the dark rectangle, the height of the
                    #dark rectangle is equal to the height of the Legal page in landscape mode
                    #minus two inches (8.5"-2"=6.5"). 70 pixels are subtracted from that amount
                    #to allow for space between the pale rectangle horizontal edges and the text.
                    available_vertical_space_pixels = 6.5*4200/14-70

                    #If either the length of the "spine_string" in pixels ("spine_string_length_pixels")
                    #exceeds the "available_vertical_space_pixels" or if the height of the spine font
                    #"spine_font_size" is above the "available_horizontal_space_pixels", the "spine_font_size"
                    #will be decremented until both dimensions are within range of the available space.
                    if (spine_string_length_pixels > available_vertical_space_pixels or
                    spine_font_size > available_horizontal_space_pixels):
                        while spine_font_size > 25:
                            if (image_editable.textlength(spine_string, font_spine) >
                            available_vertical_space_pixels or
                            spine_font_size > available_horizontal_space_pixels):
                                spine_font_size-=1
                                font_spine = ImageFont.truetype(cover_font, spine_font_size)
                            else:
                                break
                        spine_string_length_pixels = image_editable.textlength(spine_string, font_spine)
                    #The offset on the x and y axis are determined by subtracting the halfpoint of
                    #either dimension of the "spine_string" from the that of the available space in
                    #the corresponding dimension of the rectangle.
                    offset_x = round(available_vertical_space_pixels/2 - spine_string_length_pixels/2)
                    offset_y = round(available_horizontal_space_pixels/2 - spine_font_size/2)

                    #The image is outputted in PNG format.
                    image.save(txt_file_name[:-4] + "(cover).png", "PNG")

                    #As text can only be written horizontally in Pillow, the image is reloaded and
                    #rotated 90 degrees clockwise in order to write the text on the spine.
                    image_rotated = (Image.open(txt_file_name[:-4] +
                    "(cover).png").convert("RGBA").rotate(90, expand = True))
                    image_rotated_editable = ImageDraw.Draw(image_rotated)

                    #The starting x and y coordinates mirror the measurements in the unrotated image.
                    #The left side of the dark rectangle is then one inch from the top of the canvas
                    #in the rotated image, with 35 pixels to reach the point where the text will start
                    #to be written, with the addition of the "offset_x".
                    #The top of the dark rectangle now stands 5.5 inches from the top of the canvas
                    #(the origin 0,0 being in the top left corner), with "space_offset/2" pixels to reach
                    #the point where the text will start to be written, with the addition of the "offset_y"
                    spine_text_starting_x = round(1.0*4200/14 + 35 + offset_x)
                    spine_text_starting_y = round(5.5*4200/14 + (space_offset/2) + offset_y)

                    image_rotated_editable.text((spine_text_starting_x, spine_text_starting_y),
                    spine_string, fill=cover_text_color, font=font_spine, align="center")

                #The image is once more outputted in PNG format, thus
                #overwriting the unrotated version.
                image_rotated.save(txt_file_name[:-4] + "(cover).png", "PNG")

#If the user hasn't provided a title, author and valid file name,
#the following error message will be displayed on screen.
else:
    print("\nPlease provide the title, author and TXT file name as additional " +
    "arguments (with a space in-between each argument) when running the code.")
    print('For example: python3 gutenbooks.py "author:H. G. Wells" '
    + '"title:The Time Machine" "number_of_pages:330" "inches_per_ream_500_pages:2"')
