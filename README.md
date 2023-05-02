# PrintABook
This app allows you to generate printer-friendly versions of book TXT files from Project Gutenberg!

![PrintABook Thumbnail](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/PrintABook%20Thumbnail.jpg)
<h3 align="center">PrintABook</h3>
<div align="center">
  
  [![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3.0-brightgreen.svg)](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/LICENSE)
  [![GitHub issues](https://img.shields.io/github/issues/LPBeaulieu/Book-Generator-PrintABook)](https://github.com/LPBeaulieu/Book-Generator-PrintABook)
  [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
  [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
  [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
  
</div>

---

<p align="left"> <b>PrintABook</b> is a tool enabling you to generate printer-friendly versions of book TXT files from Project Gutenberg, complete with the cover image! </p>

- Simply follow the steps below to set up your system, and then add the text file (.txt) and cover background JPEG image to your working folder for the Project Gutenberg book that you wish to output in printable format, before running the Python code.

- The instructions below will show you how to customize the formatting elements of the Rich Text Document (RTF) output file, so that your book is exactly how you want it to be.
    <br> 
</p>

## 📝 Table of Contents
- [Dependencies / Limitations](#limitations)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>
- This Python code automatically parses the TXT file of a book from the Project Gutenberg collection in order to remove certain elements, such as the table of contents, and formats it such as to be readily printable on 8 1/2" by 11" paper in brochure duplex mode. Please make sure to <b>read the Project Gutenberg license</b> before printing or distributing printed copies of the books: https://www.gutenberg.org/policy/license.html.
- The code follows a certain set of rules in order to format the TXT files, which are only applicable to novels with conventional chapter headings such as "Chapter 1. / Chapter I. / Chapter One. / 1. / I. / One." (with or without the periods). You should therefore <b>inspect the RTF file to ensure that it was formatted adequately before printing</b>. Many formatting elements aren't dealt with, such as footnotes, so it's up to you to make the necessary adjustments to the generated RTF document. However, the code does a good job of taking care of most of the nitty-gritty details for you.
- The code for cover image generation was optimized on books having <b>at least 100 pages</b>, so you could combine a few shorter books by the same author if you like.
- The Python code automatically removes any instances of three or more spaces within the TXT file. If certain paragraphs were <b>centered</b> through the inclusion of spaces, that <b>formatting would be lost</b> in the RTF file. However, the code automatically adds tabs at the start of every new paragraph, so the overall text should look nice.


## 🏁 Getting Started <a name = "getting_started"></a>

The following instructions will be provided in great detail, as they are intended for a broad audience and will
allow to run a copy of <b>PrintABook</b> on a local computer. You can also view the YouTube version of the instructions at the following link: https://www.youtube.com/watch?v=t8ogF_J91_s&list=PL8fAaOg_mhoFZ-qInXAn91k2g8x4bOn4f. 

The instructions below are for Windows operating systems, but the code should run nicely on Linux and Mac-OS as well.

<b>Step 1</b>- Hold the "Shift" key while right-clicking in your working folder and select "Open PowerShell window here" to access the PowerShell in your working folder. Then, install <b>NumPy</b>  and <b>Pillow</b> (Required Python modules to generate the cover image) by entering the following command:
```
py -m pip install NumPy --upgrade Pillow
```

<b>Step 2</b>- You're now ready to use <b>PrintABook</b>! 🎉


## 🎈 Usage <a name="usage"></a>

<b>Step 1</b> In your working folder, you need to have <b>exactly one of each of the following</b>: a <b>True Type Font file (.ttf)</b> for the cover text font (when you set up your system, the "Baskerville" TTF file will be included in your working folder by default), a <b>JPEG image</b> for the cover illustration and a <b>text file</b> for your Project Gutenberg book. 

- First, <b>remove any text</b>, if present, from the TXT file <b>in-between the Project Gutenberg opening tag</b> (for example: "*** START OF THE PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***") <b>and the book title</b> ("The Adventures of Sherlock Holmes"). 
- <b>Similarly, remove any text in-between the author name</b> ("Arthur Conan Doyle") <b>and the table of contents heading</b> ("Contents"). This will prevent superfluous text from appearing on your title page. If the table of contents doesn't have a heading, go ahead and remove it by hand, as the code relies on the presence of such a heading to automatically take out the table of contents.
 
<b>Step 2</b>- Hold the "Shift" key while right-clicking in your working folder and select "Open PowerShell window here" to access the PowerShell in your working folder, and <b>enter the following command, adjusted to your own TXT file</b>:
```
py -m printabook.py "title:Book title as found in TXT file" "author:Author name as found in TXT file"
```
You may choose to include line breaks at certain points in the title by including at least two successive spaces in-between the words that you want to be split on different lines. Make sure that those extra spaces are present both in the TXT file and the "title:Book title as found in TXT file" argument in the Python call.

In a few seconds, your RTF file will be generated in your working folder. For a list of additional arguments that you can pass in when running the Python code, in order to change the formatting of the RTF document (font, font size, line spacing, etc.) and cover image, please consult Figures 1 to 3 below. <b>Should you just want to print books without worrying about all these details, simply run the code with the default settings and you will get nice results, allowing you to move on to step 3</b>.

![Additional Formatting Parameters 1](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/PrintABook%20Additional%20Parameters%20Image%201.png)<hr> <b>Figure 1.</b> The image above lists some of the formatting parameters that can be altered when generating the RTF document. Any measurements may be reported either in inches or centimeters (with or without decimals, but without units). The number of lines doesn't have a unit either. Make sure to include a space in-between the different arguments passed in when you run the Python code and to include the quotes.
<br><br>


![Additional Formatting Parameters 2](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/PrintABook%20Additional%20Parameters%20image%202.png)<hr> <b>Figure 2.</b> This figure lists the other formatting parameters that can be altered when generating the RTF document. Once again, simply pass in the number after the colon (":") symbol, without units. In the case of the font, enter the name of the font (ex: "font:Arial"). For spacing in-between paragraphs, measurements are in points, as for the font size. So a spacing of 6 points should be half of the height of a font size of 12. By default, the forward slashes are changed to smallcaps formatting delimiters. In order to keep the forward slashes unchanged, simply enter "keep_forward_slashes" as an additional argument. 
<br><br>


![Additional Formatting Parameters 3](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/PrintABook%20Settings-Instructions-Image-3.png)<hr> <b>Figure 3.</b> The image above lists the different formatting parameters that can be altered when generating the cover image. If ever you change the font of the cover text from Baskerville to some other font, the horizontal and vertical text alignment on the spine might be off center. In order to bring the text to the right by a certain amount of pixels within the spine dark rectangle, simply pass in the number of pixels (without units) after "pixels_from_left_cover_spine:", where a negative value would bring the text to the left. Similarly, the text can be moved up by a certain number of pixels by including the number after "pixels_from_bottom_cover_spine:", where a negative value would bring the text down. In order center the text on the front cover title box, add the number of pixels after "pixels_from_top_cover_title_box:", where a positive value would bring the text down and a negative value would shift the text up, and "pixels_from_left_cover_title_box:", where a positive value would shift the text to the right and a negative value would bring the text to the left.   
The cover image may be generated in greyscale tones for printing in black and white. The cover box color would then automatically be set as black and the text color would be light grey. By default, color images are generated, so you would need to pass in the argument "greyscale" in order to generate a greyscale image. For color images, the color of the boxes is set by default as the complementary color of the darkest color, and then adjusted automatically so that it is dark enough to render the text nicely. The text color is by default the lightest color found in the image. However, both of these may be set as any color of your choice, using either the HTML color names or RGB values.

The largest possible title font size on the front cover may be modified by entering the desired font size (in pixels, the default value being 125 px) after the "cover_title_font_size:" argument. Similarly, the largest possible author size on the front cover may be set by adding the font size after the "cover_author_font_size:" argument, the default value being 94 px in this case. The code will then scale the text down to the largest font size that fits within the front cover box. The same can be done with the spine font size, by entering the desired font size the default value being 100 px), after the "spine_font_size:" argument.

Finally, the spine text may be customized to include your own text. By default, the spine text contains the initialled author name, with only the last name written in full, followed by an em dash and then the book title. To enter your custom spine text, enter it as an additional argument when running the code, preceded by "spine_text:".
<br><br><br>


<b>Step 3</b>- Review the RTF document to correct any formatting elements that weren't covered by the Python code (such as footnotes) and save it either as an ".odt" (in LibreOffice) or ".docx" (in MS Word) file. <b>Take note of the number of pages in the document</b>, as you will enter this when running the same code once again in order to allow the code to determine how wide the spine should be for your book.

<b>Step 4</b>- You can modify the header in LibreOffice in order for it to not show up on the title page, and to display the author name on the left pages and the book title on the right pages by following the steps illustrated in the figures below:

![Format Header 1](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Format%20Header-Image.png)<hr>
<b>Figure 4.</b> Left-click on the number within the header in order to display the "Page Header" blue button. Click on it and then select "Format Header...". 
<br><br><br>


![Format Header 2](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Format%20Header-Image%202.png)<hr>
<b>Figure 5.</b> Remove the check marks in the boxes "Same content on left and right pages" and "Same content on first page". Then, delete the number "1" in the title page and move on to page two. 
<br><br><br>


![Format Header 3](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Format%20Header-Image%203.png)<hr>
<b>Figure 6.</b> Enter the author name (in caps) after the number, with a four-space divider in-between. Select left-alignment to bring the header to the left corner of the page. Move on to page three. 
<br><br><br>


![Format Header 4](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Format%20Header-Image%204.png)<hr>
<b>Figure 7.</b> Enter the book title (in caps) before the number, with a four-space divider in-between. Select right-alignment to bring the header to the right corner of the page.
<br><br><br>

<b>Step 5</b>- <b>Save your file</b> either as an ".odt" (in LibreOffice) or ".docx" (in MS Word) file.

<b>Step 6</b>- <b>Print your book</b> on your home printer by following the steps shown below. I recommend placing some heavy books on the printed pages, as they may be bowed after printing. You should also consider purchasing a guillotine stack paper cutter to cut your pages in half after printing and to trim the margins once the book is bound, in order to get clean edges. 

![Printing Instructions](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Printing%20Instructions.png)<hr>
<b>Figure 8.</b> First, select the "brochure" printing mode. Second, click on the "Properties" button. Third, select the "Print on Both Sides" option, and "Flip on Short Edge".
<br><br><br>
 
 
<b>Step 7</b>- <b>Run the Python code once again</b>, this time including the number of pages in the book, so that the code could determine the width of the spine. You can simply press the "up" arrow in the PowerShell in order to automatically enter the same command as before. You will then add another parameter: the width/thickness of a ream of 500 pages of the paper you will be printing on, as in the example below. 

```
py -m printabook.py "title:The Adventures of Sherlock Holmes" "author:Arthur Conan Doyle" "number_of_pages:331" "inches_per_ream_500_pages:2"
```

<b>Step 8</b>- The code will take a bit longer to run this time, as it is generating the PDF book cover file. You need to print this image on Legal (14" x 8 1/2") cover cardstock (65 lbs to 80 lbs recommended) and then cut off the excess paper. The book cover is framed with a white border, which must not be removed. This white border accommodates the non-printable area of most printers (about a quarter of an inch, or  6.4 mm). You can adjust the width of the white border to the specifications of your printer by entering another parameter "cover_trim_width:" followed by the measurement in inches or "cover_trim_width_cm:" for centimeters (with 0 being no border, and you would then need to cut at the solid line, while leaving the line within the cover). The Figures 9 to 12 describe how to print the cover PDF file in <b>Foxit PDF Reader</b>.

![Cover Printing Instructions 1](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Printing%20Cover%201.png)<hr>
<b>Figure 9.</b> Open the book cover PDF file in <b>Foxit PDF Reader</b> and select "Print" in the "File" menu. Click on the "Page Setting" button in the bottom left corner of the window. Then, select "Legal" from the "Page Size" drop-down menu. 
<br><br><br>


![Cover Printing Instructions 2](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Printing%20Cover%202.png)<hr>
<b>Figure 10.</b> Also in the "Page Setting" window, bring all of the "Page Margins" down to zero and click on "OK".
<br><br><br>


![Cover Printing Instructions 3](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Printing%20Cover%203.png)<hr>
<b>Figure 11.</b> Click on the "Properties" button next to your printer and select "Legal" in the "Paper Size" drop-down menu. Click "OK" to exit the window.
<br><br><br>


![Cover Printing Instructions 4](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/Printing%20Cover-4.png)<hr>
<b>Figure 12.</b> Finally, if needed, adjust the "Scale" to 24% in the "Custom scale" option and click on the "OK" button.
<br><br><br>



<b>Step 9</b>- Assemble your book using an acid-free Polyvinyl Acetate (PVA) glue. You can use large 2" binder clips to hold the pages in place while you apply the glue to the spine. At least two applications of glue are recommended for good adhesion, and the cover could then be glued on afterwards. The images below provide guidance in assembling your book.

![1-General Setup](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/1-%20General%20Setup.jpg)<hr>
<b>Figure 13.</b> Some paper or cardstock strips should line the side where you will apply the binding clips (on both sides of the book), to avoid damaging the paper. You will require some wax paper or parchment paper (here muffin tin parchment paper liners) to lay on the book before placing heavy books on it. This will prevent the glue from adhering to the books or the blotting paper that you will place over the parchment paper. Also, you will need an old paintbrush or a foam brush in order to apply the PVA glue to the spine. Please make sure to wash the brush with soapy water right after you are done, so that you could use it for more binding projects afterwards. Also, it's a good idea to have a damp cloth available to clean up any spills or glue on your hands while you work.
<br><br><br>


![1-Sanding the Spine Edges, Part 1](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/1-Sanding%20the%20edges%20(part%201).jpg)<hr>
<b>Figure 14.</b> You could optionally sand the spine edges to give a cleaner look after gluing on the cover. I used some very fine P220 grit sandpaper. <br><br><br>

![1-Sanding the Spine Edges, Part 2](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/1-Sanding%20the%20edges%20(part%202).jpg)<hr>
<b>Figure 15.</b> When sanding the spine edges, make sure to wear the appropriate personal protective equipment, as it produces some paper dust. <br><br><br>

![2-Fanning Out the Pages](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/2-%20Fanning%20Out%20the%20Pages.jpg)<hr> 
<b>Figure 16.</b> In order to increase the surface area exposed to the application of glue, it is recommended to fan out the pages using a large plastic container as a support. Apply an even layer of PVA glue onto the pages with your brush. When done, turn the book and fan out the spine pages in the other direction, using the same plastic container as a support. Apply some glue the same way and then let the pages stand upright. Press the pages together to encourage good adhesion.   
<br><br><br>


![3-Assembling the Sandwitch (Part 1)](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/3-%20Assembling%20the%20Sandwich%20(Part%201).jpg)<hr> <b>Figure 17.</b> Lay the book flat on some blotting paper, with some parchment paper covering both sides of the spine. 
<br><br><br>


![4-Assembling the Sandwitch (Part 2)](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/4-%20Assembling%20the%20Sandwich%20(Part%202).jpg)<hr> <b>Figure 18.</b> Place another sheet of blotting paper over the parchment paper, and then lay some heavy books on your binding project. This will allow the book to dry relatively flat, with the moisture from the glue reaching the blotting paper.  
<br><br>


![5-General Setup for Cover Assembly](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/1-Applying%20cover%20general%20setup.jpg)<hr> 
<b>Figure 19.</b> The image above shows the tools needed to add the cover to your book. Use scissors or other more precise cutting tools to remove the excess cardstock, while leaving the white trim, as shown in the image. There is an extra 1/64 inch (or 0.5 mm) of white space where you need to cut along the background, so you don't need to cut too close to the background on the leftover cardstock. A pencil will be used later to figure out where to fold the cover on either side of the spine. A bone folder tool may be useful when folding, but is not strictly necessary. A flat-tip paintbrush will help you apply the PVA glue more precisely. 
<br><br><br>


![6-Tracing Spine Outline](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/2-Drawing%20the%20spine%20contour.jpg)<hr> 
<b>Figure 20.</b> Use the pencil to trace the outline of the dark spine rectangle on the back of the cardstock cover, while holding it up against a light source to see through it. This will enable you to line up the ruler and crease the paper to get the folds on the spine. 
<br><br><br>

![10-Folding the Spine](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/2-Placing%20the%20ruler.jpg)<hr> 
<b>Figure 21.</b> Lay the ruler about 1/64 - 1/32 inch (0.5 - 1 mm) on the outer side of the pencil line, and carefully lift the other side of the cardstock to make a fold on one side of the spine. You can use a bone folder to make the fold crisper afterwards. 
<br><br><br>

![10-Folding the Spine](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/2-Folding%20the%20cover.jpg)<hr> 
<b>Figure 22.</b> Be vigilant when folding covers printed with laser toner, which tends to flake off when rubbed. If possible, try to fold right before the edge to avoid scraping the toner, as shown in the next image. Furthermore, I recommend using inkjet printers to print the spines of books with more than around 200 pages (using 20 lb 8 1/2" x 11" copy paper), as thicker books will result in the toner on the spine to crack when being opened, thus reducing the legibility of the spine text. When printing book covers with inkjet printers, you would need to apply a sealer to make the cover waterproof and increase its durability. <br><br><br>

![7-First Fold Result](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/3-First%20fold%20result.jpg)<hr>
<b>Figure 23.</b> Here are the results for the first fold. Note that the fold is right before the edge of the spine dark rectangle. Repeat the procedure for the other fold. 
<br><br><br>

![10-Measure "cover_extra_cm"](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/6-Measure%20cover_extra_cm.jpg)<hr> 
<b>Figure 24.</b> This is a good time to place the bound pages in your folded cover and ensure that the sizing is adequate. If you won't be using a guillotine stack page cutter to even out any discrepancies, you might want to print your cover again with some adjustments made to its page width. Simply measure the length of the overhanging bound pages relative to the cover (either in inches or centimeters, in decimal form) and enter that number as an additional parameter (preceded by "cover_extra_inches:" or "cover_extra_cm:" when running the Python code. For example, if the bound pages are 2 mm longer than the cover on both sides of the book, you would then enter "cover_extra_cm:0.2" as an additional argument. Should the measurements be uneven on both sides, it is likely that you didn't fold the cover exactly the same distance from the spine on both sides and you could then just take the average between the two measurements and input it as above.  
<br><br>


![11-Apply glue onto the spine](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/7-Applying%20glue%20on%20spine.jpg)<hr> 
<b>Figure 25.</b> Apply some PVA glue on the back side of the spine with your paintbrush and then add another coat of glue onto the spine of the bound pages to ensure good contact between cover and pages. 
<br><br><br>


![11-Apply glue onto the spine](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/8-Assembling%20the%20book.jpg)<hr> 
<b>Figure 26.</b> Line up the bound pages on top of the glue on the cover, using the folds to guide you. Carefully adjust the alignment before applying too much downwards pressure on the pages. Then fold the cover pages around the book and gently tap the spine on your working surface. Smooth the spine with your fingers and place the finished book under some other books as done previously to ensure that the book dries flat. 
<br><br><br>


![12-Stack of bound books](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/10-Stack%20of%20books.jpg)<hr>
<b>Figure 27.</b> Here's a display of my first handbound books! There's certainly room for improvement, but given that I used perforated paper with perforations in the middle of the 8 1/2" x 11" pages that were somewhat uneven, I think that the books are quite decent! For best results, I would recommend carefully lining up the pages so that the spine is perfectly flat and then trimming the margins using a guillotine stack page cutter (which I didn't have access to) after your project is done.
<br><br><br>


![13-Stack of bound books](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Github%20Page%20Images/11-Book%20Reading%20Experience.jpg)<hr> 
<b>Figure 28.</b> Most importantly, the resulting book reads like... well a book!
<br><br><br>


<b>And that's it!</b> You're now ready to convert your favorite Project Gutenberg book TXT files into your very own printable books formatted just the way you like them! Now dollop some glue onto the spine, slap on the cover, let it dry under some books and you'll soon be able to curl up around your handcrafted book! 🎉📖
  
  
## ✍️ Authors <a name = "author"></a>
- 👋 Hi, I’m Louis-Philippe!
- 👀 I’m interested in natural language processing (NLP) and anything to do with words, really! 📝
- 🌱 I’m currently reading about deep learning (and reviewing the underlying math involved in coding such applications 🧮😕)
- 📫 How to reach me: By e-mail! louis.philippe.bonhomme.beaulieu.1@gmail.com 💻


## 🎉 Acknowledgments <a name = "acknowledgments"></a>
- <b>Shout out to the talented Rajesh Misra for the gorgeous illustration</b> featured on the cover (https://www.publicdomainpictures.net/en/view-image.php?image=214080&picture=floral-pattern-background-843) 
- Hat tip to [@kylelobo](https://github.com/kylelobo) for the GitHub README template!



<!---
LPBeaulieu/LPBeaulieu is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
