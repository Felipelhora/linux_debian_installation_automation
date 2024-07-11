'''import subprocess

class CommandRunner:
    def prompt_commands(self, prompt: str) -> str:
        process = subprocess.Popen(prompt, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = []

        while True:
            # Lê a saída linha a linha
            line = process.stdout.readline()
            if line:
                print(line, end='')  # Imprime em tempo real
                output.append(line)
            elif process.poll() is not None:
                break

        # Captura qualquer saída restante (se houver)
        remaining_output = process.communicate()
        output.extend(remaining_output)

        return ''.join(output)

# Exemplo de uso
runner = CommandRunner()
command = "ping -c 4 google.com"
print("Executing command...")
result = runner.prompt_commands(command)
print("\nCommand output:\n", result)
'''