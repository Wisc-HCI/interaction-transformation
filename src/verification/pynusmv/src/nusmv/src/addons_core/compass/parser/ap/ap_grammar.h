/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TOK_TRUEEXP = 258,
     TOK_FALSEEXP = 259,
     TOK_ATOM = 260,
     TOK_NUMBER_EXP = 261,
     TOK_NUMBER_REAL = 262,
     TOK_NUMBER_FRAC = 263,
     TOK_NUMBER = 264,
     TOK_NUMBER_WORD = 265,
     TOK_SEMI = 266,
     TOK_CONS = 267,
     TOK_RCB = 268,
     TOK_LCB = 269,
     TOK_RB = 270,
     TOK_RP = 271,
     TOK_LP = 272,
     TOK_COLON = 273,
     TOK_ESAC = 274,
     TOK_CASE = 275,
     TOK_SELF = 276,
     TOK_TWODOTS = 277,
     TOK_NOT = 278,
     TOK_AND = 279,
     TOK_XNOR = 280,
     TOK_XOR = 281,
     TOK_OR = 282,
     TOK_IFF = 283,
     TOK_IMPLIES = 284,
     TOK_COMMA = 285,
     TOK_AA = 286,
     TOK_EE = 287,
     TOK_AG = 288,
     TOK_EG = 289,
     TOK_AF = 290,
     TOK_EF = 291,
     TOK_AX = 292,
     TOK_EX = 293,
     TOK_RELEASES = 294,
     TOK_TRIGGERED = 295,
     TOK_UNTIL = 296,
     TOK_SINCE = 297,
     TOK_MMAX = 298,
     TOK_MMIN = 299,
     TOK_BUNTIL = 300,
     TOK_ABG = 301,
     TOK_ABF = 302,
     TOK_EBG = 303,
     TOK_EBF = 304,
     TOK_OP_FUTURE = 305,
     TOK_OP_GLOBAL = 306,
     TOK_OP_NEXT = 307,
     TOK_OP_ONCE = 308,
     TOK_OP_HISTORICAL = 309,
     TOK_OP_NOTPRECNOT = 310,
     TOK_OP_PREC = 311,
     TOK_GE = 312,
     TOK_LE = 313,
     TOK_GT = 314,
     TOK_LT = 315,
     TOK_NOTEQUAL = 316,
     TOK_EQUAL = 317,
     TOK_RROTATE = 318,
     TOK_LROTATE = 319,
     TOK_RSHIFT = 320,
     TOK_LSHIFT = 321,
     TOK_SETIN = 322,
     TOK_UNION = 323,
     TOK_DIVIDE = 324,
     TOK_TIMES = 325,
     TOK_MINUS = 326,
     TOK_PLUS = 327,
     TOK_MOD = 328,
     TOK_CONCATENATION = 329,
     TOK_SMALLINIT = 330,
     TOK_NEXT = 331,
     TOK_BIT = 332,
     TOK_DOT = 333,
     TOK_LB = 334,
     TOK_EXTEND = 335,
     TOK_UNSIGNED = 336,
     TOK_SIGNED = 337,
     TOK_WORD1 = 338,
     TOK_BOOL = 339
   };
#endif
/* Tokens.  */
#define TOK_TRUEEXP 258
#define TOK_FALSEEXP 259
#define TOK_ATOM 260
#define TOK_NUMBER_EXP 261
#define TOK_NUMBER_REAL 262
#define TOK_NUMBER_FRAC 263
#define TOK_NUMBER 264
#define TOK_NUMBER_WORD 265
#define TOK_SEMI 266
#define TOK_CONS 267
#define TOK_RCB 268
#define TOK_LCB 269
#define TOK_RB 270
#define TOK_RP 271
#define TOK_LP 272
#define TOK_COLON 273
#define TOK_ESAC 274
#define TOK_CASE 275
#define TOK_SELF 276
#define TOK_TWODOTS 277
#define TOK_NOT 278
#define TOK_AND 279
#define TOK_XNOR 280
#define TOK_XOR 281
#define TOK_OR 282
#define TOK_IFF 283
#define TOK_IMPLIES 284
#define TOK_COMMA 285
#define TOK_AA 286
#define TOK_EE 287
#define TOK_AG 288
#define TOK_EG 289
#define TOK_AF 290
#define TOK_EF 291
#define TOK_AX 292
#define TOK_EX 293
#define TOK_RELEASES 294
#define TOK_TRIGGERED 295
#define TOK_UNTIL 296
#define TOK_SINCE 297
#define TOK_MMAX 298
#define TOK_MMIN 299
#define TOK_BUNTIL 300
#define TOK_ABG 301
#define TOK_ABF 302
#define TOK_EBG 303
#define TOK_EBF 304
#define TOK_OP_FUTURE 305
#define TOK_OP_GLOBAL 306
#define TOK_OP_NEXT 307
#define TOK_OP_ONCE 308
#define TOK_OP_HISTORICAL 309
#define TOK_OP_NOTPRECNOT 310
#define TOK_OP_PREC 311
#define TOK_GE 312
#define TOK_LE 313
#define TOK_GT 314
#define TOK_LT 315
#define TOK_NOTEQUAL 316
#define TOK_EQUAL 317
#define TOK_RROTATE 318
#define TOK_LROTATE 319
#define TOK_RSHIFT 320
#define TOK_LSHIFT 321
#define TOK_SETIN 322
#define TOK_UNION 323
#define TOK_DIVIDE 324
#define TOK_TIMES 325
#define TOK_MINUS 326
#define TOK_PLUS 327
#define TOK_MOD 328
#define TOK_CONCATENATION 329
#define TOK_SMALLINIT 330
#define TOK_NEXT 331
#define TOK_BIT 332
#define TOK_DOT 333
#define TOK_LB 334
#define TOK_EXTEND 335
#define TOK_UNSIGNED 336
#define TOK_SIGNED 337
#define TOK_WORD1 338
#define TOK_BOOL 339




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 83 "ap_grammar.y"
{
  node_ptr node;
}
/* Line 1529 of yacc.c.  */
#line 221 "ap_grammar.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE parser_ap_lval;

