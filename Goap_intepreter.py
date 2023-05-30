class Solution:
    def interpret(self, command: str) -> str:
        def intep(command):
            if command == "":
               return ""
            if command[0] == 'G':
              return 'G' + intep(command[1:])
            elif command[1] == 'a':
                    return 'al' + intep(command[4:])
            else: 
                  return 'o' + intep(command[2:])

        return intep(command)
