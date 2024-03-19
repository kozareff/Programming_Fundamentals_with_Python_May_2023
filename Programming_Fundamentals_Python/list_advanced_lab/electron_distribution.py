electrons = int(input())
shell_of_electrons = []
shell_number = 0

while True :
    shell_number += 1
    current_electrons_shell = 2 * shell_number ** 2
    if electrons > current_electrons_shell :
        electrons -= current_electrons_shell
        shell_of_electrons.append(current_electrons_shell)
    elif electrons == current_electrons_shell:
        shell_of_electrons.append(electrons)
        break
    else:
        shell_of_electrons.append(electrons)
        break

print(shell_of_electrons)