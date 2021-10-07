"""The tokenizer, parser, and interpreter for KeyLang, the language used by 
gachapy to save and load custom rarity to drop rate conversions

KeyLang Grammar
-------------------
Expr -> Term + Expr | Term - Expr | Term
Term -> Factor * Term | Factor / Term | Factor
Factor -> Base ^ Factor | Base
Base -> Const | ( Expr )
Const -> <float literal> | <rarity>
Rar -> <rarity>

Example: 2 * (1 + R) / 5 ^ 2 where R = rarity

Author: Jacob Kerr, 2021
"""
from typing import *


class SyntaxError(BaseException):
    """The exception thrown when a syntax error is found"""
    pass


class Ast(object):
    """The base class of the abstract syntax tree"""
    def __init__(self, left=None, right=None, data=None) -> None:
        self.left = left
        self.right = right
        self.data = data

class Expr(Ast):
    """An expression in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class Term(Ast):
    """A term in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class Factor(Ast):
    """A factor in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class Float(Ast):
    """A float literal in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.data}'

class Rar(Ast):
    """A rarity variable in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return "R"

def parse(s: str) -> Ast:
    return _parse_tokens(_tokenize(s))

def _tokenize(s: str) -> List[str]:
    """Converts the inputed KeyLang expression into a list of tokens
    
    Parameters
    ----------
    s : str
        the KeyLang expression to tokenize
    
    Returns
    -------
    List[str]
        the list of tokens"""
    return s.split()

def _parse_tokens(tokens: List[str]) -> Ast:
    """Parses the inputted tokens into a KeyLang abstract syntax tree
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the tokens"""
    return _parse_expr(tokens)

def _parse_expr(tokens: List[str]) -> Ast:
    """Parses the inputted tokens as an expression
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the expression"""
    match tokens:
        case [a, "+", *b] | [a, "-", *b]:
            expr = Expr(_parse_term(a), _parse_expr(b), tokens[1])
        case _:
            expr = _parse_term(tokens)
    return expr

def _parse_term(tokens: List[str]) -> Ast:
    """Parses the inputted tokens as a term
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the term"""
    match tokens:
        case [a, "*", *b] | [a, "/", *b]:
            term = Term(_parse_factor(a), _parse_term(b), tokens[1])
        case _:
            term = _parse_factor(tokens)
    return term

def _parse_factor(tokens: List[str]) -> Ast:
    """Parses the inputted tokens as a factor
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the factor"""
    match tokens:
        case [a, "^", *b]:
            factor = Factor(_parse_base(a), _parse_factor(b), tokens[1])
        case _:
            factor = _parse_base(tokens)
    return factor

def _parse_base(tokens: List[str]) -> Ast:
    """Parses the inputted tokens as a base
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the base"""
    match tokens:
        case ["(", *a, ")"]:
            base = _parse_expr(a)
        case _:
            base = _parse_const(tokens[0])
    return base

def _parse_const(tokens: str) -> Ast:
    """Parses the inputted tokens as a constant
    
    Parameters
    ----------
    tokens : List[str]
        the list of tokens to parse
        
    Returns
    -------
    Ast
        the abstract syntax tree representative of the constant"""
    match tokens:
        case "R":
            const = Rar()
        case tokens:
            try:
                const = Float(data=float(tokens))
            except:
                raise SyntaxError(f'Float literal not found in place of constant: {tokens}')
    return const

def interpret(ast: Ast, rarity: float) -> float:
    """Interprets the ast """
    match ast:
        case Expr():
            if ast.data == "+":
                return interpret(ast.left, rarity) + interpret(ast.right, rarity)
            else: 
                return interpret(ast.left, rarity) - interpret(ast.right, rarity)
        case Term():
            if ast.data == "*":
                return interpret(ast.left, rarity) * interpret(ast.right, rarity)
            else: 
                return interpret(ast.left, rarity) / interpret(ast.right, rarity)
        case Factor():
            return interpret(ast.left, rarity) ** interpret(ast.right, rarity)
        case Float():
            return ast.data
        case Rar():
            return rarity