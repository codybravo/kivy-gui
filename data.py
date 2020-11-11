import sigfig
from io import StringIO  
import sys

class numerical(object):
    def __init__(self,a,n,h,exp):
        self.a = a
        self.x = 0
        self.h = h
        self.n = n
        self.exp = exp
        self.x_list = []
        self.f_list = []
    
    def value_x(self):
        self.x += self.a
        for i in range(0,self.n+1):
            self.x_list.append(round(self.x,10))
            self.f_list.append(round(eval(self.exp),10))
            self.x += self.h
        
        return self.x_list,self.f_list

class New(object):
        def __init__(self,a,b,n,exp,file,correction,d):
        	self.a = float(a)
        	self.b = float(b)
        	self.n = int(n)
        	self.h = 0
        	self.exp = str(exp)
        	self.x_list = []
        	self.f_list = []
        	self.correction = str(correction)
        	self.d = int(d)
        	self.t = 0
        	self.s = 0
        	self.file = file
        	
        def add(self):
        	self.h = (self.b-self.a)/(self.n)
        	self.x_list, self.f_list = numerical(self.a,self.n,self.h,self.exp).value_x()
        	self.s = T_and_S(self.x_list, self.f_list, self.n, self.h,self.file,self.d,self.correction).simson_y()
        	self.t = T_and_S(self.x_list, self.f_list, self.n, self.h,self.file,self.d,self.correction).trapezoidal_y()
        	#self.i = significant(self.i,self.d,self.correction)
        	return str(self.s),str(self.t)
        	
#a, b, n, h = New().add()

class Write(object):
        	def __init__(self,file,w_file):
        		self.file = file
        		self.w_file = w_file
        		
        		
        	def writing(self):
        		with open(self.file, "a") as fobj:
        			fobj.writelines(self.w_file)
        		
def significant(i,d,correction):
        if correction == "dec":
            i = round(i,d)
        elif correction == "sig":
            i = sigfig.round(i,d)
        return i
        
                
        
class T_and_S(object):
    def __init__(self, x_list, f_list, n, h,file,d,correction):
        self.x_list  = x_list
        self.f_list = f_list
        self.n = n
        self.h = h
        self.sum1,self.sum2,self.sum3 = 0,0,0
        self.y1 = ["-" for i in range(n+1)]
        self.y2 = list(self.y1)
        self.y3 = list(self.y1)
        self.i = 0
        self.file = file
        self.correction = correction
        self.d = d
        print1 = ""
        self.blank = " "
     
    #def significant(self):
#        if self.correction == "dec":
#            self.i = round(self.i,self.d)
#        elif self.correction == "sig":
#            self.i = sigfig.round(self.i,self.d)
#        return self.i
            
    def simson_y(self):
        stop_stdout = sys.stdout
        sys.stdout = open(self.file, 'a')
        print("Simpson's (1/3)rd Rule",end="\n\n")
        print('{:-<75}'.format("-"))
        print('{: <4}'.format("i"),'{: <13}'.format("x"),'{: <13}'.format("f(x)"),'{: <13}'.format(f'y(i=0,{self.n})'),'{: <13}'.format("y(i=1,3,5,..)"),'{: <13}'.format("y(i=2,4,6,..)"))
        print('{:-<75}'.format("-"))
        

        for i in range(0,self.n+1):
            if (i == 0 or i == self.n): 
                self.y1[i] = round(self.f_list[i],10)
                self.sum1 += self.y1[i]
        
        for i in range(1,self.n,2):
            self.y2[i] = round(self.f_list[i],10)
            self.sum2 += self.y2[i]
            
        for i in range(2,self.n,2):
            self.y3[i] = round(self.f_list[i],10)
            self.sum3 += self.y3[i]
    
        for i in range(0,self.n+1):
            print('{: <4}'.format(i),'{: <13}'.format(self.x_list[i]),'{: <13}'.format(self.f_list[i]),'{: <13}'.format(self.y1[i]),'{: <13}'.format(self.y2[i]),'{: <13}'.format(self.y3[i]))
        
        print('{:-<75}'.format("-"))
    
        self.i = (self.h/3)*(self.sum1+(4*self.sum2)+(2*self.sum3))
        
        print(f"Now by Simpson's (1/3)rd Rule,\nI = h/3[(y0+yn+(4×(y1+y3+y5+..))+(2*(y2+y4+..))]\nI = {self.h}/3[{self.sum1}+(4*{self.sum2})+(2*{self.sum3})]\nI = {self.i}")
		
        self.i = significant(self.i,self.d,self.correction)
		
        print(f'I={self.i}')
					
        sys.stdout = stop_stdout
        
        return self.i
    
    
    def trapezoidal_y(self):
        stop_stdout = sys.stdout
        sys.stdout = open(self.file, 'a')
        print("Trapezoidal's Rule",end="\n\n")
        print('{:-<75}'.format("-"))
        print('{: <4}'.format("i"),'{: <13}'.format("x"),'{: <13}'.format("f(x)"),'{: <13}'.format("y(i=0,1)"),'{: <13}'.format("y(i=1,..,n-1)"))
        print('{:-<75}'.format("-"))
        
        for i in range(0,self.n+1):
            if (i == 0 or i == self.n): 
                self.y1[i] = round(self.f_list[i],10)
                self.sum1 += self.y1[i] 
                
        for i in range(1,self.n):
            self.y2[i] = round(self.f_list[i],10)
            self.sum2 += self.y2[i]
            
        for i in range(0,self.n+1):
            print('{: <4}'.format(i),'{: <13}'.format(self.x_list[i]),'{: <13}'.format(self.f_list[i]),'{: <13}'.format(self.y1[i]),'{: <13}'.format(self.y2[i]))
        
        print('{:-<75}'.format("-"))
        
        self.i = (self.h/2)*((self.sum1)+(2*self.sum2))
        
        print(f'Now by Trapezoidal Rule,\nI = h/2[(y0+y{self.n}+2(y1+y2+y3+...+y{self.n-1})]\nI = {self.h}/2[({self.sum1}+2*{self.sum2})\nI = {self.i}')
        
        self.i = significant(self.i,self.d,self.correction)
        
        print(f'I={self.i}')
        
        sys.stdout = stop_stdout
        
        return self.i

#print("""what type of correction required
#         1. Decimal places
#         2. Significant figures""")
#correction = int(input("enter number:"))
#d = int(input("correction:"))
#print("")
#print("enter limits of integration")
#a = float(input("a:"))
#b = float(input("b:"))
#n = int(input("enter no. of subinterval, n:"))
#print("h = (b-a)/n")
#h = (b-a)/n
#print(f'h={h}')
#x = 0 + a
#exp = input("enter expression:")
#print("")
#t = numerical()
#x_list,f_list = t.value_x(x,h,exp) 
#print(T_and_S().simson_y(x_list,f_list)) 
#print(T_and_S().trapezoidal_y(x_list,f_list))



    

