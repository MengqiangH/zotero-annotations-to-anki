# zotero-annonations-to-anki
This script is able to convert zotero annonations formed by 'Zotero PDF Translate' plugin into anki cards.

**Requirements:**
1. Installation of Zotero
2. Installation of Anki
3. Installation of the 'Zotero PDF Translate' plugin provided by windingwind in Zotero (can be downloaded here: https://github.com/windingwind/zotero-pdf-translate#readme)
4. Installation of Python

**How to use:**

After the prepration of software installation.
You can use the plugin 'Zotero PDF Translate' to generate some annotations.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/5568829c-d063-4863-9697-99a8a1217e2c)

Then, you should use the "add notes from annotations" provided by Zotero.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/09b2ffc4-27b5-4a8f-afb3-a9ae0b085e42)

And open this notes in the right-window of Zotero.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/8278904c-e93e-4bda-b0a0-318a668269ab)

Next, you should copy all of the contents in the note to a '.txt' file named '2.txt' in this path 'C:/Users/hu/Desktop'.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/ffd08325-204e-4a8f-b16c-f956be3fa06b)  ![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/446cff02-15ad-4d91-845a-8949d61d0018)

Now, you can run the Python script and a '.txt' file named 'anki.txt' will be creaed in the same path 'C:/Users/hu/Desktop'.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/23a3968c-f877-4ac4-97d9-e262ac052ebf)

Next, open the Anki and import the 'anki.txt' file using the specific Notetype, please use pipe as the field separator.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/7662fcc7-92ad-46a8-bd06-91d84723e182)

After that, the annotations have been created as crads in the Anki; furthermore, there are two links to the Item in Zotero and the annotation in the Zotero PDF, respectively.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/23aaac05-d976-4089-a3fa-d2d8c5dff75c)
![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/6788d524-d8c8-4455-8c1f-3f3839ee0284)

Besides, if you want to add some personal thoughts, please firsly marked the original sentense or words by the 'Zotero PDF Translate' plugin in Zotero. Then you can edit the comment on this annotation. After pressing the space bar twice, youu can add the personal thoughts before "~" in the  annotation.

![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/abe3863e-6351-4359-93af-5de650d4d2bd)

In the Anki, you can see your personal thoughts in the back of the card.
![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/918dd22a-0d1a-41fd-8d19-d7e5b3e3401c)
![image](https://github.com/MengqiangH/zotero-annonations-to-anki/assets/47101970/19f3711a-2b5b-415c-9ce1-d8b70264160a)

Last but not least, all of the file name or path used should be reivesed according to your machine.









