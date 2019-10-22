"""mylibをimportする。
   使うときは
   from mylib import capsulenet
   capsulenet.CapsuleNet()
   みたいな感じ

   以下importのメモ
   from mylib import capsulenetとすると__init__.py(mylib)の中からcapsulenetとしてimportされているものを探す。
   例えば、
   import numpy as capsulenet
   とすると
   capsulenet.max([1,2])
   みたいに使える。
   *を使うときは*の部分をpythonファイルにしないとややこしいことになる。"""
from mylib.capsulenet import capsulenet
from mylib.resnet import resnet
