"""The tokenizer, parser, and interpreter for KeyLang, the language used by 
gachapy to save and load custom rarity to drop rate functions
KeyLang is a simple calculator-based language. Each token in the language must
be separated by a space. The expressions follow standard order of operations. 
The following are allowed operations:
+ : addition 
- : subtraction 
* : multiplication 
/ : division 
^ : exponent 
( ... ) : parentheses (for overriding order of operations), where ... is any
expression 
any float literal 
R : rarity, to be substituted upon interpretation time 

KeyLang Grammar
-------------------
Expr -> Term + Expr | Term - Expr | Term
Term -> Factor * Term | Factor / Term | Factor
Factor -> Base ^ Factor | Base
Base -> Const | ( Expr )
Const -> <float literal> | <rarity>
Rar -> <rarity>

Example: 2 * ( 1 + R ) / 5 ^ 2 where R = rarity

Author: Jacob Kerr, 2021
"""
from typing import List


class SyntaxError(BaseException):
    """The exception thrown when a syntax error is found"""
    pass


class Ast(object):
    """The base class of the abstract syntax tree"""
    def __init__(self, left=None, right=None, data=None) -> None:
        self.left = left
        self.right = right
        self.data = data

class _Expr(Ast):
    """An expression in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class _Term(Ast):
    """A term in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class _Factor(Ast):
    """A factor in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.left} {self.data} {self.right}'

class _Float(Ast):
    """A float literal in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return f'{self.data}'

class _Rar(Ast):
    """A rarity variable in the KeyLang grammar"""
    
    def __str__(self) -> str:
        return "R"

def parse(s: str) -> Ast:
    """Parses the inputed KeyLang expression into a KeyLang abstract syntax 
    tree
    
    Parameters
    ----------
    s : str
        the expression to parse
        
    Returns
    -------
    Ast
        the KeyLang AST representative of the expression"""
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
    term = _parse_term(tokens)
    if len(tokens) == 0:
        return term
    match tokens[0]:
        case '+':
            tokens.pop(0)
            return _Expr(term, _parse_expr(tokens), '+')
        case '-':
            tokens.pop(0)
            return _Expr(term, _parse_expr(tokens), '-')
        case _:
            return term

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
    factor = _parse_factor(tokens)
    if len(tokens) == 0:
        return factor
    match tokens[0]:
        case '*':
            tokens.pop(0)
            return _Term(factor, _parse_term(tokens), '*')
        case '/':
            tokens.pop(0)
            return _Term(factor, _parse_term(tokens), '/')
        case _:
            return factor

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
    base = _parse_base(tokens)
    if len(tokens) == 0:
        return base
    match tokens[0]:
        case '^':
            tokens.pop(0)
            return _Factor(base, _parse_factor(tokens), '^')
        case _:
            return base

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
    if len(tokens) == 0:
        raise SyntaxError(f'Abrupt end of expression found')
    match tokens[0]:
        case '(':
            tokens.pop(0)
            base = _parse_expr(tokens)
            if tokens.pop(0) != ')':
                raise SyntaxError(f'Mismatched parentheses at -> {" ".join(tokens)}')
            return base
        case _:
            return _parse_const(tokens)

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
    match tokens[0]:
        case "R":
            return _Rar()
        case _:
            try:
                num = tokens.pop(0)
                return _Float(data=float(num))
            except:
                raise SyntaxError(f'Float literal not found -> {" ".join(tokens)}')

def interpret(ast: Ast, rarity: float) -> float:
    """Evaluates the KeyLang AST to a value using the rarity
    
    Parameters
    ----------
    ast : Ast
        the AST of the expression
    rarity : float
        the value for the rarity
        
    Returns
    -------
    float
        the result of the expression"""
    match ast:
        case _Expr():
            if ast.data == "+":
                return interpret(ast.left, rarity) + interpret(ast.right, rarity)
            else: 
                return interpret(ast.left, rarity) - interpret(ast.right, rarity)
        case _Term():
            if ast.data == "*":
                return interpret(ast.left, rarity) * interpret(ast.right, rarity)
            else: 
                return interpret(ast.left, rarity) / interpret(ast.right, rarity)
        case _Factor():
            return interpret(ast.left, rarity) ** interpret(ast.right, rarity)
        case _Float():
            return ast.data
        case _Rar():
            return rarity