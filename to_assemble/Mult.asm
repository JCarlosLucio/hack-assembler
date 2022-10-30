// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Computes R2 = R0 * R1 
// R2 = R1 + ... + R1  
//
// START
//    n = R0
//    i = 1
//    sum = 0
// LOOP:
//    if i > n goto STOP
//    sum = sum + R1
//    i = i + 1
//    goto LOOP
// STOP
//    R2 = sum

@R0
D=M
@n // n = RAM[0]
M=D

@R1
D=M
@num
M=D // num = RAM[1]

@i
M=1 // i = 1

@sum
M=0 // sum = 0

@R2
M=0

(LOOP)
  @i
  D=M
  @n
  D=D-M
  @STOP
  D;JGT // if i > n goto STOP

  @sum
  D=M
  @num
  D=D+M
  @sum
  M=D     // sum = sum + num
  @i
  M=M+1   // i = i + 1
  @LOOP
  0;JMP



(STOP)
  @sum
  D=M
  @R2
  M=D // RAM[2] = sum

(END)
  @END
  0;JMP

