
from fileposition import FilePosition
from typing import List, Dict, Set, Optional 

class Occurrences : 
   occs : Dict[ str, Dict[ str, Set[ FilePosition ]]] 

   def __init__( self ) :
      self. occs = dict( ) 


   def add( self, word : str, filename : str, pos : FilePosition ) -> None :
      word = word.lower()
      if word in self.occs:
         if filename in self.occs.get(word):
            self.occs.get(word).get(filename).add(pos)
         else:
            posSet: set[FilePosition] = {pos}
            self.occs.get(word).update({ filename: posSet})
      else:
         posSet = { pos }
         thisdict = { filename: posSet }
         self.occs.update({ word: thisdict})

 
   # Should return the number of distinct words:
 
   def distinctWords( self ) -> int :
      return len(self.occs)

    
   # Should return the total number of words occurrences: 
 
   def totalOccurrences( self, word : Optional[str] = None,
                               fname : Optional[str] = None ) -> int :
      total = 0
      if isinstance( word, str):
         if isinstance( fname, str):
            if word in self.occs:
               if fname in self.occs.get(word):
                  total = len(self.occs.get(word).get(fname))
         else:
            if word in self.occs:
               for f, s in self.occs.get(word).items():
                  total += len(s)
      else:
         for w in self.occs:
            for f, s in self.occs.get(w).items():
               total += len(s)
      return total


   # This is for debugging, so it doesn't need to be pretty: 

   def __repr__( self ) -> str : 
      return str( self. occs )

 
   # Here the occurrences must be sorted and shown in a nice way: 

   def __str__( self ) -> str :
      result : str = ""
      sortedKeys = sorted(self.occs.keys())
      for x in sortedKeys:
         result = result + "\"" + x + "\" has " + str(self.totalOccurrences(x)) + " occurrence(s):\n"
         for y in sorted(self.occs.get(x).keys()):
            result = result + "   in file " + y + "\n"
            sortedSet = sorted(self.occs.get(x).get(y))
            for z in sortedSet:
               result = result + "      at " + str(z) + "\n"
      return result


 
