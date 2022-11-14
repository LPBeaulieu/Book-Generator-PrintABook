# PrintABook
This app allows you to generate printer-friendly versions of TXT books from Project Gutenberg!

![PrintABook Thumbnail](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/PrintABook%20Thumbnail.jpg)
<h3 align="center">PrintABook</h3>
<div align="center">
  
  [![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3.0-brightgreen.svg)](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/LICENSE)
  [![GitHub issues](https://img.shields.io/github/issues/LPBeaulieu/Book-Generator-PrintABook)](https://github.com/LPBeaulieu/Book-Generator-PrintABook)
  [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
  [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
  [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
  
</div>

---

<p align="left"> <b>PrintABook</b> is a tool enabling you to generate printer-friendly versions of TXT books from Project Gutenberg, complete with the cover image! </p>
- Simply follow the steps below to set up your system, and then add the text file (.txt) and cover background JPEG image to your working folder for the Project Gutenberg book that you wish to output in printable format before running the Python code.
- The instructions below will show you how to cusomize the formatting elements of the Rich Text Document (RTF) output file, so that your book is exactly how you want it to be.
    <br> 
</p>

## 📝 Table of Contents
- [Dependencies / Limitations](#limitations)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## ⛓️ Dependencies / Limitations <a name = "limitations"></a>
- This Python code automatically parses the TXT file of a book from the Project Gutenberg collection in order to remove certain elements, such as the table of contents and formats it such as to be readily printable on 8 1/2" by 11" paper in booklet duplex mode. Please make sure to read the Project Gutenberg license before printing or distributing printed copies of the books: https://www.gutenberg.org/policy/license.html.
- The code follows a certain set of rules in order to format the TXT files, which are only applicable to novels with conventional chapter headings such as "Chapter 1. / Chapter I. / Chapter One. / 1. / I. / One." (with or without the periods). You should therefore inspect the RTF file to ensure that it was formatted adequately before printing. Many formatting elements aren't dealt with, such as footnotes, so it's up to you to make the necessary adjustments to the generated RTF document. However, the code does a good job of taking care of most of the nitty-gritty details for you. 

## 🏁 Getting Started <a name = "getting_started"></a>

The following instructions will be provided in great detail, as they are intended for a broad audience and will
allow to run a copy of <b>PrintABook</b> on a local computer. 

The instructions below are for Windows operating systems, but the code should run nicely on Linux and Mac-OS as well.

<b>Step 1</b>- Hold the "Shift" key while right-clicking in your working folder and select "Open PowerShell window here" to access the PowerShell in your working folder and install <b>NumPy</b>  and <b>Pillow</b> (Required Python modules to generate the cover image) using the following command:
```
py -m pip install NumPy --upgrade Pillow
```

<b>Step 2</b>- You're now ready to use <b>PrintABook</b>! 🎉

## 🎈 Usage <a name="usage"></a>

<b>Step 1</b>- First, <b>remove any text</b>, if present, from the TXT file <b>in-between the Project Gutenberg opening tag</b> (for example: "*** START OF THE PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***") <b>and the book title</b> ("The Adventures of Sherlock Holmes"). <b>Similarly, remove any text in-between the author name</b> ("Arthur Conan Doyle") <b>and the table of contents heading</b> ("Contents"). This will prevent superfluous text from appearing on your title page. If the table of contents doesn't have a heading, go ahead and remove it by hand, as the code relies on the presence of such a heading to automatically take out the table of contents.

<b>Step 2</b>- Hold the "Shift" key while right-clicking in your working folder and select "Open PowerShell window here" to access the PowerShell in your working folder, and <b>enter the following command, adjusted to your own TXT file</b>:
```
py -m printabook.py "title:Book title as found in TXT file" "author:Author name as found in TXT file"
```
In a few seconds, your RTF file will be generated in your working folder. For a list of additional arguments that you can pass in when running the Python code in order to change the formatting of the RTF document (font, font size, line spacing, etc.) please consult the PDF document located in the github repository.

<b>Step 3</b>- Review the RTF document to correct any formatting elements that weren't covered by the Python code (such as footnotes) and save it either as an ".odt" (in LibreOffice) or ".docx" (in MS Word) file. <b>Take note of the number of pages in the document</b>, as you will enter this when running the same code once again in order to allow the code to determine how wide the spine should be for your book.

<b>Step 4</b>- You can modify the header in LibreOffice in order for it to not show up on the title page, and to display the author name on the left pages and the book title on the right pages by following the steps illustrated in the figures below:

![Format Header 1](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Format%20Header-Image%201.png)<hr>
Left-click on the number within the header in order to display the "Page Header" blue button. Click on it and then select "Format Header...". <br><br>


![Format Header 2](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Format%20Header-Image%202.png)<hr>
Remove the check marks in the boxes "Same content on left and right pages" and "Same content on first page". Then, delete the number "1" in the title page and move on to page two. 
<br><br>

![Format Header 3](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Format%20Header-Image%203.png)<hr>
Enter the author name (in caps) after the number, with a four-space divider in-between. Select left-alignment to bring the header to the left corner of the page. Move on to page three. 
<br><br>

![Format Header 4](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Format%20Header-Image%204.png)<hr>
Enter the author name (in caps) before the number, with a four-space divider in-between. Select right-alignment to bring the header to the right corner of the page.
<br><br>

<b>Step 4</b>- <b>Save your file</b> either as an ".odt" (in LibreOffice) or ".docx" (in MS Word) file.

<b>Step 5</b>- <b>Print your book</b> on your home printer by following the steps shown below. I recommend printing on perforated paper (5 1/2" horizontal perforation from bottom, in the middle of the page), as you then wouldn't need to purchase a guillotine cutter to cut your pages after printing. Also, after cutting the pages in half, you should stack the pages and place some heavy books on them, as they may be bowed after printing.

![Printing Instructions](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/Printing%20Instructions.png)<hr>
First, select the "brochure" printing mode. Second, click on the "Properties" button. Third, select the "Print on Both Sides" option, and "Flip on Short Edge".
 
<b>Step 6</b>- <b>Run the Python code once again</b>, this time including the number of pages in the book, so that the code can determine the width of the spine. You can simply press the "up" arrow in the PowerShell in order to automatically enter the same command as before. You will then add another parameter: the width/thickness of a ream of 500 pages of the paper you will be printing on, as in the example below. 

```
py -m printabook.py "title:The Adventures of Sherlock Holmes" "author:Arthur Conan Doyle" "number_of_pages:331" "inches_per_ream_500_pages:2"
```

<b>Step 7</b>- The code will take a bit longer to run this time, as it is generating the PNG image file for the book cover. You need to print this image on Legal (14" x 8 1/2") cover cardstock (65 lbs to 80 lbs recommended) and then cut the excess paper. The book cover is framed with a white border, which must not be removed. This white border accomodates the non-printable area of most printers (about a quarter of an inch, or  6.4 mm). You can adjust the width of the white border to the specifications of your printer by entering another parameter "cover_trim_width:" followed by the measurement in inches or "cover_trim_width_cm:" for centimeters (with 0 being no border, and you would then need to cut at the solid line, while leaving the line within the cover).

<b>Step 8</b>- Assemble your book using an acid-free Polyvinyl Acetate (PVA) glue. You can use large 2" binder clips to hold the pages in place while you apply the glue to the spine. Two applications of glue may be needed for good adhesion, and the cover could then be glued on afterwards.

<br><b>And that's it!</b> You're now ready to convert your favorite Project Gutenberg book TXT files into your very own printable books formatted just the way you like them! Now dollop some glue onto the spine, slap on the cover, let it dry under some books and you'll soon be able to curl up around your handcrafted book! 🎉📖
  
  
## ✍️ Authors <a name = "author"></a>
- 👋 Hi, I’m Louis-Philippe!
- 👀 I’m interested in natural language processing (NLP) and anything to do with words, really! 📝
- 🌱 I’m currently reading about deep learning (and reviewing the underlying math involved in coding such applications 🧮😕)
- 📫 How to reach me: By e-mail! LPBeaulieu@gmail.com 💻


## 🎉 Acknowledgments <a name = "acknowledgments"></a>
- <b>Shout out to the talented Rajesh Misra for the gorgeous illustration</b> featured on the cover (https://www.publicdomainpictures.net/en/view-image.php?image=214080&picture=floral-pattern-background-843) 
- Hat tip to [@kylelobo](https://github.com/kylelobo) for the GitHub README template!



<!---
LPBeaulieu/LPBeaulieu is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
