# imports
import datetime
import os

# variables
logdatetime = datetime.datetime.now()

# setup and stuff
logname = f"{logdatetime.strftime('%Y-%m-%d %H-%M-%S')}.log"
log = open(f"logs/{logname}", "w")

# classes
class color:


    '''Colors class:reset all colors with colors.reset; two
    sub classes fg for foreground
    and bg for background; use as colors.subclass.colorname.
    i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
    underline, reverse, strike through,
    and invisible work with the main class i.e. colors.bold
    Stolen from geeksforgeeks'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

# defs

def main():
    print("Prometheus Command Line Interface [Dev Build 1]")
    print()

    while True:
        print(color.fg.yellow,"\b$",color.reset, end="")
        command = input(str()) 
        commandToAnalise = list(command.split(" "))

        if command in ["exit"]:

            while True:
                print(color.fg.red,"You want to save the logs? [y/n]")
            
                exitanswer = input("> ")
                if exitanswer in ["y", "yes", "s", "si"]:
                    print(color.reset)
                    break
                elif exitanswer in ["n", "no"]:
                    os.remove(logname)
                    print(color.reset)
                    break
                else:
                    print("please try again")
            
            log.write(f"{logdatetime} DEBUG: Prometheus Command Line Interface exited at {logdatetime}")
            break
        
        elif command in ["clear", "cls"]:
            os.system("cls")
            log.write(f"{logdatetime} INFO: Command {command} executed successfully\n")
        
        elif commandToAnalise[0] == "calc":
            
            try:
                print(f"{commandToAnalise[1]} = {eval(commandToAnalise[1])}")
            except ZeroDivisionError:
                print(color.fg.red,"Error ", color.reset ,"No es posible dividir entre cero, revisa la operacion.")
                log.write(f"{logdatetime} ERROR: Prometheus Command Line Interface failed to evaluate \"{commandToAnalise[1]}\" due to ZeroDivisionError, command executed \"{command}\"\n")
            except ArithmeticError:
                print(color.fg.red, "Error ", color.reset, "Un error aritmetico ha ocurrido durante la resolucion del problema")
                log.write(f"{logdatetime} ERROR: Prometheus Command Line Interface failed to evaluate \"{commandToAnalise[1]}\" due to ArithmeticError, command executed \"{command}\"\n")
            except FloatingPointError:
                print(color.fg.red, "Error ", color.reset, "Un error de punto flotante ha ocurrido durante la resolucion del problema")
                log.write(f"{logdatetime} ERROR: Prometheus Command Line Interface failed to evaluate \"{commandToAnalise[1]}\" due to FloatingPointError, command executed \"{command}\"\n")
            except Exception:
                print(color.fg.red, "Error ", color.reset, "Un error de punto flotante ha ocurrido durante la evaluacion del problema")
                log.write(f"{logdatetime} ERROR: Prometheus Command Line Interface failed to evaluate \"{commandToAnalise[1]}\" due to an unknown, command executed \"{command}\"\n")


# entry point

if __name__ == '__main__':
    pass
    log.write(f"{logdatetime} DEBUG: Prometheus Command Line Interface started at {logdatetime}\n")
    
    main()
    log.close()
