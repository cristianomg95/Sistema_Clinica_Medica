from main import menu

def validateToRepeat(msg,function):  # confirmar uma repetição de um metodo
  opc = input(msg).lower()
  if opc == "y":
    function()
  elif opc == "n":
    menu()
  else:
    print("OPÇÃO INCORRETA!!!")
    validateToRepeat(msg,function)

def validateToContinue(msg): # confirmar uma ação
  opc = input(msg).lower()
  if opc == "y":
    return True
  elif opc == "n":
    return False
  else:
    print("OPÇÃO INCORRETA!!!")
    validateToContinue(msg)