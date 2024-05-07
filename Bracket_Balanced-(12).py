# Program :12
# Python program to implement Bracket matching using stack

def Bracket_Balanced(expr):
    STACK=[]

    for char in expr:
        if char in ['(','{','[']:
            STACK.append(char)
        else:
            if not STACK:
                return False
            current_char=STACK.pop()
            if current_char=='(':
                if char!=')':
                    return False
                
            if current_char=='{':
                if char!="}":
                    return False
            
            if current_char=="[":
                if char!="]":
                    return False
        
    if STACK:
        return False
    return True

if __name__=="__main__":
    expr=input("Enter expression:")
    if Bracket_Balanced(expr):
        print("Balanced")
    else:
        print("Not balanced") 



# Time and Space complexity: 0(n)