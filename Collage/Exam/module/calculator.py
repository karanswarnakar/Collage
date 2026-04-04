
import Collage.Exam.module.oprations as oprations

def calculator(a,b,c):
    match c: 
        case 1:
            oprations.add(a,b)
        case 2:
            oprations.sub(a,b)
        case 3:
            oprations.mul(a,b)
        case 4:
            oprations.divide(a,b)
