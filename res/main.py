import numpy as np

class fraction:
    """
    An implementation of fractions
    """
    def __init__(self,numerator,denominator):
        """
        This is where we initialize the fraction object. The numerator and denominator should be 
        provided here.
        """
        if (numerator<0 and denominator<0):
            numerator=-numerator
            denominator=-denominator
        self._numerator = numerator
        self._denominator = denominator
        self._val = numerator / denominator
    def _find_common_den(self,frac):
        """
        Utility function to find out the common denominator. Useful in addition and subtraction
        """
        
        return np.lcm(self._denominator,frac._denominator)

    def _hcf(self):
        """
        Utility function to find out the Highest Common factor between numerator and denominator
        """
        a=np.abs(self._numerator)
        b=np.abs(self._denominator)
        if a<b:a,b=b,a
        while b!=0:
            c=a
            a=b
            b=c%b
            
        return a 
    
    def _reduce(self):
        """
        Utility function to reduce to fraction into its base form.
        """
        h=self._hcf()
        self._numerator=int(np.divide(self._numerator,h))
        self._denominator=int(np.divide(self._denominator,h))
        return self
    def __pos__(self):
        """
        Overloaded + unary operator
        """
        return fraction(self._numerator,self._denominator)
    def __neg__(self):
        """
        Overloaded - unary operator
        """
        return fraction(-self._numerator,self._denominator)
    def __add__(self,frac):
        """
        You can add two fractions
        """
        cd=self._find_common_den(frac)
        print(cd)
        n1=cd//self._denominator#int(np.divide(cd,self._numerator))
        n2=cd//frac._denominator#int(np.divide(cd,frac._numerator))
        return fraction((n1)*self._numerator + (n2)*frac._numerator,cd)._reduce()
    
    def __sub__(self,frac):
        """
        You can substract two fractions
        """
        cd=self._find_common_den(frac)
        n1=int(np.divide(cd,self._denominator))
        n2=int(np.divide(cd,frac._denominator))
        return fraction((n1)*self._numerator - (n2)*frac._numerator,cd)._reduce()   

    def __mul__(self,frac):
        """
        You can multiply two fractions
        """
        num=self._numerator*frac._numerator
        den=self._denominator*frac._denominator
        n=fraction(num,den)
        n._reduce()
        return n

    def __truediv__(self,frac):
        """
        You can divide two fractions
        """
        frac._numerator,frac._denominator=frac._denominator,frac._numerator      
        return self.__mul__(frac)
    
    def __floordiv__(self,frac):
        return self.__truediv__(frac)

    def __pow__(self,n:int):
        """
        You can raise the fraction to any power
        """
        return fraction(self._numerator**n,self._denominator**n)

    def __iadd__(self,frac):
        return self.__add__(frac)
    def __isub__(self,frac):
        return self.__sub__(frac)   
    def __imul__(self,frac):
        return self.__mul__(frac)
    def __itruediv__(self,frac):
        return self.__truediv__(frac)
    def __ifloordiv__(self,frac):
        return self.__truediv__(frac)
    def __ipow__(self,n:int):
        return self.__pow__(n)
    def __str__(self):
        return f"  {self._numerator}\n-----\n  {self._denominator}"

    def __lt__(self,frac):
        if self._val<frac._val:
            return True
        return False

    def __gt__(self,frac):
        if self._val>frac._val:
            return True
        return False
    
    def __le__(self,frac):
        if self._val<=frac._val:
            return True
        return False

    def __ge__(self,frac):
        if self._val>=frac._val:
            return True
        return False

    def __eq__(self,frac):
        if self._val==frac._val:
            return True
        return False
    
    def __ne__(self,frac):
        if self._val!=frac._val:
            return True
        return False

if __name__ == "__main__":
    a = fraction(3,4)
    b = fraction(3,4)

    
