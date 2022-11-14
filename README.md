# PrintABook
This app allows you to generate printer-friendly versions of TXT books from Project Gutenberg!

![Image RTF basic mode](https://github.com/LPBeaulieu/Typewriter-OCR-TintypeText/blob/main/TintypeText%20basic%20rtf%20mode%20screenshot.jpg)
<h3 align="center">Tintype¶Text</h3>
<div align="center">
  
  [![License: AGPL-3.0](https://img.shields.io/badge/License-AGPLv3.0-brightgreen.svg)](https://github.com/LPBeaulieu/Book-Generator-PrintABook/blob/main/LICENSE)
  [![GitHub issues](https://img.shields.io/github/issues/LPBeaulieu/Book-Generator-PrintABook)](https://github.com/LPBeaulieu/Book-Generator-PrintABook)
  [![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
  [![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
  [![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
  
</div>

---

<p align="left"> <b>PrintABook</b> is a tool enabling you to allows you to generate printer-friendly versions of TXT books from Project Gutenberg, complete with the cover image! </p>
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
- This Python code automatically parses the TXT file of a book from the Project Gutenberg collection in order to remove certain elements, such as the table of contents and to format it in order to be readily printable on 8 1/2" by 11" paper in booklet duplex mode. Please make sure to read the Project Gutenberg license before printing or distributing printed copies of the books: https://www.gutenberg.org/policy/license.html.
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

<b>Step 1</b>- First, <b>remove any text</b>, if present, from TXT file <b>in-between the Project Gutenberg opening tag</b> (for example: "*** START OF THE PROJECT GUTENBERG EBOOK THE ADVENTURES OF SHERLOCK HOLMES ***") <b>and the book title</b> ("The Adventures of Sherlock Holmes"). <b>Similarly, remove any text in-between the author name</b> ("Arthur Conan Doyle") <b>and the table of contents heading</b> ("Contents"). This will prevent the text from appearing on your title page. If the table of contents doesn't have a heading, go ahead and remove it by hand, as the code relies on the presence of the heading to take it out of the TXT file.

<b>Step 2</b>- Hold the "Shift" key while right-clicking in your working folder and select "Open PowerShell window here" to access the PowerShell in your working folder, and <b>enter the following command, adjusted to your own TXT file</b>:
```
py -m printabook.py "title:Book title as found in TXT file" "author:Author name as found in TXT file"
```
In a few seconds, your RTF file will be generated in your working folder. For a list of additional arguments that you can pass in when running the Python code in order to change the formatting of the RTF document (font, font size, line spacing, etc.) please consult the PDF document located in the github repository.

<b>Step 3</b>- Review the RTF document to correct any formatting elements that weren't covered by the Python code (such as footnotes) and save it wither as an ".odt" (in LibreOffice) or ".docx" (in MS Word) file. <b>Take note of the number of pages in the document<\b>, as you will enter this when running the same code once again in order to let the code know how wide the spine should be for your book.

<b>Step 4</b>- You can modify the header in LibreOffice in order for it to not show up on the title page, and to display the author name on the left pages and the book title on the right pages by .
        
<br><b>And that's it!</b> You're now ready to convert your favorite Project Gutenberg book TXT files into your very own printable books formatted just the way you like them! Now dollop some glue on the spine, slap on the cover, let it dry under some books and you'll soon be able to curl up around a nice book! 🎉📖
  
  
## ✍️ Authors <a name = "author"></a>
- 👋 Hi, I’m Louis-Philippe!
- 👀 I’m interested in natural language processing (NLP) and anything to do with words, really! 📝
- 🌱 I’m currently reading about deep learning (and reviewing the underlying math involved in coding such applications 🧮😕)
- 📫 How to reach me: By e-mail! LPBeaulieu@gmail.com 💻


## 🎉 Acknowledgments <a name = "acknowledgments"></a>
- Hat tip to [@kylelobo](https://github.com/kylelobo) for the GitHub README template!




<!---
LPBeaulieu/LPBeaulieu is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
