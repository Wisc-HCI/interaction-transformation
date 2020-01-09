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




/* Copy the first part of user declarations.  */
#line 3 "grammar.y"

/**CFile***********************************************************************

  FileName    [grammar.y]

  PackageName [parser]

  Synopsis    [Grammar (for Yacc and Bison) of NuSMV input language]

  SeeAlso     [input.l]

  Author      [Andrei Tchaltsev, Marco Roveri]

  Copyright   [
  This file is part of the ``parser'' package of NuSMV version 2.
  Copyright (C) 1998-2005 by CMU and FBK-irst.

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

#if HAVE_CONFIG_H
# include "nusmv-config.h"
#endif

#include <setjmp.h>

#if NUSMV_HAVE_MALLOC_H
# if NUSMV_HAVE_SYS_TYPES_H
#  include <sys/types.h>
# endif
# include <malloc.h>
#elif NUSMV_HAVE_SYS_MALLOC_H
# if NUSMV_HAVE_SYS_TYPES_H
#  include <sys/types.h>
# endif
# include <sys/malloc.h>
#elif NUSMV_HAVE_STDLIB_H
# include <stdlib.h>
#endif

#include <limits.h>

#include "parser/parserInt.h"
#include "utils/utils.h"
#include "utils/ustring.h"
#include "node/node.h"
#include "opt/opt.h"
#include "prop/propPkg.h"
#include "utils/error.h"

#include "parser/symbols.h"

static char rcsid[] UTIL_UNUSED = "$Id: grammar.y,v 1.19.4.10.4.46.4.45 2010-02-17 15:13:41 nusmv Exp $";

#define YYMAXDEPTH INT_MAX

#define SYNTAX_ERROR_HANDLING(dest, src) \
  {                                      \
    if (OptsHandler_get_bool_option_value(OptsHandler_get_instance(), \
                                          OPT_PARSER_IS_LAX)) {       \
      dest = src;                                                     \
    }                                                                 \
    else {                                                            \
      YYABORT;                                                        \
    }                                                                 \
 }


node_ptr parsed_tree; /* the returned value of parsing */

enum PARSE_MODE parse_mode_flag; /* the flag what should be parsed */

extern FILE * nusmv_stderr;

void yyerror ARGS((char *s));
void yyerror_lined ARGS((const char *s, int line));
static node_ptr node2maincontext ARGS((node_ptr node));

/* this enum is used to distinguish
   different kinds of expressions: SIMPLE, NEXT, CTL and LTL.
   Since syntactically only one global kind of expressions exists,
   we have to invoke a special function which checks that an expression
   complies to the additional syntactic constrains.
   So, if an ltl-expression is expected then occurrences of NEXT or EBF
   operators will cause the termination of parsing.

   NB: An alternative to invoking a checking function would be to write quite
   intricate syntactic rules to distinguish all the cases.

   NB: This checking function could also be a part of the type checker,
   but it is more straightforward to write a separate function.
*/
  enum EXP_KIND {EXP_SIMPLE, EXP_NEXT, EXP_LTL, EXP_CTL};

  static boolean isCorrectExp ARGS((node_ptr exp, enum EXP_KIND expectedKind));

  static node_ptr build_case_colon_node ARGS((node_ptr l,
                                              node_ptr r,
                                              int linum));

  static int nusmv_parse_psl ARGS((void));


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
#line 125 "grammar.y"
{
  node_ptr node;
  int lineno;
}
/* Line 193 of yacc.c.  */
#line 507 "grammar.c"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 520 "grammar.c"

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
#define YYFINAL  5
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   2227

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  143
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  109
/* YYNRULES -- Number of rules.  */
#define YYNRULES  313
/* YYNRULES -- Number of states.  */
#define YYNSTATES  662

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   397

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
     135,   136,   137,   138,   139,   140,   141,   142
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     8,    10,    13,    16,    18,    20,
      22,    24,    28,    32,    34,    36,    43,    50,    55,    60,
      62,    64,    66,    68,    70,    72,    75,    77,    79,    83,
      87,    92,    99,   103,   106,   111,   116,   121,   126,   131,
     138,   145,   149,   156,   165,   170,   172,   176,   178,   181,
     186,   188,   192,   194,   198,   202,   206,   208,   212,   216,
     218,   222,   226,   228,   230,   234,   236,   240,   242,   246,
     248,   252,   254,   258,   262,   266,   270,   274,   278,   280,
     282,   285,   288,   291,   294,   297,   300,   307,   314,   322,
     330,   334,   338,   342,   346,   349,   351,   355,   357,   361,
     365,   369,   371,   375,   377,   381,   383,   385,   387,   390,
     393,   396,   399,   402,   405,   408,   411,   413,   417,   421,
     425,   429,   431,   435,   437,   441,   445,   449,   451,   457,
     459,   463,   465,   469,   471,   473,   475,   477,   479,   486,
     493,   495,   497,   499,   504,   510,   516,   518,   522,   533,
     538,   540,   542,   545,   547,   551,   553,   555,   557,   559,
     561,   565,   567,   571,   576,   581,   583,   587,   589,   592,
     596,   598,   602,   607,   609,   613,   614,   617,   620,   622,
     624,   626,   628,   630,   632,   634,   636,   638,   640,   642,
     644,   646,   648,   650,   652,   654,   656,   658,   660,   662,
     664,   667,   669,   672,   674,   677,   679,   682,   685,   687,
     690,   693,   695,   698,   701,   706,   711,   716,   719,   720,
     723,   726,   731,   736,   739,   740,   746,   749,   753,   757,
     759,   763,   767,   769,   772,   773,   776,   779,   784,   792,
     800,   804,   808,   812,   816,   820,   828,   831,   836,   839,
     845,   848,   853,   856,   859,   865,   871,   874,   879,   882,
     888,   891,   896,   899,   905,   907,   911,   912,   914,   918,
     920,   923,   927,   934,   942,   953,   957,   960,   961,   963,
     965,   969,   973,   978,   984,   986,   988,   992,   996,  1001,
    1003,  1006,  1008,  1012,  1016,  1020,  1024,  1027,  1030,  1033,
    1036,  1039,  1043,  1046,  1048,  1052,  1057,  1060,  1065,  1066,
    1069,  1070,  1073,  1074
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int16 yyrhs[] =
{
     248,     0,    -1,    80,    -1,   132,    80,    -1,    80,    -1,
     132,    80,    -1,   131,    80,    -1,    81,    -1,    79,    -1,
      78,    -1,    77,    -1,   145,    42,   145,    -1,   160,    42,
     160,    -1,    75,    -1,    74,    -1,    70,    41,   182,    90,
     160,    40,    -1,    69,    41,   182,    90,   160,    40,    -1,
      67,    41,   183,    40,    -1,    66,    41,   183,    40,    -1,
     144,    -1,   146,    -1,   147,    -1,   149,    -1,   148,    -1,
     152,    -1,   131,   153,    -1,    76,    -1,    44,    -1,   153,
     138,    76,    -1,   153,   138,    80,    -1,   153,   139,   183,
      39,    -1,   153,   139,   182,    45,   182,    39,    -1,    41,
     181,    40,    -1,    83,   153,    -1,    62,    41,   181,    40,
      -1,    61,    41,   181,    40,    -1,   136,    41,   181,    40,
      -1,    73,    41,   181,    40,    -1,    72,    41,   181,    40,
      -1,    71,    41,   181,    90,   181,    40,    -1,    68,    41,
     181,    90,   181,    40,    -1,    47,   155,    46,    -1,    64,
      41,   182,    90,   182,    40,    -1,    63,    41,   182,    90,
     182,    90,   182,    40,    -1,    65,    41,   154,    40,    -1,
     153,    -1,   153,    90,   154,    -1,   156,    -1,   156,   155,
      -1,   181,    45,   181,    34,    -1,   153,    -1,   157,   134,
     153,    -1,   157,    -1,   158,   130,   157,    -1,   158,   129,
     157,    -1,   158,   133,   157,    -1,   158,    -1,   159,   132,
     158,    -1,   159,   131,   158,    -1,   159,    -1,   160,   126,
     159,    -1,   160,   125,   159,    -1,   160,    -1,   150,    -1,
      38,   162,    37,    -1,   181,    -1,   162,    90,   181,    -1,
     161,    -1,   163,   128,   161,    -1,   163,    -1,   164,   127,
     163,    -1,   164,    -1,   165,   122,   164,    -1,   165,   121,
     164,    -1,   165,   120,   164,    -1,   165,   119,   164,    -1,
     165,   118,   164,    -1,   165,   117,   164,    -1,   165,    -1,
     167,    -1,    98,   166,    -1,    97,   166,    -1,    96,   166,
      -1,    95,   166,    -1,    94,   166,    -1,    93,   166,    -1,
      91,   139,   172,   101,   172,    39,    -1,    92,   139,   172,
     101,   172,    39,    -1,    91,   139,   172,   105,   150,   172,
      39,    -1,    92,   139,   172,   105,   150,   172,    39,    -1,
     109,   150,   166,    -1,   107,   150,   166,    -1,   108,   150,
     166,    -1,   106,   150,   166,    -1,    83,   167,    -1,   166,
      -1,   168,    84,   166,    -1,   168,    -1,   169,    87,   168,
      -1,   169,    86,   168,    -1,   169,    85,   168,    -1,   169,
      -1,   170,    88,   169,    -1,   170,    -1,   170,    89,   171,
      -1,   171,    -1,   166,    -1,   174,    -1,   112,   173,    -1,
     116,   173,    -1,   115,   173,    -1,   111,   173,    -1,   114,
     173,    -1,   110,   173,    -1,   113,   173,    -1,    83,   174,
      -1,   173,    -1,   175,   101,   173,    -1,   175,   102,   173,
      -1,   175,    99,   173,    -1,   175,   100,   173,    -1,   175,
      -1,   176,    84,   175,    -1,   176,    -1,   177,    87,   176,
      -1,   177,    86,   176,    -1,   177,    85,   176,    -1,   177,
      -1,   177,    82,   181,    45,   178,    -1,   178,    -1,   179,
      88,   178,    -1,   179,    -1,   179,    89,   180,    -1,   180,
      -1,   181,    -1,   181,    -1,   181,    -1,   181,    -1,   104,
     139,   184,    90,   184,    39,    -1,   103,   139,   184,    90,
     184,    39,    -1,    59,    -1,    58,    -1,    57,    -1,    56,
     139,   182,    39,    -1,    72,    56,   139,   182,    39,    -1,
      73,    56,   139,   182,    39,    -1,   151,    -1,    38,   189,
      37,    -1,    60,    56,   139,   182,    39,    36,    56,   139,
     182,    39,    -1,    60,   151,    36,   187,    -1,   187,    -1,
     192,    -1,    11,   192,    -1,   190,    -1,   189,    90,   190,
      -1,   191,    -1,   145,    -1,    75,    -1,    74,    -1,    76,
      -1,   191,   138,    76,    -1,    76,    -1,    76,    41,    40,
      -1,    76,    41,   193,    40,    -1,    60,   151,    36,   192,
      -1,   183,    -1,   193,    90,   183,    -1,   195,    -1,   194,
     195,    -1,    12,   196,   198,    -1,    76,    -1,    76,    41,
      40,    -1,    76,    41,   197,    40,    -1,    76,    -1,   197,
      90,    76,    -1,    -1,   198,   199,    -1,   198,     1,    -1,
     240,    -1,   200,    -1,   201,    -1,   202,    -1,   217,    -1,
     220,    -1,   221,    -1,   222,    -1,   209,    -1,   212,    -1,
     223,    -1,   224,    -1,   225,    -1,   227,    -1,   229,    -1,
     231,    -1,   234,    -1,   233,    -1,   235,    -1,   238,    -1,
     239,    -1,    25,    -1,    25,   203,    -1,    24,    -1,    24,
     204,    -1,    23,    -1,    23,   205,    -1,   206,    -1,   203,
     206,    -1,   203,     1,    -1,   207,    -1,   204,   207,    -1,
     204,     1,    -1,   208,    -1,   205,   208,    -1,   205,     1,
      -1,   242,    45,   188,    34,    -1,   242,    45,   187,    34,
      -1,   242,    45,   187,    34,    -1,    22,   210,    -1,    -1,
     210,   211,    -1,   210,     1,    -1,   242,    43,   183,    34,
      -1,   242,    43,   214,    34,    -1,    21,   213,    -1,    -1,
     213,   242,    43,   214,    34,    -1,   213,     1,    -1,   139,
     216,    39,    -1,   139,   215,    39,    -1,   214,    -1,   214,
      90,   215,    -1,   183,    90,   216,    -1,   183,    -1,    32,
     218,    -1,    -1,   218,   219,    -1,   218,     1,    -1,   243,
      43,   182,    34,    -1,   135,    41,   243,    40,    43,   182,
      34,    -1,   136,    41,   243,    40,    43,   183,    34,    -1,
      20,   182,   241,    -1,    18,   182,   241,    -1,    19,   183,
     241,    -1,    30,   182,   241,    -1,    28,   182,   241,    -1,
      29,    41,   182,    90,   182,    40,   241,    -1,   183,   241,
      -1,   183,    55,   246,   241,    -1,    31,   226,    -1,    31,
      13,   243,    43,   226,    -1,   184,   241,    -1,   184,    55,
     246,   241,    -1,    17,   228,    -1,    16,   228,    -1,    17,
      13,   243,    43,   228,    -1,    16,    13,   243,    43,   228,
      -1,   185,   241,    -1,   185,    55,   246,   241,    -1,    15,
     230,    -1,    15,    13,   243,    43,   230,    -1,   186,   241,
      -1,   186,    55,   246,   241,    -1,    14,   232,    -1,    14,
      13,   243,    43,   232,    -1,    26,    -1,    27,   236,    34,
      -1,    -1,   191,    -1,   236,    90,   191,    -1,   238,    -1,
     237,   238,    -1,   142,   182,   241,    -1,   142,   139,    80,
      39,   182,   241,    -1,   142,   120,   243,   119,    43,   182,
     241,    -1,   142,   139,    80,    39,   120,   243,   119,    43,
     182,   241,    -1,   140,   242,   241,    -1,    33,    76,    -1,
      -1,    34,    -1,    76,    -1,   242,   138,    76,    -1,   242,
     138,    80,    -1,   242,   139,    80,    39,    -1,   242,   139,
     131,    80,    39,    -1,    76,    -1,    44,    -1,   243,   138,
      76,    -1,   243,   138,    80,    -1,   243,   139,   182,    39,
      -1,   245,    -1,     1,    34,    -1,     1,    -1,    20,   182,
      34,    -1,    30,   182,    34,    -1,    19,   183,    34,    -1,
       3,   182,    34,    -1,    54,   247,    -1,    53,   226,    -1,
      50,   228,    -1,    52,   230,    -1,    49,   232,    -1,    48,
     243,    34,    -1,   141,   237,    -1,    76,    -1,   246,   138,
      76,    -1,   246,   139,   182,    39,    -1,   182,   241,    -1,
     182,    55,   246,   241,    -1,    -1,   249,   194,    -1,    -1,
     250,   244,    -1,    -1,   251,   185,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   233,   233,   234,   237,   238,   239,   243,   245,   247,
     249,   252,   256,   260,   261,   262,   264,   266,   268,   270,
     271,   272,   277,   282,   296,   297,   298,   299,   300,   309,
     318,   324,   329,   330,   331,   332,   333,   334,   335,   336,
     337,   338,   340,   343,   346,   351,   352,   356,   358,   362,
     367,   368,   372,   373,   374,   375,   379,   380,   381,   384,
     385,   386,   392,   393,   394,   397,   398,   402,   403,   406,
     407,   411,   412,   413,   414,   415,   416,   417,   420,   421,
     425,   426,   427,   428,   429,   430,   431,   433,   435,   437,
     439,   440,   441,   442,   445,   451,   452,   455,   456,   457,
     458,   461,   462,   466,   467,   470,   474,   475,   480,   481,
     482,   483,   484,   485,   486,   488,   495,   496,   498,   500,
     507,   517,   518,   522,   523,   524,   525,   529,   530,   534,
     535,   539,   540,   544,   551,   554,   557,   560,   564,   566,
     575,   576,   580,   584,   586,   588,   590,   591,   593,   595,
     599,   600,   601,   605,   606,   609,   610,   611,   612,   615,
     616,   619,   620,   621,   623,   635,   636,   648,   649,   652,
     655,   656,   657,   660,   661,   666,   667,   668,   671,   672,
     673,   674,   675,   676,   677,   678,   679,   680,   681,   682,
     683,   684,   685,   686,   687,   688,   689,   690,   691,   700,
     701,   704,   705,   708,   709,   712,   713,   714,   716,   717,
     718,   720,   721,   722,   725,   727,   729,   733,   736,   737,
     738,   741,   743,   756,   760,   761,   762,   766,   767,   771,
     772,   776,   777,   781,   783,   784,   785,   787,   789,   794,
     802,   804,   806,   810,   813,   816,   822,   823,   825,   826,
     829,   830,   832,   833,   834,   835,   838,   839,   842,   843,
     846,   847,   849,   850,   854,   864,   869,   870,   871,   875,
     876,   880,   885,   891,   897,   905,   913,   917,   917,   925,
     926,   927,   928,   929,   938,   939,   940,   941,   942,   949,
     950,   951,   954,   956,   958,   960,   964,   965,   966,   967,
     968,   969,   970,   978,   979,   980,   983,   984,   990,   990,
    1000,  1000,  1007,  1007
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "TOK_CONSTRAINT", "TOK_MAXU", "TOK_MINU",
  "TOK_ABU", "TOK_EBU", "TOK_AU", "TOK_EU", "TOK_CONTEXT", "TOK_PROCESS",
  "TOK_MODULE", "TOK_NAME", "TOK_COMPUTE", "TOK_LTLSPEC", "TOK_CTLSPEC",
  "TOK_SPEC", "TOK_INVAR", "TOK_TRANS", "TOK_INIT", "TOK_ARRAY_DEFINE",
  "TOK_DEFINE", "TOK_IVAR", "TOK_FROZENVAR", "TOK_VAR", "TOK_PSLSPEC",
  "TOK_CONSTANTS", "TOK_JUSTICE", "TOK_COMPASSION", "TOK_FAIRNESS",
  "TOK_INVARSPEC", "TOK_ASSIGN", "TOK_ISA", "TOK_SEMI", "TOK_CONS",
  "TOK_OF", "TOK_RCB", "TOK_LCB", "TOK_RB", "TOK_RP", "TOK_LP",
  "TOK_TWODOTS", "TOK_EQDEF", "TOK_SELF", "TOK_COLON", "TOK_ESAC",
  "TOK_CASE", "TOK_COMPID", "TOK_COMPWFF", "TOK_CTLWFF", "TOK_LTLPSL",
  "TOK_LTLWFF", "TOK_NEXTWFF", "TOK_SIMPWFF", "TOK_INCONTEXT", "TOK_WORD",
  "TOK_REAL", "TOK_INTEGER", "TOK_BOOLEAN", "TOK_ARRAY", "TOK_WORD1",
  "TOK_BOOL", "TOK_WAWRITE", "TOK_WAREAD", "TOK_COUNT", "TOK_WTOINT",
  "TOK_WSIZEOF", "TOK_WRESIZE", "TOK_SWCONST", "TOK_UWCONST", "TOK_EXTEND",
  "TOK_UNSIGNED", "TOK_SIGNED", "TOK_TRUEEXP", "TOK_FALSEEXP", "TOK_ATOM",
  "TOK_NUMBER_EXP", "TOK_NUMBER_REAL", "TOK_NUMBER_FRAC", "TOK_NUMBER",
  "TOK_NUMBER_WORD", "TOK_QUESTIONMARK", "TOK_NOT", "TOK_AND", "TOK_XNOR",
  "TOK_XOR", "TOK_OR", "TOK_IFF", "TOK_IMPLIES", "TOK_COMMA", "TOK_AA",
  "TOK_EE", "TOK_AG", "TOK_EG", "TOK_AF", "TOK_EF", "TOK_AX", "TOK_EX",
  "TOK_RELEASES", "TOK_TRIGGERED", "TOK_UNTIL", "TOK_SINCE", "TOK_MMAX",
  "TOK_MMIN", "TOK_BUNTIL", "TOK_ABG", "TOK_ABF", "TOK_EBG", "TOK_EBF",
  "TOK_OP_FUTURE", "TOK_OP_GLOBAL", "TOK_OP_NEXT", "TOK_OP_ONCE",
  "TOK_OP_HISTORICAL", "TOK_OP_NOTPRECNOT", "TOK_OP_PREC", "TOK_GE",
  "TOK_LE", "TOK_GT", "TOK_LT", "TOK_NOTEQUAL", "TOK_EQUAL", "TOK_RROTATE",
  "TOK_LROTATE", "TOK_RSHIFT", "TOK_LSHIFT", "TOK_SETIN", "TOK_UNION",
  "TOK_DIVIDE", "TOK_TIMES", "TOK_MINUS", "TOK_PLUS", "TOK_MOD",
  "TOK_CONCATENATION", "TOK_SMALLINIT", "TOK_NEXT", "TOK_BIT", "TOK_DOT",
  "TOK_LB", "TOK_MIRROR", "TOK_PREDSLIST", "TOK_PRED", "$accept", "number",
  "integer", "number_word", "number_frac", "number_real", "number_exp",
  "subrange", "subrangetype", "constant", "primary_expr",
  "count_param_list", "case_element_list_expr", "case_element_expr",
  "concatination_expr", "multiplicative_expr", "additive_expr",
  "shift_expr", "set_expr", "set_list_expr", "union_expr", "in_expr",
  "relational_expr", "ctl_expr", "pure_ctl_expr", "ctl_and_expr",
  "ctl_or_expr", "ctl_iff_expr", "ctl_implies_expr", "ctl_basic_expr",
  "ltl_unary_expr", "pure_ltl_unary_expr", "ltl_binary_expr", "and_expr",
  "or_expr", "ite_expr", "iff_expr", "implies_expr", "basic_expr",
  "simple_expression", "next_expression", "ctl_expression",
  "ltl_expression", "compute_expression", "itype", "type",
  "type_value_list", "type_value", "complex_atom", "module_type",
  "next_list_expression", "module_list", "module", "module_sign",
  "atom_list", "declarations", "declaration", "var", "frozen_var",
  "input_var", "var_decl_list", "fvar_decl_list", "ivar_decl_list",
  "var_decl", "fvar_decl", "ivar_decl", "define_decls", "define_list",
  "define", "array_define", "array_define_list", "array_expression",
  "array_expression_list", "array_contents", "assign", "assign_list",
  "one_assign", "init", "invar", "trans", "fairness", "justice",
  "compassion", "_invarspec", "invarspec", "_ctlspec", "ctlspec",
  "_ltlspec", "ltlspec", "_compute", "compute", "pslspec", "constants",
  "constants_expression", "predicate_list", "predicate", "mirror", "isa",
  "optsemi", "decl_var_id", "var_id", "command", "command_case", "context",
  "_simpwff", "begin", "@1", "@2", "@3", 0
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
     395,   396,   397
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   143,   144,   144,   145,   145,   145,   146,   147,   148,
     149,   150,   151,   152,   152,   152,   152,   152,   152,   152,
     152,   152,   152,   152,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   153,   153,   153,   153,   153,   153,
     153,   153,   153,   153,   153,   154,   154,   155,   155,   156,
     157,   157,   158,   158,   158,   158,   159,   159,   159,   160,
     160,   160,   161,   161,   161,   162,   162,   163,   163,   164,
     164,   165,   165,   165,   165,   165,   165,   165,   166,   166,
     167,   167,   167,   167,   167,   167,   167,   167,   167,   167,
     167,   167,   167,   167,   167,   168,   168,   169,   169,   169,
     169,   170,   170,   171,   171,   172,   173,   173,   174,   174,
     174,   174,   174,   174,   174,   174,   175,   175,   175,   175,
     175,   176,   176,   177,   177,   177,   177,   178,   178,   179,
     179,   180,   180,   181,   182,   183,   184,   185,   186,   186,
     187,   187,   187,   187,   187,   187,   187,   187,   187,   187,
     188,   188,   188,   189,   189,   190,   190,   190,   190,   191,
     191,   192,   192,   192,   192,   193,   193,   194,   194,   195,
     196,   196,   196,   197,   197,   198,   198,   198,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   199,
     199,   199,   199,   199,   199,   199,   199,   199,   199,   200,
     200,   201,   201,   202,   202,   203,   203,   203,   204,   204,
     204,   205,   205,   205,   206,   207,   208,   209,   210,   210,
     210,   211,   211,   212,   213,   213,   213,   214,   214,   215,
     215,   216,   216,   217,   218,   218,   218,   219,   219,   219,
     220,   221,   222,   223,   224,   225,   226,   226,   227,   227,
     228,   228,   229,   229,   229,   229,   230,   230,   231,   231,
     232,   232,   233,   233,   234,   235,   236,   236,   236,   237,
     237,   238,   238,   238,   238,   239,   240,   241,   241,   242,
     242,   242,   242,   242,   243,   243,   243,   243,   243,   244,
     244,   244,   245,   245,   245,   245,   245,   245,   245,   245,
     245,   245,   245,   246,   246,   246,   247,   247,   249,   248,
     250,   248,   251,   248
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     1,     2,     2,     1,     1,     1,
       1,     3,     3,     1,     1,     6,     6,     4,     4,     1,
       1,     1,     1,     1,     1,     2,     1,     1,     3,     3,
       4,     6,     3,     2,     4,     4,     4,     4,     4,     6,
       6,     3,     6,     8,     4,     1,     3,     1,     2,     4,
       1,     3,     1,     3,     3,     3,     1,     3,     3,     1,
       3,     3,     1,     1,     3,     1,     3,     1,     3,     1,
       3,     1,     3,     3,     3,     3,     3,     3,     1,     1,
       2,     2,     2,     2,     2,     2,     6,     6,     7,     7,
       3,     3,     3,     3,     2,     1,     3,     1,     3,     3,
       3,     1,     3,     1,     3,     1,     1,     1,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     3,     3,     3,
       3,     1,     3,     1,     3,     3,     3,     1,     5,     1,
       3,     1,     3,     1,     1,     1,     1,     1,     6,     6,
       1,     1,     1,     4,     5,     5,     1,     3,    10,     4,
       1,     1,     2,     1,     3,     1,     1,     1,     1,     1,
       3,     1,     3,     4,     4,     1,     3,     1,     2,     3,
       1,     3,     4,     1,     3,     0,     2,     2,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       2,     1,     2,     1,     2,     1,     2,     2,     1,     2,
       2,     1,     2,     2,     4,     4,     4,     2,     0,     2,
       2,     4,     4,     2,     0,     5,     2,     3,     3,     1,
       3,     3,     1,     2,     0,     2,     2,     4,     7,     7,
       3,     3,     3,     3,     3,     7,     2,     4,     2,     5,
       2,     4,     2,     2,     5,     5,     2,     4,     2,     5,
       2,     4,     2,     5,     1,     3,     0,     1,     3,     1,
       2,     3,     6,     7,    10,     3,     2,     0,     1,     1,
       3,     3,     4,     5,     1,     1,     3,     3,     4,     1,
       2,     1,     3,     3,     3,     3,     2,     2,     2,     2,
       2,     3,     2,     1,     3,     4,     2,     4,     0,     2,
       0,     2,     0,     2
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
     312,     0,     0,     0,     0,     1,     0,   309,   167,   291,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,   311,   289,     0,     0,    27,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      14,    13,    26,    10,     9,     8,     2,     7,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    19,     0,    20,    21,    23,    22,    63,    24,    50,
      52,    56,    59,    62,    67,    69,    71,    78,   106,    79,
     116,   107,   121,   123,   127,   129,   131,   133,   137,   313,
     170,   175,   168,   290,   134,     0,   135,     0,     0,     0,
     285,   284,     0,     0,     0,   277,   300,   136,   277,   298,
     277,   299,   277,   297,   277,   296,     0,   302,   269,     0,
      65,     0,     0,    47,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     2,     0,
       0,    33,    94,   115,     0,     0,     0,    85,    84,    83,
      82,    81,    80,     4,     0,     0,     0,     0,     0,     0,
     113,   111,   108,   114,   112,   110,   109,     2,     0,    25,
       3,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   295,   294,   292,   293,   301,     0,
       0,     0,     0,   278,     0,   260,     0,   250,     0,   256,
       0,   246,     0,   306,     0,     0,   277,   270,    64,     0,
      32,    41,    48,     0,     0,     0,     0,     0,    45,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     3,    95,
      97,   101,   103,   105,     0,     0,     6,     5,    93,    91,
      92,    90,     0,    11,    28,    29,   134,     0,     0,    51,
      54,    53,    55,    58,    57,    61,    60,    68,    70,    77,
      76,    75,    74,    73,    72,   119,   120,   117,   118,   122,
       0,   126,   125,   124,   130,   132,   171,   173,     0,   177,
       0,     0,     0,     0,     0,     0,     0,   224,   218,   203,
     201,   199,   264,   266,     0,     0,     0,     0,   234,     0,
       0,   176,   179,   180,   181,   186,   187,   182,   183,   184,
     185,   188,   189,   190,   191,   192,   193,   195,   194,   196,
     197,   198,   178,   286,   287,     0,     0,     0,   303,   277,
     277,   277,   277,   277,     0,     0,   271,    66,     0,    35,
      34,     0,     0,     0,    44,    18,    17,     0,     0,     0,
       0,    38,    37,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    36,     0,    30,     0,   172,     0,     0,
     262,     0,   258,     0,   253,     0,   252,   277,   277,   277,
       0,     0,   279,     0,   211,     0,     0,   208,     0,     0,
     205,     0,   159,   267,     0,   277,     0,   277,     0,   248,
       0,   276,   277,   288,     0,     0,     0,     0,   261,   251,
     257,   247,   307,     0,     0,    49,     0,     0,    46,     0,
       0,     0,     0,    96,   100,    99,    98,   102,   104,     0,
       0,     0,     0,     0,   128,   174,     0,     0,     0,     0,
     241,   242,   240,   226,     0,   220,   219,     0,   213,   212,
       0,     0,     0,   210,   209,     0,   207,   206,     0,     0,
     265,     0,   244,     0,   243,     0,   236,     0,     0,   235,
       0,   275,     0,     0,   304,     0,     0,     0,   277,     0,
      42,    40,    16,    15,    39,    86,     0,    87,     0,    31,
       0,     0,     0,     0,     0,     0,     0,     0,   142,   141,
     140,     0,     0,     0,   146,     0,     0,   280,   281,     0,
       0,     0,     0,     0,    26,   150,     0,   151,   160,   268,
       0,     0,     0,     0,     0,   139,   138,   305,   277,     0,
     272,     0,    88,    89,   263,   259,   255,   254,     0,     0,
       0,     0,   158,   157,   156,     0,   153,   155,     0,     0,
       0,     0,     0,     0,   216,   282,     0,   215,     0,   161,
     152,     0,     0,   214,     0,   249,     0,     0,     0,   273,
       0,    43,   232,   229,     0,     0,   225,   221,   222,   147,
       0,     0,     0,     0,     0,     0,    12,   283,     0,     0,
     162,   165,     0,   277,     0,     0,   237,     0,     0,     0,
     228,   227,   154,   143,     0,   149,     0,     0,     0,   164,
     163,     0,   245,     0,     0,   277,   231,   230,     0,   144,
     145,   166,     0,     0,   274,     0,   238,   239,     0,     0,
       0,   148
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,    71,    72,    73,    74,    75,    76,    77,   534,    78,
      79,   249,   132,   133,    80,    81,    82,    83,    84,   129,
      85,    86,    87,    88,    89,   260,   261,   262,   263,   264,
      90,    91,    92,    93,    94,    95,    96,    97,   104,   105,
     122,   118,   120,   115,   635,   546,   575,   576,   577,   639,
     622,     7,     8,   101,   308,   213,   331,   332,   333,   334,
     419,   416,   413,   420,   417,   414,   335,   411,   476,   336,
     410,   603,   604,   605,   337,   430,   499,   338,   339,   340,
     341,   342,   343,   123,   344,   119,   345,   121,   346,   116,
     347,   348,   349,   424,   127,   128,   351,   352,   225,   415,
     112,    21,    22,   359,   125,     1,     2,     3,     4
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -468
static const yytype_int16 yypact[] =
{
      40,    34,    50,   236,  1530,  -468,    62,    50,  -468,   107,
    1530,  1530,  1530,  1530,    31,   -26,  1530,  1530,  1530,  1530,
      13,  -468,  -468,  1530,  1530,  -468,  1530,   194,   205,   230,
     232,   241,   259,   266,   282,   292,   321,   342,   351,   357,
    -468,  -468,  -468,  -468,  -468,  -468,   159,  -468,  1856,   152,
     189,  1609,  1609,  1609,  1609,  1609,  1609,   136,   136,   136,
     136,  1530,  1530,  1530,  1530,  1530,  1530,  1530,  2050,   326,
     360,  -468,   268,  -468,  -468,  -468,  -468,  -468,  -468,   182,
     273,   -25,   209,   250,  -468,   280,   283,   217,  -468,  -468,
    -468,  -468,   269,   325,   279,  -468,   306,  -468,  -468,  -468,
     370,  -468,  -468,  -468,  -468,   378,  -468,   379,   381,   382,
    -468,  -468,    14,   278,   281,   169,  -468,  -468,   173,  -468,
     183,  -468,   196,  -468,   215,  -468,  1211,    13,  -468,    29,
    -468,   383,   372,  1530,   374,  1530,  1530,  1530,  1530,  2091,
    1530,  1530,  1530,  1530,  1530,  1530,  1530,  1530,  -468,  2091,
     341,   182,  -468,  -468,  1609,  1609,  1932,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,   344,   347,  1609,  1609,  1609,  1609,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,   380,  2091,   182,
     389,  1530,   136,   207,  1530,  2091,  2091,  2091,  2091,  2091,
    2091,  2091,  2091,  1810,  1810,  1810,  1810,  1810,  1810,  1810,
    1810,  1530,  1530,  1530,  1530,  1530,  1530,  1530,  1530,  1530,
    1530,  1530,    -3,   428,  -468,  -468,  -468,  -468,  -468,   218,
    1530,  1530,  1530,  -468,   358,  -468,   358,  -468,   358,  -468,
     358,  -468,   358,  -468,    31,   353,   401,  -468,  -468,  1530,
    -468,  -468,  -468,  1530,   396,   397,   373,   375,   -22,   426,
     427,   429,   384,   385,   387,   388,   430,   431,  -468,  -468,
     395,   287,   308,  -468,   204,   262,  -468,  -468,  -468,  -468,
    -468,  -468,   432,  -468,  -468,  -468,   402,   423,   434,   182,
     273,   273,   273,   -25,   -25,   209,   209,  -468,   280,   283,
     283,   283,   283,   283,   283,  -468,  -468,  -468,  -468,   269,
     435,   325,   325,   325,  -468,  -468,  -468,  -468,    21,  -468,
      61,   874,   960,  1046,  1530,  1530,  1530,  -468,  -468,   405,
     405,   405,  -468,   406,  1530,   442,  1530,  1132,  -468,   410,
     405,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -468,  -468,   448,   398,   399,  -468,    35,
      35,    35,    35,    35,   125,   451,  -468,  -468,   457,  -468,
    -468,  1530,  1530,  2091,  -468,  -468,  -468,  1530,  2091,  2091,
    1530,  -468,  -468,  1609,  1609,  1609,  1609,  1609,  1609,  1609,
     136,  1609,   136,  -468,  1530,  -468,  1530,  -468,   416,    31,
    -468,    31,  -468,    31,  -468,    31,  -468,   401,   401,   401,
     638,   672,  -468,   706,  -468,    41,   740,  -468,    67,   774,
    -468,    73,  -468,   355,     5,   401,  1530,   401,    31,  -468,
     484,  -468,    37,  -468,  1530,  1530,   419,  1530,  -468,  -468,
    -468,  -468,  -468,   476,  1370,  -468,   433,   480,  -468,   481,
     127,   149,   482,  -468,   395,   395,   395,   287,  -468,   485,
    1609,   491,  1609,   492,  -468,  -468,   -11,    20,    22,    24,
    -468,  -468,  -468,  -468,    44,  -468,  -468,    48,  -468,  -468,
    1690,   242,   134,  -468,  -468,  1690,  -468,  -468,   798,   456,
    -468,   406,  -468,   443,  -468,    54,  -468,   493,   494,  -468,
      56,  -468,   497,   498,  -468,   500,  1530,    31,   401,  1530,
    -468,  -468,  -468,  -468,  -468,  -468,   501,  -468,   504,  -468,
     -26,  1530,  1530,  1530,   407,  1291,   -29,   408,  -468,  -468,
    -468,  2009,    68,   216,  -468,   167,   510,  -468,  -468,   506,
     468,   515,   185,  2009,   228,  -468,   516,  -468,  -468,   355,
    1530,  1530,    31,    31,  1530,  -468,  -468,  -468,   401,   157,
    -468,   511,  -468,  -468,  -468,  -468,  -468,  -468,  1291,   518,
     519,   520,  -468,  -468,  -468,   160,  -468,   355,  1530,   417,
     521,   420,   425,  2091,  -468,  -468,   523,  -468,  2091,   517,
    -468,   529,  1451,  -468,   527,  -468,    -9,     9,   535,  -468,
     528,  -468,   483,   486,   536,   538,  -468,  -468,  -468,  -468,
     -29,   539,  1530,  1690,  1530,  1530,   250,  -468,   543,  1734,
    -468,  -468,    32,   401,   531,   537,  -468,  1530,  1530,   407,
    -468,  -468,  -468,  -468,   542,  -468,   544,   545,   185,  -468,
    -468,  1530,  -468,  1530,  1530,   401,  -468,  -468,   546,  -468,
    -468,  -468,   552,   553,  -468,   532,  -468,  -468,   450,  1530,
     551,  -468
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -468,  -468,  -180,  -468,  -468,  -468,  -468,   -48,  -467,  -468,
     -43,   219,   458,  -468,    72,   210,   211,  -365,   400,  -468,
     403,   158,  -468,     2,   -13,   -37,   208,  -468,   206,  -149,
      18,   550,   394,   171,  -468,  -181,  -468,   390,     4,   -12,
      -7,  -203,   600,  -468,  -156,  -468,  -468,    -5,  -307,  -444,
    -468,  -468,   599,  -468,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,   188,   192,   197,  -468,  -468,  -468,  -468,
    -468,  -120,   -20,   -17,  -468,  -468,  -468,  -468,  -468,  -468,
    -468,  -468,  -468,  -310,  -468,  -289,  -468,  -308,  -468,  -284,
    -468,  -468,  -468,  -468,  -468,   -77,  -468,  -468,   -82,  -220,
    -201,  -468,  -468,    71,  -468,  -468,  -468,  -468,  -468
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -311
static const yytype_int16 yytable[] =
{
     108,   109,   273,   402,   107,   151,   265,   124,    98,   166,
     167,   168,   169,   450,   451,   106,   423,   429,   356,   357,
     117,    98,   106,   404,   406,   179,   400,   130,   131,   304,
     134,   624,   520,   364,     5,   152,   227,   306,   229,   490,
     231,  -310,   233,  -310,   547,   572,   573,   422,   218,   625,
     237,   163,  -308,   157,   158,   159,   160,   161,   162,  -310,
    -310,   397,     6,   521,   580,   522,   238,   523,   373,   223,
    -310,   223,   640,   307,   399,   110,   591,   113,   114,   170,
     171,   172,   173,   174,   175,   176,   480,   524,  -310,  -310,
    -310,   525,  -310,  -310,  -310,   491,   248,   551,   590,   554,
     418,   421,   164,   165,   186,   187,   179,   111,   188,   146,
     432,   398,   485,   151,   236,   535,   183,   184,   488,   239,
     535,   618,   641,   535,   581,   246,   247,   219,   220,   219,
     220,   253,   254,   250,   251,   151,   350,   134,   100,   244,
     245,   103,   279,   152,   106,   106,   252,   219,   220,   255,
     256,   257,   219,   220,   366,   126,   259,   259,   219,   220,
     219,   220,   219,   220,   113,   114,   535,   512,   268,   269,
     270,   271,   277,   436,   437,   481,   482,   278,   535,   481,
     482,  -310,   481,   482,   549,   272,   481,   482,   276,   513,
     474,   477,   219,   220,   219,   220,   418,   609,   466,   421,
     467,    -4,   468,   223,   469,   481,   482,   223,   355,   583,
     300,   481,   482,   565,   539,   464,   163,   223,   616,   295,
     296,   297,   298,   535,   224,   117,   117,   495,   226,   500,
     223,   502,   503,   566,   567,   135,   564,     9,   228,    10,
     459,   595,   461,   367,   443,   588,   136,   368,   535,   223,
     610,   230,   191,   192,   535,    11,    12,   147,   280,   281,
     282,   589,  -161,   219,   220,   540,    13,   164,   165,   592,
     232,   137,   582,   138,   191,   192,   600,   438,   439,   440,
     441,   442,   139,   274,    14,    15,    16,   275,    17,    18,
      19,   154,   191,   192,   353,   219,   220,   360,   354,   361,
     140,   362,   407,   363,   409,   389,   559,   141,   408,   390,
     182,   516,   425,   518,   427,    98,   117,   117,   537,   106,
     183,   184,   538,   142,   536,   470,   471,   472,   155,   541,
     248,   106,   545,   143,   195,   196,   197,   198,   199,   200,
     189,   190,   460,   492,   462,   494,   574,   454,   455,   456,
     501,   596,   597,   289,   290,   291,   292,   293,   294,   446,
     447,   206,   144,   391,   207,   208,   209,   392,   201,   202,
     203,   204,   384,   385,   386,   191,   192,    20,   301,   302,
     303,   449,   463,   145,   452,   453,   259,   259,   259,   259,
     259,   259,   146,   259,   210,   211,   387,   388,   147,   283,
     284,   181,   285,   286,   569,   571,   180,   185,   193,   205,
     194,   212,   214,   215,   493,   216,   217,   221,   241,   243,
     222,   258,    -6,   240,   266,   505,   560,   267,  -169,   309,
     574,    -5,   508,   365,   358,   223,   369,   370,   117,   117,
    -169,  -135,   310,   311,   312,   313,   314,   315,   316,   317,
     318,   319,   320,   321,   322,   323,   324,   325,   326,   327,
     328,   329,   259,   371,   259,   372,   374,   375,   394,   376,
     381,   382,   393,   395,   377,   378,   599,   379,   380,   383,
     396,   412,   422,   426,  -233,   496,   431,   433,   434,   435,
     444,   445,   465,   489,   558,   504,  -233,   561,  -233,  -233,
    -233,  -233,  -233,  -233,  -233,  -233,  -233,  -233,  -233,  -233,
    -233,  -233,  -233,  -233,  -233,  -233,  -233,  -233,   570,   506,
     510,   511,   514,   509,   515,    98,   117,   117,   110,   106,
     517,   519,   548,   550,   552,   553,   555,   556,   594,   557,
     562,   642,   598,   563,   584,   585,   568,   578,   586,   587,
     593,   601,   606,   607,   608,   106,   612,   613,   592,   614,
     111,   602,   617,   654,   615,   619,   611,   623,   330,   626,
     126,   627,   106,   628,   643,   630,   629,   631,   633,   638,
     644,   648,   655,   649,   650,   621,   656,   657,   658,   659,
     661,   242,   448,   287,   458,   457,   106,   288,   153,   299,
     634,   305,   636,   637,    99,   632,   102,   487,   484,   647,
     479,   646,     0,     0,     0,   645,     0,     0,     0,   497,
     498,   602,     0,     0,  -233,     0,  -233,     0,     0,     0,
       0,   652,   106,     0,   651,     0,     0,   653,  -223,   473,
       0,     0,     0,     0,     0,   106,     0,   660,   106,     0,
    -223,     0,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,
    -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,  -223,
    -223,  -223,  -217,   475,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,  -217,     0,  -217,  -217,  -217,  -217,
    -217,  -217,  -217,  -217,  -217,  -217,  -217,  -217,  -217,  -217,
    -217,  -217,  -217,  -217,  -217,  -217,  -204,   478,     0,     0,
       0,     0,     0,     0,   412,     0,     0,     0,  -204,     0,
    -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,
    -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,  -204,
    -202,   483,     0,     0,     0,     0,     0,     0,   412,     0,
       0,     0,  -202,     0,  -202,  -202,  -202,  -202,  -202,  -202,
    -202,  -202,  -202,  -202,  -202,  -202,  -202,  -202,  -202,  -202,
    -202,  -202,  -202,  -202,  -200,   486,     0,     0,  -223,     0,
    -223,     0,   412,     0,     0,     0,  -200,     0,  -200,  -200,
    -200,  -200,  -200,  -200,  -200,  -200,  -200,  -200,  -200,  -200,
    -200,  -200,  -200,  -200,  -200,  -200,  -200,  -200,     0,   542,
       0,     0,  -217,     0,  -217,     0,   412,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   526,     0,     0,    24,
       0,     0,    25,     0,     0,    26,  -204,     0,  -204,     0,
     412,     0,     0,     0,   527,   528,   529,   530,   543,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
     532,   533,    40,    41,   544,    43,    44,    45,   148,    47,
    -202,   178,  -202,     0,     0,     0,     0,   401,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,    23,     0,  -200,    24,  -200,     0,    25,     0,
       0,    26,     0,     0,     0,     0,     0,     0,     0,   149,
     150,     0,     0,     0,    70,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    43,    44,    45,    46,    47,     0,    48,     0,     0,
       0,     0,     0,     0,     0,    49,    50,    51,    52,    53,
      54,    55,    56,   403,     0,     0,     0,     0,     0,     0,
      57,    58,    59,    60,    61,    62,    63,    64,    65,    66,
      67,     0,     0,     0,     0,     0,     0,     0,    23,     0,
       0,    24,     0,     0,    25,    68,    69,    26,     0,     0,
      70,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,     0,    48,     0,     0,     0,     0,     0,     0,
       0,    49,    50,    51,    52,    53,    54,    55,    56,   405,
       0,     0,     0,     0,     0,     0,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,     0,     0,     0,
       0,     0,     0,     0,    23,     0,     0,    24,     0,     0,
      25,    68,    69,    26,     0,     0,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,    46,    47,     0,    48,
       0,     0,     0,     0,     0,     0,     0,    49,    50,    51,
      52,    53,    54,    55,    56,   428,     0,     0,     0,     0,
       0,     0,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,     0,     0,     0,     0,     0,     0,     0,
      23,     0,     0,    24,     0,     0,    25,    68,    69,    26,
       0,     0,    70,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,    46,    47,     0,    48,     0,     0,     0,     0,
       0,     0,     0,    49,    50,    51,    52,    53,    54,    55,
      56,     0,     0,     0,     0,     0,     0,     0,    57,    58,
      59,    60,    61,    62,    63,    64,    65,    66,    67,    23,
       0,     0,    24,     0,     0,    25,     0,     0,    26,     0,
       0,     0,     0,    68,    69,     0,     0,     0,    70,     0,
       0,     0,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,     0,    48,     0,     0,     0,     0,     0,
       0,     0,    49,    50,    51,    52,    53,    54,    55,    56,
       0,     0,     0,     0,     0,     0,     0,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,     0,    23,
       0,   234,    24,     0,     0,    25,     0,     0,    26,     0,
       0,     0,    68,    69,     0,     0,     0,    70,     0,     0,
     235,     0,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,     0,    48,     0,     0,     0,     0,     0,
       0,     0,    49,    50,    51,    52,    53,    54,    55,    56,
       0,     0,     0,     0,     0,     0,     0,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,    23,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
       0,     0,    68,    69,     0,     0,     0,    70,     0,     0,
     568,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,     0,    48,     0,     0,     0,     0,     0,     0,
       0,    49,    50,    51,    52,    53,    54,    55,    56,     0,
       0,     0,     0,     0,     0,     0,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,     0,     0,    23,
     507,   620,    24,     0,     0,    25,     0,     0,    26,     0,
       0,    68,    69,     0,     0,     0,    70,     0,     0,     0,
       0,     0,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,    46,    47,     0,    48,     0,     0,     0,     0,     0,
       0,     0,    49,    50,    51,    52,    53,    54,    55,    56,
       0,     0,     0,     0,     0,     0,     0,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,    23,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
       0,     0,    68,    69,     0,     0,     0,    70,     0,     0,
       0,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,     0,    48,     0,     0,     0,     0,     0,     0,
       0,    49,    50,    51,    52,    53,    54,    55,    56,     0,
       0,     0,     0,     0,     0,     0,    57,    58,    59,    60,
      61,    62,    63,    64,    65,    66,    67,    23,     0,     0,
      24,     0,     0,    25,     0,     0,    26,     0,     0,     0,
       0,    68,    69,     0,     0,     0,    70,     0,     0,     0,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,    46,
      47,     0,   156,     0,     0,     0,     0,     0,     0,     0,
      49,    50,    51,    52,    53,    54,    55,    56,     0,     0,
       0,     0,     0,     0,     0,    57,    58,    59,    60,     0,
       0,     0,     0,     0,     0,     0,     0,     0,   526,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
      68,    69,     0,     0,     0,    70,   527,   528,   529,   530,
     531,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,   532,   533,    40,    41,    42,    43,    44,    45,
     148,    47,   526,   178,     0,    24,     0,     0,    25,     0,
       0,    26,     0,     0,     0,     0,     0,     0,     0,     0,
     527,   528,   529,   530,   543,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,   532,   533,    40,    41,
     544,    43,    44,    45,   148,    47,     0,   178,     0,     0,
       0,   149,   150,     0,     0,     0,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    23,     0,
       0,    24,     0,     0,    25,     0,     0,    26,     0,     0,
       0,     0,     0,     0,     0,   149,   150,     0,     0,     0,
      70,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
      46,    47,     0,   178,     0,     0,     0,    24,     0,     0,
      25,     0,     0,    26,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,    43,    44,    45,   148,    47,     0,    48,
       0,    68,    69,     0,     0,     0,    70,    49,    50,    51,
      52,    53,    54,    55,    56,     0,     0,     0,     0,     0,
       0,     0,    57,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,    24,     0,     0,    25,     0,     0,    26,
       0,     0,     0,     0,     0,     0,     0,   149,   150,     0,
       0,     0,    70,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    43,
      44,    45,   148,    47,     0,   156,     0,     0,     0,     0,
       0,     0,     0,    49,    50,    51,    52,    53,    54,    55,
      56,     0,     0,     0,     0,     0,     0,     0,    57,    58,
      59,    60,     0,     0,     0,     0,     0,     0,     0,     0,
      24,     0,     0,    25,     0,     0,    26,     0,     0,     0,
       0,     0,     0,   149,   150,   579,     0,     0,    70,     0,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    43,    44,    45,   148,
      47,    24,   178,     0,    25,     0,     0,    26,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    43,    44,    45,
     177,    47,    24,   178,     0,    25,     0,     0,    26,     0,
     149,   150,     0,     0,     0,    70,     0,     0,     0,     0,
       0,     0,    27,    28,    29,    30,    31,    32,    33,    34,
      35,    36,    37,    38,    39,    40,    41,    42,    43,    44,
      45,   148,    47,     0,   178,     0,     0,     0,     0,     0,
       0,   149,   150,     0,     0,     0,    70,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   149,   150,     0,     0,     0,    70
};

static const yytype_int16 yycheck[] =
{
      12,    13,   182,   311,    11,    48,   155,    19,     4,    57,
      58,    59,    60,   378,   379,    11,   323,   327,   221,   222,
      16,    17,    18,   312,   313,    68,   310,    23,    24,   210,
      26,    40,    43,   234,     0,    48,   118,    40,   120,    34,
     122,     1,   124,     3,   488,    74,    75,    76,    34,    40,
     127,    80,    12,    51,    52,    53,    54,    55,    56,    19,
      20,    40,    12,    43,   531,    43,    37,    43,    90,    34,
      30,    34,    40,    76,    13,    44,   543,   103,   104,    61,
      62,    63,    64,    65,    66,    67,    45,    43,    48,    49,
      50,    43,    52,    53,    54,    90,   139,    43,   542,    43,
     320,   321,   131,   132,   129,   130,   149,    76,   133,    41,
     330,    90,    45,   156,   126,   480,   138,   139,    45,    90,
     485,   588,    90,   488,    56,   137,   138,   138,   139,   138,
     139,   143,   144,   140,   141,   178,   213,   133,    76,   135,
     136,    34,   185,   156,   140,   141,   142,   138,   139,   145,
     146,   147,   138,   139,   236,   142,   154,   155,   138,   139,
     138,   139,   138,   139,   103,   104,   531,    40,   166,   167,
     168,   169,   184,   138,   139,   138,   139,   184,   543,   138,
     139,   141,   138,   139,   491,   181,   138,   139,   184,    40,
     410,   411,   138,   139,   138,   139,   416,    37,   399,   419,
     401,    42,   403,    34,   405,   138,   139,    34,   220,    42,
     206,   138,   139,   521,    80,   396,    80,    34,   583,   201,
     202,   203,   204,   588,    55,   221,   222,   428,    55,   430,
      34,   434,   435,   522,   523,    41,   520,     1,    55,     3,
     389,   551,   391,   239,   119,    60,    41,   243,   613,    34,
      90,    55,   125,   126,   619,    19,    20,    41,   186,   187,
     188,    76,    34,   138,   139,   131,    30,   131,   132,    41,
      55,    41,    56,    41,   125,   126,   119,   359,   360,   361,
     362,   363,    41,    76,    48,    49,    50,    80,    52,    53,
      54,   139,   125,   126,    76,   138,   139,   226,    80,   228,
      41,   230,   314,   232,   316,   101,   507,    41,   315,   105,
      42,   460,   324,   462,   326,   311,   312,   313,    76,   315,
     138,   139,    80,    41,   480,   407,   408,   409,   139,   485,
     373,   327,   488,    41,   117,   118,   119,   120,   121,   122,
     131,   132,   390,   425,   392,   427,   526,   384,   385,   386,
     432,   552,   553,   195,   196,   197,   198,   199,   200,   371,
     372,    82,    41,   101,    85,    86,    87,   105,    99,   100,
     101,   102,    85,    86,    87,   125,   126,   141,   207,   208,
     209,   377,   394,    41,   380,   383,   384,   385,   386,   387,
     388,   389,    41,   391,    88,    89,    88,    89,    41,   189,
     190,    41,   191,   192,   524,   525,    80,   134,   128,    84,
     127,    41,    34,    34,   426,    34,    34,   139,    46,    45,
     139,    80,    42,    40,    80,   437,   508,    80,     0,     1,
     610,    42,   444,    80,    76,    34,    40,    40,   434,   435,
      12,    39,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,   460,    90,   462,    90,    40,    40,    45,    40,
      40,    40,    40,    39,    90,    90,   558,    90,    90,    84,
      45,    76,    76,    41,     0,     1,    76,    39,    90,    90,
      39,    34,    76,   138,   506,    76,    12,   509,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,   525,    43,
      40,    40,    40,    90,    39,   521,   522,   523,    44,   525,
      39,    39,    76,    90,    41,    41,    39,    39,   550,    39,
      39,   623,   554,    39,    34,    39,   139,   139,    80,    34,
      34,    40,    34,    34,    34,   551,   139,    36,    41,   139,
      76,   568,    39,   645,   139,    36,   578,    40,   140,    34,
     142,    43,   568,    90,    43,    39,    90,    39,    39,    36,
      43,    39,    36,    39,    39,   592,    34,    34,    56,   139,
      39,   133,   373,   193,   388,   387,   592,   194,    48,   205,
     612,   211,   614,   615,     4,   610,     7,   419,   416,   629,
     413,   628,    -1,    -1,    -1,   627,    -1,    -1,    -1,   135,
     136,   628,    -1,    -1,   140,    -1,   142,    -1,    -1,    -1,
      -1,   643,   628,    -1,   641,    -1,    -1,   644,     0,     1,
      -1,    -1,    -1,    -1,    -1,   641,    -1,   659,   644,    -1,
      12,    -1,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,     0,     1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    12,    -1,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,     0,     1,    -1,    -1,
      -1,    -1,    -1,    -1,    76,    -1,    -1,    -1,    12,    -1,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
       0,     1,    -1,    -1,    -1,    -1,    -1,    -1,    76,    -1,
      -1,    -1,    12,    -1,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,     0,     1,    -1,    -1,   140,    -1,
     142,    -1,    76,    -1,    -1,    -1,    12,    -1,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    -1,    11,
      -1,    -1,   140,    -1,   142,    -1,    76,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    38,    -1,    -1,    41,
      -1,    -1,    44,    -1,    -1,    47,   140,    -1,   142,    -1,
      76,    -1,    -1,    -1,    56,    57,    58,    59,    60,    61,
      62,    63,    64,    65,    66,    67,    68,    69,    70,    71,
      72,    73,    74,    75,    76,    77,    78,    79,    80,    81,
     140,    83,   142,    -1,    -1,    -1,    -1,    13,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    38,    -1,   140,    41,   142,    -1,    44,    -1,
      -1,    47,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   131,
     132,    -1,    -1,    -1,   136,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    -1,    83,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    91,    92,    93,    94,    95,
      96,    97,    98,    13,    -1,    -1,    -1,    -1,    -1,    -1,
     106,   107,   108,   109,   110,   111,   112,   113,   114,   115,
     116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    38,    -1,
      -1,    41,    -1,    -1,    44,   131,   132,    47,    -1,    -1,
     136,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    94,    95,    96,    97,    98,    13,
      -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,   109,
     110,   111,   112,   113,   114,   115,   116,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    38,    -1,    -1,    41,    -1,    -1,
      44,   131,   132,    47,    -1,    -1,   136,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    -1,    83,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    91,    92,    93,
      94,    95,    96,    97,    98,    13,    -1,    -1,    -1,    -1,
      -1,    -1,   106,   107,   108,   109,   110,   111,   112,   113,
     114,   115,   116,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      38,    -1,    -1,    41,    -1,    -1,    44,   131,   132,    47,
      -1,    -1,   136,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    94,    95,    96,    97,
      98,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,
     108,   109,   110,   111,   112,   113,   114,   115,   116,    38,
      -1,    -1,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,
      -1,    -1,    -1,   131,   132,    -1,    -1,    -1,   136,    -1,
      -1,    -1,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    94,    95,    96,    97,    98,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   115,   116,    -1,    38,
      -1,   120,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,
      -1,    -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,
     139,    -1,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    94,    95,    96,    97,    98,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   115,   116,    38,    -1,
      -1,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,
      -1,    -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,
     139,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    94,    95,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,   109,
     110,   111,   112,   113,   114,   115,   116,    -1,    -1,    38,
     120,    40,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,
      -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,    -1,
      -1,    -1,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    91,    92,    93,    94,    95,    96,    97,    98,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   115,   116,    38,    -1,
      -1,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,
      -1,    -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,
      -1,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    91,    92,    93,    94,    95,    96,    97,    98,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,   106,   107,   108,   109,
     110,   111,   112,   113,   114,   115,   116,    38,    -1,    -1,
      41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,    -1,
      -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,    -1,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    -1,    83,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      91,    92,    93,    94,    95,    96,    97,    98,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   106,   107,   108,   109,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    38,    -1,
      -1,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,
     131,   132,    -1,    -1,    -1,   136,    56,    57,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    38,    83,    -1,    41,    -1,    -1,    44,    -1,
      -1,    47,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      56,    57,    58,    59,    60,    61,    62,    63,    64,    65,
      66,    67,    68,    69,    70,    71,    72,    73,    74,    75,
      76,    77,    78,    79,    80,    81,    -1,    83,    -1,    -1,
      -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    38,    -1,
      -1,    41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,   131,   132,    -1,    -1,    -1,
     136,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    -1,    83,    -1,    -1,    -1,    41,    -1,    -1,
      44,    -1,    -1,    47,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    -1,    83,
      -1,   131,   132,    -1,    -1,    -1,   136,    91,    92,    93,
      94,    95,    96,    97,    98,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   106,   107,   108,   109,   110,   111,   112,   113,
     114,   115,   116,    41,    -1,    -1,    44,    -1,    -1,    47,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,   131,   132,    -1,
      -1,    -1,   136,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    91,    92,    93,    94,    95,    96,    97,
      98,    -1,    -1,    -1,    -1,    -1,    -1,    -1,   106,   107,
     108,   109,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      41,    -1,    -1,    44,    -1,    -1,    47,    -1,    -1,    -1,
      -1,    -1,    -1,   131,   132,    56,    -1,    -1,   136,    -1,
      61,    62,    63,    64,    65,    66,    67,    68,    69,    70,
      71,    72,    73,    74,    75,    76,    77,    78,    79,    80,
      81,    41,    83,    -1,    44,    -1,    -1,    47,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    61,    62,    63,    64,    65,    66,    67,    68,    69,
      70,    71,    72,    73,    74,    75,    76,    77,    78,    79,
      80,    81,    41,    83,    -1,    44,    -1,    -1,    47,    -1,
     131,   132,    -1,    -1,    -1,   136,    -1,    -1,    -1,    -1,
      -1,    -1,    61,    62,    63,    64,    65,    66,    67,    68,
      69,    70,    71,    72,    73,    74,    75,    76,    77,    78,
      79,    80,    81,    -1,    83,    -1,    -1,    -1,    -1,    -1,
      -1,   131,   132,    -1,    -1,    -1,   136,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,   131,   132,    -1,    -1,    -1,   136
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,   248,   249,   250,   251,     0,    12,   194,   195,     1,
       3,    19,    20,    30,    48,    49,    50,    52,    53,    54,
     141,   244,   245,    38,    41,    44,    47,    61,    62,    63,
      64,    65,    66,    67,    68,    69,    70,    71,    72,    73,
      74,    75,    76,    77,    78,    79,    80,    81,    83,    91,
      92,    93,    94,    95,    96,    97,    98,   106,   107,   108,
     109,   110,   111,   112,   113,   114,   115,   116,   131,   132,
     136,   144,   145,   146,   147,   148,   149,   150,   152,   153,
     157,   158,   159,   160,   161,   163,   164,   165,   166,   167,
     173,   174,   175,   176,   177,   178,   179,   180,   181,   185,
      76,   196,   195,    34,   181,   182,   181,   183,   182,   182,
      44,    76,   243,   103,   104,   186,   232,   181,   184,   228,
     185,   230,   183,   226,   182,   247,   142,   237,   238,   162,
     181,   181,   155,   156,   181,    41,    41,    41,    41,    41,
      41,    41,    41,    41,    41,    41,    41,    41,    80,   131,
     132,   153,   167,   174,   139,   139,    83,   166,   166,   166,
     166,   166,   166,    80,   131,   132,   150,   150,   150,   150,
     173,   173,   173,   173,   173,   173,   173,    80,    83,   153,
      80,    41,    42,   138,   139,   134,   129,   130,   133,   131,
     132,   125,   126,   128,   127,   117,   118,   119,   120,   121,
     122,    99,   100,   101,   102,    84,    82,    85,    86,    87,
      88,    89,    41,   198,    34,    34,    34,    34,    34,   138,
     139,   139,   139,    34,    55,   241,    55,   241,    55,   241,
      55,   241,    55,   241,   120,   139,   182,   238,    37,    90,
      40,    46,   155,    45,   181,   181,   182,   182,   153,   154,
     183,   183,   181,   182,   182,   181,   181,   181,    80,   166,
     168,   169,   170,   171,   172,   172,    80,    80,   166,   166,
     166,   166,   181,   145,    76,    80,   181,   182,   183,   153,
     157,   157,   157,   158,   158,   159,   159,   161,   163,   164,
     164,   164,   164,   164,   164,   173,   173,   173,   173,   175,
     181,   176,   176,   176,   178,   180,    40,    76,   197,     1,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
     140,   199,   200,   201,   202,   209,   212,   217,   220,   221,
     222,   223,   224,   225,   227,   229,   231,   233,   234,   235,
     238,   239,   240,    76,    80,   182,   184,   184,    76,   246,
     246,   246,   246,   246,   243,    80,   241,   181,   181,    40,
      40,    90,    90,    90,    40,    40,    40,    90,    90,    90,
      90,    40,    40,    84,    85,    86,    87,    88,    89,   101,
     105,   101,   105,    40,    45,    39,    45,    40,    90,    13,
     232,    13,   230,    13,   228,    13,   228,   182,   183,   182,
     213,   210,    76,   205,   208,   242,   204,   207,   242,   203,
     206,   242,    76,   191,   236,   182,    41,   182,    13,   226,
     218,    76,   242,    39,    90,    90,   138,   139,   241,   241,
     241,   241,   241,   119,    39,    34,   182,   182,   154,   181,
     160,   160,   181,   166,   168,   168,   168,   169,   171,   172,
     150,   172,   150,   182,   178,    76,   243,   243,   243,   243,
     241,   241,   241,     1,   242,     1,   211,   242,     1,   208,
      45,   138,   139,     1,   207,    45,     1,   206,    45,   138,
      34,    90,   241,   182,   241,   243,     1,   135,   136,   219,
     243,   241,   184,   184,    76,   182,    43,   120,   182,    90,
      40,    40,    40,    40,    40,    39,   172,    39,   172,    39,
      43,    43,    43,    43,    43,    43,    38,    56,    57,    58,
      59,    60,    72,    73,   151,   160,   187,    76,    80,    80,
     131,   187,    11,    60,    76,   187,   188,   192,    76,   191,
      90,    43,    41,    41,    43,    39,    39,    39,   182,   243,
     241,   182,    39,    39,   232,   230,   228,   228,   139,   214,
     183,   214,    74,    75,   145,   189,   190,   191,   139,    56,
     151,    56,    56,    42,    34,    39,    80,    34,    60,    76,
     192,   151,    41,    34,   182,   226,   243,   243,   182,   241,
     119,    40,   183,   214,   215,   216,    34,    34,    34,    37,
      90,   182,   139,    36,   139,   139,   160,    39,   151,    36,
      40,   183,   193,    40,    40,    40,    34,    43,    90,    90,
      39,    39,   190,    39,   182,   187,   182,   182,    36,   192,
      40,    90,   241,    43,    43,   182,   216,   215,    39,    39,
      39,   183,   182,   183,   241,    36,    34,    34,    56,   139,
     182,    39
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
        case 3:
#line 234 "grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); }
    break;

  case 5:
#line 238 "grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); }
    break;

  case 6:
#line 240 "grammar.y"
    {node_int_setcar((yyvsp[(2) - (2)].node), -(node_get_int((yyvsp[(2) - (2)].node)))); (yyval.node) = (yyvsp[(2) - (2)].node);}
    break;

  case 11:
#line 253 "grammar.y"
    {(yyval.node) = new_lined_node(TWODOTS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 12:
#line 257 "grammar.y"
    {(yyval.node) = new_lined_node(TWODOTS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 15:
#line 263 "grammar.y"
    {(yyval.node) = new_lined_node(UWCONST, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 16:
#line 265 "grammar.y"
    {(yyval.node) = new_lined_node(SWCONST, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 17:
#line 267 "grammar.y"
    {(yyval.node) = new_lined_node(WSIZEOF, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 18:
#line 269 "grammar.y"
    {(yyval.node) = new_lined_node(CAST_TOINT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 21:
#line 273 "grammar.y"
    {
                 yyerror("fractional constants are not supported.");
                 YYABORT;
               }
    break;

  case 22:
#line 278 "grammar.y"
    {
                 yyerror("exponential constants are not supported.");
                 YYABORT;
               }
    break;

  case 23:
#line 283 "grammar.y"
    {
                 yyerror("real constants are not supported.");
                 YYABORT;
               }
    break;

  case 25:
#line 297 "grammar.y"
    { (yyval.node) = new_lined_node(UMINUS, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 27:
#line 299 "grammar.y"
    {(yyval.node) = new_node(SELF,Nil,Nil);}
    break;

  case 28:
#line 301 "grammar.y"
    {
                    int ntype = node_get_type((yyvsp[(1) - (3)].node));
                    if (ATOM != ntype && DOT != ntype && ARRAY != ntype && SELF != ntype) {
                      yyerror_lined("incorrect DOT expression", (yyvsp[(2) - (3)].lineno));
                      YYABORT;
                    }
                    (yyval.node) = new_lined_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)) ;
                  }
    break;

  case 29:
#line 310 "grammar.y"
    {
                   int ntype = node_get_type((yyvsp[(1) - (3)].node));
                   if (ATOM != ntype && DOT != ntype && ARRAY != ntype && SELF != ntype) {
                     yyerror_lined("incorrect DOT expression", (yyvsp[(2) - (3)].lineno));
                     YYABORT;
                   }
                   (yyval.node) = new_lined_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)) ;
                  }
    break;

  case 30:
#line 319 "grammar.y"
    {
                   /* array may have any expression on the left.
                      The type check will detect any problems */
                   (yyval.node) = new_lined_node(ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));
                  }
    break;

  case 31:
#line 325 "grammar.y"
    {
                    (yyval.node) = new_lined_node(BIT_SELECTION, (yyvsp[(1) - (6)].node),
                                        new_lined_node(COLON, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(4) - (6)].lineno)), (yyvsp[(2) - (6)].lineno));
                  }
    break;

  case 32:
#line 329 "grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 33:
#line 330 "grammar.y"
    { (yyval.node) = new_lined_node(NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 34:
#line 331 "grammar.y"
    { (yyval.node) = new_lined_node(CAST_BOOL, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 35:
#line 332 "grammar.y"
    { (yyval.node) = new_lined_node(CAST_WORD1, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 36:
#line 333 "grammar.y"
    { (yyval.node) = new_lined_node(NEXT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 37:
#line 334 "grammar.y"
    { (yyval.node) = new_lined_node(CAST_SIGNED, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 38:
#line 335 "grammar.y"
    { (yyval.node) = new_lined_node(CAST_UNSIGNED, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno)); }
    break;

  case 39:
#line 336 "grammar.y"
    { (yyval.node) = new_lined_node(EXTEND, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 40:
#line 337 "grammar.y"
    { (yyval.node) = new_lined_node(WRESIZE, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 41:
#line 338 "grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 42:
#line 342 "grammar.y"
    { (yyval.node) = new_lined_node(WAREAD, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 43:
#line 345 "grammar.y"
    { (yyval.node) = new_lined_node(WAWRITE, (yyvsp[(3) - (8)].node), new_node(WAWRITE, (yyvsp[(5) - (8)].node), (yyvsp[(7) - (8)].node)), (yyvsp[(2) - (8)].lineno)); }
    break;

  case 44:
#line 347 "grammar.y"
    { (yyval.node) = new_lined_node(COUNT, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(2) - (4)].lineno)); }
    break;

  case 45:
#line 351 "grammar.y"
    { (yyval.node) = cons((yyvsp[(1) - (1)].node), Nil); }
    break;

  case 46:
#line 352 "grammar.y"
    { (yyval.node) = cons((yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 47:
#line 357 "grammar.y"
    { (yyval.node) = new_node(CASE, (yyvsp[(1) - (1)].node), failure_make("case conditions are not exhaustive", FAILURE_CASE_NOT_EXHAUSTIVE, yylineno));}
    break;

  case 48:
#line 358 "grammar.y"
    { (yyval.node) = new_node(CASE, (yyvsp[(1) - (2)].node), (yyvsp[(2) - (2)].node)); }
    break;

  case 49:
#line 363 "grammar.y"
    { (yyval.node) = build_case_colon_node((yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno)); }
    break;

  case 51:
#line 368 "grammar.y"
    { (yyval.node) = new_lined_node(CONCATENATION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 53:
#line 373 "grammar.y"
    { (yyval.node) = new_lined_node(TIMES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 54:
#line 374 "grammar.y"
    { (yyval.node) = new_lined_node(DIVIDE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 55:
#line 375 "grammar.y"
    { (yyval.node) = new_lined_node(MOD, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 57:
#line 380 "grammar.y"
    { (yyval.node) = new_lined_node(PLUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 58:
#line 381 "grammar.y"
    { (yyval.node) = new_lined_node(MINUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 60:
#line 385 "grammar.y"
    { (yyval.node) = new_lined_node(LSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 61:
#line 386 "grammar.y"
    { (yyval.node) = new_lined_node(RSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 64:
#line 394 "grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 66:
#line 398 "grammar.y"
    {(yyval.node) = new_lined_node(UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 68:
#line 403 "grammar.y"
    { (yyval.node) = new_lined_node(UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 70:
#line 407 "grammar.y"
    { (yyval.node) = new_lined_node(SETIN, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 72:
#line 412 "grammar.y"
    { (yyval.node) = new_lined_node(EQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 73:
#line 413 "grammar.y"
    { (yyval.node) = new_lined_node(NOTEQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 74:
#line 414 "grammar.y"
    { (yyval.node) = new_lined_node(LT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 75:
#line 415 "grammar.y"
    { (yyval.node) = new_lined_node(GT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 76:
#line 416 "grammar.y"
    { (yyval.node) = new_lined_node(LE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 77:
#line 417 "grammar.y"
    { (yyval.node) = new_lined_node(GE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 80:
#line 425 "grammar.y"
    { (yyval.node) = new_lined_node(EX, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 81:
#line 426 "grammar.y"
    { (yyval.node) = new_lined_node(AX, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 82:
#line 427 "grammar.y"
    { (yyval.node) = new_lined_node(EF, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 83:
#line 428 "grammar.y"
    { (yyval.node) = new_lined_node(AF, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 84:
#line 429 "grammar.y"
    { (yyval.node) = new_lined_node(EG, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 85:
#line 430 "grammar.y"
    { (yyval.node) = new_lined_node(AG, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 86:
#line 432 "grammar.y"
    { (yyval.node) = new_lined_node(AU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 87:
#line 434 "grammar.y"
    { (yyval.node) = new_lined_node(EU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 88:
#line 436 "grammar.y"
    { (yyval.node) = new_lined_node(ABU, new_lined_node(AU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)); }
    break;

  case 89:
#line 438 "grammar.y"
    { (yyval.node) = new_lined_node(EBU, new_lined_node(EU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node), (yyvsp[(1) - (7)].lineno)), (yyvsp[(5) - (7)].node), (yyvsp[(1) - (7)].lineno)); }
    break;

  case 90:
#line 439 "grammar.y"
    { (yyval.node) = new_lined_node(EBF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); }
    break;

  case 91:
#line 440 "grammar.y"
    { (yyval.node) = new_lined_node(ABF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); }
    break;

  case 92:
#line 441 "grammar.y"
    { (yyval.node) = new_lined_node(EBG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); }
    break;

  case 93:
#line 442 "grammar.y"
    { (yyval.node) = new_lined_node(ABG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node), (yyvsp[(1) - (3)].lineno)); }
    break;

  case 94:
#line 445 "grammar.y"
    { (yyval.node) = new_lined_node(NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 96:
#line 452 "grammar.y"
    { (yyval.node) = new_lined_node(AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 98:
#line 456 "grammar.y"
    { (yyval.node) = new_lined_node(OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 99:
#line 457 "grammar.y"
    { (yyval.node) = new_lined_node(XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 100:
#line 458 "grammar.y"
    { (yyval.node) = new_lined_node(XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 102:
#line 462 "grammar.y"
    { (yyval.node) = new_lined_node(IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 104:
#line 467 "grammar.y"
    { (yyval.node) = new_lined_node(IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 108:
#line 480 "grammar.y"
    {(yyval.node) = new_lined_node(OP_NEXT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 109:
#line 481 "grammar.y"
    {(yyval.node) = new_lined_node(OP_PREC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 110:
#line 482 "grammar.y"
    {(yyval.node) = new_lined_node(OP_NOTPRECNOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 111:
#line 483 "grammar.y"
    {(yyval.node) = new_lined_node(OP_GLOBAL, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 112:
#line 484 "grammar.y"
    {(yyval.node) = new_lined_node(OP_HISTORICAL, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 113:
#line 485 "grammar.y"
    {(yyval.node) = new_lined_node(OP_FUTURE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 114:
#line 486 "grammar.y"
    {(yyval.node) = new_lined_node(OP_ONCE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 115:
#line 488 "grammar.y"
    { (yyval.node) = new_lined_node(NOT, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno)); }
    break;

  case 117:
#line 497 "grammar.y"
    {(yyval.node) = new_lined_node(UNTIL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 118:
#line 499 "grammar.y"
    {(yyval.node) = new_lined_node(SINCE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 119:
#line 501 "grammar.y"
    {(yyval.node) = new_lined_node(NOT,
                           new_lined_node(UNTIL,
                             new_lined_node(NOT, (yyvsp[(1) - (3)].node), Nil, node_get_lineno((yyvsp[(1) - (3)].node))),
                             new_lined_node(NOT, (yyvsp[(3) - (3)].node), Nil, node_get_lineno((yyvsp[(3) - (3)].node))),
                             (yyvsp[(2) - (3)].lineno)), Nil, (yyvsp[(2) - (3)].lineno));
                  }
    break;

  case 120:
#line 508 "grammar.y"
    {(yyval.node) = new_lined_node(NOT,
                          new_lined_node(SINCE,
                              new_lined_node(NOT, (yyvsp[(1) - (3)].node), Nil, node_get_lineno((yyvsp[(1) - (3)].node))),
                              new_lined_node(NOT, (yyvsp[(3) - (3)].node), Nil, node_get_lineno((yyvsp[(3) - (3)].node))),
                              (yyvsp[(2) - (3)].lineno)), Nil, (yyvsp[(2) - (3)].lineno));
                  }
    break;

  case 122:
#line 518 "grammar.y"
    { (yyval.node) = new_lined_node(AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 124:
#line 523 "grammar.y"
    { (yyval.node) = new_lined_node(OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 125:
#line 524 "grammar.y"
    { (yyval.node) = new_lined_node(XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 126:
#line 525 "grammar.y"
    { (yyval.node) = new_lined_node(XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 128:
#line 530 "grammar.y"
    { (yyval.node) = new_lined_node(IFTHENELSE, new_lined_node(COLON, (yyvsp[(1) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(2) - (5)].lineno)), (yyvsp[(5) - (5)].node), (yyvsp[(2) - (5)].lineno)); }
    break;

  case 130:
#line 535 "grammar.y"
    { (yyval.node) = new_lined_node(IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 132:
#line 540 "grammar.y"
    { (yyval.node) = new_lined_node(IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno)); }
    break;

  case 134:
#line 551 "grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_SIMPLE)) YYABORT;}
    break;

  case 135:
#line 554 "grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_NEXT)) YYABORT;}
    break;

  case 136:
#line 557 "grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_CTL)) YYABORT;}
    break;

  case 137:
#line 560 "grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_LTL)) YYABORT;}
    break;

  case 138:
#line 565 "grammar.y"
    { (yyval.node) = new_lined_node(MINU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 139:
#line 567 "grammar.y"
    { (yyval.node) = new_lined_node(MAXU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node), (yyvsp[(1) - (6)].lineno)); }
    break;

  case 140:
#line 575 "grammar.y"
    {(yyval.node) = new_node(BOOLEAN, Nil, Nil);}
    break;

  case 141:
#line 576 "grammar.y"
    {
                yyerror("given token is not supported.");
                YYABORT;
              }
    break;

  case 142:
#line 580 "grammar.y"
    {
                yyerror("given token is not supported.");
                YYABORT;
              }
    break;

  case 143:
#line 585 "grammar.y"
    {(yyval.node) = new_lined_node(UNSIGNED_WORD, (yyvsp[(3) - (4)].node), Nil, (yyvsp[(1) - (4)].lineno));}
    break;

  case 144:
#line 587 "grammar.y"
    {(yyval.node) = new_lined_node(UNSIGNED_WORD, (yyvsp[(4) - (5)].node), Nil, (yyvsp[(1) - (5)].lineno));}
    break;

  case 145:
#line 589 "grammar.y"
    {(yyval.node) = new_lined_node(SIGNED_WORD, (yyvsp[(4) - (5)].node), Nil, (yyvsp[(1) - (5)].lineno));}
    break;

  case 147:
#line 592 "grammar.y"
    {(yyval.node) = new_lined_node(SCALAR, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 148:
#line 594 "grammar.y"
    {(yyval.node) = new_lined_node(WORDARRAY, (yyvsp[(4) - (10)].node), (yyvsp[(9) - (10)].node), (yyvsp[(1) - (10)].lineno));}
    break;

  case 149:
#line 596 "grammar.y"
    {(yyval.node) = new_lined_node(ARRAY_TYPE, (yyvsp[(2) - (4)].node), (yyvsp[(4) - (4)].node), (yyvsp[(1) - (4)].lineno));}
    break;

  case 152:
#line 602 "grammar.y"
    {(yyval.node) = new_lined_node(PROCESS, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 153:
#line 605 "grammar.y"
    {(yyval.node) = cons(find_atom((yyvsp[(1) - (1)].node)), Nil); free_node((yyvsp[(1) - (1)].node));}
    break;

  case 154:
#line 606 "grammar.y"
    {(yyval.node) = cons(find_atom((yyvsp[(3) - (3)].node)), (yyvsp[(1) - (3)].node)); free_node((yyvsp[(3) - (3)].node));}
    break;

  case 160:
#line 616 "grammar.y"
    {(yyval.node) = new_lined_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].lineno));}
    break;

  case 161:
#line 619 "grammar.y"
    {(yyval.node) = new_node(MODTYPE, (yyvsp[(1) - (1)].node), Nil);}
    break;

  case 162:
#line 620 "grammar.y"
    {(yyval.node) = new_node(MODTYPE, (yyvsp[(1) - (3)].node), Nil);}
    break;

  case 163:
#line 622 "grammar.y"
    {(yyval.node) = new_lined_node(MODTYPE, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), node_get_lineno((yyvsp[(1) - (4)].node)));}
    break;

  case 164:
#line 624 "grammar.y"
    {
                    /* $$ = new_lined_node(ARRAY, $2, $4, $1); */
                    /* array of modules is not supported any more.
                       NOTE: In future if there are some syntact conflicts
                       this case can be removed */
                    yyerror_lined("array of modules is no supported", (yyvsp[(1) - (4)].lineno));
                    YYABORT;
                  }
    break;

  case 165:
#line 635 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node),Nil);}
    break;

  case 166:
#line 636 "grammar.y"
    {(yyval.node) = cons((yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].node));}
    break;

  case 167:
#line 648 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 168:
#line 649 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 169:
#line 653 "grammar.y"
    {(yyval.node) = new_lined_node(MODULE, (yyvsp[(2) - (3)].node), (yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].lineno));}
    break;

  case 170:
#line 655 "grammar.y"
    {(yyval.node) = new_node(MODTYPE, (yyvsp[(1) - (1)].node), Nil);}
    break;

  case 171:
#line 656 "grammar.y"
    {(yyval.node) = new_node(MODTYPE, (yyvsp[(1) - (3)].node), Nil);}
    break;

  case 172:
#line 658 "grammar.y"
    {(yyval.node) = new_node(MODTYPE, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));}
    break;

  case 173:
#line 660 "grammar.y"
    {(yyval.node) = cons(find_atom((yyvsp[(1) - (1)].node)), Nil); free_node((yyvsp[(1) - (1)].node));}
    break;

  case 174:
#line 661 "grammar.y"
    {(yyval.node) = cons(find_atom((yyvsp[(3) - (3)].node)), (yyvsp[(1) - (3)].node)); free_node((yyvsp[(3) - (3)].node));}
    break;

  case 175:
#line 666 "grammar.y"
    {(yyval.node) = Nil;}
    break;

  case 176:
#line 667 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 177:
#line 668 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 199:
#line 700 "grammar.y"
    {(yyval.node) = new_lined_node(VAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));}
    break;

  case 200:
#line 701 "grammar.y"
    {(yyval.node) = new_lined_node(VAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 201:
#line 704 "grammar.y"
    {(yyval.node) = new_lined_node(FROZENVAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));}
    break;

  case 202:
#line 705 "grammar.y"
    {(yyval.node) = new_lined_node(FROZENVAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 203:
#line 708 "grammar.y"
    {(yyval.node) = new_lined_node(IVAR, Nil, Nil, (yyvsp[(1) - (1)].lineno));}
    break;

  case 204:
#line 709 "grammar.y"
    {(yyval.node) = new_lined_node(IVAR, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 205:
#line 712 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 206:
#line 713 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 207:
#line 714 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 208:
#line 716 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 209:
#line 717 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 210:
#line 718 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 211:
#line 720 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 212:
#line 721 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 213:
#line 722 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 214:
#line 725 "grammar.y"
    {(yyval.node) = new_lined_node(COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));}
    break;

  case 215:
#line 727 "grammar.y"
    {(yyval.node) = new_lined_node(COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));}
    break;

  case 216:
#line 729 "grammar.y"
    {(yyval.node) = new_lined_node(COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));}
    break;

  case 217:
#line 734 "grammar.y"
    {(yyval.node) = new_lined_node(DEFINE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 218:
#line 736 "grammar.y"
    {(yyval.node) = Nil;}
    break;

  case 219:
#line 737 "grammar.y"
    {(yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 220:
#line 738 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 221:
#line 742 "grammar.y"
    {(yyval.node) = new_lined_node(EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));}
    break;

  case 222:
#line 744 "grammar.y"
    {(yyval.node) = new_lined_node(EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));
                                 /* Note that array-define is declared
                                    as normal define.
                                    Then compile_instantiate in compileFlatten.c
                                    distinguish them by detecting
                                    ARRAY_DEF on right hand side.
                                   */
                                 }
    break;

  case 223:
#line 756 "grammar.y"
    {(yyval.node) = new_lined_node(DEFINE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 224:
#line 760 "grammar.y"
    {(yyval.node) = Nil;}
    break;

  case 225:
#line 761 "grammar.y"
    {(yyval.node) = cons(new_lined_node(EQDEF, (yyvsp[(2) - (5)].node), (yyvsp[(4) - (5)].node), (yyvsp[(3) - (5)].lineno)), (yyvsp[(1) - (5)].node));}
    break;

  case 226:
#line 762 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 227:
#line 766 "grammar.y"
    {(yyval.node) =  new_lined_node(ARRAY_DEF, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 228:
#line 767 "grammar.y"
    {(yyval.node) =  new_lined_node(ARRAY_DEF, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 229:
#line 771 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 230:
#line 772 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 231:
#line 776 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 232:
#line 777 "grammar.y"
    {(yyval.node) = cons((yyvsp[(1) - (1)].node),Nil);}
    break;

  case 233:
#line 781 "grammar.y"
    {(yyval.node) = new_lined_node(ASSIGN, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 234:
#line 783 "grammar.y"
    {(yyval.node) = Nil;}
    break;

  case 235:
#line 784 "grammar.y"
    {(yyval.node) = new_node(AND, (yyvsp[(1) - (2)].node), (yyvsp[(2) - (2)].node));}
    break;

  case 236:
#line 785 "grammar.y"
    { SYNTAX_ERROR_HANDLING((yyval.node), (yyvsp[(1) - (2)].node)); }
    break;

  case 237:
#line 788 "grammar.y"
    {(yyval.node) = new_lined_node(EQDEF, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node), (yyvsp[(2) - (4)].lineno));}
    break;

  case 238:
#line 790 "grammar.y"
    { (yyval.node) = new_lined_node(EQDEF,
                                        new_lined_node(SMALLINIT, (yyvsp[(3) - (7)].node), Nil, (yyvsp[(1) - (7)].lineno)),
                                        (yyvsp[(6) - (7)].node), (yyvsp[(5) - (7)].lineno));
                  }
    break;

  case 239:
#line 795 "grammar.y"
    { (yyval.node) = new_lined_node(EQDEF,
                                        new_lined_node(NEXT, (yyvsp[(3) - (7)].node), Nil, (yyvsp[(1) - (7)].lineno)),
                                        (yyvsp[(6) - (7)].node), (yyvsp[(5) - (7)].lineno));
                  }
    break;

  case 240:
#line 802 "grammar.y"
    {(yyval.node) = new_lined_node(INIT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 241:
#line 804 "grammar.y"
    {(yyval.node) = new_lined_node(INVAR, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 242:
#line 806 "grammar.y"
    {(yyval.node) = new_lined_node(TRANS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 243:
#line 810 "grammar.y"
    {(yyval.node) = new_lined_node(JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 244:
#line 813 "grammar.y"
    {(yyval.node) = new_lined_node(JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 245:
#line 818 "grammar.y"
    {(yyval.node) = new_lined_node(COMPASSION, cons((yyvsp[(3) - (7)].node),(yyvsp[(5) - (7)].node)), Nil, (yyvsp[(1) - (7)].lineno));}
    break;

  case 246:
#line 822 "grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); }
    break;

  case 247:
#line 823 "grammar.y"
    {(yyval.node) = new_node(CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));}
    break;

  case 248:
#line 825 "grammar.y"
    {(yyval.node) = new_lined_node(INVARSPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 249:
#line 826 "grammar.y"
    {(yyval.node) = new_lined_node(INVARSPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));}
    break;

  case 250:
#line 829 "grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); }
    break;

  case 251:
#line 830 "grammar.y"
    {(yyval.node) = new_node(CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));}
    break;

  case 252:
#line 832 "grammar.y"
    {(yyval.node) = new_lined_node(SPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 253:
#line 833 "grammar.y"
    {(yyval.node) = new_lined_node(SPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 254:
#line 834 "grammar.y"
    {(yyval.node) = new_lined_node(SPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));}
    break;

  case 255:
#line 835 "grammar.y"
    {(yyval.node) = new_lined_node(SPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));}
    break;

  case 256:
#line 838 "grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); }
    break;

  case 257:
#line 839 "grammar.y"
    {(yyval.node) = new_node(CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));}
    break;

  case 258:
#line 842 "grammar.y"
    {(yyval.node) = new_lined_node(LTLSPEC, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 259:
#line 843 "grammar.y"
    {(yyval.node) = new_lined_node(LTLSPEC, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));}
    break;

  case 260:
#line 846 "grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); }
    break;

  case 261:
#line 847 "grammar.y"
    {(yyval.node) = new_node(CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));}
    break;

  case 262:
#line 849 "grammar.y"
    {(yyval.node) = new_lined_node(COMPUTE, (yyvsp[(2) - (2)].node), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 263:
#line 850 "grammar.y"
    {(yyval.node) = new_lined_node(COMPUTE, (yyvsp[(5) - (5)].node), (yyvsp[(3) - (5)].node), (yyvsp[(1) - (5)].lineno));}
    break;

  case 264:
#line 855 "grammar.y"
    {
  if (nusmv_parse_psl() != 0) {
    YYABORT;
  }
  (yyval.node) = new_lined_node(PSLSPEC, psl_parsed_tree, psl_property_name, (yyvsp[(1) - (1)].lineno));
  psl_property_name = Nil;
}
    break;

  case 265:
#line 865 "grammar.y"
    {(yyval.node) = new_lined_node(CONSTANTS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 266:
#line 869 "grammar.y"
    {(yyval.node) = Nil;}
    break;

  case 267:
#line 870 "grammar.y"
    { (yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 268:
#line 871 "grammar.y"
    {(yyval.node) = cons((yyvsp[(3) - (3)].node), (yyvsp[(1) - (3)].node));}
    break;

  case 269:
#line 875 "grammar.y"
    { (yyval.node) = cons((yyvsp[(1) - (1)].node), Nil);}
    break;

  case 270:
#line 876 "grammar.y"
    { (yyval.node) = cons((yyvsp[(2) - (2)].node), (yyvsp[(1) - (2)].node));}
    break;

  case 271:
#line 881 "grammar.y"
    {
                   yyerror("given token is not supported.");
                   YYABORT;
                 }
    break;

  case 272:
#line 886 "grammar.y"
    {
                   yyerror("given token is not supported.");
                   YYABORT;
                 }
    break;

  case 273:
#line 892 "grammar.y"
    {
                   yyerror("given token is not supported.");
                   YYABORT;
                 }
    break;

  case 274:
#line 899 "grammar.y"
    {
                   yyerror("given token is not supported.");
                   YYABORT;
                 }
    break;

  case 275:
#line 906 "grammar.y"
    {
                    yyerror("given token is not supported.");
                    YYABORT;
                  }
    break;

  case 276:
#line 913 "grammar.y"
    {(yyval.node) = new_node(ISA, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 278:
#line 917 "grammar.y"
    {}
    break;

  case 280:
#line 926 "grammar.y"
    {(yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 281:
#line 927 "grammar.y"
    {(yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 282:
#line 928 "grammar.y"
    {(yyval.node) = new_node(ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));}
    break;

  case 283:
#line 930 "grammar.y"
    { node_ptr tmp = new_lined_node(NUMBER,
                                                      PTR_FROM_INT(node_ptr, -node_get_int((yyvsp[(4) - (5)].node))),
                                                      Nil,
                                                      (yyvsp[(3) - (5)].lineno));
                        (yyval.node) = new_node(ARRAY, (yyvsp[(1) - (5)].node), tmp);
                      }
    break;

  case 285:
#line 939 "grammar.y"
    {(yyval.node) = new_node(SELF,Nil,Nil);}
    break;

  case 286:
#line 940 "grammar.y"
    {(yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 287:
#line 941 "grammar.y"
    {(yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 288:
#line 942 "grammar.y"
    {(yyval.node) = new_node(ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));}
    break;

  case 289:
#line 949 "grammar.y"
    {(yyval.node) = (yyvsp[(1) - (1)].node);}
    break;

  case 290:
#line 950 "grammar.y"
    {return(1);}
    break;

  case 291:
#line 951 "grammar.y"
    {return(1);}
    break;

  case 292:
#line 955 "grammar.y"
    {(yyval.node) = new_lined_node(INIT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 293:
#line 957 "grammar.y"
    {(yyval.node) = new_lined_node(JUSTICE, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 294:
#line 959 "grammar.y"
    {(yyval.node) = new_lined_node(TRANS, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 295:
#line 961 "grammar.y"
    {(yyval.node) = new_lined_node(CONSTRAINT, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 296:
#line 964 "grammar.y"
    {(yyval.node) = new_lined_node(SIMPWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 297:
#line 965 "grammar.y"
    {(yyval.node) = new_lined_node(NEXTWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 298:
#line 966 "grammar.y"
    {(yyval.node) = new_lined_node(CTLWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 299:
#line 967 "grammar.y"
    {(yyval.node) = new_lined_node(LTLWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 300:
#line 968 "grammar.y"
    {(yyval.node) = new_lined_node(COMPWFF, node2maincontext((yyvsp[(2) - (2)].node)), Nil, (yyvsp[(1) - (2)].lineno));}
    break;

  case 301:
#line 969 "grammar.y"
    {(yyval.node) = new_lined_node(COMPID, (yyvsp[(2) - (3)].node), Nil, (yyvsp[(1) - (3)].lineno));}
    break;

  case 302:
#line 971 "grammar.y"
    {
                  yyerror("given token is not supported.");
                  YYABORT;
                }
    break;

  case 303:
#line 978 "grammar.y"
    {(yyval.node) = find_atom((yyvsp[(1) - (1)].node)); free_node((yyvsp[(1) - (1)].node)); }
    break;

  case 304:
#line 979 "grammar.y"
    {(yyval.node) = find_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 305:
#line 980 "grammar.y"
    {(yyval.node) = find_node(ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));}
    break;

  case 306:
#line 983 "grammar.y"
    { (yyval.node) = (yyvsp[(1) - (2)].node); }
    break;

  case 307:
#line 984 "grammar.y"
    {(yyval.node) = new_node(CONTEXT, (yyvsp[(3) - (4)].node), (yyvsp[(1) - (4)].node));}
    break;

  case 308:
#line 990 "grammar.y"
    {
  if (PARSE_MODULES != parse_mode_flag) {
    yyerror("unexpected MODULE definition encountered during parsing");
    YYABORT;
  }
}
    break;

  case 309:
#line 997 "grammar.y"
    {
                  parsed_tree = (yyvsp[(2) - (2)].node);
                }
    break;

  case 310:
#line 1000 "grammar.y"
    {
                  if (PARSE_COMMAND != parse_mode_flag) {
                    yyerror("unexpected command encountered during parsing");
                    YYABORT;
                  }
                }
    break;

  case 311:
#line 1006 "grammar.y"
    {parsed_tree = (yyvsp[(2) - (2)].node);}
    break;

  case 312:
#line 1007 "grammar.y"
    {
                  if (PARSE_LTL_EXPR != parse_mode_flag){
                    yyerror("unexpected expression encountered during parsing");
                    YYABORT;
                  }
                }
    break;

  case 313:
#line 1013 "grammar.y"
    {parsed_tree = (yyvsp[(2) - (2)].node);}
    break;


/* Line 1267 of yacc.c.  */
#line 3992 "grammar.c"
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


#line 1016 "grammar.y"

  /* BEGINS: grammar.y.3.50 */
/***************************************************************  -*-C-*-  ***/

/* Additional source code */

/* outputs the current token with the provided string and then may terminate */
void yyerror(char *s)
{
  /* In the input.l file we explicity tell flex that we want a pointer
     (see man flex -> %pointer). So we don't need to check if yytext
     is declared as pointer or as array  */
  extern char* yytext;
  extern int yylineno;
  OptsHandler_ptr opmgr = OptsHandler_get_instance();
  
  if (OptsHandler_get_bool_option_value(opmgr, OPT_PARSER_IS_LAX)) {
    parser_add_syntax_error(get_input_file(opmgr), yylineno, yytext, s);
  }
  else {
    start_parsing_err();
    fprintf(nusmv_stderr, "at token \"%s\": %s\n", yytext, s);
    if (opt_batch(opmgr)) { finish_parsing_err(); }
  }
}

/* the same as yyerror, except at first it sets the line number and does
 not output the current token
*/
void yyerror_lined(const char *s, int line)
{
  extern char* yytext;
  extern int yylineno;
  OptsHandler_ptr opmgr = OptsHandler_get_instance();

  /*set the line number */
  yylineno = line;

  if (OptsHandler_get_bool_option_value(opmgr, OPT_PARSER_IS_LAX)) {
    parser_add_syntax_error(get_input_file(opmgr), line, yytext, s);
  }
  else {
    start_parsing_err();
    fprintf(nusmv_stderr, ": %s\n", s);
    if (opt_batch(opmgr)) { finish_parsing_err(); }
  }
}

int yywrap()
{
  return(1);
}


/* Given a node (possibly a relative or absolute context)
   constructs a node that is contextualized absolutely
   (i.e. relatively to main module). This is used to construct
   context of properties that have to be instatiated in main
   module */
static node_ptr node2maincontext(node_ptr node)
{
  node_ptr ctx;

  if (node_get_type(node) == CONTEXT) {
    /* already a context */
    ctx = CompileFlatten_concat_contexts(Nil, car(node));
    return find_node(CONTEXT, ctx, cdr(node));
  }

  /* an atom, array or dot */
  return find_node(CONTEXT, Nil, node);
}

/* This functions build the COLON node for case expressions.  If
   backward compatibility is enabled, and the condition expression is
   found to be the constant "1", then a warning is printed and the
   condition is replaced with TRUE. */
static node_ptr build_case_colon_node(node_ptr l,
                                      node_ptr r,
                                      int linum)
{
  node_ptr res;

  static int user_warned = 0;

  if (opt_backward_comp(OptsHandler_get_instance()) &&
      (NUMBER == node_get_type(l)) && (1 == NODE_TO_INT(car(l)))) {

    /* Print this warning only once. */
    if (!user_warned) {
      fprintf(nusmv_stderr,
              "\nWARNING *** Option backward_compatibility (-old) is deprecate ***\n");
      fprintf(nusmv_stderr,
              "WARNING *** and will no longer be supported in future NuSMV versions. ***\n\n");
      user_warned = 1;
    }

    fprintf(nusmv_stderr, "WARNING (");

    if (get_input_file(OptsHandler_get_instance())) {
      fprintf(nusmv_stderr, "file %s", get_input_file(OptsHandler_get_instance()));
    }
    else fprintf(nusmv_stderr, "file stdin");

    fprintf(nusmv_stderr,
            ", line %d) : Deprecated use of \"1\" for case condition\n", linum);

    res = new_lined_node(COLON, new_node(TRUEEXP, Nil, Nil), r, linum);
  }
  else {
    res = new_lined_node(COLON, l, r, linum);
  }

  return res;
}

/* this functions checks that the expression is formed syntactically correct.
   Takes the expression to be checked, the expected kind of the
   expression. Returns true if the expression is formed correctly, and
   false otherwise.
   See enum EXP_KIND for more info about syntactic well-formedness.
*/
static boolean isCorrectExp(node_ptr exp, enum EXP_KIND expectedKind)
{
  switch(node_get_type(exp))
    {
      /* atomic expression (or thier operands have been checked earlier) */
    case FAILURE:
    case FALSEEXP:
    case TRUEEXP:
    case NUMBER:
    case NUMBER_UNSIGNED_WORD:
    case NUMBER_SIGNED_WORD:
    case NUMBER_FRAC:
    case NUMBER_REAL:
    case NUMBER_EXP:
    case UWCONST:
    case SWCONST:
    case TWODOTS:
    case DOT:
    case ATOM:
    case SELF:
    case ARRAY:
    case COUNT:
      return true;

      /* unary operators incompatible with LTL and CTL operator */
    case CAST_BOOL:
    case CAST_WORD1:
    case CAST_SIGNED:
    case CAST_UNSIGNED:
    case WSIZEOF:
    case CAST_TOINT:
      if (EXP_LTL == expectedKind || EXP_CTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_SIMPLE);
      }
      /* unary operators compatible with LTL and CTL operator */
    case NOT:
    case UMINUS:
      return isCorrectExp(car(exp), expectedKind);

      /* binary opertors incompatible with LTL and CTL operator */
    case BIT_SELECTION:
    case CASE: case COLON:
    case CONCATENATION:
    case TIMES: case DIVIDE: case PLUS :case MINUS: case MOD:
    case LSHIFT: case RSHIFT: case LROTATE: case RROTATE:
    case WAREAD: case WAWRITE: /* AC ADDED THESE */
    case UNION: case SETIN:
    case EQUAL: case NOTEQUAL: case LT: case GT: case LE: case GE:
    case IFTHENELSE:
    case EXTEND:
    case WRESIZE:
      if (EXP_LTL == expectedKind || EXP_CTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_SIMPLE)
          && isCorrectExp(cdr(exp), EXP_SIMPLE);
      }
      /* binary opertors compatible LTL and CTL operator */
    case AND: case OR: case XOR: case XNOR: case IFF: case IMPLIES:
      return isCorrectExp(car(exp), expectedKind)
        && isCorrectExp(cdr(exp), expectedKind);

      /* next expression */
    case NEXT:
      if (EXP_NEXT != expectedKind) {
        yyerror_lined("unexpected 'next' operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_SIMPLE); /* NEXT cannot contain NEXT */

      /* CTL unary expressions */
    case EX: case AX: case EF: case AF: case EG: case AG:
    case ABU: case EBU:
    case EBF: case ABF: case EBG: case ABG:
      if (EXP_CTL != expectedKind) {
        yyerror_lined("unexpected CTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_CTL); /* continue to check CTL */

      /* CTL binary expressions */
    case AU: case EU:
      if (EXP_CTL != expectedKind) {
        yyerror_lined("unexpected CTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_CTL)
        && isCorrectExp(cdr(exp), EXP_CTL); /* continue to check CTL */


      /* LTL unary expressions */
    case OP_NEXT: case OP_PREC: case OP_NOTPRECNOT: case OP_GLOBAL:
    case OP_HISTORICAL: case OP_FUTURE: case OP_ONCE:
      if (EXP_LTL != expectedKind) {
        yyerror_lined("unexpected LTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_LTL); /* continue to check LTL */


      /* LTL binary expressions */
    case UNTIL: case SINCE:
      if (EXP_LTL != expectedKind) {
        yyerror_lined("unexpected LTL operator", node_get_lineno(exp));
        return false;
      }
      return isCorrectExp(car(exp), EXP_LTL)
        && isCorrectExp(cdr(exp), EXP_LTL); /* continue to check LTL */

    default: nusmv_assert(false); /* unknown expression */
    }
  return false; /* should never be invoked */
}


static int nusmv_parse_psl()
{
  int res;
  res = psl_yyparse();
  return res;
}

  /* ENDS:   grammar.y.3.50 */

