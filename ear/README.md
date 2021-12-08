# KAB-Semestralka
How-To Use Instructions

This is a project that I used for a semestral project at my collage. I hope it helps someone, at some point. You can use this program to brute-force a number of ciphers 
(Ceaser, Affine, Password Substitution, Vignere, Table, Column Transposition and Double Transposition ciphers, to be exact). The program is written in python and is prepared to be used on ciphered English texts, though you can use it on any language if you supply the project with the proper word-list txt file. Keep in mind, however, that if you plan to use a non-latin alphabet for the text, you would first have to heavilly modefy some lines in every class, pretty much.

The result is always a sorted file that has text that is most likely to be correctly deciphered at its top. The line also includes information about the cipheres properties, such as the shift, password, etc.


STEPS of Usage:

1) Fist, install all neccicary Dependencies, found in requirements.txt (not all of the mentioned requirements are neccicary, but some of them are and it's just easier to download everything)
2) Add or remove or change the tasks. A task is a cipher text you want to brute force
3) Prepare the main method
  Set the path variable to the projects folder. Then for each task you want to break, do the following steps:
    1) replace the filename variable with your chosen filename, that you want the decoded possibilities to be outputed
    2) replace the task variable with your proper task (keep it lower case, or replace the alphabets to match the case of the task)
    3) run the decipher method from the appropriate cipher class (Table ciphers are the decipher method in ColumnTransposition class, decipherPassword is the method to use on Column Transposition ciphers and decipherDouble is used on Double transposition ciphers. These are the only exceptions). If you suspect a combination of two ciphers were used, use the method bruteForceAllMethods to try breaking all of the combinations. The results will include which cipher methods were used, and you will still get the cipher details information for both of them
 
 Hope this helps!
 
 
 - Levyaton
