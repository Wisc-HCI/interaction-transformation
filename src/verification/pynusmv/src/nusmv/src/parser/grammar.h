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
     TOK_CONSTRAINT = 258,
     TOK_MAXU = 259,
     TOK_MINU = 260,
     TOK_ABU = 261,
     TOK_EBU = 262,
     TOK_AU = 263,
     TOK_EU = 264,
     TOK_CONTEXT = 265,
     TOK_PROCESS = 266,
     TOK_MODULE = 267,
     TOK_NAME = 268,
     TOK_COMPUTE = 269,
     TOK_LTLSPEC = 270,
     TOK_CTLSPEC = 271,
     TOK_SPEC = 272,
     TOK_INVAR = 273,
     TOK_TRANS = 274,
     TOK_INIT = 275,
     TOK_ARRAY_DEFINE = 276,
     TOK_DEFINE = 277,
     TOK_IVAR = 278,
     TOK_FROZENVAR = 279,
     TOK_VAR = 280,
     TOK_PSLSPEC = 281,
     TOK_CONSTANTS = 282,
     TOK_JUSTICE = 283,
     TOK_COMPASSION = 284,
     TOK_FAIRNESS = 285,
     TOK_INVARSPEC = 286,
     TOK_ASSIGN = 287,
     TOK_ISA = 288,
     TOK_SEMI = 289,
     TOK_CONS = 290,
     TOK_OF = 291,
     TOK_RCB = 292,
     TOK_LCB = 293,
     TOK_RB = 294,
     TOK_RP = 295,
     TOK_LP = 296,
     TOK_TWODOTS = 297,
     TOK_EQDEF = 298,
     TOK_SELF = 299,
     TOK_COLON = 300,
     TOK_ESAC = 301,
     TOK_CASE = 302,
     TOK_COMPID = 303,
     TOK_COMPWFF = 304,
     TOK_CTLWFF = 305,
     TOK_LTLPSL = 306,
     TOK_LTLWFF = 307,
     TOK_NEXTWFF = 308,
     TOK_SIMPWFF = 309,
     TOK_INCONTEXT = 310,
     TOK_WORD = 311,
     TOK_REAL = 312,
     TOK_INTEGER = 313,
     TOK_BOOLEAN = 314,
     TOK_ARRAY = 315,
     TOK_WORD1 = 316,
     TOK_BOOL = 317,
     TOK_WAWRITE = 318,
     TOK_WAREAD = 319,
     TOK_COUNT = 320,
     TOK_WTOINT = 321,
     TOK_WSIZEOF = 322,
     TOK_WRESIZE = 323,
     TOK_SWCONST = 324,
     TOK_UWCONST = 325,
     TOK_EXTEND = 326,
     TOK_UNSIGNED = 327,
     TOK_SIGNED = 328,
     TOK_TRUEEXP = 329,
     TOK_FALSEEXP = 330,
     TOK_ATOM = 331,
     TOK_NUMBER_EXP = 332,
     TOK_NUMBER_REAL = 333,
     TOK_NUMBER_FRAC = 334,
     TOK_NUMBER = 335,
     TOK_NUMBER_WORD = 336,
     TOK_QUESTIONMARK = 337,
     TOK_NOT = 338,
     TOK_AND = 339,
     TOK_XNOR = 340,
     TOK_XOR = 341,
     TOK_OR = 342,
     TOK_IFF = 343,
     TOK_IMPLIES = 344,
     TOK_COMMA = 345,
     TOK_AA = 346,
     TOK_EE = 347,
     TOK_AG = 348,
     TOK_EG = 349,
     TOK_AF = 350,
     TOK_EF = 351,
     TOK_AX = 352,
     TOK_EX = 353,
     TOK_RELEASES = 354,
     TOK_TRIGGERED = 355,
     TOK_UNTIL = 356,
     TOK_SINCE = 357,
     TOK_MMAX = 358,
     TOK_MMIN = 359,
     TOK_BUNTIL = 360,
     TOK_ABG = 361,
     TOK_ABF = 362,
     TOK_EBG = 363,
     TOK_EBF = 364,
     TOK_OP_FUTURE = 365,
     TOK_OP_GLOBAL = 366,
     TOK_OP_NEXT = 367,
     TOK_OP_ONCE = 368,
     TOK_OP_HISTORICAL = 369,
     TOK_OP_NOTPRECNOT = 370,
     TOK_OP_PREC = 371,
     TOK_GE = 372,
     TOK_LE = 373,
     TOK_GT = 374,
     TOK_LT = 375,
     TOK_NOTEQUAL = 376,
     TOK_EQUAL = 377,
     TOK_RROTATE = 378,
     TOK_LROTATE = 379,
     TOK_RSHIFT = 380,
     TOK_LSHIFT = 381,
     TOK_SETIN = 382,
     TOK_UNION = 383,
     TOK_DIVIDE = 384,
     TOK_TIMES = 385,
     TOK_MINUS = 386,
     TOK_PLUS = 387,
     TOK_MOD = 388,
     TOK_CONCATENATION = 389,
     TOK_SMALLINIT = 390,
     TOK_NEXT = 391,
     TOK_BIT = 392,
     TOK_DOT = 393,
     TOK_LB = 394,
     TOK_MIRROR = 395,
     TOK_PREDSLIST = 396,
     TOK_PRED = 397
   };
#endif
/* Tokens.  */
#define TOK_CONSTRAINT 258
#define TOK_MAXU 259
#define TOK_MINU 260
#define TOK_ABU 261
#define TOK_EBU 262
#define TOK_AU 263
#define TOK_EU 264
#define TOK_CONTEXT 265
#define TOK_PROCESS 266
#define TOK_MODULE 267
#define TOK_NAME 268
#define TOK_COMPUTE 269
#define TOK_LTLSPEC 270
#define TOK_CTLSPEC 271
#define TOK_SPEC 272
#define TOK_INVAR 273
#define TOK_TRANS 274
#define TOK_INIT 275
#define TOK_ARRAY_DEFINE 276
#define TOK_DEFINE 277
#define TOK_IVAR 278
#define TOK_FROZENVAR 279
#define TOK_VAR 280
#define TOK_PSLSPEC 281
#define TOK_CONSTANTS 282
#define TOK_JUSTICE 283
#define TOK_COMPASSION 284
#define TOK_FAIRNESS 285
#define TOK_INVARSPEC 286
#define TOK_ASSIGN 287
#define TOK_ISA 288
#define TOK_SEMI 289
#define TOK_CONS 290
#define TOK_OF 291
#define TOK_RCB 292
#define TOK_LCB 293
#define TOK_RB 294
#define TOK_RP 295
#define TOK_LP 296
#define TOK_TWODOTS 297
#define TOK_EQDEF 298
#define TOK_SELF 299
#define TOK_COLON 300
#define TOK_ESAC 301
#define TOK_CASE 302
#define TOK_COMPID 303
#define TOK_COMPWFF 304
#define TOK_CTLWFF 305
#define TOK_LTLPSL 306
#define TOK_LTLWFF 307
#define TOK_NEXTWFF 308
#define TOK_SIMPWFF 309
#define TOK_INCONTEXT 310
#define TOK_WORD 311
#define TOK_REAL 312
#define TOK_INTEGER 313
#define TOK_BOOLEAN 314
#define TOK_ARRAY 315
#define TOK_WORD1 316
#define TOK_BOOL 317
#define TOK_WAWRITE 318
#define TOK_WAREAD 319
#define TOK_COUNT 320
#define TOK_WTOINT 321
#define TOK_WSIZEOF 322
#define TOK_WRESIZE 323
#define TOK_SWCONST 324
#define TOK_UWCONST 325
#define TOK_EXTEND 326
#define TOK_UNSIGNED 327
#define TOK_SIGNED 328
#define TOK_TRUEEXP 329
#define TOK_FALSEEXP 330
#define TOK_ATOM 331
#define TOK_NUMBER_EXP 332
#define TOK_NUMBER_REAL 333
#define TOK_NUMBER_FRAC 334
#define TOK_NUMBER 335
#define TOK_NUMBER_WORD 336
#define TOK_QUESTIONMARK 337
#define TOK_NOT 338
#define TOK_AND 339
#define TOK_XNOR 340
#define TOK_XOR 341
#define TOK_OR 342
#define TOK_IFF 343
#define TOK_IMPLIES 344
#define TOK_COMMA 345
#define TOK_AA 346
#define TOK_EE 347
#define TOK_AG 348
#define TOK_EG 349
#define TOK_AF 350
#define TOK_EF 351
#define TOK_AX 352
#define TOK_EX 353
#define TOK_RELEASES 354
#define TOK_TRIGGERED 355
#define TOK_UNTIL 356
#define TOK_SINCE 357
#define TOK_MMAX 358
#define TOK_MMIN 359
#define TOK_BUNTIL 360
#define TOK_ABG 361
#define TOK_ABF 362
#define TOK_EBG 363
#define TOK_EBF 364
#define TOK_OP_FUTURE 365
#define TOK_OP_GLOBAL 366
#define TOK_OP_NEXT 367
#define TOK_OP_ONCE 368
#define TOK_OP_HISTORICAL 369
#define TOK_OP_NOTPRECNOT 370
#define TOK_OP_PREC 371
#define TOK_GE 372
#define TOK_LE 373
#define TOK_GT 374
#define TOK_LT 375
#define TOK_NOTEQUAL 376
#define TOK_EQUAL 377
#define TOK_RROTATE 378
#define TOK_LROTATE 379
#define TOK_RSHIFT 380
#define TOK_LSHIFT 381
#define TOK_SETIN 382
#define TOK_UNION 383
#define TOK_DIVIDE 384
#define TOK_TIMES 385
#define TOK_MINUS 386
#define TOK_PLUS 387
#define TOK_MOD 388
#define TOK_CONCATENATION 389
#define TOK_SMALLINIT 390
#define TOK_NEXT 391
#define TOK_BIT 392
#define TOK_DOT 393
#define TOK_LB 394
#define TOK_MIRROR 395
#define TOK_PREDSLIST 396
#define TOK_PRED 397




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 125 "grammar.y"
{
  node_ptr node;
  int lineno;
}
/* Line 1529 of yacc.c.  */
#line 338 "grammar.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

