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
#define yyparse parser_ap_parse
#define yylex   parser_ap_lex
#define yyerror parser_ap_error
#define yylval  parser_ap_lval
#define yychar  parser_ap_char
#define yydebug parser_ap_debug
#define yynerrs parser_ap_nerrs


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




/* Copy the first part of user declarations.  */
#line 1 "ap_grammar.y"

/**CFile***********************************************************************

  FileName    [ap_grammar.y]

  PackageName [parser.ap]

  Synopsis    [Yacc for apability input file]

  SeeAlso     [ap_input.l]

  Author      [Marco Roveri]

  Copyright   [
  This file is part of the ``compass.parser.ap'' package of NuSMV version 2.
  Copyright (C) 2008 by FBK-irst.

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

#include "ParserAp.h"
#include "ParserAp_private.h"
#include "apInt.h"

#include "node/node.h"
#include "utils/error.h"
#include "utils/utils.h"

#include "parser/symbols.h"

static char rcsid[] UTIL_UNUSED = "$Id: ";

extern FILE* nusmv_stderr;


void parser_ap_error(char *s);

enum EXP_KIND {EXP_SIMPLE, EXP_NEXT, EXP_LTL, EXP_CTL};
static boolean isCorrectExp ARGS((node_ptr exp, enum EXP_KIND expectedKind));




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
#line 83 "ap_grammar.y"
{
  node_ptr node;
}
/* Line 193 of yacc.c.  */
#line 358 "ap_grammar.c"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif



/* Copy the second part of user declarations.  */


/* Line 216 of yacc.c.  */
#line 371 "ap_grammar.c"

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
#define YYFINAL  6
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   612

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  85
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  41
/* YYNRULES -- Number of rules.  */
#define YYNRULES  127
/* YYNRULES -- Number of states.  */
#define YYNSTATES  249

/* YYTRANSLATE(YYLEX) -- Bison symbol number corresponding to YYLEX.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   339

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
      75,    76,    77,    78,    79,    80,    81,    82,    83,    84
};

#if YYDEBUG
/* YYPRHS[YYN] -- Index of the first RHS symbol of rule number YYN in
   YYRHS.  */
static const yytype_uint16 yyprhs[] =
{
       0,     0,     3,     5,     6,     9,    14,    15,    17,    19,
      22,    24,    27,    30,    32,    34,    36,    38,    42,    44,
      46,    48,    50,    52,    54,    56,    58,    61,    63,    65,
      69,    73,    78,    85,    89,    92,    97,   102,   107,   112,
     117,   124,   128,   130,   133,   138,   140,   144,   146,   150,
     154,   158,   160,   164,   168,   170,   174,   178,   180,   182,
     186,   188,   192,   194,   198,   200,   204,   206,   210,   214,
     218,   222,   226,   230,   232,   234,   237,   240,   243,   246,
     249,   252,   259,   266,   274,   282,   286,   290,   294,   298,
     301,   303,   307,   309,   313,   317,   321,   323,   327,   329,
     333,   335,   337,   339,   342,   345,   348,   351,   354,   357,
     360,   363,   365,   369,   373,   377,   381,   383,   387,   389,
     393,   397,   401,   403,   407,   409,   413,   415
};

/* YYRHS -- A `-1'-separated list of the rules' RHS.  */
static const yytype_int8 yyrhs[] =
{
      86,     0,    -1,    87,    -1,    -1,    88,    87,    -1,     5,
      18,   125,    89,    -1,    -1,    11,    -1,     9,    -1,    72,
       9,    -1,     9,    -1,    72,     9,    -1,    71,     9,    -1,
      10,    -1,     8,    -1,     7,    -1,     6,    -1,    91,    22,
      91,    -1,     4,    -1,     3,    -1,    90,    -1,    92,    -1,
      93,    -1,    95,    -1,    94,    -1,    97,    -1,    71,    98,
      -1,     5,    -1,    21,    -1,    98,    78,     5,    -1,    98,
      78,     9,    -1,    98,    79,   125,    15,    -1,    98,    79,
     125,    18,   125,    15,    -1,    17,   124,    16,    -1,    23,
      98,    -1,    84,    17,   124,    16,    -1,    83,    17,   124,
      16,    -1,    76,    17,   124,    16,    -1,    82,    17,   124,
      16,    -1,    81,    17,   124,    16,    -1,    80,    17,   124,
      30,   124,    16,    -1,    20,    99,    19,    -1,   100,    -1,
     100,    99,    -1,   124,    18,   124,    11,    -1,    98,    -1,
     101,    74,    98,    -1,   101,    -1,   102,    70,   101,    -1,
     102,    69,   101,    -1,   102,    73,   101,    -1,   102,    -1,
     103,    72,   102,    -1,   103,    71,   102,    -1,   103,    -1,
     104,    66,   103,    -1,   104,    65,   103,    -1,   104,    -1,
      96,    -1,    14,   106,    13,    -1,   124,    -1,   106,    30,
     124,    -1,   105,    -1,   107,    68,   105,    -1,   107,    -1,
     108,    67,   107,    -1,   108,    -1,   109,    62,   108,    -1,
     109,    61,   108,    -1,   109,    60,   108,    -1,   109,    59,
     108,    -1,   109,    58,   108,    -1,   109,    57,   108,    -1,
     109,    -1,   111,    -1,    38,   110,    -1,    37,   110,    -1,
      36,   110,    -1,    35,   110,    -1,    34,   110,    -1,    33,
     110,    -1,    31,    79,   116,    41,   116,    15,    -1,    32,
      79,   116,    41,   116,    15,    -1,    31,    79,   116,    45,
      96,   116,    15,    -1,    32,    79,   116,    45,    96,   116,
      15,    -1,    49,    96,   110,    -1,    47,    96,   110,    -1,
      48,    96,   110,    -1,    46,    96,   110,    -1,    23,   111,
      -1,   110,    -1,   112,    24,   110,    -1,   112,    -1,   113,
      27,   112,    -1,   113,    26,   112,    -1,   113,    25,   112,
      -1,   113,    -1,   114,    28,   113,    -1,   114,    -1,   114,
      29,   115,    -1,   115,    -1,   110,    -1,   118,    -1,    52,
     117,    -1,    56,   117,    -1,    55,   117,    -1,    51,   117,
      -1,    54,   117,    -1,    50,   117,    -1,    53,   117,    -1,
      23,   118,    -1,   117,    -1,   119,    41,   117,    -1,   119,
      42,   117,    -1,   119,    39,   117,    -1,   119,    40,   117,
      -1,   119,    -1,   120,    24,   119,    -1,   120,    -1,   121,
      27,   120,    -1,   121,    26,   120,    -1,   121,    25,   120,
      -1,   121,    -1,   122,    28,   121,    -1,   122,    -1,   122,
      29,   123,    -1,   123,    -1,   124,    -1
};

/* YYRLINE[YYN] -- source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   139,   139,   143,   144,   150,   157,   157,   159,   160,
     163,   164,   165,   169,   171,   173,   175,   178,   182,   183,
     184,   185,   186,   190,   194,   207,   208,   209,   210,   211,
     222,   233,   244,   248,   249,   250,   251,   252,   253,   254,
     255,   256,   260,   262,   266,   271,   272,   276,   277,   278,
     279,   283,   284,   285,   288,   289,   290,   296,   297,   298,
     301,   302,   306,   307,   310,   311,   315,   316,   317,   318,
     319,   320,   321,   324,   325,   329,   330,   331,   332,   333,
     334,   335,   337,   339,   341,   343,   344,   345,   346,   349,
     355,   356,   359,   360,   361,   362,   365,   366,   370,   371,
     374,   378,   379,   384,   385,   386,   387,   388,   389,   390,
     392,   397,   398,   400,   402,   408,   417,   418,   422,   423,
     424,   425,   429,   430,   434,   435,   438,   440
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || YYTOKEN_TABLE
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "TOK_TRUEEXP", "TOK_FALSEEXP",
  "TOK_ATOM", "TOK_NUMBER_EXP", "TOK_NUMBER_REAL", "TOK_NUMBER_FRAC",
  "TOK_NUMBER", "TOK_NUMBER_WORD", "TOK_SEMI", "TOK_CONS", "TOK_RCB",
  "TOK_LCB", "TOK_RB", "TOK_RP", "TOK_LP", "TOK_COLON", "TOK_ESAC",
  "TOK_CASE", "TOK_SELF", "TOK_TWODOTS", "TOK_NOT", "TOK_AND", "TOK_XNOR",
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
  "TOK_LB", "TOK_EXTEND", "TOK_UNSIGNED", "TOK_SIGNED", "TOK_WORD1",
  "TOK_BOOL", "$accept", "begin", "ap_list", "ap_list_item", "optsemi",
  "number", "integer", "number_word", "number_frac", "number_real",
  "number_exp", "subrange", "constant", "primary_expr",
  "case_element_list_expr", "case_element_expr", "concatination_expr",
  "multiplicative_expr", "additive_expr", "shift_expr", "set_expr",
  "set_list_expr", "union_expr", "in_expr", "relational_expr", "ctl_expr",
  "pure_ctl_expr", "ctl_and_expr", "ctl_or_expr", "ctl_iff_expr",
  "ctl_implies_expr", "ctl_basic_expr", "ltl_unary_expr",
  "pure_ltl_unary_expr", "ltl_binary_expr", "and_expr", "or_expr",
  "iff_expr", "implies_expr", "basic_expr", "simple_expression", 0
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
     335,   336,   337,   338,   339
};
# endif

/* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,    85,    86,    87,    87,    88,    89,    89,    90,    90,
      91,    91,    91,    92,    93,    94,    95,    96,    97,    97,
      97,    97,    97,    97,    97,    98,    98,    98,    98,    98,
      98,    98,    98,    98,    98,    98,    98,    98,    98,    98,
      98,    98,    99,    99,   100,   101,   101,   102,   102,   102,
     102,   103,   103,   103,   104,   104,   104,   105,   105,   105,
     106,   106,   107,   107,   108,   108,   109,   109,   109,   109,
     109,   109,   109,   110,   110,   111,   111,   111,   111,   111,
     111,   111,   111,   111,   111,   111,   111,   111,   111,   111,
     112,   112,   113,   113,   113,   113,   114,   114,   115,   115,
     116,   117,   117,   118,   118,   118,   118,   118,   118,   118,
     118,   119,   119,   119,   119,   119,   120,   120,   121,   121,
     121,   121,   122,   122,   123,   123,   124,   125
};

/* YYR2[YYN] -- Number of symbols composing right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     0,     2,     4,     0,     1,     1,     2,
       1,     2,     2,     1,     1,     1,     1,     3,     1,     1,
       1,     1,     1,     1,     1,     1,     2,     1,     1,     3,
       3,     4,     6,     3,     2,     4,     4,     4,     4,     4,
       6,     3,     1,     2,     4,     1,     3,     1,     3,     3,
       3,     1,     3,     3,     1,     3,     3,     1,     1,     3,
       1,     3,     1,     3,     1,     3,     1,     3,     3,     3,
       3,     3,     3,     1,     1,     2,     2,     2,     2,     2,
       2,     6,     6,     7,     7,     3,     3,     3,     3,     2,
       1,     3,     1,     3,     3,     3,     1,     3,     1,     3,
       1,     1,     1,     2,     2,     2,     2,     2,     2,     2,
       2,     1,     3,     3,     3,     3,     1,     3,     1,     3,
       3,     3,     1,     3,     1,     3,     1,     1
};

/* YYDEFACT[STATE-NAME] -- Default rule to reduce with in state
   STATE-NUM when YYTABLE doesn't specify something else to do.  Zero
   means the default is an error.  */
static const yytype_uint8 yydefact[] =
{
       3,     0,     0,     2,     3,     0,     1,     4,    19,    18,
      27,    16,    15,    14,     8,    13,     0,     0,     0,    28,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,    20,     0,
      21,    22,    24,    23,    58,    25,    45,    47,    51,    54,
      57,    62,    64,    66,    73,   101,    74,   111,   102,   116,
     118,   122,   124,   126,   127,     6,     0,    60,     0,     0,
      42,     0,     8,     0,     0,    34,    89,   110,     0,     0,
       0,    80,    79,    78,    77,    76,    75,    10,     0,     0,
       0,     0,     0,     0,   108,   106,   103,   109,   107,   105,
     104,     8,     0,    26,     9,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       7,     5,    59,     0,    33,    41,    43,     0,     9,    90,
      92,    96,    98,   100,     0,     0,    12,    11,    88,    86,
      87,    85,     0,     0,     0,     0,     0,     0,    17,    29,
      30,     0,    46,    49,    48,    50,    53,    52,    56,    55,
      63,    65,    72,    71,    70,    69,    68,    67,   114,   115,
     112,   113,   117,   121,   120,   119,   123,   125,    61,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
      37,     0,    39,    38,    36,    35,    31,     0,    44,    91,
      95,    94,    93,    97,    99,     0,     0,     0,     0,     0,
       0,    81,     0,    82,     0,    40,    32,    83,    84
};

/* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     2,     3,     4,   151,    48,    49,    50,    51,    52,
      53,    54,    55,    56,    79,    80,    57,    58,    59,    60,
      61,    76,    62,    63,    64,    65,    66,   160,   161,   162,
     163,   164,    67,    68,    69,    70,    71,    72,    73,    74,
      75
};

/* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
   STATE-NUM.  */
#define YYPACT_NINF -138
static const yytype_int16 yypact[] =
{
      33,    29,    51,  -138,    33,   200,  -138,  -138,  -138,  -138,
    -138,  -138,  -138,  -138,    63,  -138,   200,   200,   200,  -138,
     282,    11,    17,   364,   364,   364,   364,   364,   364,    15,
      15,    15,    15,   200,   200,   200,   200,   200,   200,   200,
      94,    83,    95,    99,   103,   112,   115,   116,  -138,   113,
    -138,  -138,  -138,  -138,  -138,  -138,   -21,    60,   -30,    -8,
      23,  -138,    68,    70,   -31,  -138,  -138,  -138,  -138,    13,
     114,    35,    66,  -138,  -138,   128,    12,  -138,   125,   126,
     200,   130,  -138,   528,   135,   -21,  -138,  -138,   364,   364,
     446,  -138,  -138,  -138,  -138,  -138,  -138,  -138,   137,   140,
     364,   364,   364,   364,  -138,  -138,  -138,  -138,  -138,  -138,
    -138,   129,   528,   -21,   131,   200,   200,   200,   200,   200,
     200,    15,    39,   200,   528,   528,   528,   528,   528,   528,
     528,   528,   493,   493,   493,   493,   493,   493,   493,   493,
     200,   200,   200,   200,   200,   200,   200,   200,   200,   200,
    -138,  -138,  -138,   200,  -138,  -138,  -138,   200,  -138,  -138,
     132,    42,    90,  -138,     4,     5,  -138,  -138,  -138,  -138,
    -138,  -138,   134,   122,   138,   139,   141,   142,  -138,  -138,
    -138,    41,   -21,    60,    60,    60,   -30,   -30,    -8,    -8,
    -138,    68,    70,    70,    70,    70,    70,    70,  -138,  -138,
    -138,  -138,    13,   114,   114,   114,    35,  -138,  -138,   148,
     364,   364,   364,   364,   364,   364,   364,    15,   364,    15,
    -138,   200,  -138,  -138,  -138,  -138,  -138,   200,  -138,  -138,
     132,   132,   132,    42,  -138,   146,   364,   149,   364,   147,
     152,  -138,   153,  -138,   154,  -138,  -138,  -138,  -138
};

/* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -138,  -138,   167,  -138,  -138,  -138,    52,  -138,  -138,  -138,
    -138,   -20,  -138,     1,    92,  -138,   -54,    -1,     0,  -138,
      47,  -138,    48,  -102,  -138,   -23,     3,  -137,   -34,  -138,
     -33,   -76,   -19,   163,    40,   -64,    37,  -138,    45,   -10,
    -101
};

/* YYTABLE[YYPACT[STATE-NUM]].  What to do in state STATE-NUM.  If
   positive, shift that token.  If negative, reduce the rule which
   number is the opposite.  If zero, do what YYDEFACT says.
   If YYTABLE_NINF, syntax error.  */
#define YYTABLE_NINF -13
static const yytype_int16 yytable[] =
{
      91,    92,    93,    94,    95,    96,    77,    78,    81,   100,
     101,   102,   103,   165,   104,   105,   106,   107,   108,   109,
     110,    85,   181,    86,    97,   152,   134,   135,   136,   137,
     138,   139,   192,   193,   194,   195,   196,   197,     1,   125,
     126,   113,   153,   127,   179,   216,   218,     5,   180,   217,
     219,     6,   140,   141,   142,   143,   226,   122,   123,   227,
     145,   146,   147,   128,   129,   159,   159,   211,   212,   213,
      81,   183,   184,   185,   230,   231,   232,   168,   169,   170,
     171,   203,   204,   205,   113,   -10,    98,    99,   130,   131,
      88,    85,   114,    86,   148,   149,    89,     8,     9,    10,
      11,    12,    13,   111,    15,   172,   173,   174,   175,   176,
     177,    17,   115,    85,    18,    19,   116,   112,   214,   215,
     117,   198,   199,   200,   201,   182,   240,   186,   187,   118,
     188,   189,   119,   120,   124,   121,   132,   133,   144,   150,
     235,   154,   237,   208,   158,   155,   166,   209,   157,   167,
     220,   -12,   221,   -11,   222,   223,   210,   224,   225,   228,
     242,   241,   244,   245,   243,    83,    84,   246,   247,   248,
      42,     7,   156,   178,    43,    44,    45,    46,    47,   190,
     233,   191,   234,    87,   202,   206,     0,   229,   159,   159,
     159,   159,   159,   159,   207,   159,     0,   236,     0,   238,
       0,     0,     0,     8,     9,    10,    11,    12,    13,    14,
      15,   239,     0,   159,    16,   159,     0,    17,     0,     0,
      18,    19,     0,    20,     0,     0,     0,     0,     0,     0,
       0,    21,    22,    23,    24,    25,    26,    27,    28,     0,
       0,     0,     0,     0,     0,     0,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    40,    41,     0,     0,     0,    42,     0,     0,     0,
      43,    44,    45,    46,    47,     8,     9,    10,    11,    12,
      13,    82,    15,     0,     0,     0,     0,     0,     0,    17,
       0,     0,    18,    19,     0,    20,     0,     0,     0,     0,
       0,     0,     0,    21,    22,    23,    24,    25,    26,    27,
      28,     0,     0,     0,     0,     0,     0,     0,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,    83,    84,     0,     0,     0,    42,     0,
       0,     0,    43,    44,    45,    46,    47,     8,     9,    10,
      11,    12,    13,    14,    15,     0,     0,     0,    16,     0,
       0,    17,     0,     0,    18,    19,     0,    90,     0,     0,
       0,     0,     0,     0,     0,    21,    22,    23,    24,    25,
      26,    27,    28,     0,     0,     0,     0,     0,     0,     0,
      29,    30,    31,    32,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,    40,    41,     0,     0,     0,
      42,     0,     0,     0,    43,    44,    45,    46,    47,     8,
       9,    10,    11,    12,    13,    82,    15,     0,     0,     0,
       0,     0,     0,    17,     0,     0,    18,    19,     0,    90,
       0,     0,     0,     0,     0,     0,     0,    21,    22,    23,
      24,    25,    26,    27,    28,     0,     0,     0,     0,     0,
       0,     0,    29,    30,    31,    32,     8,     9,    10,    11,
      12,    13,    14,    15,     0,     0,     0,    16,     0,     0,
      17,     0,     0,    18,    19,     0,   112,    83,    84,     0,
       0,     0,    42,     0,     0,     0,    43,    44,    45,    46,
      47,     8,     9,    10,    11,    12,    13,    82,    15,     0,
       0,     0,     0,     0,     0,    17,     0,     0,    18,    19,
       0,   112,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,    40,    41,     0,     0,     0,    42,
       0,     0,     0,    43,    44,    45,    46,    47,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,    83,
      84,     0,     0,     0,    42,     0,     0,     0,    43,    44,
      45,    46,    47
};

static const yytype_int16 yycheck[] =
{
      23,    24,    25,    26,    27,    28,    16,    17,    18,    29,
      30,    31,    32,    89,    33,    34,    35,    36,    37,    38,
      39,    20,   123,    20,     9,    13,    57,    58,    59,    60,
      61,    62,   134,   135,   136,   137,   138,   139,     5,    69,
      70,    40,    30,    73,     5,    41,    41,    18,     9,    45,
      45,     0,    39,    40,    41,    42,    15,    78,    79,    18,
      25,    26,    27,    71,    72,    88,    89,    25,    26,    27,
      80,   125,   126,   127,   211,   212,   213,   100,   101,   102,
     103,   145,   146,   147,    83,    22,    71,    72,    65,    66,
      79,    90,     9,    90,    28,    29,    79,     3,     4,     5,
       6,     7,     8,     9,    10,   115,   116,   117,   118,   119,
     120,    17,    17,   112,    20,    21,    17,    23,    28,    29,
      17,   140,   141,   142,   143,   124,   227,   128,   129,    17,
     130,   131,    17,    17,    74,    22,    68,    67,    24,    11,
     216,    16,   218,   153,     9,    19,     9,   157,    18,     9,
      16,    22,    30,    22,    16,    16,    24,    16,    16,    11,
     236,    15,   238,    16,    15,    71,    72,    15,    15,    15,
      76,     4,    80,   121,    80,    81,    82,    83,    84,   132,
     214,   133,   215,    20,   144,   148,    -1,   210,   211,   212,
     213,   214,   215,   216,   149,   218,    -1,   217,    -1,   219,
      -1,    -1,    -1,     3,     4,     5,     6,     7,     8,     9,
      10,   221,    -1,   236,    14,   238,    -1,    17,    -1,    -1,
      20,    21,    -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    31,    32,    33,    34,    35,    36,    37,    38,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    46,    47,    48,    49,
      50,    51,    52,    53,    54,    55,    56,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    71,    72,    -1,    -1,    -1,    76,    -1,    -1,    -1,
      80,    81,    82,    83,    84,     3,     4,     5,     6,     7,
       8,     9,    10,    -1,    -1,    -1,    -1,    -1,    -1,    17,
      -1,    -1,    20,    21,    -1,    23,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    31,    32,    33,    34,    35,    36,    37,
      38,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    71,    72,    -1,    -1,    -1,    76,    -1,
      -1,    -1,    80,    81,    82,    83,    84,     3,     4,     5,
       6,     7,     8,     9,    10,    -1,    -1,    -1,    14,    -1,
      -1,    17,    -1,    -1,    20,    21,    -1,    23,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    31,    32,    33,    34,    35,
      36,    37,    38,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      46,    47,    48,    49,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    71,    72,    -1,    -1,    -1,
      76,    -1,    -1,    -1,    80,    81,    82,    83,    84,     3,
       4,     5,     6,     7,     8,     9,    10,    -1,    -1,    -1,
      -1,    -1,    -1,    17,    -1,    -1,    20,    21,    -1,    23,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    31,    32,    33,
      34,    35,    36,    37,    38,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    46,    47,    48,    49,     3,     4,     5,     6,
       7,     8,     9,    10,    -1,    -1,    -1,    14,    -1,    -1,
      17,    -1,    -1,    20,    21,    -1,    23,    71,    72,    -1,
      -1,    -1,    76,    -1,    -1,    -1,    80,    81,    82,    83,
      84,     3,     4,     5,     6,     7,     8,     9,    10,    -1,
      -1,    -1,    -1,    -1,    -1,    17,    -1,    -1,    20,    21,
      -1,    23,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    71,    72,    -1,    -1,    -1,    76,
      -1,    -1,    -1,    80,    81,    82,    83,    84,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    -1,    71,
      72,    -1,    -1,    -1,    76,    -1,    -1,    -1,    80,    81,
      82,    83,    84
};

/* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
   symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,     5,    86,    87,    88,    18,     0,    87,     3,     4,
       5,     6,     7,     8,     9,    10,    14,    17,    20,    21,
      23,    31,    32,    33,    34,    35,    36,    37,    38,    46,
      47,    48,    49,    50,    51,    52,    53,    54,    55,    56,
      71,    72,    76,    80,    81,    82,    83,    84,    90,    91,
      92,    93,    94,    95,    96,    97,    98,   101,   102,   103,
     104,   105,   107,   108,   109,   110,   111,   117,   118,   119,
     120,   121,   122,   123,   124,   125,   106,   124,   124,    99,
     100,   124,     9,    71,    72,    98,   111,   118,    79,    79,
      23,   110,   110,   110,   110,   110,   110,     9,    71,    72,
      96,    96,    96,    96,   117,   117,   117,   117,   117,   117,
     117,     9,    23,    98,     9,    17,    17,    17,    17,    17,
      17,    22,    78,    79,    74,    69,    70,    73,    71,    72,
      65,    66,    68,    67,    57,    58,    59,    60,    61,    62,
      39,    40,    41,    42,    24,    25,    26,    27,    28,    29,
      11,    89,    13,    30,    16,    19,    99,    18,     9,   110,
     112,   113,   114,   115,   116,   116,     9,     9,   110,   110,
     110,   110,   124,   124,   124,   124,   124,   124,    91,     5,
       9,   125,    98,   101,   101,   101,   102,   102,   103,   103,
     105,   107,   108,   108,   108,   108,   108,   108,   117,   117,
     117,   117,   119,   120,   120,   120,   121,   123,   124,   124,
      24,    25,    26,    27,    28,    29,    41,    45,    41,    45,
      16,    30,    16,    16,    16,    16,    15,    18,    11,   110,
     112,   112,   112,   113,   115,   116,    96,   116,    96,   124,
     125,    15,   116,    15,   116,    16,    15,    15,    15
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
#line 139 "ap_grammar.y"
    { }
    break;

  case 3:
#line 143 "ap_grammar.y"
    {}
    break;

  case 4:
#line 145 "ap_grammar.y"
    {
               parser_ap_add(parser_ap_get_global_parser(), (yyvsp[(1) - (2)].node));
             }
    break;

  case 5:
#line 151 "ap_grammar.y"
    {
  (yyval.node) = parser_ap_mk_ap(parser_ap_get_global_parser(), (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));
}
    break;

  case 7:
#line 157 "ap_grammar.y"
    {}
    break;

  case 9:
#line 160 "ap_grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); }
    break;

  case 11:
#line 164 "ap_grammar.y"
    { (yyval.node) = (yyvsp[(2) - (2)].node); }
    break;

  case 12:
#line 166 "ap_grammar.y"
    {node_int_setcar((yyvsp[(2) - (2)].node), -(node_get_int((yyvsp[(2) - (2)].node)))); (yyval.node) = (yyvsp[(2) - (2)].node);}
    break;

  case 17:
#line 179 "ap_grammar.y"
    {(yyval.node) = new_node(TWODOTS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 22:
#line 187 "ap_grammar.y"
    {
                 (yyval.node) = (yyvsp[(1) - (1)].node);
               }
    break;

  case 23:
#line 191 "ap_grammar.y"
    {
                 (yyval.node) = (yyvsp[(1) - (1)].node);
               }
    break;

  case 24:
#line 195 "ap_grammar.y"
    {
                 (yyval.node) = (yyvsp[(1) - (1)].node);
               }
    break;

  case 26:
#line 208 "ap_grammar.y"
    { (yyval.node) = new_node(UMINUS, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 28:
#line 210 "ap_grammar.y"
    {(yyval.node) = new_node(SELF,Nil,Nil);}
    break;

  case 29:
#line 212 "ap_grammar.y"
    {
                      if (ATOM != node_get_type((yyvsp[(1) - (3)].node)) &&
                          DOT != node_get_type((yyvsp[(1) - (3)].node)) &&
                          ARRAY != node_get_type((yyvsp[(1) - (3)].node)) &&
                          SELF != node_get_type((yyvsp[(1) - (3)].node))) {
                        yyerror("incorrect DOT expression");
                        YYABORT;
                      }
                      (yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)) ;
                    }
    break;

  case 30:
#line 223 "ap_grammar.y"
    {
                      if (ATOM != node_get_type((yyvsp[(1) - (3)].node)) &&
                          DOT != node_get_type((yyvsp[(1) - (3)].node)) &&
                          ARRAY != node_get_type((yyvsp[(1) - (3)].node)) &&
                          SELF != node_get_type((yyvsp[(1) - (3)].node))) {
                        yyerror("incorrect DOT expression");
                        YYABORT;
                      }
                      (yyval.node) = new_node(DOT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)) ;
                    }
    break;

  case 31:
#line 234 "ap_grammar.y"
    {
                       if (ATOM != node_get_type((yyvsp[(1) - (4)].node)) &&
                           DOT != node_get_type((yyvsp[(1) - (4)].node)) &&
                           ARRAY != node_get_type((yyvsp[(1) - (4)].node)) &&
                           SELF != node_get_type((yyvsp[(1) - (4)].node))) {
                        yyerror("incorrect ARRAY expression");
                        YYABORT;
                       }
                       (yyval.node) = new_node(ARRAY, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));
                     }
    break;

  case 32:
#line 245 "ap_grammar.y"
    {
                        (yyval.node) = new_node(BIT_SELECTION, (yyvsp[(1) - (6)].node), new_node(COLON, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node)));
                       }
    break;

  case 33:
#line 248 "ap_grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 34:
#line 249 "ap_grammar.y"
    { (yyval.node) = new_node(NOT, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 35:
#line 250 "ap_grammar.y"
    { (yyval.node) = new_node(CAST_BOOL, (yyvsp[(3) - (4)].node), Nil); }
    break;

  case 36:
#line 251 "ap_grammar.y"
    { (yyval.node) = new_node(CAST_WORD1, (yyvsp[(3) - (4)].node), Nil); }
    break;

  case 37:
#line 252 "ap_grammar.y"
    { (yyval.node) = new_node(NEXT, (yyvsp[(3) - (4)].node), Nil); }
    break;

  case 38:
#line 253 "ap_grammar.y"
    { (yyval.node) = new_node(CAST_SIGNED, (yyvsp[(3) - (4)].node), Nil); }
    break;

  case 39:
#line 254 "ap_grammar.y"
    { (yyval.node) = new_node(CAST_UNSIGNED, (yyvsp[(3) - (4)].node), Nil); }
    break;

  case 40:
#line 255 "ap_grammar.y"
    { (yyval.node) = new_node(EXTEND, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node)); }
    break;

  case 41:
#line 256 "ap_grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 42:
#line 261 "ap_grammar.y"
    { (yyval.node) = new_node(CASE, (yyvsp[(1) - (1)].node), failure_make("case conditions are not exhaustive", FAILURE_CASE_NOT_EXHAUSTIVE, parser_ap_lineno));}
    break;

  case 43:
#line 262 "ap_grammar.y"
    { (yyval.node) = new_node(CASE, (yyvsp[(1) - (2)].node), (yyvsp[(2) - (2)].node)); }
    break;

  case 44:
#line 267 "ap_grammar.y"
    {(yyval.node) = new_node(COLON, (yyvsp[(1) - (4)].node), (yyvsp[(3) - (4)].node));}
    break;

  case 46:
#line 272 "ap_grammar.y"
    { (yyval.node) = new_node(CONCATENATION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 48:
#line 277 "ap_grammar.y"
    { (yyval.node) = new_node(TIMES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 49:
#line 278 "ap_grammar.y"
    { (yyval.node) = new_node(DIVIDE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 50:
#line 279 "ap_grammar.y"
    { (yyval.node) = new_node(MOD, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 52:
#line 284 "ap_grammar.y"
    { (yyval.node) = new_node(PLUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 53:
#line 285 "ap_grammar.y"
    { (yyval.node) = new_node(MINUS, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 55:
#line 289 "ap_grammar.y"
    { (yyval.node) = new_node(LSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 56:
#line 290 "ap_grammar.y"
    { (yyval.node) = new_node(RSHIFT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 59:
#line 298 "ap_grammar.y"
    { (yyval.node) = (yyvsp[(2) - (3)].node); }
    break;

  case 61:
#line 302 "ap_grammar.y"
    {(yyval.node) = new_node(UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 63:
#line 307 "ap_grammar.y"
    { (yyval.node) = new_node(UNION, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 65:
#line 311 "ap_grammar.y"
    { (yyval.node) = new_node(SETIN, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 67:
#line 316 "ap_grammar.y"
    { (yyval.node) = new_node(EQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 68:
#line 317 "ap_grammar.y"
    { (yyval.node) = new_node(NOTEQUAL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 69:
#line 318 "ap_grammar.y"
    { (yyval.node) = new_node(LT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 70:
#line 319 "ap_grammar.y"
    { (yyval.node) = new_node(GT, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 71:
#line 320 "ap_grammar.y"
    { (yyval.node) = new_node(LE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 72:
#line 321 "ap_grammar.y"
    { (yyval.node) = new_node(GE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 75:
#line 329 "ap_grammar.y"
    { (yyval.node) = new_node(EX, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 76:
#line 330 "ap_grammar.y"
    { (yyval.node) = new_node(AX, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 77:
#line 331 "ap_grammar.y"
    { (yyval.node) = new_node(EF, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 78:
#line 332 "ap_grammar.y"
    { (yyval.node) = new_node(AF, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 79:
#line 333 "ap_grammar.y"
    { (yyval.node) = new_node(EG, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 80:
#line 334 "ap_grammar.y"
    { (yyval.node) = new_node(AG, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 81:
#line 336 "ap_grammar.y"
    { (yyval.node) = new_node(AU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node)); }
    break;

  case 82:
#line 338 "ap_grammar.y"
    { (yyval.node) = new_node(EU, (yyvsp[(3) - (6)].node), (yyvsp[(5) - (6)].node)); }
    break;

  case 83:
#line 340 "ap_grammar.y"
    { (yyval.node) = new_node(ABU, new_node(AU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node)), (yyvsp[(5) - (7)].node)); }
    break;

  case 84:
#line 342 "ap_grammar.y"
    { (yyval.node) = new_node(EBU, new_node(EU, (yyvsp[(3) - (7)].node), (yyvsp[(6) - (7)].node)), (yyvsp[(5) - (7)].node)); }
    break;

  case 85:
#line 343 "ap_grammar.y"
    { (yyval.node) = new_node(EBF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node)); }
    break;

  case 86:
#line 344 "ap_grammar.y"
    { (yyval.node) = new_node(ABF, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node)); }
    break;

  case 87:
#line 345 "ap_grammar.y"
    { (yyval.node) = new_node(EBG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node)); }
    break;

  case 88:
#line 346 "ap_grammar.y"
    { (yyval.node) = new_node(ABG, (yyvsp[(3) - (3)].node), (yyvsp[(2) - (3)].node)); }
    break;

  case 89:
#line 349 "ap_grammar.y"
    { (yyval.node) = new_node(NOT, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 91:
#line 356 "ap_grammar.y"
    { (yyval.node) = new_node(AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 93:
#line 360 "ap_grammar.y"
    { (yyval.node) = new_node(OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 94:
#line 361 "ap_grammar.y"
    { (yyval.node) = new_node(XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 95:
#line 362 "ap_grammar.y"
    { (yyval.node) = new_node(XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 97:
#line 366 "ap_grammar.y"
    { (yyval.node) = new_node(IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 99:
#line 371 "ap_grammar.y"
    { (yyval.node) = new_node(IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 103:
#line 384 "ap_grammar.y"
    {(yyval.node) = new_node(OP_NEXT, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 104:
#line 385 "ap_grammar.y"
    {(yyval.node) = new_node(OP_PREC, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 105:
#line 386 "ap_grammar.y"
    {(yyval.node) = new_node(OP_NOTPRECNOT, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 106:
#line 387 "ap_grammar.y"
    {(yyval.node) = new_node(OP_GLOBAL, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 107:
#line 388 "ap_grammar.y"
    {(yyval.node) = new_node(OP_HISTORICAL, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 108:
#line 389 "ap_grammar.y"
    {(yyval.node) = new_node(OP_FUTURE, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 109:
#line 390 "ap_grammar.y"
    {(yyval.node) = new_node(OP_ONCE, (yyvsp[(2) - (2)].node), Nil);}
    break;

  case 110:
#line 392 "ap_grammar.y"
    { (yyval.node) = new_node(NOT, (yyvsp[(2) - (2)].node), Nil); }
    break;

  case 112:
#line 399 "ap_grammar.y"
    {(yyval.node) = new_node(UNTIL, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 113:
#line 401 "ap_grammar.y"
    {(yyval.node) = new_node(SINCE, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node));}
    break;

  case 114:
#line 403 "ap_grammar.y"
    {(yyval.node) = new_node(NOT,
                           new_node(UNTIL,
                             new_node(NOT, (yyvsp[(1) - (3)].node), Nil),
                             new_node(NOT, (yyvsp[(3) - (3)].node), Nil)), Nil);
                  }
    break;

  case 115:
#line 409 "ap_grammar.y"
    {(yyval.node) = new_node(NOT,
                          new_node(SINCE,
                              new_node(NOT, (yyvsp[(1) - (3)].node), Nil),
                              new_node(NOT, (yyvsp[(3) - (3)].node), Nil)), Nil);
                  }
    break;

  case 117:
#line 418 "ap_grammar.y"
    { (yyval.node) = new_node(AND, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 119:
#line 423 "ap_grammar.y"
    { (yyval.node) = new_node(OR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 120:
#line 424 "ap_grammar.y"
    { (yyval.node) = new_node(XOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 121:
#line 425 "ap_grammar.y"
    { (yyval.node) = new_node(XNOR,(yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 123:
#line 430 "ap_grammar.y"
    { (yyval.node) = new_node(IFF, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 125:
#line 435 "ap_grammar.y"
    { (yyval.node) = new_node(IMPLIES, (yyvsp[(1) - (3)].node), (yyvsp[(3) - (3)].node)); }
    break;

  case 127:
#line 440 "ap_grammar.y"
    {if (!isCorrectExp((yyval.node), EXP_SIMPLE)) YYABORT;}
    break;


/* Line 1267 of yacc.c.  */
#line 2368 "ap_grammar.c"
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


#line 454 "ap_grammar.y"



/* Additional source code */
void parser_ap_error(char *s)
{
    extern char parser_ap_text[];

    fprintf(nusmv_stderr,"\n");
    if (get_output_order_file(OptsHandler_get_instance())) {
      fprintf(nusmv_stderr, "file %s: ",
              get_output_order_file(OptsHandler_get_instance()));
    }
    else {
      fprintf(nusmv_stderr, "file stdin: ");
    }

    if (parser_ap_lineno) {
      fprintf(nusmv_stderr, "line %d: ", parser_ap_lineno);
    }

    fprintf(nusmv_stderr, "at token \"%s\": %s\n", parser_ap_text, s);
    if (opt_batch(OptsHandler_get_instance())) {
      /* exits the execution */
      fprintf(nusmv_stderr, "\n");
      print_io_atom_stack(nusmv_stderr);
      nusmv_exit(1);
    }
}

int parser_ap_wrap()  { return 1; }

extern void yyerror_lined(const char *s, int line);

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
    case TWODOTS:
    case DOT:
    case ATOM:
    case SELF:
    case ARRAY:
    case BIT_SELECTION:
      return true;

      /* unary operators incompatible with LTL and CTL operator */
    case CAST_BOOL:
    case CAST_WORD1:
    case CAST_SIGNED:
    case CAST_UNSIGNED:
    case EXTEND:
      if (EXP_LTL == expectedKind || EXP_CTL == expectedKind) {
        return isCorrectExp(car(exp), EXP_SIMPLE);
      }
      /* unary operators compatible with LTL and CTL operator */
    case NOT:
    case UMINUS:
      return isCorrectExp(car(exp), expectedKind);

      /* binary opertors incompatible with LTL and CTL operator */
    case CASE: case COLON:
    case CONCATENATION:
    case TIMES: case DIVIDE: case PLUS :case MINUS: case MOD:
    case LSHIFT: case RSHIFT: case LROTATE: case RROTATE:
    case WAREAD: case WAWRITE: /* AC ADDED THESE */
    case UNION: case SETIN:
    case EQUAL: case NOTEQUAL: case LT: case GT: case LE: case GE:
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

