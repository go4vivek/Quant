def newton_raphson(f,guess,tolerance,max_iter,increment,epsilon):
    for iter in range(max_iter):
        func_value=f(guess)
        fprime=(f(guess+increment)-f(guess-increment))/(2.0*increment) 
        if (abs(fprime)>epsilon):
            next_guess=guess-(float(func_value)/float(fprime))
            if(abs(next_guess-guess)<=tolerance*abs(next_guess)) or fprime==0:
                break
            else:
                    guess=next_guess                      
        else: break
    print("Root of the function %s is: %f" %(f,next_guess) )
    
if __name__=="__main__":
    newton_raphson(lambda x:x**2-x*4,1,.000001,100,.001,.001)
