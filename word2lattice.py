#!/usr/bin/python3
#encoding:utf-8
from ctypes import CDLL, POINTER, c_uint, c_char_p, create_string_buffer, Structure
import sys
import time
import random
class Lattice_struct(Structure):
    _fileds_ = [("ptr", POINTER), ("rows", c_uint), ("columns", c_uint)]

lab = ["now:" + time.strftime("%H:%M"),"彳亍口巴" ,"Lebrance"]
def Initial():
    lib = CDLL("./lib/libword2lattice.so")
    lattice_func = lib.statement_to_lattice
    lattice_func.restype = POINTER(Lattice_struct)
    lattice_func.argtypes = (c_char_p,)

    show_func = lib.draw_lattice
    show_func.argtypes = (POINTER(Lattice_struct),)

    return lattice_func, show_func
def main(word, lattice_func, show_func):
    

    statement = create_string_buffer(word.encode("gb2312"))
    a = lattice_func(statement)
    show_func(a)

if __name__ == "__main__":
    lattice_func, show_func = Initial()
    if len(sys.argv)==1:
        main(lab[random.randint(0, 2)], lattice_func, show_func)
    else:
        main(sys.argv[1], lattice_func, show_func)