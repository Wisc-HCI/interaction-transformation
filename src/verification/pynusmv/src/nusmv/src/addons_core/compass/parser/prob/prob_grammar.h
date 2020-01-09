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
     TK_COLON = 258,
     TK_EQUAL = 259,
     TK_RB = 260,
     TK_LB = 261,
     TK_FALSE = 262,
     TK_TRUE = 263,
     TK_REAL = 264,
     TK_NUMBER = 265,
     TK_ATOM = 266,
     TK_SEMI = 267,
     TK_DOT = 268,
     TK_AND = 269
   };
#endif
/* Tokens.  */
#define TK_COLON 258
#define TK_EQUAL 259
#define TK_RB 260
#define TK_LB 261
#define TK_FALSE 262
#define TK_TRUE 263
#define TK_REAL 264
#define TK_NUMBER 265
#define TK_ATOM 266
#define TK_SEMI 267
#define TK_DOT 268
#define TK_AND 269




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 77 "prob_grammar.y"
{
  node_ptr node;
}
/* Line 1529 of yacc.c.  */
#line 81 "prob_grammar.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE parser_prob_lval;

