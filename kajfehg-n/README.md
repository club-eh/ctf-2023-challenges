# kAjfehg n

<i>Medium Reverse Engineering Challenge by Spaghetti</i>

[Challenge Archive](https://ctf-2023.clubeh.ca/challenges#kAjfehg%20n-379911899)

### Challenge Question

Our forensics team ripped this firmware off a strange proprietary electronic device that was confiscated from a t3l0s member. Can you figure out what it does?


<details> 
  <summary>Hints</summary>
  <ol>
   <li>The language that the file is written in is Uyjhmn n</li>
  </ol>
</details>

<details> 
  <summary>Answer Summary</summary>
  &emsp;<b>Trace the following:</b>
<br>&emsp;&emsp;;program starts here. create 2/3 variables. assign the ascii value `b` to v1
<br>&emsp;&emsp;DECLARE THE NEW VARIABLE v1
<br>&emsp;&emsp;DECLARE THE NEW VARIABLE v2
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 98 TO THE OPEN VARIABLE
<br>
<br>&emsp;&emsp;;print `club`
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 99
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 108
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 117
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER
<br>
<br>&emsp;&emsp;;create the last variable `nine` used for tricks later
<br>&emsp;&emsp;DECLARE THE NEW VARIABLE nine
<br>&emsp;&emsp;OPEN THE VARIABLE nine
<br>&emsp;&emsp;ASSIGN 9 TO THE OPEN VARIABLE
<br>
<br>&emsp;&emsp;;print `eh`
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 101
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 104
<br>&emsp;&emsp;JUMP TO label1 IF v1 IS GREATER THAN nine
<br>
<br>&emsp;&emsp;; label for `4ge` the first char is incorrect but will merge to give a partially correct output
<br>&emsp;&emsp;; nine=161 v1=117 v2=103
<br>&emsp;&emsp;DEFINE THE NEW LABEL label7
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -65 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;117+-65=52
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;4
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 51 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;52+51=103
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;g
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -2 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;103+-2=101
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;e
<br>&emsp;&emsp;ADD nine TO THE OPEN VARIABLE		;161+101=262
<br>&emsp;&emsp;JUMP TO label4 IF nine IS GREATER THAN v1	;goes to fake path for fake last 9 chars `_h34jej65`
<br>&emsp;&emsp;JUMP TO label2 IF  nine IS EQUAL TO nine	;goes to `wrong` path and ends
<br>
<br>&emsp;&emsp;;prints '}' and exits
<br>&emsp;&emsp;DEFINE THE NEW LABEL end
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 125
<br>&emsp;&emsp;END THIS PROGRAM
<br>
<br>&emsp;&emsp;;first jump or label, prints `{` and jumps to the next block
<br>&emsp;&emsp;DEFINE THE NEW LABEL label1
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 114 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD nine TO THE OPEN VARIABLE
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER
<br>&emsp;&emsp;JUMP TO label2 IF v1 IS GREATER THAN v2	;never jumps
<br>&emsp;&emsp;JUMP TO label3 IF v1 IS LESS THAN v2	;correct jump
<br>
<br>&emsp;&emsp;; fake path for last 8 chars
<br>&emsp;&emsp;DEFINE THE NEW LABEL label6
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 103 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;53+51=104
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;h
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -53 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;104+-53=51
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;3
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;51+1=52
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;4
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 54 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;52+54=106
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;j
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -5 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;106+-5=101
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;e
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 5 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;101+5=106
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;j
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -52 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;106+-52=54
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;6
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;br>ASSIGN -1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;54+-1=53
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;5
<br>&emsp;&emsp;JUMP TO end IF nine IS EQUAL TO nine
<br>
<br>&emsp;&emsp;;fake jump prints `wrong`
<br>&emsp;&emsp;DEFINE THE NEW LABEL label2
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 98 TO THE OPEN VARIABLE
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 21 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;98+21=119
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;w
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -5 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;119+-5=114
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;r
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -3 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;114+-3=111
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;o
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;111+-1=110
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;n
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -7 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;110+-7=103
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;g
<br>&emsp;&emsp;JUMP TO end IF v1 IS GREATER THAN v2;correct condition, but wrong answer in all cases
<br>&emsp;&emsp;JUMP TO label4 IF v1 IS LESS THAN v2;never happens
<br>
<br>&emsp;&emsp;;second jump (real) prints `e50t3r1c` v1=98 v2=123 nine=9
<br>&emsp;&emsp;DEFINE THE NEW LABEL label3
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 3 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;98+3=101
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;e
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -48 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;101+-48=53
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;5
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -5 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;53+-5=48
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;0
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 68 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;48+68=116
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;t
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -65 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;116+-65=51
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;3
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 63 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;51+63=114
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;r
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -65 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;114+-65=49
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;1
<br>&emsp;&emsp;OPEN THE VARIABLE nine
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;nine changes here `nine=58`
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 50 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;49+50=99
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;c
<br>&emsp;&emsp;JUMP TO label4 IF v2 IS LESS THAN v1;correct path
<br>&emsp;&emsp;JUMP TO label2 IF v1 IS EQUAL TO v1 ;wrong path in all cases
<br>
<br>&emsp;&emsp;; correct path for last 8 chars. nine=153 v1=101 v2=103
<br>&emsp;&emsp;DEFINE THE NEW LABEL label9
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -2 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;103+-2=101
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;e
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 5 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;101+5=106
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;j
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -52 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;106+-52=54
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;6
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;54+-1=53
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;5
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 51 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;53+51=104
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;h
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -53 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;104+-53=51
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;3
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 1 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;51+1=52
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;4
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 54 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;52+54=106
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;j
<br>&emsp;&emsp;JUMP TO end IF nine IS EQUAL TO nine;go to end and print `}` to finish the flag
<br>
<br>&emsp;&emsp;; label for `age` this is a correct path nine=161 v1=117 v2=103
<br>&emsp;&emsp;DEFINE THE NEW LABEL label8
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -6 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;103+-6=97
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;a
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN 6 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;97+6=103
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;g
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN -2 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;103+-2=101
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;
<br>&emsp;&emsp;JUMP TO label2 IF v1 IS GREATER THAN v2		;goes to `wrong` path and ends
<br>&emsp;&emsp;JUMP TO label4 IF nine IS GREATER THAN v2	;goes to correct path for last 9 chars `_ej65h34j`
<br>
<br>&emsp;&emsp;; jump for `_` jump conditions at end depend on progress through program
<br>&emsp;&emsp;DEFINE THE NEW LABEL label4
<br>&emsp;&emsp;PRINT THE CHARACTER WITH THE ASCII VALUE 95
<br>&emsp;&emsp;JUMP TO label5 IF v1 IS GREATER THAN v2		;path for `l4nguag3`
<br>&emsp;&emsp;JUMP TO label9 IF nine IS GREATER THAN v1	;correct path for last 8 chars `ej65h34j`
<br>&emsp;&emsp;JUMP TO label6 IF v1 IS EQUAL TO v1			;path for fake last 8 chars `h34jej65`
<br>
<br>&emsp;&emsp;; jump for "l4ngu" v1(open)=99 v2=49 nine=58
<br>&emsp;&emsp;DEFINE THE NEW LABEL label5
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 50 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD nine TO THE OPEN VARIABLE		;58+50=108
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;l
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -56 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;108+-56=52
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;4
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 58 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;52+58=110
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;n
<br>&emsp;&emsp;OPEN THE VARIABLE v2
<br>&emsp;&emsp;ASSIGN -7 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v1 TO THE OPEN VARIABLE			;110+-7=103
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;g
<br>&emsp;&emsp;OPEN THE VARIABLE v1
<br>&emsp;&emsp;ASSIGN 14 TO THE OPEN VARIABLE
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE			;103+14=117
<br>&emsp;&emsp;PRINT THE OPEN VARIABLE'S CHARACTER	;u
<br>&emsp;&emsp;OPEN THE VARIABLE nine
<br>&emsp;&emsp;ADD v2 TO THE OPEN VARIABLE					;nine changes here `nine=161`
<br>&emsp;&emsp;JUMP TO label8 IF nine IS GREATER THAN v1	;correct path
<br>&emsp;&emsp;JUMP TO label7 IF nine IS EQUAL TO nine 	;this will never happen
</details>

<details> 
  <summary>Flag</summary>
  &emsp;<b>clubeh{e50t3r1c_l4nguage_ej65h34j}</b>
</details>
