<h1>Huffman</h1>

File compression is widely used in modern computing systems. For example, many image and video formats, such a JPEG or MP3, are compressed. Data, document and program files are also often compressed; for example using the zip format. Compressing these files allows them to be stored, streamed, downloaded and/or transferred more efficiently.

There are two primary forms of compression, lossy compression and lossless compression. With lossy compression, information is discarded during the compression process. Thus, the full original file cannot be reproduced exactly from the compressed file. In the case of images or video the loss of information is often acceptable because the compressed image or video looks nearly indistinguishable from the original but takes less storage or arrives more quickly. However, in the case of data, document files or programs, lossy compression would destroy the file contents and is thus unacceptable. A lossless compression scheme must be used for these types of files.

Huffman coding is a lossless data compression scheme. Huffman Coding is not usually used directly to compress files in modern systems, however, it or a related technique is used as part of many commonly used lossy and lossless compression schemes (e.g. zip, JPEG and MP3).

<h3>Sample Input</h3>
F<br/>
!"#$%&'()*+,-./0123456789:;< =>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

<h3>Sample Output</h3>
 :1<br/>
!:1<br/>
":1<br/>
#:1<br/>
$:1<br/>
%:1<br/>
&:1<br/>
':1<br/>
(:1<br/>
):1<br/>
*:1<br/>
+:1<br/>
,:1<br/>
-:1<br/>
.:1<br/>
/:1<br/>
0:1<br/>
1:1<br/>
2:1<br/>
3:1<br/>
4:1<br/>
5:1<br/>
6:1<br/>
7:1<br/>
8:1<br/>
9:1<br/>
::1<br/>
;:1<br/>
<:1<br/>
=:1<br/>
>:1<br/>
?:1<br/>
@:1<br/>
A:1<br/>
B:1<br/>
C:1<br/>
D:1<br/>
E:1<br/>
F:1<br/>
G:1<br/>
H:1<br/>
I:1<br/>
J:1<br/>
K:1<br/>
L:1<br/>
M:1<br/>
N:1<br/>
O:1<br/>
P:1<br/>
Q:1<br/>
R:1<br/>
S:1<br/>
T:1<br/>
U:1<br/>
V:1<br/>
W:1<br/>
X:1<br/>
Y:1<br/>
Z:1<br/>
[:1<br/>
\:1<br/>
]:1<br/>
^:1<br/>
_:1<br/>
`:1<br/>
a:1<br/>
b:1<br/>
c:1<br/>
d:1<br/>
e:1<br/>
f:1<br/>
g:1<br/>
h:1<br/>
i:1<br/>
j:1<br/>
k:1<br/>
l:1<br/>
m:1<br/>
n:1<br/>
o:1<br/>
p:1<br/>
q:1<br/>
r:1<br/>
s:1<br/>
t:1<br/>
u:1<br/>
v:1<br/>
w:1<br/>
x:1<br/>
y:1<br/>
z:1<br/>
{:1<br/>
|:1<br/>
}:1<br/>
~:1