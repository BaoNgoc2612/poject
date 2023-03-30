##In Python, Loops are used to iterate repeatedly over a block of code. 
#In order to change the way a loop is executed from its usual behavior, control statements are used. 
#Control statements are used to control the flow of the execution of the loop based on a condition. 
#There are many types of control statements in Python and in this tutorial, we will discuss all of them.
##Control Statements in Python
 #1.Break 
 #2.Continue 
 #3.Pass
##1. Break statement 
    #The break statement in Python is used to terminate or abandon the loop containing the statement and brings the control out of the loop. 
    #It is used with both the while and the for loops, especially with nested loops (loop within a loop) to quit the loop. 
    #It terminates the inner loop and control shifts to the statement in the outer loop.
      #ex: for index in range(5):
              # print(index)
              #if index == 2:
                  #break
##2. Continue statement
    #When a program encounters a continue statement in Python, it skips the execution of the current iteration when the condition is met and lets the loop continue to move to the next iteration.
    #It is used to continue running the program even after the program encounters a break during execution.
        #ex2:for index in range(10):
            #if not index  % 2 == 0: #%2 là số lẻ 
                #continue
            #print(index)
    
##3.Pass statement
  #The pass statement is a null operator and is used when the programmer wants to do nothing when the condition is satisfied. 
  #This control statement in Python does not terminate or skip the execution, it simply passes to the next iteration.
  #A loop cannot be left empty otherwise the interpreter will throw an error and to avoid this, a programmer can use the pass statement.
          #ex3:a = 5
             # b = 10

            #if a > b :
                #print("A lớn  hơn B")
            #else:
            #    pass
            # print('The end!')