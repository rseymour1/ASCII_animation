[ASCII art Repository](https://www.asciiart.eu/)
[Amazing Star Wars ASCII Animation](https://www.asciimation.co.nz/index.php#)

Unfortunately, I had to remove the artists' initials from the ASCII art pieces 
to be able to train this model. 
As such, I'd like to recognize several of them here: Joan Stark(JGS), 
Morfina(MRF), llizard(ejm), Donovan Bake, Hayley Jane Wakenshaw(HJW), 
Linda Ball, sk, cjr, Shanaka Dias(SND), Maija Haavisto(MH), David Berner, 
Max Strandberg, Veronica Karlsson, Keely, Seal, Mark Harms
This is the code made to create a neural network that has the purpose of 
generating novel, abstract ASCII art. 
This is different than simple image-based ASCII art that takes an image and uses 
ASCII characters to represent it. 
Abstract ASCII art is not based on a specific image, but rather is simply trying 
to use ASCII characters to represent the original object. 

Here is the difference represented:

Abstract
```
{
 /\_/\
( o.o )
 > ^ <
}
```

Image-based
```
{
""""""""""""""""""""""""""`^^^"""""`````^^^^^"""""""""""^`;~-?+;""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""^"lI;"`^^^""^^^^""""""""""^""^^':]|){|r~^"""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""")t){~l,`^``^^""^^^^^"^"^,"^"l]ft-ii?r]`"""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""^!f\}11}_<<>l,`^""","^"^!11[1uu(>;:>}|]`"""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""`>f|[?)jnrt[i!+-?]1}~il<]|trz/_:,^>]?<`"^"""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""^]-,I-1\)+~]?_}(/{--[]+i><+++~I,":<[i""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""^i+_>iiI~{{({{fj[{|)t(--iIlII:!?~<1-^"""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""`i{+ii_<>r{}t|zj(\_)f?[1_>i!lI;i_?|1"^""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""^I~_il+})~}/)jtcr1]?](jUvuf}[{-!,,I-|~^""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""^^l?{)1{(Cw8Yutuvft\},)zYd/jntt)){~I,:+~"""^"""""""""""""""""""""""""""""""
""""""""""""""""""""""""",!]|)[+<!?/c_jC(n{-}~[0({jt|//)]+_]+!:;l,^"""""""""""""""""""""""""""""""""
"""""""""""""""""""""""^"~](u1{)}]]{)(}vx-?_]tzxvXxf\1]_ili~_>l:,""","""""""""""""""""""""""""""""":
""""""""""""""""""""""^,_11|r\[][-}(trt/zJnJC{])rx|{?_~>i~+>!lI;:,""""""""""""""""""""""""""""""""":
""""""""""""""""""""",>1\|((ruf|)[[-]]+I;?Jr;`">>_-_il>?[}]~ii!I,`^""""""""""""""""""""""""^","",",:
"""""""""""""""""""""i\t)||{(||rxr/[~+i^'.trl,^:,;III:::;i<><i::>(>^"""""""""""""""""""""",,,:::::::
"""""""""""""""""""",]\nXr/t/1}{1tj[??+~_-<><<<~i>i!" .`,;!ii+/Jqoi`,"""""""""""""""""""""::::::::::
"""""""""""""^^^^^",I{/tcdhqqwJuuLwOOCvr|>`...`;-|t\fYQ0wpwZOmOUq| ^^","""""""""""""""^":,::::::::::
"""""^^^^",,,,,,,,,:-\ft)fp&#ohooaba*aaZCQUvXvvQbo*ao#MM8&%$8k0C[ ^``^""""""""""""""",,,::::::::::::
"^""",,,,,:::::::::>)|\\\(|L*ohkbqb*Wdhhk**#*aoM&*aaaakdhkdpkqqO-^^```^"""""""""""""":::::::::::::::
,,::::::::::::::::;]/fjj|/fnmqqdpqdbW#bkddpqwdaMoboohaahkbOLmmZOz!`````^""""""""""""":::::::::::::::
::::::::::::::::Il_\rnnf)\vLLZmqkoo*#*oodwwpddpddMm0ooooohdQQmwZ0f:```^"""""""""""""":::::::::::::::
:::::::::;;IIlll!>)ttjj()r0QOwmmOdmhhbkqdOQOOCqpzZUzkkaakbdmOmZmmzI````^^""^^^^^^^^"":::::::::::::::
:::::;;Ill!!!iii>-|/ff()(zZOOZmOQLJYXwbOOQUUCmkhwZpkkkbkdmZOOwwppYl`"^^,,,",,,,,,,,,,:::::::::::::::
:;Ill!II!!ii><~~_{/frf)((umpQL0000QQCYLpOLYXZOZwkhbdddddddpdbahZvt))?+?_>I::::::::,,"",:;:::::::::::
l!!lll!ii><~~++?(/juzn||fvQmwqqmmqpwCJXZ&8%hOCQQ0qkahkdddk*aZu}>!>+}||\)?l,::::::>++_?-+<:::::::::;;
lll!ii>>~~++++?)\juCwY\fuXCOwbo**M*kwQYuQW*0CCLmmpbdwQLYXqOt_!llIi<>+>>-]!,:::;::~?{{[}[]I,;Illll!!!
iii>><~++++_-[{)|x0pL\(fvXCmh*M8W&B%#dmmbM*adwwqpp0urjftfu1]+!i!>!ii!!~?[~I;:;lI:<-}\\)(|{+I!lllllll
>>>~~++++_--?})(xZhwt1|f)?[{(rcJwZvzJpkbqZmwkwCXuuzuj\)}}[]?~I:I;,i?>l!?1}<!lllll~]][}}}?~|_!>>><~+-
<<~+++_--??[)|/cqhop/)|r|<>:,,:l[zr|1|fuu/\rnnfrffn[___??_+~<i~]>i1|]~<~]}_~<<<~~+__---_--?[?]}}{1))
+++_-?]][[{\tfXb*#Mou(\/rt+ll!!~)/t(}]])/|txuuuurf}?[<~?}}?[]++->-jf}}1}[}--]]]]?-???][]]][][]???[]}
_-???[[[}1\/rCdhkh*aU/xvzCXt-~<+}1}}??<{f/rxvXznx/]f1::i>-)|)11]<i~[\/ff\1][?-_+______-]-_-_--_++__+
?-_+++--}\/xUphkh*##ZtxYQmOvxzj\|)}]}_:IxrtunvXxf{{r_+)/junuvur|]<!l]f\ft\{){?-_+_++_+++++~++__+++_-
~?(fuYLOujuXmh*MWWWWw\trrnXJZwu(||(({[}+(x{t1?)[[?!-YWw/zftjxxjt}+<l:_|t/\[1f}??]]-+--?}]?]+~~+~+~~-
Q*%@$$$hncXLd*M&B%WMkxrr|tvUCz\|//1[rp*8xYn-\]_-[> tOUUr|tu/)??]?+~ilI{f\|)}\f[~+~+--+~~~_??_++~>i~+
Xk&8WWhrrvJwk*WB$$@%*n|rf/rzYrtxx)[?_|J0vQdi[j\//1>[[~?]{1-~ilI;liiii!-xnjj/1rt]??+>><<<~<~~~+~~+--~
>_{\ucxxjxYd*#&%BBMoqxtrffuYr\trn(???>>++;i)xJznucf{I:>>!;;I:::,,,;l!l~jr//(+jU|{1})\1}1{-_-++<>>>ii
uLZbqcrttrYp%8o&&dZ0Ourxxzuut(\jf}iI;::"``^<(u->-|>;:"^^^"",:llI::,;II-(cr+?]0pz|]-1[]/r|][++-??){?_
JLdoYvzvnuYb%&kdwLJLOYxvzYzvu|(jf?~>I,,^^^,";?1][>```^``^^`^",:;II::Ii[|zUUCmkkZu){[[]+-++_><<i++++[
~~[rUnLJzmOwpbqmQJU0wZuuczJzULzff([?-~!;;:;I^ `][```'``^"^`````^":,:I<_]}xh&#hp0Xt(xu\?(]~--_1[?~>i>
++_-)1\)(unjuzUO0UJOmZYxuuvYCwZn\1~II<>li>ii!l;>1+!l;;:,"````````,,;li><>I?mhhpOYx[]}[[(tf1[~[[}}]})
>>~+??-_?-[{)|\jY0OmQZOrxnnvUQQUj]I",,:;l>++-?~ili!!I,^`````````^,:II!i!l;iL#abwUux)_>_}}]~}{>~]??|\
~~??-+~++~?}{[{)(zOOQwLfnjxuuXvxn/?iI,`'''`^:Ilill;,^```````````":;IIllIII}wWWopQcvuj[}-><+-~~i++I;l
~_++<~+~<_--]?+_?/UOZqUfuxrruzXjtrnt1-+<;,,,":::::;;;:"^^```````,::::::;;~XqoWW*pJcux\x)-{}++?}_i?[+
++i+_~~~_++]-+~><-)YwbOrrrffncXu\)|t/{|\?++>ilI:,"^^^^^`````````"""",:Ii+)Lkh&WMaZJzf)(r)+{>ii_-~]]}
+~<i><~_-~+iIlii<??_/mazxxrxucYLc)??-~~<>>iI:,^`^````````````````^"::;l<_|Cpkobhad0Yu}~-}11)[ll!!<~_
><<!~-_>!lII;::li!>~[cpxxzrnzvcYUuj)-~>l:,:,,,^```````'```''``'^:,::;Ili>-JbdbkkhbZYvf??[[]}~i-l!~>!
;Ii<-_>illl;::!+_+++-]uxnr\cx|jttrzz(]_~>i;::,""````^^"^^^,,^"<?+-]{))1[[}/ZhbkkhhwCUcr1?~>i+][{]]~<
i>i>~I>>~+>;::il:!_?~+~~[-+[)|xuxYdkCcvcnj/\\{}}?]}[?}})([<+?tUrtj[~/r/}]1?1Jhka##apZ0LYn|11]+1}?--?
III!_>I:ll,:,::,,I><:::,:",">__1|uuXvxcxfrux/||()\\)}]+<~+<l[ZQ||]li{?~I^IIi\mkbhdqZwmOOpmOn}~~i:lII
;I!I;I;:,:,,::,,I!~~!II;,,;;l>i!>~i:lI;lIi>>li~~-~>illI:;Il;;]+!!lii!;;I;;:l_1|/}!+><<i-){_::``,,:;!
}
```