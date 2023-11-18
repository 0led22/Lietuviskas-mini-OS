import os

class PaprastasOS:
    def __init__(self):
        self.current_directory = '/'
        self.text_editor_content = ''

    def run(self):
        while True:
            command = input(f'{self.current_directory} $ ')
            self.execute_command(command)

    def execute_command(self, command):
        if command.lower() == 'exit':
            print('Exiting PaprastasOS...')
            exit()
        elif command.lower() == 'pwd':
            print(self.current_directory)
        elif command.lower() == 'ls':
            self.list_directory()
        elif command.lower() == 'knygelė':
            self.edit_file()
        elif command.lower().startswith('cd '):
            self.change_directory(command[3:])
        else:
            print(f"Kaska netaip padariai mulkiau---→: {command}")

    def list_directory(self):
        print('Skelbimų katalogas:')
        for item in os.listdir(self.current_directory):
            print(f'  {item}')

    def change_directory(self, new_directory):
        if new_directory == '..':
            # Move up one level
            self.current_directory = os.path.dirname(self.current_directory)
        else:
            # Join the current directory with the new directory
            new_path = os.path.join(self.current_directory, new_directory)

            # Check if the new path exists and is a directory
            if os.path.exists(new_path) and os.path.isdir(new_path):
                self.current_directory = new_path
            else:
                print(f"Katalogas nerastas: {new_directory}")

    def edit_file(self):
        print('Atidaryta teksto knygelė. Įveskite tekstą. Įveskite "išsaugoti", kad išsaugotumėte, ir "išeiti", kad išeitumėte.')
        while True:
            line = input()
            if line.lower() == 'išsaugoti':
                self.save_text_editor_content()
                print("Failas išsaugotas.")
                break
            elif line.lower() == 'išeiti':
                print("Išėinama iš teksto knygelės.")
                break
            else:
                self.text_editor_content += line + '\n'

    def save_text_editor_content(self):
        file_name = input("Enter the file name to save: ")
        file_path = os.path.join(self.current_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(self.text_editor_content)

if __name__ == "__main__":
    PaprastasOS_os = PaprastasOS()
    PaprastasOS_os.run()
