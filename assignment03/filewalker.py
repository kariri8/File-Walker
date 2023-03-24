
from fileposition import FilePosition
from typing import Tuple, Generator, TextIO

import os
import syntax
import copy
import codecs


class FileWalker : 
   topdir : str  # Python uses strings for representing file names. 
  
   def __init__( self, topdir ) :
      self. topdir = topdir # No checks here. 


   def recDirIterator( self ) -> Generator[ Tuple[ str, str, FilePosition ], None, None ] :
      if not os.path.exists(self.topdir) or not os.path.isdir(self.topdir):
         raise FileExistsError(" Root file does not exist or not a directory")
      for dir, subdirs, files in os.walk(self.topdir):
         for fileName in files:
            joinedName = os.path.join( dir, fileName )
            f = open(joinedName, "r", encoding = "utf8")
            for word, pos in self.fileIterator(f):
               yield joinedName, word, pos




   @staticmethod 
   def fileIterator( f : TextIO ) -> Generator[ Tuple[ str, FilePosition ], None, None ] :
      token = ""
      pos = FilePosition()
      while True:
         char = f.read(1)
         if not syntax.inWord(str(char)):
            if len(token) > 0:
               newPos = copy.copy(pos)
               newPos.column = newPos.column - len( token )
               token = token.lower()
               yield token, newPos
               token = ""
         elif syntax.inWord(str(char)):
            token += str(char)
         pos.advance(1)
         if syntax.isNewLine(str(char)):
            pos.nextLine()

         if not char:
            break

   def __repr__( self ) -> str : 
      return "FileWalker: " + self. topdir 

   def __str__( self ) -> str :
      return "FileWalker: " + self. topdir


