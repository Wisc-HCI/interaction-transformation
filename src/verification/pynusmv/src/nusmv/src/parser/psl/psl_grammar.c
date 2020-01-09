/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton implementation for Bison's Yacc-like parsers in C

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

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "2.3"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Using locations.  */
#define YYLSP_NEEDED 0

/* Substitute the variable and function names.  */
#define yyparse psl_yyparse
#define yylex   psl_yylex
#define yyerror psl_yyerror
#define yylval  psl_yylval
#define yychar  psl_yychar
#define yydebug psl_yydebug
#define yynerrs psl_yynerrs


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TKEOF = 258,
     TKSTRING = 259,
     TKERROR = 260,
     TKSTRUCT = 261,
     TKNUMBER = 262,
     TKREALNUMBER = 263,
     TKWORDNUMBER = 264,
     TKBASENUMBER = 265,
     TKTRUE = 266,
     TKFALSE = 267,
     TKUNSIGNEDWORDNUMBER = 268,
     TKSIGNEDWORDNUMBER = 269,
     TKINCONTEXT = 270,
     TKEQDEF = 271,
     TKNAME = 272,
     TKSERE = 273,
     TKSERECONCAT = 274,
     TKSEREFUSION = 275,
     TKSERECOMPOUND = 276,
     TKSEREREPEATED = 277,
     TKCONS = 278,
     TKCONCATENATION = 279,
     TKREPLPROP = 280,
     TKARRAY = 281,
     TKCONTEXT = 282,
     TKATOM = 283,
     TKFAILURE = 284,
     TKITE = 285,
     TKVUNIT = 286,
     TKVMODE = 287,
     TKVPROP = 288,
     TKSTRONG = 289,
     TKDEFPARAM = 290,
     TKINHERIT = 291,
     TKFAIRNESS = 292,
     TKCONST = 293,
     TKBEGIN = 294,
     TKEND = 295,
     TKPARAMETER = 296,
     TKTASK = 297,
     TKENDTASK = 298,
     TKFORK = 299,
     TKJOIN = 300,
     TKSUPPLY0 = 301,
     TKSUPPLY1 = 302,
     TKSTRONG0 = 303,
     TKPULL0 = 304,
     TKWEAK0 = 305,
     TKHIGHZ0 = 306,
     TKSTRONG1 = 307,
     TKPULL1 = 308,
     TKWEAK1 = 309,
     TKHIGHZ1 = 310,
     TKINPUT = 311,
     TKOUTPUT = 312,
     TKINOUT = 313,
     TKDEFAULT_CLOCK = 314,
     TKDEFAULT_COLON = 315,
     TKDEASSIGN = 316,
     TKDISABLE = 317,
     TKENDSPECIFY = 318,
     TKFOR = 319,
     TKINITIAL = 320,
     TKSPECIFY = 321,
     TKWAIT = 322,
     TKFOREVER = 323,
     TKREPEAT = 324,
     TKWHILE = 325,
     TKENDMODULE = 326,
     TKENDFUNCTION = 327,
     TKWIRE = 328,
     TKTRI = 329,
     TKTRI1 = 330,
     TKWAND = 331,
     TKTRIAND = 332,
     TKTRI0 = 333,
     TKWOR = 334,
     TKTRIOR = 335,
     TKTRIREG = 336,
     TKREG = 337,
     TKINTEGER = 338,
     TKINF = 339,
     TKDOT = 340,
     TKENDPOINT = 341,
     TKASSIGN = 342,
     TKFORCE = 343,
     TKRELEASE = 344,
     TKPROPERTY = 345,
     TKSEQUENCE = 346,
     TKMODULE = 347,
     TKFUNCTION = 348,
     TKRESTRICT = 349,
     TKRESTRICT_GUARANTEE = 350,
     TKFORALL = 351,
     TKFORANY = 352,
     TKASSERT = 353,
     TKASSUME = 354,
     TKASSUME_GUARANTEE = 355,
     TKCOVER = 356,
     TKBOOLEAN = 357,
     TKCASE = 358,
     TKCASEX = 359,
     TKCASEZ = 360,
     TKELSE = 361,
     TKENDCASE = 362,
     TKIF = 363,
     TKNONDET = 364,
     TKNONDET_VECTOR = 365,
     TKNONDET_RANGE = 366,
     TKWNONDET = 367,
     TKBASE = 368,
     TKDOTDOT = 369,
     TKPIPEMINUSGT = 370,
     TKPIPEEQGT = 371,
     TKIDENTIFIER = 372,
     TKHIERARCHICALID = 373,
     TKLP = 374,
     TKRP = 375,
     TKLC = 376,
     TKRC = 377,
     TKLB = 378,
     TKRB = 379,
     TKCOMMA = 380,
     TKDIEZ = 381,
     TKTRANS = 382,
     TKHINT = 383,
     TKTEST_PINS = 384,
     TKALWAYS = 385,
     TKNEVER = 386,
     TKEVENTUALLYBANG = 387,
     TKWITHINBANG = 388,
     TKWITHIN = 389,
     TKWITHINBANG_ = 390,
     TKWITHIN_ = 391,
     TKWHILENOTBANG = 392,
     TKWHILENOT = 393,
     TKWHILENOTBANG_ = 394,
     TKWHILENOT_ = 395,
     TKNEXT_EVENT_ABANG = 396,
     TKNEXT_EVENT_A = 397,
     TKNEXT_EVENT_EBANG = 398,
     TKNEXT_EVENT_E = 399,
     TKNEXT_EVENTBANG = 400,
     TKNEXT_EVENT = 401,
     TKNEXT_ABANG = 402,
     TKNEXT_EBANG = 403,
     TKNEXT_A = 404,
     TKNEXT_E = 405,
     TKNEXTBANG = 406,
     TKNEXT = 407,
     TKNEXTfunc = 408,
     TKBEFOREBANG = 409,
     TKBEFORE = 410,
     TKBEFOREBANG_ = 411,
     TKBEFORE_ = 412,
     TKUNTILBANG = 413,
     TKUNTIL = 414,
     TKUNTILBANG_ = 415,
     TKUNTIL_ = 416,
     TKABORT = 417,
     TKROSE = 418,
     TKFELL = 419,
     TKPREV = 420,
     TKG = 421,
     TKXBANG = 422,
     TKX = 423,
     TKF = 424,
     TKU = 425,
     TKW = 426,
     TKEG = 427,
     TKEX = 428,
     TKEF = 429,
     TKAG = 430,
     TKAX = 431,
     TKAF = 432,
     TKA = 433,
     TKE = 434,
     TKIN = 435,
     TKUNION = 436,
     TKQUESTIONMARK = 437,
     TKCOLON = 438,
     TKSEMI = 439,
     TKPIPEPIPE = 440,
     TKAMPERSANDAMPERSAND = 441,
     TKMINUSGT = 442,
     TKLTMINUSGT = 443,
     TKPIPE = 444,
     TKTILDEPIPE = 445,
     TKOR = 446,
     TKPOSEDGE = 447,
     TKNEGEDGE = 448,
     TKCARET = 449,
     TKXOR = 450,
     TKXNOR = 451,
     TKCARETTILDE = 452,
     TKTILDECARET = 453,
     TKAMPERSAND = 454,
     TKTILDEAMPERSAND = 455,
     TKEQEQ = 456,
     TKBANGEQ = 457,
     TKEQEQEQ = 458,
     TKBANGEQEQ = 459,
     TKEQ = 460,
     TKGT = 461,
     TKGE = 462,
     TKLT = 463,
     TKLE = 464,
     TKLTLT = 465,
     TKGTGT = 466,
     TKWSELECT = 467,
     TKGTGTGT = 468,
     TKLTLTLT = 469,
     TKPLUS = 470,
     TKMINUS = 471,
     TKSPLAT = 472,
     TKSLASH = 473,
     TKPERCENT = 474,
     TKSPLATSPLAT = 475,
     TKBANG = 476,
     TKTILDE = 477,
     TKLBSPLAT = 478,
     TKLBEQ = 479,
     TKLBMINUSGT = 480,
     TKLBPLUSRB = 481,
     TKWCONCATENATION = 482,
     TKBOOL = 483,
     TKWRESIZE = 484,
     TKWSIZEOF = 485,
     TKWTOINT = 486,
     TKUWCONST = 487,
     TKBITSELECTION = 488,
     TKUMINUS = 489,
     TKSWCONST = 490,
     TKWORD1 = 491,
     TKSIGNED = 492,
     TKUNSIGNED = 493,
     TKEXTEND = 494,
     TKSTRUDLE = 495,
     TKSEREFORGR = 496,
     TKPSLSPEC = 497
   };
#endif
/* Tokens.  */
#define TKEOF 258
#define TKSTRING 259
#define TKERROR 260
#define TKSTRUCT 261
#define TKNUMBER 262
#define TKREALNUMBER 263
#define TKWORDNUMBER 264
#define TKBASENUMBER 265
#define TKTRUE 266
#define TKFALSE 267
#define TKUNSIGNEDWORDNUMBER 268
#define TKSIGNEDWORDNUMBER 269
#define TKINCONTEXT 270
#define TKEQDEF 271
#define TKNAME 272
#define TKSERE 273
#define TKSERECONCAT 274
#define TKSEREFUSION 275
#define TKSERECOMPOUND 276
#define TKSEREREPEATED 277
#define TKCONS 278
#define TKCONCATENATION 279
#define TKREPLPROP 280
#define TKARRAY 281
#define TKCONTEXT 282
#define TKATOM 283
#define TKFAILURE 284
#define TKITE 285
#define TKVUNIT 286
#define TKVMODE 287
#define TKVPROP 288
#define TKSTRONG 289
#define TKDEFPARAM 290
#define TKINHERIT 291
#define TKFAIRNESS 292
#define TKCONST 293
#define TKBEGIN 294
#define TKEND 295
#define TKPARAMETER 296
#define TKTASK 297
#define TKENDTASK 298
#define TKFORK 299
#define TKJOIN 300
#define TKSUPPLY0 301
#define TKSUPPLY1 302
#define TKSTRONG0 303
#define TKPULL0 304
#define TKWEAK0 305
#define TKHIGHZ0 306
#define TKSTRONG1 307
#define TKPULL1 308
#define TKWEAK1 309
#define TKHIGHZ1 310
#define TKINPUT 311
#define TKOUTPUT 312
#define TKINOUT 313
#define TKDEFAULT_CLOCK 314
#define TKDEFAULT_COLON 315
#define TKDEASSIGN 316
#define TKDISABLE 317
#define TKENDSPECIFY 318
#define TKFOR 319
#define TKINITIAL 320
#define TKSPECIFY 321
#define TKWAIT 322
#define TKFOREVER 323
#define TKREPEAT 324
#define TKWHILE 325
#define TKENDMODULE 326
#define TKENDFUNCTION 327
#define TKWIRE 328
#define TKTRI 329
#define TKTRI1 330
#define TKWAND 331
#define TKTRIAND 332
#define TKTRI0 333
#define TKWOR 334
#define TKTRIOR 335
#define TKTRIREG 336
#define TKREG 337
#define TKINTEGER 338
#define TKINF 339
#define TKDOT 340
#define TKENDPOINT 341
#define TKASSIGN 342
#define TKFORCE 343
#define TKRELEASE 344
#define TKPROPERTY 345
#define TKSEQUENCE 346
#define TKMODULE 347
#define TKFUNCTION 348
#define TKRESTRICT 349
#define TKRESTRICT_GUARANTEE 350
#define TKFORALL 351
#define TKFORANY 352
#define TKASSERT 353
#define TKASSUME 354
#define TKASSUME_GUARANTEE 355
#define TKCOVER 356
#define TKBOOLEAN 357
#define TKCASE 358
#define TKCASEX 359
#define TKCASEZ 360
#define TKELSE 361
#define TKENDCASE 362
#define TKIF 363
#define TKNONDET 364
#define TKNONDET_VECTOR 365
#define TKNONDET_RANGE 366
#define TKWNONDET 367
#define TKBASE 368
#define TKDOTDOT 369
#define TKPIPEMINUSGT 370
#define TKPIPEEQGT 371
#define TKIDENTIFIER 372
#define TKHIERARCHICALID 373
#define TKLP 374
#define TKRP 375
#define TKLC 376
#define TKRC 377
#define TKLB 378
#define TKRB 379
#define TKCOMMA 380
#define TKDIEZ 381
#define TKTRANS 382
#define TKHINT 383
#define TKTEST_PINS 384
#define TKALWAYS 385
#define TKNEVER 386
#define TKEVENTUALLYBANG 387
#define TKWITHINBANG 388
#define TKWITHIN 389
#define TKWITHINBANG_ 390
#define TKWITHIN_ 391
#define TKWHILENOTBANG 392
#define TKWHILENOT 393
#define TKWHILENOTBANG_ 394
#define TKWHILENOT_ 395
#define TKNEXT_EVENT_ABANG 396
#define TKNEXT_EVENT_A 397
#define TKNEXT_EVENT_EBANG 398
#define TKNEXT_EVENT_E 399
#define TKNEXT_EVENTBANG 400
#define TKNEXT_EVENT 401
#define TKNEXT_ABANG 402
#define TKNEXT_EBANG 403
#define TKNEXT_A 404
#define TKNEXT_E 405
#define TKNEXTBANG 406
#define TKNEXT 407
#define TKNEXTfunc 408
#define TKBEFOREBANG 409
#define TKBEFORE 410
#define TKBEFOREBANG_ 411
#define TKBEFORE_ 412
#define TKUNTILBANG 413
#define TKUNTIL 414
#define TKUNTILBANG_ 415
#define TKUNTIL_ 416
#define TKABORT 417
#define TKROSE 418
#define TKFELL 419
#define TKPREV 420
#define TKG 421
#define TKXBANG 422
#define TKX 423
#define TKF 424
#define TKU 425
#define TKW 426
#define TKEG 427
#define TKEX 428
#define TKEF 429
#define TKAG 430
#define TKAX 431
#define TKAF 432
#define TKA 433
#define TKE 434
#define TKIN 435
#define TKUNION 436
#define TKQUESTIONMARK 437
#define TKCOLON 438
#define TKSEMI 439
#define TKPIPEPIPE 440
#define TKAMPERSANDAMPERSAND 441
#define TKMINUSGT 442
#define TKLTMINUSGT 443
#define TKPIPE 444
#define TKTILDEPIPE 445
#define TKOR 446
#define TKPOSEDGE 447
#define TKNEGEDGE 448
#define TKCARET 449
#define TKXOR 450
#define TKXNOR 451
#define TKCARETTILDE 452
#define TKTILDECARET 453
#define TKAMPERSAND 454
#define TKTILDEAMPERSAND 455
#define TKEQEQ 456
#define TKBANGEQ 457
#define TKEQEQEQ 458
#define TKBANGEQEQ 459
#define TKEQ 460
#define TKGT 461
#define TKGE 462
#define TKLT 463
#define TKLE 464
#define TKLTLT 465
#define TKGTGT 466
#define TKWSELECT 467
#define TKGTGTGT 468
#define TKLTLTLT 469
#define TKPLUS 470
#define TKMINUS 471
#define TKSPLAT 472
#define TKSLASH 473
#define TKPERCENT 474
#define TKSPLATSPLAT 475
#define TKBANG 476
#define TKTILDE 477
#define TKLBSPLAT 478
#define TKLBEQ 479
#define TKLBMINUSGT 480
#define TKLBPLUSRB 481
#define TKWCONCATENATION 482
#define TKBOOL 483
#define TKWRESIZE 484
#define TKWSIZEOF 485
#define TKWTOINT 486
#define TKUWCONST 487
#define TKBITSELECTION 488
#define TKUMINUS 489
#define TKSWCONST 490
#define TKWORD1 491
#define TKSIGNED 492
#define TKUNSIGNED 493
#define TKEXTEND 494
#define TKSTRUDLE 495
#define TKSEREFORGR 496
#define TKPSLSPEC 497




/* Copy the first part of user declarations.  */
#line 1 "psl_grammar.y"

/**CFile***********************************************************************

  FileName    [psl_grammar.y]

  PackageName [parser.psl]

  Synopsis [Grammar (for Yacc and Bison) of PSL specification input
  language]

  SeeAlso     [psl_input.l]

  Author      [Roberto Cavada]

  Copyright   [
  This file is part of the ``parser.psl'' package of NuSMV version 2. 
  Copyright (C) 2005 by FBK-irst. 

  NuSMV version 2 is free software; you can redistribute it and/or 
  modify it under the terms of the GNU Lesser General Public 
  License as published by the Free Software Foundation; either 
  version 2 of the License, or (at your option) any later version.

  NuSMV version 2 is distributed in the hope that it will be useful, 
  but WITHOUT ANY WARRANTY; without even the implied warranty of 
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU 
  Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public 
  License along with this library; if not, write to the Free Software 
  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA.

  For more information on NuSMV see <http://nusmv.fbk.eu>
  or email to <nusmv-users@fbk.eu>.
  Please report bugs to <nusmv-users@fbk.eu>.

  To contact the NuSMV development board, email to <nusmv@fbk.eu>. ]

******************************************************************************/

#include "pslExpr.h"
#include "utils/error.h"

EXTERN int yylex ARGS((void));
EXTERN void Parser_switch_to_smv ARGS(());

EXTERN void psl_yyerror ARGS((char* s, ...));
EXTERN int psl_error ARGS((void));

  node_ptr psl_parsed_tree; /* the returned value of parsing */
  node_ptr psl_property_name = Nil; /* the property name, Nil if none */


/* Enabling traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* Enabling the token table.  */
#ifndef YYTOKEN_TABLE
# define YYTOKEN_TABLE 0
#endif

#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 61 "psl_grammar.y"
{
  node_ptr node; 
  int lineno;

  /* these are news */
  int ival;
  char* wval;
  char* fval;
  char* baseval;
  char* idname;
  PslExpr psl_expr;
  PslOp operator;
}
/* Line 193 of yacc.c.  */
#line 655 "psl_grammar.c"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 668 "psl_grammar.c"

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#elif (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
typedef signed char yytype_int8;
#else
typedef short int yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(msgid) dgettext ("bison-runtime", msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(msgid) msgid
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(e) ((void) (e))
#else
# define YYUSE(e) /* empty */
#endif

/* Identity function, used to suppress warnings about constant conditions.  */
#ifndef lint
# define YYID(n) (n)
#else
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static int
YYID (int i)
#else
static int
YYID (i)
    int i;
#endif
{
  return i;
}
#endif

#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#     ifndef _STDLIB_H
#      define _STDLIB_H 1
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's `empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (YYID (0))
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined _STDLIB_H \
       && ! ((defined YYMALLOC || defined malloc) \
	     && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef _STDLIB_H
#    define _STDLIB_H 1
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined _STDLIB_H && (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
	 || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss;
  YYSTYPE yyvs;
  };

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

/* Copy COUNT objects from FROM to TO.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(To, From, Count) \
      __builtin_memcpy (To, From, (Count) * sizeof (*(From)))
#  else
#   define YYCOPY(To, From, Count)		\
      do					\
	{					\
	  YYSIZE_T yyi;				\
	  for (yyi = 0; yyi < (Count); yyi++)	\
	    (To)[yyi] = (From)[yyi];		\
	}					\
      while (YYID (0))
#  endif
# endif

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack)					\
    do									\
      {									\
	YYSIZE_T yynewbytes;						\
	YYCOPY (&yyptr->Stack, Stack, yysize);				\
	Stack = &yyptr->Stack;						\
	yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
	yyptr += yynewbytes / sizeof (*yyptr);				\
      }									\
    while (YYID (0))

#endif

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  162
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   7520

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  243
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  39
/* YYNRULES -- Number of rules.  */
#define YYNRULES  194
/* YYNRULES -- Number of states.  */
#define YYNSTATES  523

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   497

#define YYTRANSLATE(YYX)						\
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[YYLEX] -- Bison symbol number corresponding to YYLEX.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     6,     7,     8,     9,    10,    11,    12,    13,    14,
      15,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,    48,    49,    50,    51,    52,    53,    54,
      55,    56,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    68,    69,    70,    71,    72,    73,    74,
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84,
      85,    86,    87,    88,    89,    90,    91,    92,    93,    94,
      95,    96,    97,    98,    99,   100,   101,   102,   103,   104,
     105,   106,   107,   108,   109,   110,   111,   112,   113,   114,
     115,   116,   117,   118,   119,   120,   121,   122,   123,   124,
     125,   126,   127,   128,   129,   130,   131,   132,   133,   134,
     135,   136,   137,   138,   139,   140,   141,   142,   143,   144,
     145,   146,   147,   148,   149,   150,   151,   152,   153,   154,
     155,   156,   157,   158,   159,   160,   161,   162,   163,   164,
     165,   166,   167,   168,   169,   170,   171,   172,   173,   174,
     175,   176,   177,   178,   179,   180,   181,   182,   183,   184,
     185,   186,   187,   188,   189,   190,   191,   192,   193,   194,
     195,   196,   197,   198,   199,   200,   201,   202,   203,   204,
     205,   206,   207,   208,   209,   210,   211,   212,   213,   214,
     215,   216,   217,   218,   219,   220,   221,   222,   223,   224,
     225,   226,   227,   228,   229,   230,   231,   232,   233,   234,
     235,   236,   237,   238,   239,   240,   241,   242
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     8,    13,    16,    19,    21,    26,    28,
      32,    35,    43,    45,    47,    49,    51,    53,    54,    56,
      60,    64,    69,    74,    76,    80,    84,    85,    87,    89,
      92,    95,    98,   101,   107,   113,   116,   119,   122,   125,
     128,   132,   136,   140,   144,   148,   152,   156,   160,   168,
     176,   184,   192,   200,   208,   216,   224,   232,   240,   251,
     262,   273,   284,   295,   306,   311,   316,   320,   325,   329,
     332,   335,   338,   346,   354,   362,   370,   376,   382,   388,
     394,   396,   398,   402,   406,   410,   414,   416,   418,   422,
     426,   430,   435,   439,   442,   444,   449,   454,   456,   458,
     460,   461,   463,   465,   467,   469,   471,   475,   477,   480,
     482,   484,   486,   489,   491,   493,   495,   498,   501,   504,
     511,   514,   517,   520,   527,   529,   531,   533,   535,   537,
     539,   542,   545,   548,   553,   558,   563,   568,   575,   582,
     586,   590,   594,   598,   602,   606,   610,   614,   618,   622,
     626,   630,   634,   638,   642,   646,   650,   654,   658,   662,
     666,   670,   674,   683,   687,   693,   697,   698,   704,   706,
     708,   710,   712,   714,   721,   728,   730,   735,   740,   742,
     744,   746,   748,   750,   752,   754,   758,   760,   764,   768,
     773,   775,   779,   783,   785
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     244,     0,    -1,   242,   245,   184,     3,    -1,   241,   257,
     184,     3,    -1,   245,   184,    -1,   245,     3,    -1,   246,
      -1,    17,   277,    16,   246,    -1,   266,    -1,   266,    15,
     277,    -1,    91,   257,    -1,   248,    28,   249,   180,   251,
     183,   266,    -1,   256,    -1,   254,    -1,   265,    -1,    96,
      -1,    97,    -1,    -1,   250,    -1,   123,   262,   124,    -1,
     123,     1,   124,    -1,   121,   252,   253,   122,    -1,   121,
     252,     1,   122,    -1,   102,    -1,   252,   253,   125,    -1,
     252,     1,   125,    -1,    -1,   266,    -1,   262,    -1,   168,
     266,    -1,   167,   266,    -1,   169,   266,    -1,   166,   266,
      -1,   123,   266,   170,   266,   124,    -1,   123,   266,   171,
     266,   124,    -1,   130,   266,    -1,   131,   266,    -1,   152,
     266,    -1,   151,   266,    -1,   132,   266,    -1,   266,   158,
     266,    -1,   266,   159,   266,    -1,   266,   160,   266,    -1,
     266,   161,   266,    -1,   266,   154,   266,    -1,   266,   155,
     266,    -1,   266,   156,   266,    -1,   266,   157,   266,    -1,
     168,   123,   266,   124,   119,   266,   120,    -1,   167,   123,
     266,   124,   119,   266,   120,    -1,   152,   123,   266,   124,
     119,   266,   120,    -1,   151,   123,   266,   124,   119,   266,
     120,    -1,   149,   123,   262,   124,   119,   266,   120,    -1,
     147,   123,   262,   124,   119,   266,   120,    -1,   150,   123,
     262,   124,   119,   266,   120,    -1,   148,   123,   262,   124,
     119,   266,   120,    -1,   145,   119,   266,   120,   119,   266,
     120,    -1,   146,   119,   266,   120,   119,   266,   120,    -1,
     145,   119,   266,   120,   123,   266,   124,   119,   266,   120,
      -1,   146,   119,   266,   120,   123,   266,   124,   119,   266,
     120,    -1,   141,   119,   266,   120,   123,   262,   124,   119,
     266,   120,    -1,   142,   119,   266,   120,   123,   262,   124,
     119,   266,   120,    -1,   143,   119,   266,   120,   123,   262,
     124,   119,   266,   120,    -1,   144,   119,   266,   120,   123,
     262,   124,   119,   266,   120,    -1,   257,   119,   266,   120,
      -1,   257,   115,   257,   221,    -1,   257,   115,   257,    -1,
     257,   116,   257,   221,    -1,   257,   116,   257,    -1,   130,
     257,    -1,   131,   257,    -1,   132,   257,    -1,   133,   119,
     255,   125,   266,   120,   257,    -1,   134,   119,   255,   125,
     266,   120,   257,    -1,   135,   119,   255,   125,   266,   120,
     257,    -1,   136,   119,   255,   125,   266,   120,   257,    -1,
     137,   119,   266,   120,   257,    -1,   138,   119,   266,   120,
     257,    -1,   139,   119,   266,   120,   257,    -1,   140,   119,
     266,   120,   257,    -1,   257,    -1,   266,    -1,   266,   162,
     266,    -1,   266,   188,   266,    -1,   266,   187,   266,    -1,
     121,   258,   122,    -1,   266,    -1,   257,    -1,   258,   184,
     258,    -1,   257,   183,   257,    -1,   257,   259,   257,    -1,
     258,   223,   260,   124,    -1,   223,   260,   124,    -1,   258,
     226,    -1,   226,    -1,   266,   224,   261,   124,    -1,   266,
     225,   260,   124,    -1,   186,    -1,   199,    -1,   189,    -1,
      -1,   261,    -1,     7,    -1,    10,    -1,   262,    -1,   277,
      -1,   263,   183,   264,    -1,     7,    -1,   216,     7,    -1,
      10,    -1,   277,    -1,     7,    -1,   216,     7,    -1,    10,
      -1,    84,    -1,   277,    -1,   176,   266,    -1,   175,   266,
      -1,   177,   266,    -1,   178,   123,   266,   170,   266,   124,
      -1,   173,   266,    -1,   172,   266,    -1,   174,   266,    -1,
     179,   123,   266,   170,   266,   124,    -1,   276,    -1,   267,
      -1,   268,    -1,   269,    -1,   270,    -1,   247,    -1,   215,
     276,    -1,   216,   276,    -1,   221,   276,    -1,   228,   119,
     266,   120,    -1,   236,   119,   266,   120,    -1,   237,   119,
     266,   120,    -1,   238,   119,   266,   120,    -1,   239,   119,
     266,   125,   276,   120,    -1,   229,   119,   266,   125,   276,
     120,    -1,   266,   215,   266,    -1,   266,   181,   266,    -1,
     266,   180,   266,    -1,   266,   216,   266,    -1,   266,   217,
     266,    -1,   266,   218,   266,    -1,   266,   219,   266,    -1,
     266,   205,   266,    -1,   266,   201,   266,    -1,   266,   202,
     266,    -1,   266,   208,   266,    -1,   266,   209,   266,    -1,
     266,   206,   266,    -1,   266,   207,   266,    -1,   266,   199,
     266,    -1,   266,   186,   266,    -1,   266,   189,   266,    -1,
     266,   185,   266,    -1,   266,   194,   266,    -1,   266,   195,
     266,    -1,   266,   196,   266,    -1,   266,   210,   266,    -1,
     266,   211,   266,    -1,   212,   119,   266,   125,   266,   125,
     266,   120,    -1,   266,   227,   266,    -1,   266,   182,   266,
     183,   266,    -1,   103,   271,   107,    -1,    -1,   266,   183,
     266,   184,   271,    -1,    11,    -1,    12,    -1,    10,    -1,
       7,    -1,     8,    -1,   232,   119,   266,   125,   266,   120,
      -1,   235,   119,   266,   125,   266,   120,    -1,     9,    -1,
     230,   119,   266,   120,    -1,   231,   119,   266,   120,    -1,
     273,    -1,   272,    -1,   274,    -1,   275,    -1,   277,    -1,
     279,    -1,   281,    -1,   119,   278,   120,    -1,    28,    -1,
     277,    85,    28,    -1,   277,    85,     7,    -1,   277,   123,
     266,   124,    -1,   266,    -1,   121,   280,   122,    -1,   280,
     125,   266,    -1,   266,    -1,   121,   266,   121,   280,   122,
     122,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   420,   420,   423,   426,   429,   436,   437,   441,   442,
     444,   448,   455,   456,   457,   462,   463,   467,   468,   472,
     473,   477,   478,   479,   483,   484,   485,   489,   490,   496,
     497,   498,   499,   500,   501,   505,   506,   507,   508,   509,
     512,   513,   514,   515,   517,   518,   519,   520,   523,   526,
     529,   532,   536,   539,   542,   545,   549,   552,   555,   558,
     561,   564,   567,   570,   575,   577,   579,   581,   583,   586,
     587,   588,   590,   592,   594,   596,   599,   601,   603,   605,
     610,   611,   616,   619,   620,   624,   628,   629,   632,   633,
     634,   637,   638,   640,   642,   646,   647,   652,   653,   654,
     658,   659,   663,   664,   665,   666,   670,   674,   675,   676,
     677,   681,   682,   683,   684,   685,   690,   691,   692,   693,
     696,   697,   698,   699,   704,   705,   706,   707,   708,   709,
     713,   714,   715,   716,   717,   718,   719,   720,   722,   727,
     728,   729,   730,   731,   732,   733,   734,   735,   736,   738,
     739,   740,   741,   743,   744,   746,   747,   749,   750,   751,
     752,   753,   756,   759,   764,   769,   773,   775,   779,   780,
     784,   785,   786,   790,   792,   794,   798,   799,   803,   804,
     805,   806,   807,   808,   809,   810,   814,   816,   819,   822,
     827,   832,   837,   838,   842
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "\"eof\"", "\"string\"", "TKERROR",
  "\"struct\"", "\"number\"", "\"real number\"", "\"word number\"",
  "\"based number\"", "TKTRUE", "TKFALSE", "TKUNSIGNEDWORDNUMBER",
  "TKSIGNEDWORDNUMBER", "TKINCONTEXT", "TKEQDEF", "TKNAME", "TKSERE",
  "TKSERECONCAT", "TKSEREFUSION", "TKSERECOMPOUND", "TKSEREREPEATED",
  "TKCONS", "TKCONCATENATION", "TKREPLPROP", "TKARRAY", "TKCONTEXT",
  "TKATOM", "TKFAILURE", "TKITE", "\"vunit\"", "\"vmode\"", "\"vprop\"",
  "\"strong\"", "\"defparam\"", "\"inherit\"", "\"fairness\"", "\"const\"",
  "\"begin\"", "\"end\"", "\"parameter\"", "\"task\"", "\"endtask\"",
  "\"fork\"", "\"join\"", "\"supply0\"", "\"supply1\"", "\"strong0\"",
  "\"pull0\"", "\"weak0\"", "\"highz0\"", "\"strong1\"", "\"pull1\"",
  "\"weak1\"", "\"highz1\"", "\"input\"", "\"output\"", "\"inout\"",
  "\"default clock\"", "\"default\"", "\"deassign\"", "\"disable\"",
  "\"endspecify\"", "\"for\"", "\"initial\"", "\"specify\"", "\"wait\"",
  "\"forever\"", "\"repeat\"", "\"while\"", "\"endmodule\"",
  "\"endfunction\"", "\"wire\"", "\"tri\"", "\"try1\"", "\"wand\"",
  "\"triand\"", "\"tri0\"", "\"wor\"", "\"trior\"", "\"trireg\"",
  "\"reg\"", "\"integer\"", "\"inf\"", "\"dot\"", "\"endpoint\"",
  "\"assign\"", "\"force\"", "\"release\"", "\"property\"", "\"sequence\"",
  "\"module\"", "\"function\"", "\"restrict\"", "\"restrict_guarantee\"",
  "\"forall\"", "\"forany\"", "\"assert\"", "\"assume\"",
  "\"assume_guarantee\"", "\"cover\"", "\"boolean\"", "\"case\"",
  "\"casex\"", "\"casez\"", "\"else\"", "\"esac\"", "\"if\"",
  "\"$nondet\"", "\"$nondet_vector\"", "\"$nondet_range\"", "\"$wnondet\"",
  "TKBASE", "\"..\"", "\"|->\"", "\"|=>\"", "\"identifier\"",
  "TKHIERARCHICALID", "\"(\"", "\")\"", "\"{\"", "\"}\"", "\"[\"", "\"]\"",
  "\",\"", "\"#\"", "\"trans\"", "\"hint\"", "\"test_pins\"", "\"always\"",
  "\"never\"", "\"eventually!\"", "\"within!\"", "\"within\"",
  "\"within!_\"", "\"within_\"", "\"whilenot!\"", "\"whilenot\"",
  "\"whilenot!_\"", "\"whilenot_\"", "\"next_event_a!\"",
  "\"next_event_a\"", "\"next_event_e!\"", "\"next_event_e\"",
  "\"next_event!\"", "\"next_event\"", "\"next_a!\"", "\"next_e!\"",
  "\"next_a\"", "\"next_e\"", "\"next!\"", "\"next\"",
  "\"next (function)\"", "\"before!\"", "\"before\"", "\"before!_\"",
  "\"before_\"", "\"until!\"", "\"until\"", "\"until!_\"", "\"until_\"",
  "\"abort\"", "\"rose\"", "\"fell\"", "\"prev\"", "\"G\"", "\"X!\"",
  "\"X\"", "\"F\"", "\"U\"", "\"W\"", "\"EG\"", "\"EX\"", "\"EF\"",
  "\"AG\"", "\"AX\"", "\"AF\"", "\"A\"", "\"E\"", "\"in\"", "\"union\"",
  "\"?\"", "\":\"", "\";\"", "\"||\"", "\"&&\"", "\"->\"", "\"<->\"",
  "\"|\"", "\"~|\"", "\"or\"", "\"posedge\"", "\"negedge\"", "\"^\"",
  "\"xor\"", "\"xnor\"", "\"^~\"", "\"~^\"", "\"&\"", "\"~&\"", "\"==\"",
  "\"!=\"", "\"===\"", "\"!==\"", "\"=\"", "\">\"", "\">=\"", "\"<\"",
  "\"<=\"", "\"<<\"", "\">>\"", "\"select\"", "\">>>\"", "\"<<<\"",
  "\"+\"", "\"-\"", "\"*\"", "\"/\"", "\"mod\"", "\"**\"", "\"!\"",
  "\"~\"", "\"[*\"", "\"[=\"", "\"[->\"", "\"[+]\"", "\"::\"", "\"bool\"",
  "\"resize\"", "\"sizeof\"", "\"toint\"", "\"uwconst\"",
  "\"bit selection\"", "\"unary minus\"", "\"swconst\"", "\"word1\"",
  "\"signed\"", "\"unsigned\"", "\"extend\"", "\"@\"", "\"grsequence\"",
  "\"PSLSPEC\"", "$accept", "PslSpecSemi", "PslSpec", "_PslSpec",
  "Property", "ForStar", "Opt_IndexRange", "IndexRange", "ValueSet",
  "ValueRange_List", "ValueRange", "FL_Property", "Sequence_or_Expression",
  "Additional_Binary_Operators", "Sequence", "Sere", "AndOrOp",
  "Opt_Count", "Count", "Range", "LowBound", "HighBound", "OBE_Property",
  "Expression", "Unary_Expression", "Binary_Expression",
  "Conditional_Expression", "Case_Expression", "case_list", "boolean",
  "number", "word_number", "word_operators", "Primary",
  "hierarchical_identifier", "Mintypmax_Expression", "Concatenation",
  "Expression_List", "Multiple_Concatenation", 0
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[YYLEX-NUM] -- Internal token number corresponding to
   token YYLEX-NUM.  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   261,   262,   263,   264,
     265,   266,   267,   268,   269,   270,   271,   272,   273,   274,
     275,   276,   277,   278,   279,   280,   281,   282,   283,   284,
     285,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   299,   300,   301,   302,   303,   304,
     305,   306,   307,   308,   309,   310,   311,   312,   313,   314,
     315,   316,   317,   318,   319,   320,   321,   322,   323,   324,
     325,   326,   327,   328,   329,   330,   331,   332,   333,   334,
     335,   336,   337,   338,   339,   340,   341,   342,   343,   344,
     345,   346,   347,   348,   349,   350,   351,   352,   353,   354,
     355,   356,   357,   358,   359,   360,   361,   362,   363,   364,
     365,   366,   367,   368,   369,   370,   371,   372,   373,   374,
     375,   376,   377,   378,   379,   380,   381,   382,   383,   384,
     385,   386,   387,   388,   389,   390,   391,   392,   393,   394,
     395,   396,   397,   398,   399,   400,   401,   402,   403,   404,
     405,   406,   407,   408,   409,   410,   411,   412,   413,   414,
     415,   416,   417,   418,   419,   420,   421,   422,   423,   424,
     425,   426,   427,   428,   429,   430,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   461,   462,   463,   464,
     465,   466,   467,   468,   469,   470,   471,   472,   473,   474,
     475,   476,   477,   478,   479,   480,   481,   482,   483,   484,
     485,   486,   487,   488,   489,   490,   491,   492,   493,   494,
     495,   496,   497
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint16 yyr1[] =
{
       0,   243,   244,   244,   244,   244,   245,   245,   246,   246,
     246,   247,   247,   247,   247,   248,   248,   249,   249,   250,
     250,   251,   251,   251,   252,   252,   252,   253,   253,   254,
     254,   254,   254,   254,   254,   254,   254,   254,   254,   254,
     254,   254,   254,   254,   254,   254,   254,   254,   254,   254,
     254,   254,   254,   254,   254,   254,   254,   254,   254,   254,
     254,   254,   254,   254,   254,   254,   254,   254,   254,   254,
     254,   254,   254,   254,   254,   254,   254,   254,   254,   254,
     255,   255,   256,   256,   256,   257,   258,   258,   258,   258,
     258,   258,   258,   258,   258,   258,   258,   259,   259,   259,
     260,   260,   261,   261,   261,   261,   262,   263,   263,   263,
     263,   264,   264,   264,   264,   264,   265,   265,   265,   265,
     265,   265,   265,   265,   266,   266,   266,   266,   266,   266,
     267,   267,   267,   267,   267,   267,   267,   267,   267,   268,
     268,   268,   268,   268,   268,   268,   268,   268,   268,   268,
     268,   268,   268,   268,   268,   268,   268,   268,   268,   268,
     268,   268,   268,   268,   269,   270,   271,   271,   272,   272,
     273,   273,   273,   274,   274,   274,   275,   275,   276,   276,
     276,   276,   276,   276,   276,   276,   277,   277,   277,   277,
     278,   279,   280,   280,   281
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     4,     4,     2,     2,     1,     4,     1,     3,
       2,     7,     1,     1,     1,     1,     1,     0,     1,     3,
       3,     4,     4,     1,     3,     3,     0,     1,     1,     2,
       2,     2,     2,     5,     5,     2,     2,     2,     2,     2,
       3,     3,     3,     3,     3,     3,     3,     3,     7,     7,
       7,     7,     7,     7,     7,     7,     7,     7,    10,    10,
      10,    10,    10,    10,     4,     4,     3,     4,     3,     2,
       2,     2,     7,     7,     7,     7,     5,     5,     5,     5,
       1,     1,     3,     3,     3,     3,     1,     1,     3,     3,
       3,     4,     3,     2,     1,     4,     4,     1,     1,     1,
       0,     1,     1,     1,     1,     1,     3,     1,     2,     1,
       1,     1,     2,     1,     1,     1,     2,     2,     2,     6,
       2,     2,     2,     6,     1,     1,     1,     1,     1,     1,
       2,     2,     2,     4,     4,     4,     4,     6,     6,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     8,     3,     5,     3,     0,     5,     1,     1,
       1,     1,     1,     6,     6,     1,     4,     4,     1,     1,
       1,     1,     1,     1,     1,     3,     1,     3,     3,     4,
       1,     3,     3,     1,     6
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       0,   171,   172,   175,   170,   168,   169,     0,   186,     0,
      15,    16,   166,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     6,
     129,     0,    13,    12,     0,    14,     8,   125,   126,   127,
     128,   179,   178,   180,   181,   124,   182,   183,   184,     0,
       0,    10,     0,     0,   190,     0,   100,    94,    87,     0,
      86,     0,     0,    69,    35,    70,    36,    71,    39,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    38,     0,
      37,    32,     0,    30,     0,    29,    31,   121,   120,   122,
     117,   116,   118,     0,     0,     0,     0,   130,   131,   132,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     1,     5,     4,    17,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    86,
       0,   165,   185,   102,   103,     0,     0,   101,   104,     0,
     105,     0,    97,    99,    98,     0,    85,     0,   100,    93,
       0,     0,   100,   191,     0,     0,     0,     0,    80,    81,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   107,   109,     0,   110,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   193,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    18,    66,    68,     0,     9,    44,    45,    46,
      47,    40,    41,    42,    43,    82,   141,   140,     0,   156,
     154,    84,    83,   155,   157,   158,   159,   153,   147,   148,
     146,   151,   152,   149,   150,   160,   161,   139,   142,   143,
     144,   145,   163,   188,   187,     0,     7,     0,   108,    92,
       0,    89,    90,    88,     0,   193,     0,     0,     0,   192,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   133,     0,   176,
     177,     0,     0,   134,   135,   136,     0,     3,     2,     0,
       0,     0,    65,    67,    64,     0,   189,   166,   111,   113,
     114,     0,   106,   115,    91,     0,    95,    96,    33,    34,
       0,     0,     0,     0,    76,    77,    78,    79,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    20,    19,    23,    26,     0,   164,   167,   112,   194,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     119,   123,     0,   138,   173,   174,   137,     0,     0,    72,
      73,    74,    75,     0,     0,     0,     0,    56,     0,    57,
       0,    53,    55,    52,    54,    51,    50,    49,    48,     0,
       0,   171,   170,     0,     0,    28,    27,   182,    11,     0,
       0,     0,     0,     0,     0,   162,    22,    25,   171,    21,
      24,     0,     0,     0,     0,     0,     0,    60,    61,    62,
      63,    58,    59
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    67,    68,    69,    70,    71,   281,   282,   435,   467,
     494,    72,   237,    73,    74,    99,   225,   216,   217,   218,
     219,   392,    75,   239,    77,    78,    79,    80,    93,    81,
      82,    83,    84,    85,    86,    95,    87,   101,    88
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -209
static const yytype_int16 yypact[] =
{
     640,  -209,  -209,  -209,  -209,  -209,  -209,     8,  -209,   -86,
    -209,  -209,  1249,  1249,   792,  1249,  1249,  1249,  1249,   -56,
     -44,   -39,   -33,    -8,    -7,     9,    12,    14,    17,    18,
      19,    20,    28,   -19,    25,    26,    37,  1401,  1553,  1249,
    1705,  1857,  1249,  1249,  1249,  1249,  1249,  1249,  1249,    40,
      42,    47,    21,    21,    21,    48,    90,    92,    94,    96,
      97,    99,   103,   104,   105,   -86,   945,   141,    22,  -209,
    -209,   197,  -209,  -209,   -34,  -209,  1943,  -209,  -209,  -209,
    -209,  -209,  -209,  -209,  -209,  -209,   -64,  -209,  -209,     7,
     792,  -209,  6664,    62,  7034,   106,    50,  -209,   169,  -100,
    5102,   -53,  6516,   -34,  7034,   -34,  7034,   -34,  7108,  1249,
    1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
    1249,  1249,  1249,    60,    60,    60,    60,  1249,  7108,  1249,
    7108,  7034,  1249,   539,  1249,   539,   539,   539,   539,   539,
     539,   539,   539,  1249,  1249,  1249,  1249,  -209,  -209,  -209,
    1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
      44,    45,  -209,  -209,  -209,   108,   -86,   -86,  1249,     8,
    1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
    1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
    1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
    1249,  1249,  1249,  1249,  1249,  1249,    61,  1249,  1097,  6590,
    1249,  -209,  -209,    49,    54,   226,   114,  -209,  -209,    56,
     -59,   -86,  -209,  -209,  -209,   -86,  -209,   792,    50,  -209,
    1249,    50,    50,  -209,  1249,  1249,  1249,   115,   -34,  7034,
     125,   129,   130,  2020,  2097,  2174,  2251,  2328,  2405,  2482,
    2559,  2636,  2713,  -209,  -209,   134,   -64,   135,   136,   137,
    5252,  5326,  5400,  5474,  6738,  6812,  6067,  5178,  2790,  6142,
    2867,  2944,  6217,  6292,  3021,  3098,  3175,  6367,   259,   260,
      55,    84,  -209,    58,    59,  3252,   -64,  7170,  7170,  7170,
    7170,  7220,  7220,  7220,  7220,   539,  7259,  7259,  6886,  7293,
     632,  7108,  7108,   362,   278,   278,   278,   173,    89,    89,
      89,  -117,  -117,  -117,  -117,    30,    30,  -208,  -208,  -209,
    -209,  -209,  -209,  -209,  -209,  5548,  -209,  6960,  -209,  -209,
      51,  -209,  -209,  -150,   145,  7034,   -48,   146,   148,  7034,
    5622,  5696,  1249,  1249,  1249,  1249,   -86,   -86,   -86,   -86,
     142,   154,   158,   159,   -99,   -32,   164,   167,   175,   182,
     183,   184,   190,   191,  1249,  1249,  1249,  -209,    21,  -209,
    -209,  1249,  1249,  -209,  -209,  -209,    21,  -209,  -209,   187,
     194,   -94,  -209,  -209,  -209,  1249,  -209,  1249,  -209,  -209,
    -209,   312,  -209,   -64,  -209,   198,  -209,  -209,  -209,  -209,
    3329,  3406,  3483,  3560,  -209,  -209,  -209,  -209,    60,    60,
      60,    60,  1249,  1249,  1249,  1249,  1249,  1249,  1249,  1249,
    1249,  1249,  1249,  1249,  5770,  5844,  6442,   201,  3637,  3714,
     202,  -209,  -209,  -209,  -209,   140,  7259,  -209,  -209,  -209,
     -86,   -86,   -86,   -86,   200,   204,   205,   206,  3791,  5918,
    3868,  5992,  3945,  4022,  4099,  4176,  4253,  4330,  4407,  4484,
    -209,  -209,  1249,  -209,  -209,  -209,  -209,   463,  1249,  -209,
    -209,  -209,  -209,   207,   208,   212,   213,  -209,   214,  -209,
     215,  -209,  -209,  -209,  -209,  -209,  -209,  -209,  -209,  4561,
     -17,    49,    54,    43,   -16,  -209,  7034,   -59,  7259,  1249,
    1249,  1249,  1249,  1249,  1249,  -209,  -209,  -209,   152,  -209,
    -209,  4638,  4715,  4792,  4869,  4946,  5023,  -209,  -209,  -209,
    -209,  -209,  -209
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -209,  -209,   270,   131,  -209,  -209,  -209,  -209,  -209,  -209,
    -209,  -209,   -15,  -209,   203,   110,  -209,  -125,   107,  -119,
    -209,  -209,  -209,     0,  -209,  -209,  -209,  -209,   -47,  -209,
    -209,  -209,  -209,   -51,   118,  -209,  -209,   111,  -209
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -194
static const yytype_int16 yytable[] =
{
      76,   147,   148,   149,   255,   257,   258,   259,   433,   202,
     203,   204,    92,    94,   100,   102,   104,   106,   108,   205,
     412,   206,   226,   208,   413,   163,   206,   434,     1,     2,
       3,     4,     5,     6,   227,    90,     8,   128,   130,   131,
     133,   135,   136,   137,   138,   139,   140,   141,   142,     8,
     508,     2,     3,     4,     5,     6,   379,   213,   388,   207,
     214,   389,   253,   109,   207,   254,    76,   253,   323,   233,
     254,     8,   234,   228,   395,   110,   229,   234,     8,     8,
     111,   166,   167,     8,   227,   168,   112,   414,     8,   324,
     209,   415,   206,   198,   199,   240,   241,   242,   200,   201,
     202,   203,   204,   334,   123,   506,   509,   338,   507,   510,
     205,   113,   114,   243,   244,   245,   246,   247,   248,   249,
     250,   251,   252,   228,  -110,    89,   229,   260,   115,   261,
     207,   116,   262,   117,   263,   390,   118,   119,   120,   121,
      13,   162,   146,   264,   265,   266,   267,   122,   124,   125,
     268,   269,   270,   271,   272,   273,   274,   275,   276,   277,
     126,   380,    13,   143,   146,   144,   145,   150,   285,   211,
     287,   288,   289,   290,   291,   292,   293,   294,   295,   296,
     297,   298,   299,   300,   301,   302,   303,   304,   305,   306,
     307,   308,   309,   310,   311,   312,   313,   314,   315,   316,
     317,   318,   319,   320,   321,   322,   164,   325,    76,   151,
     327,   152,    91,   153,   220,   154,   155,    98,   156,   103,
     105,   107,   157,   158,   159,   165,   212,   209,   278,   279,
     335,   280,  -107,   328,   339,   340,   341,  -109,   329,   330,
     342,   256,   256,   256,   256,   200,   201,   202,   203,   204,
     343,    57,    58,    59,   344,   345,    60,   205,   356,   357,
     358,   359,   377,   378,   381,   408,   215,   391,   160,   394,
     396,   215,   397,    57,    58,    59,   215,   409,    60,   382,
     383,   410,   411,   416,   166,   167,   417,   286,   168,   444,
     445,   446,   447,    98,   418,   194,   195,   196,   197,   198,
     199,   419,   420,   421,   200,   201,   202,   203,   204,   422,
     423,   431,   238,   238,   238,   238,   205,   427,   432,   438,
     439,   463,   466,   468,   473,   430,   499,   500,   474,   475,
     476,   501,   502,   503,   504,  -108,   161,   333,   337,   326,
     437,   336,   400,   401,   402,   403,   220,     0,   495,   220,
     220,     0,   221,     0,     0,   222,     0,     0,   223,     0,
       0,     0,     0,     0,   424,   425,   426,     0,   224,   283,
     284,   428,   429,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,   436,     0,    92,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,   256,     0,
     205,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   448,   449,   450,   451,   452,   453,   454,   455,
     456,   457,   458,   459,   331,     0,     0,     0,   332,     0,
      98,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   148,     0,     0,     0,     0,     0,   393,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   489,     0,   490,     0,     0,   496,   498,     0,
     491,     2,     3,   492,     5,     6,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     8,     0,   200,   201,   202,   203,   204,     0,   511,
     512,   513,   514,   515,   516,   205,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   256,   256,   256,   256,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   404,
     405,   406,   407,     0,     0,     0,   187,   188,   189,    10,
      11,   190,     0,   191,   192,     0,    12,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,    13,     0,    14,   497,    15,     0,     0,   205,
       0,     0,     0,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    39,
      40,    41,    42,     0,     0,    43,    44,    45,    46,    47,
      48,    49,    50,   469,   470,   471,   472,     1,     2,     3,
       4,     5,     6,     0,     0,     0,     0,     7,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     8,     0,
       0,     0,     0,     0,     0,    51,     0,     0,    52,   493,
       0,     0,     0,     0,    54,     0,     0,     0,     0,     0,
       0,    55,    56,    57,    58,    59,     0,     0,    60,    61,
      62,    63,    64,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   179,
     180,   181,     0,     0,   182,   183,     0,     0,   186,     0,
       0,     9,     0,   187,   188,   189,    10,    11,   190,     0,
     191,   192,     0,    12,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,    13,
       0,    14,     0,    15,     0,     0,   205,     0,     0,     0,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,     0,     0,     0,     0,     0,     0,     1,
       2,     3,     4,     5,     6,     0,    39,    40,    41,    42,
       0,     0,    43,    44,    45,    46,    47,    48,    49,    50,
       8,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,    51,     0,     0,    52,    53,     0,     0,   205,
       0,    54,     0,     0,     0,     0,     0,     0,    55,    56,
      57,    58,    59,     0,     0,    60,    61,    62,    63,    64,
       0,    65,    66,     0,     0,     0,     0,     0,    10,    11,
       0,     0,     0,     0,     0,    12,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    13,     0,    14,     0,    15,     0,     0,     0,     0,
       0,     0,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,     0,     0,     0,     0,     0,
       0,     0,     1,     2,     3,     4,     5,     6,    39,    40,
      41,    42,     7,     0,    43,    44,    45,    46,    47,    48,
      49,    50,     0,     8,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    51,     0,     0,    52,    53,     0,
       0,     0,     0,    54,     0,    96,     0,     0,    97,     0,
      55,    56,    57,    58,    59,     0,     0,    60,    61,    62,
      63,    64,     0,     0,     0,     0,     9,     0,     0,     0,
       0,    10,    11,     0,     0,     0,     0,     0,    12,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    13,     0,    14,     0,    15,     0,
       0,     0,     0,     0,     0,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,     0,     0,
       0,     0,     0,     0,     1,     2,     3,     4,     5,     6,
       0,    39,    40,    41,    42,     0,     0,    43,    44,    45,
      46,    47,    48,    49,    50,     8,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    51,     0,     0,
      52,    53,     0,     0,     0,     0,    54,     0,     0,     0,
       0,     0,     0,    55,    56,    57,    58,    59,     0,     0,
      60,    61,    62,    63,    64,     0,     0,     0,     9,     0,
       0,     0,     0,    10,    11,     0,     0,     0,     0,     0,
      12,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    13,     0,    14,     0,
      15,     0,     0,     0,     0,     0,     0,    16,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    26,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
       0,     0,     0,     0,     0,     0,     1,     2,     3,     4,
       5,     6,     0,    39,    40,    41,    42,     0,     0,    43,
      44,    45,    46,    47,    48,    49,    50,     8,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    51,
       0,     0,    52,    53,     0,     0,     0,     0,    54,     0,
       0,     0,     0,     0,     0,    55,    56,    57,    58,    59,
       0,     0,    60,    61,    62,    63,    64,     0,     0,     0,
       0,     0,     0,     0,     0,    10,    11,     0,     0,     0,
       0,     0,    12,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    13,     0,
      14,     0,    15,     0,     0,     0,     0,     0,     0,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,     0,     0,     0,     0,     0,     0,     1,     2,
       3,     4,     5,     6,     0,    39,    40,    41,    42,     0,
       0,    43,    44,    45,    46,    47,    48,    49,    50,     8,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    51,     0,     0,    52,    53,     0,     0,     0,     0,
      54,     0,     0,     0,     0,     0,     0,    55,    56,    57,
      58,    59,     0,     0,    60,    61,    62,    63,    64,     0,
       0,     0,     0,     0,     0,     0,     0,    10,    11,     0,
       0,     0,     0,     0,    12,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      13,     0,    14,     0,   127,     0,     0,     0,     0,     0,
       0,    16,    17,    18,    19,    20,    21,    22,    23,    24,
      25,    26,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,     0,     0,     0,     0,     0,     0,
       1,     2,     3,     4,     5,     6,     0,    39,    40,    41,
      42,     0,     0,    43,    44,    45,    46,    47,    48,    49,
      50,     8,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    51,     0,     0,    52,    53,     0,     0,
       0,     0,    54,     0,     0,     0,     0,     0,     0,    55,
      56,    57,    58,    59,     0,     0,    60,    61,    62,    63,
      64,     0,     0,     0,     0,     0,     0,     0,     0,    10,
      11,     0,     0,     0,     0,     0,    12,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    13,     0,    14,     0,   129,     0,     0,     0,
       0,     0,     0,    16,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,     0,     0,     0,     0,
       0,     0,     1,     2,     3,     4,     5,     6,     0,    39,
      40,    41,    42,     0,     0,    43,    44,    45,    46,    47,
      48,    49,    50,     8,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    51,     0,     0,    52,    53,
       0,     0,     0,     0,    54,     0,     0,     0,     0,     0,
       0,    55,    56,    57,    58,    59,     0,     0,    60,    61,
      62,    63,    64,     0,     0,     0,     0,     0,     0,     0,
       0,    10,    11,     0,     0,     0,     0,     0,    12,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    13,     0,    14,     0,   132,     0,
       0,     0,     0,     0,     0,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,     0,     0,
       0,     0,     0,     0,     1,     2,     3,     4,     5,     6,
       0,    39,    40,    41,    42,     0,     0,    43,    44,    45,
      46,    47,    48,    49,    50,     8,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    51,     0,     0,
      52,    53,     0,     0,     0,     0,    54,     0,     0,     0,
       0,     0,     0,    55,    56,    57,    58,    59,     0,     0,
      60,    61,    62,    63,    64,     0,     0,     0,     0,     0,
       0,     0,     0,    10,    11,     0,     0,     0,   169,     0,
      12,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,    13,     0,    14,     0,
     134,     0,     0,     0,     0,     0,     0,    16,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    26,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    39,    40,    41,    42,     0,     0,    43,
      44,    45,    46,    47,    48,    49,    50,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    51,
       0,     0,    52,    53,     0,     0,     0,     0,    54,     0,
       0,     0,     0,     0,     0,    55,    56,    57,    58,    59,
       0,     0,    60,    61,    62,    63,    64,   170,   171,   172,
     173,   174,   175,   176,   177,   178,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   179,   180,   181,     0,     0,   182,   183,
     184,   185,   186,     0,     0,     0,     0,   187,   188,   189,
     346,     0,   190,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205,     0,     0,     0,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,   347,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,     0,     0,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,   348,     0,   190,     0,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,     0,     0,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,   349,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,     0,     0,     0,   170,   171,   172,   173,   174,
     175,   176,   177,   178,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   179,   180,   181,     0,     0,   182,   183,   184,   185,
     186,     0,     0,     0,     0,   187,   188,   189,   350,     0,
     190,     0,   191,   192,     0,     0,   193,   194,   195,   196,
     197,   198,   199,     0,     0,     0,   200,   201,   202,   203,
     204,     0,     0,     0,     0,     0,     0,     0,   205,     0,
       0,     0,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,   351,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,     0,     0,     0,   170,
     171,   172,   173,   174,   175,   176,   177,   178,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   179,   180,   181,     0,     0,
     182,   183,   184,   185,   186,     0,     0,     0,     0,   187,
     188,   189,   352,     0,   190,     0,   191,   192,     0,     0,
     193,   194,   195,   196,   197,   198,   199,     0,     0,     0,
     200,   201,   202,   203,   204,     0,     0,     0,     0,     0,
       0,     0,   205,     0,     0,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,   353,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,     0,     0,   170,   171,   172,   173,   174,   175,   176,
     177,   178,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   179,
     180,   181,     0,     0,   182,   183,   184,   185,   186,     0,
       0,     0,     0,   187,   188,   189,   354,     0,   190,     0,
     191,   192,     0,     0,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,     0,
       0,     0,     0,     0,     0,     0,   205,     0,     0,     0,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,   355,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,     0,     0,     0,   170,   171,   172,
     173,   174,   175,   176,   177,   178,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   179,   180,   181,     0,     0,   182,   183,
     184,   185,   186,     0,     0,     0,     0,   187,   188,   189,
     367,     0,   190,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205,     0,     0,     0,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,   369,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,     0,     0,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,   370,     0,   190,     0,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,     0,     0,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,   373,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,     0,     0,     0,   170,   171,   172,   173,   174,
     175,   176,   177,   178,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   179,   180,   181,     0,     0,   182,   183,   184,   185,
     186,     0,     0,     0,     0,   187,   188,   189,   374,     0,
     190,     0,   191,   192,     0,     0,   193,   194,   195,   196,
     197,   198,   199,     0,     0,     0,   200,   201,   202,   203,
     204,     0,     0,     0,     0,     0,     0,     0,   205,     0,
       0,     0,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,   375,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,     0,     0,     0,   170,
     171,   172,   173,   174,   175,   176,   177,   178,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   179,   180,   181,     0,     0,
     182,   183,   184,   185,   186,     0,     0,     0,     0,   187,
     188,   189,   384,     0,   190,     0,   191,   192,     0,     0,
     193,   194,   195,   196,   197,   198,   199,     0,     0,     0,
     200,   201,   202,   203,   204,     0,     0,     0,     0,     0,
       0,     0,   205,     0,     0,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,   440,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,     0,     0,   170,   171,   172,   173,   174,   175,   176,
     177,   178,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   179,
     180,   181,     0,     0,   182,   183,   184,   185,   186,     0,
       0,     0,     0,   187,   188,   189,   441,     0,   190,     0,
     191,   192,     0,     0,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,     0,
       0,     0,     0,     0,     0,     0,   205,     0,     0,     0,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,   442,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,     0,     0,     0,   170,   171,   172,
     173,   174,   175,   176,   177,   178,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   179,   180,   181,     0,     0,   182,   183,
     184,   185,   186,     0,     0,     0,     0,   187,   188,   189,
     443,     0,   190,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205,     0,     0,     0,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,   464,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,     0,     0,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,   465,     0,   190,     0,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,     0,     0,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,   477,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,     0,     0,     0,   170,   171,   172,   173,   174,
     175,   176,   177,   178,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   179,   180,   181,     0,     0,   182,   183,   184,   185,
     186,     0,     0,     0,     0,   187,   188,   189,   479,     0,
     190,     0,   191,   192,     0,     0,   193,   194,   195,   196,
     197,   198,   199,     0,     0,     0,   200,   201,   202,   203,
     204,     0,     0,     0,     0,     0,     0,     0,   205,     0,
       0,     0,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,   481,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,     0,     0,     0,   170,
     171,   172,   173,   174,   175,   176,   177,   178,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   179,   180,   181,     0,     0,
     182,   183,   184,   185,   186,     0,     0,     0,     0,   187,
     188,   189,   482,     0,   190,     0,   191,   192,     0,     0,
     193,   194,   195,   196,   197,   198,   199,     0,     0,     0,
     200,   201,   202,   203,   204,     0,     0,     0,     0,     0,
       0,     0,   205,     0,     0,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,   483,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,     0,     0,   170,   171,   172,   173,   174,   175,   176,
     177,   178,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   179,
     180,   181,     0,     0,   182,   183,   184,   185,   186,     0,
       0,     0,     0,   187,   188,   189,   484,     0,   190,     0,
     191,   192,     0,     0,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,     0,
       0,     0,     0,     0,     0,     0,   205,     0,     0,     0,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,   485,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,     0,     0,     0,   170,   171,   172,
     173,   174,   175,   176,   177,   178,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   179,   180,   181,     0,     0,   182,   183,
     184,   185,   186,     0,     0,     0,     0,   187,   188,   189,
     486,     0,   190,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205,     0,     0,     0,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,   487,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,     0,     0,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,   488,     0,   190,     0,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,     0,     0,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,   505,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,     0,     0,     0,   170,   171,   172,   173,   174,
     175,   176,   177,   178,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   179,   180,   181,     0,     0,   182,   183,   184,   185,
     186,     0,     0,     0,     0,   187,   188,   189,   517,     0,
     190,     0,   191,   192,     0,     0,   193,   194,   195,   196,
     197,   198,   199,     0,     0,     0,   200,   201,   202,   203,
     204,     0,     0,     0,     0,     0,     0,     0,   205,     0,
       0,     0,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,   518,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,     0,     0,     0,   170,
     171,   172,   173,   174,   175,   176,   177,   178,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,   179,   180,   181,     0,     0,
     182,   183,   184,   185,   186,     0,     0,     0,     0,   187,
     188,   189,   519,     0,   190,     0,   191,   192,     0,     0,
     193,   194,   195,   196,   197,   198,   199,     0,     0,     0,
     200,   201,   202,   203,   204,     0,     0,     0,     0,     0,
       0,     0,   205,     0,     0,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,   520,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,     0,     0,   170,   171,   172,   173,   174,   175,   176,
     177,   178,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   179,
     180,   181,     0,     0,   182,   183,   184,   185,   186,     0,
       0,     0,     0,   187,   188,   189,   521,     0,   190,     0,
     191,   192,     0,     0,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,     0,
       0,     0,     0,     0,     0,     0,   205,     0,     0,     0,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,   522,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,     0,     0,     0,   170,   171,   172,
     173,   174,   175,   176,   177,   178,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,   179,   180,   181,     0,     0,   182,   183,
     184,   185,   186,     0,     0,     0,     0,   187,   188,   189,
       0,     0,   190,   230,   191,   192,     0,  -193,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205,     0,     0,     0,     0,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,   230,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,   231,   232,     0,   205,
       0,     0,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,     0,   360,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,   235,   236,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
     361,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,   235,   236,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,     0,   362,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
     235,   236,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,     0,   363,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,   235,   236,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,     0,   386,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,     0,   398,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
     399,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,     0,   460,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,     0,   461,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,     0,   478,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,     0,   480,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,   366,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,     0,     0,   190,   368,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,   371,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,     0,     0,   190,   372,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,   376,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
       0,   170,   171,   172,   173,   174,   175,   176,   177,   178,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,   179,   180,   181,
       0,     0,   182,   183,   184,   185,   186,     0,     0,     0,
       0,   187,   188,   189,     0,     0,   190,   462,   191,   192,
       0,     0,   193,   194,   195,   196,   197,   198,   199,     0,
       0,     0,   200,   201,   202,   203,   204,     0,     0,     0,
       0,     0,     0,     0,   205,     0,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,   235,   236,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,     0,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,     0,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,     0,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,   231,   232,     0,   205,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,   210,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,     0,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,   364,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,   184,   185,   186,     0,     0,
       0,     0,   187,   188,   189,     0,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,     0,     0,
       0,     0,     0,     0,     0,   205,   170,   171,   172,   173,
     174,   175,   176,   177,   178,     0,     0,     0,     0,     0,
       0,     0,   365,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   179,   180,   181,     0,     0,   182,   183,   184,
     185,   186,     0,     0,     0,     0,   187,   188,   189,     0,
       0,   190,     0,   191,   192,     0,     0,   193,   194,   195,
     196,   197,   198,   199,     0,     0,     0,   200,   201,   202,
     203,   204,     0,     0,     0,     0,     0,     0,     0,   205,
     170,   171,   172,   173,   174,   175,   176,   177,   178,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   179,   180,   181,   385,
       0,   182,   183,   184,   185,   186,     0,     0,     0,     0,
     187,   188,   189,     0,     0,   190,     0,   191,   192,     0,
       0,   193,   194,   195,   196,   197,   198,   199,     0,     0,
       0,   200,   201,   202,   203,   204,     0,     0,     0,     0,
       0,     0,     0,   205,   170,   171,   172,   173,   174,   175,
     176,   177,   178,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,   387,   182,   183,   184,   185,   186,
       0,     0,     0,     0,   187,   188,   189,     0,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,   170,   171,
     172,   173,   174,   175,   176,   177,   178,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   179,   180,   181,     0,     0,   182,
     183,   184,   185,   186,     0,     0,     0,     0,   187,   188,
     189,     0,     0,   190,     0,   191,   192,     0,     0,   193,
     194,   195,   196,   197,   198,   199,     0,     0,     0,   200,
     201,   202,   203,   204,     0,     0,     0,     0,     0,     0,
       0,   205,   170,   171,   172,   173,   174,   175,   176,   177,
     178,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   179,   180,
     181,     0,     0,   182,   183,     0,     0,   186,     0,     0,
       0,     0,   187,   188,   189,     0,     0,   190,     0,   191,
     192,     0,     0,   193,   194,   195,   196,   197,   198,   199,
       0,     0,     0,   200,   201,   202,   203,   204,   174,   175,
     176,   177,   178,     0,     0,   205,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     179,   180,   181,     0,     0,   182,   183,     0,     0,   186,
       0,     0,     0,     0,   187,   188,   189,     0,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,   178,     0,     0,   200,   201,   202,   203,   204,
       0,     0,     0,     0,     0,     0,     0,   205,     0,     0,
     179,   180,   181,     0,     0,   182,   183,     0,     0,   186,
       0,     0,     0,     0,   187,   188,   189,     0,     0,   190,
       0,   191,   192,     0,     0,   193,   194,   195,   196,   197,
     198,   199,     0,     0,     0,   200,   201,   202,   203,   204,
       0,   181,     0,     0,   182,   183,     0,   205,   186,     0,
       0,     0,     0,   187,   188,   189,     0,     0,   190,     0,
     191,   192,     0,     0,   193,   194,   195,   196,   197,   198,
     199,     0,     0,     0,   200,   201,   202,   203,   204,   183,
       0,     0,   186,     0,     0,     0,   205,   187,   188,   189,
       0,     0,   190,     0,   191,   192,     0,     0,   193,   194,
     195,   196,   197,   198,   199,     0,     0,     0,   200,   201,
     202,   203,   204,     0,     0,     0,     0,     0,     0,     0,
     205
};

static const yytype_int16 yycheck[] =
{
       0,    52,    53,    54,   123,   124,   125,   126,   102,   217,
     218,   219,    12,    13,    14,    15,    16,    17,    18,   227,
     119,    85,   122,    16,   123,     3,    85,   121,     7,     8,
       9,    10,    11,    12,   184,   121,    28,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,    48,    28,
       7,     8,     9,    10,    11,    12,     1,     7,     7,   123,
      10,    10,     7,   119,   123,    10,    66,     7,     7,   122,
      10,    28,   125,   223,   122,   119,   226,   125,    28,    28,
     119,   115,   116,    28,   184,   119,   119,   119,    28,    28,
      90,   123,    85,   210,   211,   110,   111,   112,   215,   216,
     217,   218,   219,   228,   123,   122,   122,   232,   125,   125,
     227,   119,   119,   113,   114,   115,   116,   117,   118,   119,
     120,   121,   122,   223,   183,     7,   226,   127,   119,   129,
     123,   119,   132,   119,   134,    84,   119,   119,   119,   119,
     119,     0,   121,   143,   144,   145,   146,   119,   123,   123,
     150,   151,   152,   153,   154,   155,   156,   157,   158,   159,
     123,   280,   119,   123,   121,   123,   119,   119,   168,   107,
     170,   171,   172,   173,   174,   175,   176,   177,   178,   179,
     180,   181,   182,   183,   184,   185,   186,   187,   188,   189,
     190,   191,   192,   193,   194,   195,   196,   197,   198,   199,
     200,   201,   202,   203,   204,   205,   184,   207,   208,   119,
     210,   119,     9,   119,    96,   119,   119,    14,   119,    16,
      17,    18,   119,   119,   119,    28,   120,   227,   184,   184,
     230,   123,   183,     7,   234,   235,   236,   183,   124,   183,
     125,   123,   124,   125,   126,   215,   216,   217,   218,   219,
     125,   230,   231,   232,   125,   125,   235,   227,   124,   124,
     124,   124,     3,     3,   180,   123,   216,   216,    65,   124,
     124,   216,   124,   230,   231,   232,   216,   123,   235,   221,
     221,   123,   123,   119,   115,   116,   119,   169,   119,   408,
     409,   410,   411,    90,   119,   206,   207,   208,   209,   210,
     211,   119,   119,   119,   215,   216,   217,   218,   219,   119,
     119,   124,   109,   110,   111,   112,   227,   368,   124,     7,
     122,   120,   120,   183,   124,   376,   119,   119,   124,   124,
     124,   119,   119,   119,   119,   183,    66,   227,   231,   208,
     387,   230,   342,   343,   344,   345,   228,    -1,   467,   231,
     232,    -1,   183,    -1,    -1,   186,    -1,    -1,   189,    -1,
      -1,    -1,    -1,    -1,   364,   365,   366,    -1,   199,   166,
     167,   371,   372,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,   385,    -1,   387,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,   280,    -1,
     227,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   412,   413,   414,   415,   416,   417,   418,   419,
     420,   421,   422,   423,   221,    -1,    -1,    -1,   225,    -1,
     227,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   493,    -1,    -1,    -1,    -1,    -1,   330,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   462,    -1,     1,    -1,    -1,   467,   468,    -1,
       7,     8,     9,    10,    11,    12,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    28,    -1,   215,   216,   217,   218,   219,    -1,   499,
     500,   501,   502,   503,   504,   227,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   408,   409,   410,   411,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   346,
     347,   348,   349,    -1,    -1,    -1,   194,   195,   196,    96,
      97,   199,    -1,   201,   202,    -1,   103,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,   119,    -1,   121,   467,   123,    -1,    -1,   227,
      -1,    -1,    -1,   130,   131,   132,   133,   134,   135,   136,
     137,   138,   139,   140,   141,   142,   143,   144,   145,   146,
     147,   148,   149,   150,   151,   152,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   166,
     167,   168,   169,    -1,    -1,   172,   173,   174,   175,   176,
     177,   178,   179,   440,   441,   442,   443,     7,     8,     9,
      10,    11,    12,    -1,    -1,    -1,    -1,    17,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    28,    -1,
      -1,    -1,    -1,    -1,    -1,   212,    -1,    -1,   215,   216,
      -1,    -1,    -1,    -1,   221,    -1,    -1,    -1,    -1,    -1,
      -1,   228,   229,   230,   231,   232,    -1,    -1,   235,   236,
     237,   238,   239,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,
     181,   182,    -1,    -1,   185,   186,    -1,    -1,   189,    -1,
      -1,    91,    -1,   194,   195,   196,    96,    97,   199,    -1,
     201,   202,    -1,   103,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,   119,
      -1,   121,    -1,   123,    -1,    -1,   227,    -1,    -1,    -1,
     130,   131,   132,   133,   134,   135,   136,   137,   138,   139,
     140,   141,   142,   143,   144,   145,   146,   147,   148,   149,
     150,   151,   152,    -1,    -1,    -1,    -1,    -1,    -1,     7,
       8,     9,    10,    11,    12,    -1,   166,   167,   168,   169,
      -1,    -1,   172,   173,   174,   175,   176,   177,   178,   179,
      28,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,   212,    -1,    -1,   215,   216,    -1,    -1,   227,
      -1,   221,    -1,    -1,    -1,    -1,    -1,    -1,   228,   229,
     230,   231,   232,    -1,    -1,   235,   236,   237,   238,   239,
      -1,   241,   242,    -1,    -1,    -1,    -1,    -1,    96,    97,
      -1,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   119,    -1,   121,    -1,   123,    -1,    -1,    -1,    -1,
      -1,    -1,   130,   131,   132,   133,   134,   135,   136,   137,
     138,   139,   140,   141,   142,   143,   144,   145,   146,   147,
     148,   149,   150,   151,   152,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,     7,     8,     9,    10,    11,    12,   166,   167,
     168,   169,    17,    -1,   172,   173,   174,   175,   176,   177,
     178,   179,    -1,    28,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   212,    -1,    -1,   215,   216,    -1,
      -1,    -1,    -1,   221,    -1,   223,    -1,    -1,   226,    -1,
     228,   229,   230,   231,   232,    -1,    -1,   235,   236,   237,
     238,   239,    -1,    -1,    -1,    -1,    91,    -1,    -1,    -1,
      -1,    96,    97,    -1,    -1,    -1,    -1,    -1,   103,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   119,    -1,   121,    -1,   123,    -1,
      -1,    -1,    -1,    -1,    -1,   130,   131,   132,   133,   134,
     135,   136,   137,   138,   139,   140,   141,   142,   143,   144,
     145,   146,   147,   148,   149,   150,   151,   152,    -1,    -1,
      -1,    -1,    -1,    -1,     7,     8,     9,    10,    11,    12,
      -1,   166,   167,   168,   169,    -1,    -1,   172,   173,   174,
     175,   176,   177,   178,   179,    28,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   212,    -1,    -1,
     215,   216,    -1,    -1,    -1,    -1,   221,    -1,    -1,    -1,
      -1,    -1,    -1,   228,   229,   230,   231,   232,    -1,    -1,
     235,   236,   237,   238,   239,    -1,    -1,    -1,    91,    -1,
      -1,    -1,    -1,    96,    97,    -1,    -1,    -1,    -1,    -1,
     103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   119,    -1,   121,    -1,
     123,    -1,    -1,    -1,    -1,    -1,    -1,   130,   131,   132,
     133,   134,   135,   136,   137,   138,   139,   140,   141,   142,
     143,   144,   145,   146,   147,   148,   149,   150,   151,   152,
      -1,    -1,    -1,    -1,    -1,    -1,     7,     8,     9,    10,
      11,    12,    -1,   166,   167,   168,   169,    -1,    -1,   172,
     173,   174,   175,   176,   177,   178,   179,    28,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   212,
      -1,    -1,   215,   216,    -1,    -1,    -1,    -1,   221,    -1,
      -1,    -1,    -1,    -1,    -1,   228,   229,   230,   231,   232,
      -1,    -1,   235,   236,   237,   238,   239,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    96,    97,    -1,    -1,    -1,
      -1,    -1,   103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   119,    -1,
     121,    -1,   123,    -1,    -1,    -1,    -1,    -1,    -1,   130,
     131,   132,   133,   134,   135,   136,   137,   138,   139,   140,
     141,   142,   143,   144,   145,   146,   147,   148,   149,   150,
     151,   152,    -1,    -1,    -1,    -1,    -1,    -1,     7,     8,
       9,    10,    11,    12,    -1,   166,   167,   168,   169,    -1,
      -1,   172,   173,   174,   175,   176,   177,   178,   179,    28,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   212,    -1,    -1,   215,   216,    -1,    -1,    -1,    -1,
     221,    -1,    -1,    -1,    -1,    -1,    -1,   228,   229,   230,
     231,   232,    -1,    -1,   235,   236,   237,   238,   239,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    96,    97,    -1,
      -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     119,    -1,   121,    -1,   123,    -1,    -1,    -1,    -1,    -1,
      -1,   130,   131,   132,   133,   134,   135,   136,   137,   138,
     139,   140,   141,   142,   143,   144,   145,   146,   147,   148,
     149,   150,   151,   152,    -1,    -1,    -1,    -1,    -1,    -1,
       7,     8,     9,    10,    11,    12,    -1,   166,   167,   168,
     169,    -1,    -1,   172,   173,   174,   175,   176,   177,   178,
     179,    28,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   212,    -1,    -1,   215,   216,    -1,    -1,
      -1,    -1,   221,    -1,    -1,    -1,    -1,    -1,    -1,   228,
     229,   230,   231,   232,    -1,    -1,   235,   236,   237,   238,
     239,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    96,
      97,    -1,    -1,    -1,    -1,    -1,   103,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   119,    -1,   121,    -1,   123,    -1,    -1,    -1,
      -1,    -1,    -1,   130,   131,   132,   133,   134,   135,   136,
     137,   138,   139,   140,   141,   142,   143,   144,   145,   146,
     147,   148,   149,   150,   151,   152,    -1,    -1,    -1,    -1,
      -1,    -1,     7,     8,     9,    10,    11,    12,    -1,   166,
     167,   168,   169,    -1,    -1,   172,   173,   174,   175,   176,
     177,   178,   179,    28,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   212,    -1,    -1,   215,   216,
      -1,    -1,    -1,    -1,   221,    -1,    -1,    -1,    -1,    -1,
      -1,   228,   229,   230,   231,   232,    -1,    -1,   235,   236,
     237,   238,   239,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    96,    97,    -1,    -1,    -1,    -1,    -1,   103,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   119,    -1,   121,    -1,   123,    -1,
      -1,    -1,    -1,    -1,    -1,   130,   131,   132,   133,   134,
     135,   136,   137,   138,   139,   140,   141,   142,   143,   144,
     145,   146,   147,   148,   149,   150,   151,   152,    -1,    -1,
      -1,    -1,    -1,    -1,     7,     8,     9,    10,    11,    12,
      -1,   166,   167,   168,   169,    -1,    -1,   172,   173,   174,
     175,   176,   177,   178,   179,    28,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   212,    -1,    -1,
     215,   216,    -1,    -1,    -1,    -1,   221,    -1,    -1,    -1,
      -1,    -1,    -1,   228,   229,   230,   231,   232,    -1,    -1,
     235,   236,   237,   238,   239,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    96,    97,    -1,    -1,    -1,    15,    -1,
     103,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   119,    -1,   121,    -1,
     123,    -1,    -1,    -1,    -1,    -1,    -1,   130,   131,   132,
     133,   134,   135,   136,   137,   138,   139,   140,   141,   142,
     143,   144,   145,   146,   147,   148,   149,   150,   151,   152,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   166,   167,   168,   169,    -1,    -1,   172,
     173,   174,   175,   176,   177,   178,   179,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   212,
      -1,    -1,   215,   216,    -1,    -1,    -1,    -1,   221,    -1,
      -1,    -1,    -1,    -1,    -1,   228,   229,   230,   231,   232,
      -1,    -1,   235,   236,   237,   238,   239,   154,   155,   156,
     157,   158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,
     187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,
     120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227,    -1,    -1,    -1,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,   120,    -1,   199,    -1,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,   158,
     159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   180,   181,   182,    -1,    -1,   185,   186,   187,   188,
     189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,
     199,    -1,   201,   202,    -1,    -1,   205,   206,   207,   208,
     209,   210,   211,    -1,    -1,    -1,   215,   216,   217,   218,
     219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,
      -1,    -1,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,
     155,   156,   157,   158,   159,   160,   161,   162,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,
     185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,
     195,   196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,
     205,   206,   207,   208,   209,   210,   211,    -1,    -1,    -1,
     215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,    -1,    -1,   154,   155,   156,   157,   158,   159,   160,
     161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,
     181,   182,    -1,    -1,   185,   186,   187,   188,   189,    -1,
      -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,
     201,   202,    -1,    -1,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,   120,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,
     157,   158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,
     187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,
     120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227,    -1,    -1,    -1,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,   120,    -1,   199,    -1,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,   158,
     159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   180,   181,   182,    -1,    -1,   185,   186,   187,   188,
     189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,
     199,    -1,   201,   202,    -1,    -1,   205,   206,   207,   208,
     209,   210,   211,    -1,    -1,    -1,   215,   216,   217,   218,
     219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,
      -1,    -1,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,
     155,   156,   157,   158,   159,   160,   161,   162,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,
     185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,
     195,   196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,
     205,   206,   207,   208,   209,   210,   211,    -1,    -1,    -1,
     215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,    -1,    -1,   154,   155,   156,   157,   158,   159,   160,
     161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,
     181,   182,    -1,    -1,   185,   186,   187,   188,   189,    -1,
      -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,
     201,   202,    -1,    -1,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,   120,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,
     157,   158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,
     187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,
     120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227,    -1,    -1,    -1,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,   120,    -1,   199,    -1,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,   158,
     159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   180,   181,   182,    -1,    -1,   185,   186,   187,   188,
     189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,
     199,    -1,   201,   202,    -1,    -1,   205,   206,   207,   208,
     209,   210,   211,    -1,    -1,    -1,   215,   216,   217,   218,
     219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,
      -1,    -1,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,
     155,   156,   157,   158,   159,   160,   161,   162,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,
     185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,
     195,   196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,
     205,   206,   207,   208,   209,   210,   211,    -1,    -1,    -1,
     215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,    -1,    -1,   154,   155,   156,   157,   158,   159,   160,
     161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,
     181,   182,    -1,    -1,   185,   186,   187,   188,   189,    -1,
      -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,
     201,   202,    -1,    -1,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,   120,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,
     157,   158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,
     187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,
     120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227,    -1,    -1,    -1,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,   120,    -1,   199,    -1,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,   158,
     159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   180,   181,   182,    -1,    -1,   185,   186,   187,   188,
     189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,    -1,
     199,    -1,   201,   202,    -1,    -1,   205,   206,   207,   208,
     209,   210,   211,    -1,    -1,    -1,   215,   216,   217,   218,
     219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,
      -1,    -1,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,   154,
     155,   156,   157,   158,   159,   160,   161,   162,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,
     185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,
     195,   196,   120,    -1,   199,    -1,   201,   202,    -1,    -1,
     205,   206,   207,   208,   209,   210,   211,    -1,    -1,    -1,
     215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,   120,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,    -1,    -1,   154,   155,   156,   157,   158,   159,   160,
     161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,
     181,   182,    -1,    -1,   185,   186,   187,   188,   189,    -1,
      -1,    -1,    -1,   194,   195,   196,   120,    -1,   199,    -1,
     201,   202,    -1,    -1,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,    -1,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,   120,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,    -1,    -1,    -1,   154,   155,   156,
     157,   158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,
     187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,
      -1,    -1,   199,   121,   201,   202,    -1,   125,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227,    -1,    -1,    -1,    -1,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,   121,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,   224,   225,    -1,   227,
      -1,    -1,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,    -1,   124,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   170,   171,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
     124,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   170,   171,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,    -1,   124,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     170,   171,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,   124,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   170,   171,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,    -1,   124,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,    -1,   124,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
     124,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,    -1,   124,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,   124,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,    -1,   124,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,    -1,   124,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,   125,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,    -1,    -1,   199,   125,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,   125,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,    -1,    -1,   199,   125,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,   125,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
      -1,   154,   155,   156,   157,   158,   159,   160,   161,   162,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,
      -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,
      -1,   194,   195,   196,    -1,    -1,   199,   125,   201,   202,
      -1,    -1,   205,   206,   207,   208,   209,   210,   211,    -1,
      -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   227,    -1,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   170,   171,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,    -1,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,    -1,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,   224,   225,    -1,   227,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,   183,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,    -1,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   170,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,   187,   188,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,    -1,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   227,   154,   155,   156,   157,
     158,   159,   160,   161,   162,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   170,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   180,   181,   182,    -1,    -1,   185,   186,   187,
     188,   189,    -1,    -1,    -1,    -1,   194,   195,   196,    -1,
      -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,   207,
     208,   209,   210,   211,    -1,    -1,    -1,   215,   216,   217,
     218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,
     154,   155,   156,   157,   158,   159,   160,   161,   162,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   180,   181,   182,   183,
      -1,   185,   186,   187,   188,   189,    -1,    -1,    -1,    -1,
     194,   195,   196,    -1,    -1,   199,    -1,   201,   202,    -1,
      -1,   205,   206,   207,   208,   209,   210,   211,    -1,    -1,
      -1,   215,   216,   217,   218,   219,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,   227,   154,   155,   156,   157,   158,   159,
     160,   161,   162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,   184,   185,   186,   187,   188,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,   154,   155,
     156,   157,   158,   159,   160,   161,   162,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,   180,   181,   182,    -1,    -1,   185,
     186,   187,   188,   189,    -1,    -1,    -1,    -1,   194,   195,
     196,    -1,    -1,   199,    -1,   201,   202,    -1,    -1,   205,
     206,   207,   208,   209,   210,   211,    -1,    -1,    -1,   215,
     216,   217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,   227,   154,   155,   156,   157,   158,   159,   160,   161,
     162,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   180,   181,
     182,    -1,    -1,   185,   186,    -1,    -1,   189,    -1,    -1,
      -1,    -1,   194,   195,   196,    -1,    -1,   199,    -1,   201,
     202,    -1,    -1,   205,   206,   207,   208,   209,   210,   211,
      -1,    -1,    -1,   215,   216,   217,   218,   219,   158,   159,
     160,   161,   162,    -1,    -1,   227,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,    -1,    -1,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,   162,    -1,    -1,   215,   216,   217,   218,   219,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   227,    -1,    -1,
     180,   181,   182,    -1,    -1,   185,   186,    -1,    -1,   189,
      -1,    -1,    -1,    -1,   194,   195,   196,    -1,    -1,   199,
      -1,   201,   202,    -1,    -1,   205,   206,   207,   208,   209,
     210,   211,    -1,    -1,    -1,   215,   216,   217,   218,   219,
      -1,   182,    -1,    -1,   185,   186,    -1,   227,   189,    -1,
      -1,    -1,    -1,   194,   195,   196,    -1,    -1,   199,    -1,
     201,   202,    -1,    -1,   205,   206,   207,   208,   209,   210,
     211,    -1,    -1,    -1,   215,   216,   217,   218,   219,   186,
      -1,    -1,   189,    -1,    -1,    -1,   227,   194,   195,   196,
      -1,    -1,   199,    -1,   201,   202,    -1,    -1,   205,   206,
     207,   208,   209,   210,   211,    -1,    -1,    -1,   215,   216,
     217,   218,   219,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
     227
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint16 yystos[] =
{
       0,     7,     8,     9,    10,    11,    12,    17,    28,    91,
      96,    97,   103,   119,   121,   123,   130,   131,   132,   133,
     134,   135,   136,   137,   138,   139,   140,   141,   142,   143,
     144,   145,   146,   147,   148,   149,   150,   151,   152,   166,
     167,   168,   169,   172,   173,   174,   175,   176,   177,   178,
     179,   212,   215,   216,   221,   228,   229,   230,   231,   232,
     235,   236,   237,   238,   239,   241,   242,   244,   245,   246,
     247,   248,   254,   256,   257,   265,   266,   267,   268,   269,
     270,   272,   273,   274,   275,   276,   277,   279,   281,   277,
     121,   257,   266,   271,   266,   278,   223,   226,   257,   258,
     266,   280,   266,   257,   266,   257,   266,   257,   266,   119,
     119,   119,   119,   119,   119,   119,   119,   119,   119,   119,
     119,   119,   119,   123,   123,   123,   123,   123,   266,   123,
     266,   266,   123,   266,   123,   266,   266,   266,   266,   266,
     266,   266,   266,   123,   123,   119,   121,   276,   276,   276,
     119,   119,   119,   119,   119,   119,   119,   119,   119,   119,
     257,   245,     0,     3,   184,    28,   115,   116,   119,    15,
     154,   155,   156,   157,   158,   159,   160,   161,   162,   180,
     181,   182,   185,   186,   187,   188,   189,   194,   195,   196,
     199,   201,   202,   205,   206,   207,   208,   209,   210,   211,
     215,   216,   217,   218,   219,   227,    85,   123,    16,   266,
     183,   107,   120,     7,    10,   216,   260,   261,   262,   263,
     277,   183,   186,   189,   199,   259,   122,   184,   223,   226,
     121,   224,   225,   122,   125,   170,   171,   255,   257,   266,
     255,   255,   255,   266,   266,   266,   266,   266,   266,   266,
     266,   266,   266,     7,    10,   262,   277,   262,   262,   262,
     266,   266,   266,   266,   266,   266,   266,   266,   266,   266,
     266,   266,   266,   266,   266,   266,   266,   266,   184,   184,
     123,   249,   250,   257,   257,   266,   277,   266,   266,   266,
     266,   266,   266,   266,   266,   266,   266,   266,   266,   266,
     266,   266,   266,   266,   266,   266,   266,   266,   266,   266,
     266,   266,   266,   266,   266,   266,   266,   266,   266,   266,
     266,   266,   266,     7,    28,   266,   246,   266,     7,   124,
     183,   257,   257,   258,   260,   266,   280,   261,   260,   266,
     266,   266,   125,   125,   125,   125,   120,   120,   120,   120,
     120,   120,   120,   120,   120,   120,   124,   124,   124,   124,
     124,   124,   124,   124,   170,   170,   125,   120,   125,   120,
     120,   125,   125,   120,   120,   120,   125,     3,     3,     1,
     262,   180,   221,   221,   120,   183,   124,   184,     7,    10,
      84,   216,   264,   277,   124,   122,   124,   124,   124,   124,
     266,   266,   266,   266,   257,   257,   257,   257,   123,   123,
     123,   123,   119,   123,   119,   123,   119,   119,   119,   119,
     119,   119,   119,   119,   266,   266,   266,   276,   266,   266,
     276,   124,   124,   102,   121,   251,   266,   271,     7,   122,
     120,   120,   120,   120,   262,   262,   262,   262,   266,   266,
     266,   266,   266,   266,   266,   266,   266,   266,   266,   266,
     124,   124,   125,   120,   120,   120,   120,   252,   183,   257,
     257,   257,   257,   124,   124,   124,   124,   120,   124,   120,
     124,   120,   120,   120,   120,   120,   120,   120,   120,   266,
       1,     7,    10,   216,   253,   262,   266,   277,   266,   119,
     119,   119,   119,   119,   119,   120,   122,   125,     7,   122,
     125,   266,   266,   266,   266,   266,   266,   120,   120,   120,
     120,   120,   120
};

#define yyerrok		(yyerrstatus = 0)
#define yyclearin	(yychar = YYEMPTY)
#define YYEMPTY		(-2)
#define YYEOF		0

#define YYACCEPT	goto yyacceptlab
#define YYABORT		goto yyabortlab
#define YYERROR		goto yyerrorlab


/* Like YYERROR except do call yyerror.  This remains here temporarily
   to ease the transition to the new meaning of YYERROR, for GCC.
   Once GCC version 2 has supplanted version 1, this can go.  */

#define YYFAIL		goto yyerrlab

#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)					\
do								\
  if (yychar == YYEMPTY && yylen == 1)				\
    {								\
      yychar = (Token);						\
      yylval = (Value);						\
      yytoken = YYTRANSLATE (yychar);				\
      YYPOPSTACK (1);						\
      goto yybackup;						\
    }								\
  else								\
    {								\
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;							\
    }								\
while (YYID (0))


#define YYTERROR	1
#define YYERRCODE	256


/* YYLLOC_DEFAULT -- Set CURRENT to span from RHS[1] to RHS[N].
   If N is 0, then set CURRENT to the empty location which ends
   the previous symbol: RHS[0] (always defined).  */

#define YYRHSLOC(Rhs, K) ((Rhs)[K])
#ifndef YYLLOC_DEFAULT
# define YYLLOC_DEFAULT(Current, Rhs, N)				\
    do									\
      if (YYID (N))                                                    \
	{								\
	  (Current).first_line   = YYRHSLOC (Rhs, 1).first_line;	\
	  (Current).first_column = YYRHSLOC (Rhs, 1).first_column;	\
	  (Current).last_line    = YYRHSLOC (Rhs, N).last_line;		\
	  (Current).last_column  = YYRHSLOC (Rhs, N).last_column;	\
	}								\
      else								\
	{								\
	  (Current).first_line   = (Current).last_line   =		\
	    YYRHSLOC (Rhs, 0).last_line;				\
	  (Current).first_column = (Current).last_column =		\
	    YYRHSLOC (Rhs, 0).last_column;				\
	}								\
    while (YYID (0))
#endif


/* YY_LOCATION_PRINT -- Print the location on the stream.
   This macro was not mandated originally: define only if we know
   we won't break user code: when these are the locations we know.  */

#ifndef YY_LOCATION_PRINT
# if defined YYLTYPE_IS_TRIVIAL && YYLTYPE_IS_TRIVIAL
#  define YY_LOCATION_PRINT(File, Loc)			\
     fprintf (File, "%d.%d-%d.%d",			\
	      (Loc).first_line, (Loc).first_column,	\
	      (Loc).last_line,  (Loc).last_column)
# else
#  define YY_LOCATION_PRINT(File, Loc) ((void) 0)
# endif
#endif


/* YYLEX -- calling `yylex' with the right arguments.  */

#ifdef YYLEX_PARAM
# define YYLEX yylex (YYLEX_PARAM)
#else
# define YYLEX yylex ()
#endif

/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)			\
do {						\
  if (yydebug)					\
    YYFPRINTF Args;				\
} while (YYID (0))

# define YY_SYMBOL_PRINT(Title, Type, Value, Location)			  \
do {									  \
  if (yydebug)								  \
    {									  \
      YYFPRINTF (stderr, "%s ", Title);					  \
      yy_symbol_print (stderr,						  \
		  Type, Value); \
      YYFPRINTF (stderr, "\n");						  \
    }									  \
} while (YYID (0))


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_value_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# else
  YYUSE (yyoutput);
# endif
  switch (yytype)
    {
      default:
	break;
    }
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
#else
static void
yy_symbol_print (yyoutput, yytype, yyvaluep)
    FILE *yyoutput;
    int yytype;
    YYSTYPE const * const yyvaluep;
#endif
{
  if (yytype < YYNTOKENS)
    YYFPRINTF (yyoutput, "token %s (", yytname[yytype]);
  else
    YYFPRINTF (yyoutput, "nterm %s (", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_stack_print (yytype_int16 *bottom, yytype_int16 *top)
#else
static void
yy_stack_print (bottom, top)
    yytype_int16 *bottom;
    yytype_int16 *top;
#endif
{
  YYFPRINTF (stderr, "Stack now");
  for (; bottom <= top; ++bottom)
    YYFPRINTF (stderr, " %d", *bottom);
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)				\
do {								\
  if (yydebug)							\
    yy_stack_print ((Bottom), (Top));				\
} while (YYID (0))


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yy_reduce_print (YYSTYPE *yyvsp, int yyrule)
#else
static void
yy_reduce_print (yyvsp, yyrule)
    YYSTYPE *yyvsp;
    int yyrule;
#endif
{
  int yynrhs = yyr2[yyrule];
  int yyi;
  unsigned long int yylno = yyrline[yyrule];
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
	     yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      fprintf (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr, yyrhs[yyprhs[yyrule] + yyi],
		       &(yyvsp[(yyi + 1) - (yynrhs)])
		       		       );
      fprintf (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)		\
do {					\
  if (yydebug)				\
    yy_reduce_print (yyvsp, Rule); \
} while (YYID (0))

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef	YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif



#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static YYSIZE_T
yystrlen (const char *yystr)
#else
static YYSIZE_T
yystrlen (yystr)
    const char *yystr;
#endif
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static char *
yystpcpy (char *yydest, const char *yysrc)
#else
static char *
yystpcpy (yydest, yysrc)
    char *yydest;
    const char *yysrc;
#endif
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
	switch (*++yyp)
	  {
	  case '\'':
	  case ',':
	    goto do_not_strip_quotes;

	  case '\\':
	    if (*++yyp != '\\')
	      goto do_not_strip_quotes;
	    /* Fall through.  */
	  default:
	    if (yyres)
	      yyres[yyn] = *yyp;
	    yyn++;
	    break;

	  case '"':
	    if (yyres)
	      yyres[yyn] = '\0';
	    return yyn;
	  }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into YYRESULT an error message about the unexpected token
   YYCHAR while in state YYSTATE.  Return the number of bytes copied,
   including the terminating null byte.  If YYRESULT is null, do not
   copy anything; just return the number of bytes that would be
   copied.  As a special case, return 0 if an ordinary "syntax error"
   message will do.  Return YYSIZE_MAXIMUM if overflow occurs during
   size calculation.  */
static YYSIZE_T
yysyntax_error (char *yyresult, int yystate, int yychar)
{
  int yyn = yypact[yystate];

  if (! (YYPACT_NINF < yyn && yyn <= YYLAST))
    return 0;
  else
    {
      int yytype = YYTRANSLATE (yychar);
      YYSIZE_T yysize0 = yytnamerr (0, yytname[yytype]);
      YYSIZE_T yysize = yysize0;
      YYSIZE_T yysize1;
      int yysize_overflow = 0;
      enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
      char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
      int yyx;

# if 0
      /* This is so xgettext sees the translatable formats that are
	 constructed on the fly.  */
      YY_("syntax error, unexpected %s");
      YY_("syntax error, unexpected %s, expecting %s");
      YY_("syntax error, unexpected %s, expecting %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s");
      YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s");
# endif
      char *yyfmt;
      char const *yyf;
      static char const yyunexpected[] = "syntax error, unexpected %s";
      static char const yyexpecting[] = ", expecting %s";
      static char const yyor[] = " or %s";
      char yyformat[sizeof yyunexpected
		    + sizeof yyexpecting - 1
		    + ((YYERROR_VERBOSE_ARGS_MAXIMUM - 2)
		       * (sizeof yyor - 1))];
      char const *yyprefix = yyexpecting;

      /* Start YYX at -YYN if negative to avoid negative indexes in
	 YYCHECK.  */
      int yyxbegin = yyn < 0 ? -yyn : 0;

      /* Stay within bounds of both yycheck and yytname.  */
      int yychecklim = YYLAST - yyn + 1;
      int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
      int yycount = 1;

      yyarg[0] = yytname[yytype];
      yyfmt = yystpcpy (yyformat, yyunexpected);

      for (yyx = yyxbegin; yyx < yyxend; ++yyx)
	if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR)
	  {
	    if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
	      {
		yycount = 1;
		yysize = yysize0;
		yyformat[sizeof yyunexpected - 1] = '\0';
		break;
	      }
	    yyarg[yycount++] = yytname[yyx];
	    yysize1 = yysize + yytnamerr (0, yytname[yyx]);
	    yysize_overflow |= (yysize1 < yysize);
	    yysize = yysize1;
	    yyfmt = yystpcpy (yyfmt, yyprefix);
	    yyprefix = yyor;
	  }

      yyf = YY_(yyformat);
      yysize1 = yysize + yystrlen (yyf);
      yysize_overflow |= (yysize1 < yysize);
      yysize = yysize1;

      if (yysize_overflow)
	return YYSIZE_MAXIMUM;

      if (yyresult)
	{
	  /* Avoid sprintf, as that infringes on the user's name space.
	     Don't have undefined behavior even if the translation
	     produced a string with the wrong number of "%s"s.  */
	  char *yyp = yyresult;
	  int yyi = 0;
	  while ((*yyp = *yyf) != '\0')
	    {
	      if (*yyp == '%' && yyf[1] == 's' && yyi < yycount)
		{
		  yyp += yytnamerr (yyp, yyarg[yyi++]);
		  yyf += 2;
		}
	      else
		{
		  yyp++;
		  yyf++;
		}
	    }
	}
      return yysize;
    }
}
#endif /* YYERROR_VERBOSE */


/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

/*ARGSUSED*/
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
#else
static void
yydestruct (yymsg, yytype, yyvaluep)
    const char *yymsg;
    int yytype;
    YYSTYPE *yyvaluep;
#endif
{
  YYUSE (yyvaluep);

  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  switch (yytype)
    {

      default:
	break;
    }
}


/* Prevent warnings from -Wmissing-prototypes.  */

#ifdef YYPARSE_PARAM
#if defined __STDC__ || defined __cplusplus
int yyparse (void *YYPARSE_PARAM);
#else
int yyparse ();
#endif
#else /* ! YYPARSE_PARAM */
#if defined __STDC__ || defined __cplusplus
int yyparse (void);
#else
int yyparse ();
#endif
#endif /* ! YYPARSE_PARAM */



/* The look-ahead symbol.  */
int yychar;

/* The semantic value of the look-ahead symbol.  */
YYSTYPE yylval;

/* Number of syntax errors so far.  */
int yynerrs;



/*----------.
| yyparse.  |
`----------*/

#ifdef YYPARSE_PARAM
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void *YYPARSE_PARAM)
#else
int
yyparse (YYPARSE_PARAM)
    void *YYPARSE_PARAM;
#endif
#else /* ! YYPARSE_PARAM */
#if (defined __STDC__ || defined __C99__FUNC__ \
     || defined __cplusplus || defined _MSC_VER)
int
yyparse (void)
#else
int
yyparse ()

#endif
#endif
{
  
  int yystate;
  int yyn;
  int yyresult;
  /* Number of tokens to shift before error messages enabled.  */
  int yyerrstatus;
  /* Look-ahead token as an internal (translated) token number.  */
  int yytoken = 0;
#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

  /* Three stacks and their tools:
     `yyss': related to states,
     `yyvs': related to semantic values,
     `yyls': related to locations.

     Refer to the stacks thru separate pointers, to allow yyoverflow
     to reallocate them elsewhere.  */

  /* The state stack.  */
  yytype_int16 yyssa[YYINITDEPTH];
  yytype_int16 *yyss = yyssa;
  yytype_int16 *yyssp;

  /* The semantic value stack.  */
  YYSTYPE yyvsa[YYINITDEPTH];
  YYSTYPE *yyvs = yyvsa;
  YYSTYPE *yyvsp;



#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  YYSIZE_T yystacksize = YYINITDEPTH;

  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;


  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY;		/* Cause a token to be read.  */

  /* Initialize stack pointers.
     Waste one element of value and location stack
     so that they stay on the same level as the state stack.
     The wasted elements are never initialized.  */

  yyssp = yyss;
  yyvsp = yyvs;

  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
	/* Give user a chance to reallocate the stack.  Use copies of
	   these so that the &'s don't force the real ones into
	   memory.  */
	YYSTYPE *yyvs1 = yyvs;
	yytype_int16 *yyss1 = yyss;


	/* Each stack pointer address is followed by the size of the
	   data in use in that stack, in bytes.  This used to be a
	   conditional around just the two extra args, but that might
	   be undefined if yyoverflow is a macro.  */
	yyoverflow (YY_("memory exhausted"),
		    &yyss1, yysize * sizeof (*yyssp),
		    &yyvs1, yysize * sizeof (*yyvsp),

		    &yystacksize);

	yyss = yyss1;
	yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
	goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
	yystacksize = YYMAXDEPTH;

      {
	yytype_int16 *yyss1 = yyss;
	union yyalloc *yyptr =
	  (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
	if (! yyptr)
	  goto yyexhaustedlab;
	YYSTACK_RELOCATE (yyss);
	YYSTACK_RELOCATE (yyvs);

#  undef YYSTACK_RELOCATE
	if (yyss1 != yyssa)
	  YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;


      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
		  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
	YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     look-ahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to look-ahead token.  */
  yyn = yypact[yystate];
  if (yyn == YYPACT_NINF)
    goto yydefault;

  /* Not known => get a look-ahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid look-ahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = YYLEX;
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yyn == 0 || yyn == YYTABLE_NINF)
	goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the look-ahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token unless it is eof.  */
  if (yychar != YYEOF)
    yychar = YYEMPTY;

  yystate = yyn;
  *++yyvsp = yylval;

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     `$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 2:
#line 421 "psl_grammar.y"
    { psl_parsed_tree = (yyvsp[(2) - (4)].psl_expr).psl_node; YYACCEPT;}
    break;

  case 3:
#line 424 "psl_grammar.y"
    { psl_parsed_tree = (yyvsp[(2) - (4)].psl_expr).psl_node; YYACCEPT;}
    break;

  case 4:
#line 427 "psl_grammar.y"
    { psl_parsed_tree = (yyvsp[(1) - (2)].psl_expr).psl_node; Parser_switch_to_smv(); YYACCEPT;}
    break;

  case 5:
#line 430 "psl_grammar.y"
    { 
  psl_yyerror("Unexpected end of file (did you forget a semicolon ';' ?)\n"); 
  Parser_switch_to_smv(); YYABORT; 
}
    break;

  case 7:
#line 437 "psl_grammar.y"
    { psl_property_name = (yyvsp[(2) - (4)].psl_expr).psl_node; (yyval.psl_expr) = (yyvsp[(4) - (4)].psl_expr);}
    break;

  case 8:
#line 441 "psl_grammar.y"
    { }
    break;

  case 9:
#line 443 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_context((yyvsp[(3) - (3)].psl_expr), (yyvsp[(1) - (3)].psl_expr)); }
    break;

  case 10:
#line 444 "psl_grammar.y"
    { (yyval.psl_expr) = (yyvsp[(2) - (2)].psl_expr); }
    break;

  case 11:
#line 449 "psl_grammar.y"
    { 
  (yyval.psl_expr) = psl_expr_make_replicated_property(
     psl_expr_make_replicator((yyvsp[(1) - (7)].operator), psl_expr_make_atom((yyvsp[(2) - (7)].idname)), (yyvsp[(3) - (7)].psl_expr), (yyvsp[(5) - (7)].psl_expr)), (yyvsp[(7) - (7)].psl_expr)); 
  free((yyvsp[(2) - (7)].idname));  /* TKATOM must be freed */
}
    break;

  case 17:
#line 467 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_empty(); }
    break;

  case 19:
#line 472 "psl_grammar.y"
    { (yyval.psl_expr) = (yyvsp[(2) - (3)].psl_expr); }
    break;

  case 20:
#line 473 "psl_grammar.y"
    { psl_error(); }
    break;

  case 21:
#line 477 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_cons((yyvsp[(3) - (4)].psl_expr), (yyvsp[(2) - (4)].psl_expr)); }
    break;

  case 22:
#line 478 "psl_grammar.y"
    { psl_error(); }
    break;

  case 23:
#line 479 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_boolean_type(); }
    break;

  case 24:
#line 483 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_cons((yyvsp[(2) - (3)].psl_expr), (yyvsp[(1) - (3)].psl_expr)); }
    break;

  case 25:
#line 484 "psl_grammar.y"
    { psl_error(); }
    break;

  case 26:
#line 485 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_empty(); }
    break;

  case 29:
#line 496 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 30:
#line 497 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 31:
#line 498 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 32:
#line 499 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 33:
#line 500 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (5)].psl_expr), (yyvsp[(3) - (5)].operator), (yyvsp[(4) - (5)].psl_expr)); }
    break;

  case 34:
#line 501 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (5)].psl_expr), (yyvsp[(3) - (5)].operator), (yyvsp[(4) - (5)].psl_expr)); }
    break;

  case 35:
#line 505 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 36:
#line 506 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 37:
#line 507 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 38:
#line 508 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 39:
#line 509 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 40:
#line 512 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 41:
#line 513 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 42:
#line 514 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 43:
#line 515 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 44:
#line 517 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 45:
#line 518 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 46:
#line 519 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 47:
#line 520 "psl_grammar.y"
    { PSL_EXPR_MAKE_F_F2F_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 48:
#line 524 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 49:
#line 527 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 50:
#line 530 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 51:
#line 533 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 52:
#line 537 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 53:
#line 540 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 54:
#line 543 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 55:
#line 546 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 56:
#line 550 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_BOOL((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 57:
#line 553 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_BOOL((yyval.psl_expr), (yyvsp[(1) - (7)].operator), (yyvsp[(6) - (7)].psl_expr), (yyvsp[(3) - (7)].psl_expr)); }
    break;

  case 58:
#line 556 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 59:
#line 559 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 60:
#line 562 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 61:
#line 565 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 62:
#line 568 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 63:
#line 571 "psl_grammar.y"
    { PSL_EXPR_MAKE_EXT_NEXT_OP_WHEN_BOOL((yyval.psl_expr), (yyvsp[(1) - (10)].operator), (yyvsp[(9) - (10)].psl_expr), (yyvsp[(6) - (10)].psl_expr), (yyvsp[(3) - (10)].psl_expr)); }
    break;

  case 64:
#line 576 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_suffix_implication_strong((yyvsp[(1) - (4)].psl_expr), TKPIPEMINUSGT, (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 65:
#line 578 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_suffix_implication_strong((yyvsp[(1) - (4)].psl_expr), (yyvsp[(2) - (4)].operator), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 66:
#line 580 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_suffix_implication_weak((yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 67:
#line 582 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_suffix_implication_strong((yyvsp[(1) - (4)].psl_expr), (yyvsp[(2) - (4)].operator), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 68:
#line 584 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_suffix_implication_weak((yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 69:
#line 586 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 70:
#line 587 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 71:
#line 588 "psl_grammar.y"
    { PSL_EXPR_MAKE_F2F_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 72:
#line 591 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_within((yyvsp[(1) - (7)].operator), (yyvsp[(3) - (7)].psl_expr), (yyvsp[(5) - (7)].psl_expr), (yyvsp[(7) - (7)].psl_expr)); }
    break;

  case 73:
#line 593 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_within((yyvsp[(1) - (7)].operator), (yyvsp[(3) - (7)].psl_expr), (yyvsp[(5) - (7)].psl_expr), (yyvsp[(7) - (7)].psl_expr)); }
    break;

  case 74:
#line 595 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_within((yyvsp[(1) - (7)].operator), (yyvsp[(3) - (7)].psl_expr), (yyvsp[(5) - (7)].psl_expr), (yyvsp[(7) - (7)].psl_expr)); }
    break;

  case 75:
#line 597 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_within((yyvsp[(1) - (7)].operator), (yyvsp[(3) - (7)].psl_expr), (yyvsp[(5) - (7)].psl_expr), (yyvsp[(7) - (7)].psl_expr)); }
    break;

  case 76:
#line 600 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_whilenot((yyvsp[(1) - (5)].operator), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 77:
#line 602 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_whilenot((yyvsp[(1) - (5)].operator), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 78:
#line 604 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_whilenot((yyvsp[(1) - (5)].operator), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 79:
#line 606 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_whilenot((yyvsp[(1) - (5)].operator), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 82:
#line 617 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_abort((yyvsp[(1) - (3)].psl_expr), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 83:
#line 619 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 84:
#line 620 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 85:
#line 624 "psl_grammar.y"
    { (yyval.psl_expr) = (yyvsp[(2) - (3)].psl_expr); }
    break;

  case 86:
#line 628 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_sere((yyvsp[(1) - (1)].psl_expr)); }
    break;

  case 87:
#line 629 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_sere((yyvsp[(1) - (1)].psl_expr)); }
    break;

  case 88:
#line 632 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_sere_concat((yyvsp[(1) - (3)].psl_expr), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 89:
#line 633 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_sere_fusion((yyvsp[(1) - (3)].psl_expr), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 90:
#line 634 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_sere_compound_binary_op((yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 91:
#line 637 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(2) - (4)].operator), (yyvsp[(1) - (4)].psl_expr), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 92:
#line 638 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(1) - (3)].operator), 
					   psl_expr_make_empty(), (yyvsp[(2) - (3)].psl_expr)); }
    break;

  case 93:
#line 640 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(2) - (2)].operator), 
					   (yyvsp[(1) - (2)].psl_expr), psl_expr_make_empty()); }
    break;

  case 94:
#line 642 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(1) - (1)].operator), 
					   psl_expr_make_empty(), 
				           psl_expr_make_empty()); }
    break;

  case 95:
#line 646 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(2) - (4)].operator), (yyvsp[(1) - (4)].psl_expr), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 96:
#line 648 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_repeated_sere((yyvsp[(2) - (4)].operator), (yyvsp[(1) - (4)].psl_expr), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 100:
#line 658 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_empty(); }
    break;

  case 102:
#line 663 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number((yyvsp[(1) - (1)].ival)); }
    break;

  case 103:
#line 664 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_base_number((yyvsp[(1) - (1)].baseval)); }
    break;

  case 106:
#line 670 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_range((yyvsp[(1) - (3)].psl_expr), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 107:
#line 674 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number((yyvsp[(1) - (1)].ival)); }
    break;

  case 108:
#line 675 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number(-(yyvsp[(2) - (2)].ival)); }
    break;

  case 109:
#line 676 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_base_number((yyvsp[(1) - (1)].baseval)); }
    break;

  case 111:
#line 681 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number((yyvsp[(1) - (1)].ival)); }
    break;

  case 112:
#line 682 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number(-(yyvsp[(2) - (2)].ival)); }
    break;

  case 113:
#line 683 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_base_number((yyvsp[(1) - (1)].baseval)); }
    break;

  case 114:
#line 684 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_inf(); }
    break;

  case 116:
#line 690 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 117:
#line 691 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 118:
#line 692 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 119:
#line 693 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_binary((yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 120:
#line 696 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 121:
#line 697 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 122:
#line 698 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_unary((yyvsp[(1) - (2)].operator), (yyvsp[(2) - (2)].psl_expr)); }
    break;

  case 123:
#line 699 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_obe_binary((yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 130:
#line 713 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW2NW_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 131:
#line 714 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW2NW_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 132:
#line 715 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW2BW_OP((yyval.psl_expr), (yyvsp[(2) - (2)].psl_expr), (yyvsp[(1) - (2)].operator)); }
    break;

  case 133:
#line 716 "psl_grammar.y"
    { PSL_EXPR_MAKE_W2B_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator)); }
    break;

  case 134:
#line 717 "psl_grammar.y"
    { PSL_EXPR_MAKE_B2W_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator));  }
    break;

  case 135:
#line 718 "psl_grammar.y"
    { PSL_EXPR_MAKE_W2W_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator)); }
    break;

  case 136:
#line 719 "psl_grammar.y"
    { PSL_EXPR_MAKE_W2W_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator)); }
    break;

  case 137:
#line 721 "psl_grammar.y"
    { PSL_EXPR_MAKE_W_N2W_OP((yyval.psl_expr), (yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 138:
#line 723 "psl_grammar.y"
    { PSL_EXPR_MAKE_W_N2W_OP((yyval.psl_expr), (yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 139:
#line 727 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2NW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 140:
#line 728 "psl_grammar.y"
    { PSL_EXPR_MAKE_T_T2T_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 141:
#line 729 "psl_grammar.y"
    { PSL_EXPR_MAKE_NB_NB2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 142:
#line 730 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2NW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 143:
#line 731 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2NW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 144:
#line 732 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2NW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 145:
#line 733 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2NW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 146:
#line 734 "psl_grammar.y"
    { PSL_EXPR_MAKE_NBW_NBW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 147:
#line 735 "psl_grammar.y"
    { PSL_EXPR_MAKE_NBW_NBW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 148:
#line 736 "psl_grammar.y"
    { PSL_EXPR_MAKE_NBW_NBW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 149:
#line 738 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 150:
#line 739 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 151:
#line 740 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 152:
#line 741 "psl_grammar.y"
    { PSL_EXPR_MAKE_NW_NW2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 153:
#line 743 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 154:
#line 744 "psl_grammar.y"
    { PSL_EXPR_MAKE_B_B2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), TKAMPERSAND, (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 155:
#line 746 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 156:
#line 747 "psl_grammar.y"
    { PSL_EXPR_MAKE_B_B2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), TKPIPE, (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 157:
#line 749 "psl_grammar.y"
    { PSL_EXPR_MAKE_B_B2B_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 158:
#line 750 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 159:
#line 751 "psl_grammar.y"
    { PSL_EXPR_MAKE_BW_BW2BW_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 160:
#line 752 "psl_grammar.y"
    { PSL_EXPR_MAKE_W_NW2W_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 161:
#line 753 "psl_grammar.y"
    { PSL_EXPR_MAKE_W_NW2W_OP((yyval.psl_expr), (yyvsp[(1) - (3)].psl_expr), (yyvsp[(2) - (3)].operator), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 162:
#line 757 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_bit_selection((yyvsp[(3) - (8)].psl_expr), (yyvsp[(5) - (8)].psl_expr), (yyvsp[(7) - (8)].psl_expr)); }
    break;

  case 163:
#line 760 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_word_concatenation((yyvsp[(1) - (3)].psl_expr), (yyvsp[(3) - (3)].psl_expr)); }
    break;

  case 164:
#line 765 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_ite((yyvsp[(1) - (5)].psl_expr), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 165:
#line 769 "psl_grammar.y"
    { (yyval.psl_expr) = (yyvsp[(2) - (3)].psl_expr); }
    break;

  case 166:
#line 773 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_failure("case conditions are not exhaustive", 
					    FAILURE_CASE_NOT_EXHAUSTIVE); }
    break;

  case 167:
#line 775 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_case((yyvsp[(1) - (5)].psl_expr), (yyvsp[(3) - (5)].psl_expr), (yyvsp[(5) - (5)].psl_expr)); }
    break;

  case 168:
#line 779 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_boolean_value(1); }
    break;

  case 169:
#line 780 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_boolean_value(0); }
    break;

  case 170:
#line 784 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_base_number((yyvsp[(1) - (1)].baseval)); }
    break;

  case 171:
#line 785 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_number((yyvsp[(1) - (1)].ival)); }
    break;

  case 172:
#line 786 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_real_number((yyvsp[(1) - (1)].fval)); }
    break;

  case 173:
#line 791 "psl_grammar.y"
    { PSL_EXPR_MAKE_N_N2W_OP((yyval.psl_expr), (yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 174:
#line 793 "psl_grammar.y"
    { PSL_EXPR_MAKE_N_N2W_OP((yyval.psl_expr), (yyvsp[(3) - (6)].psl_expr), (yyvsp[(1) - (6)].operator), (yyvsp[(5) - (6)].psl_expr)); }
    break;

  case 175:
#line 794 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_word_number((yyvsp[(1) - (1)].wval)); }
    break;

  case 176:
#line 798 "psl_grammar.y"
    { PSL_EXPR_MAKE_W2N_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator)); }
    break;

  case 177:
#line 799 "psl_grammar.y"
    { PSL_EXPR_MAKE_W2N_OP((yyval.psl_expr), (yyvsp[(3) - (4)].psl_expr), (yyvsp[(1) - (4)].operator));  }
    break;

  case 185:
#line 810 "psl_grammar.y"
    { (yyval.psl_expr) = (yyvsp[(2) - (3)].psl_expr); }
    break;

  case 186:
#line 814 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_atom((yyvsp[(1) - (1)].idname)); free((yyvsp[(1) - (1)].idname)); }
    break;

  case 187:
#line 817 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_id((yyvsp[(1) - (3)].psl_expr), psl_expr_make_atom((yyvsp[(3) - (3)].idname))); free((yyvsp[(3) - (3)].idname)); }
    break;

  case 188:
#line 820 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_id((yyvsp[(1) - (3)].psl_expr), psl_expr_make_number((yyvsp[(3) - (3)].ival))); }
    break;

  case 189:
#line 823 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_id_array((yyvsp[(1) - (4)].psl_expr), (yyvsp[(3) - (4)].psl_expr)); }
    break;

  case 191:
#line 832 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_concatenation((yyvsp[(2) - (3)].psl_expr)); }
    break;

  case 192:
#line 837 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_cons((yyvsp[(3) - (3)].psl_expr), (yyvsp[(1) - (3)].psl_expr)); }
    break;

  case 193:
#line 838 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_cons((yyvsp[(1) - (1)].psl_expr), psl_expr_make_empty()); }
    break;

  case 194:
#line 843 "psl_grammar.y"
    { (yyval.psl_expr) = psl_expr_make_multiple_concatenation((yyvsp[(2) - (6)].psl_expr), (yyvsp[(4) - (6)].psl_expr)); }
    break;


/* Line 1267 of yacc.c.  */
#line 4584 "psl_grammar.c"
      default: break;
    }
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;


  /* Now `shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*------------------------------------.
| yyerrlab -- here on detecting error |
`------------------------------------*/
yyerrlab:
  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
      {
	YYSIZE_T yysize = yysyntax_error (0, yystate, yychar);
	if (yymsg_alloc < yysize && yymsg_alloc < YYSTACK_ALLOC_MAXIMUM)
	  {
	    YYSIZE_T yyalloc = 2 * yysize;
	    if (! (yysize <= yyalloc && yyalloc <= YYSTACK_ALLOC_MAXIMUM))
	      yyalloc = YYSTACK_ALLOC_MAXIMUM;
	    if (yymsg != yymsgbuf)
	      YYSTACK_FREE (yymsg);
	    yymsg = (char *) YYSTACK_ALLOC (yyalloc);
	    if (yymsg)
	      yymsg_alloc = yyalloc;
	    else
	      {
		yymsg = yymsgbuf;
		yymsg_alloc = sizeof yymsgbuf;
	      }
	  }

	if (0 < yysize && yysize <= yymsg_alloc)
	  {
	    (void) yysyntax_error (yymsg, yystate, yychar);
	    yyerror (yymsg);
	  }
	else
	  {
	    yyerror (YY_("syntax error"));
	    if (yysize != 0)
	      goto yyexhaustedlab;
	  }
      }
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse look-ahead token after an
	 error, discard it.  */

      if (yychar <= YYEOF)
	{
	  /* Return failure if at end of input.  */
	  if (yychar == YYEOF)
	    YYABORT;
	}
      else
	{
	  yydestruct ("Error: discarding",
		      yytoken, &yylval);
	  yychar = YYEMPTY;
	}
    }

  /* Else will try to reuse look-ahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule which action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;	/* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (yyn != YYPACT_NINF)
	{
	  yyn += YYTERROR;
	  if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
	    {
	      yyn = yytable[yyn];
	      if (0 < yyn)
		break;
	    }
	}

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
	YYABORT;


      yydestruct ("Error: popping",
		  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  if (yyn == YYFINAL)
    YYACCEPT;

  *++yyvsp = yylval;


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#ifndef yyoverflow
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEOF && yychar != YYEMPTY)
     yydestruct ("Cleanup: discarding lookahead",
		 yytoken, &yylval);
  /* Do not reclaim the symbols of the rule which action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
		  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  /* Make sure YYID is used.  */
  return YYID (yyresult);
}


#line 847 "psl_grammar.y"


#include <stdarg.h>
#include <stdio.h>

extern FILE* nusmv_stderr;
extern int yylineno;
extern int psl_yylineno;

void psl_yyerror(char* s, ...)
{
  va_list args;

  va_start(args, s);
  fprintf(nusmv_stderr, "PSL parse error line %d: ", 
	  yylineno+psl_yylineno-1);
  vfprintf(nusmv_stderr, s, args);
  fprintf(nusmv_stderr, "\n");
  va_end(args);
}

int psl_error()
{
  fprintf(nusmv_stderr, "PSL parse error line %d: \n", 
	  yylineno+psl_yylineno-1);
  return 1;
}

