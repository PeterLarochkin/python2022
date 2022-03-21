import cmd, pynames



generators =  {
        'Scandinavian':pynames.generators.scandinavian.ScandinavianNamesGenerator(),
        'Russian':  pynames.generators.russian.PaganNamesGenerator(),
        'Mongolian': pynames.generators.mongolian.MongolianNamesGenerator(),
        'Korean':  pynames.generators.korean.KoreanNamesGenerator(),
        'Goblin': pynames.generators.goblin.GoblinGenerator(),
        'Orc': pynames.generators.orc.OrcNamesGenerator(),
        'elven DnD': pynames.generators.elven.DnDNamesGenerator(),
        'elven Warhammer': pynames.generators.elven.WarhammerNamesGenerator(),
        'iron_kingdoms': { 'CaspianMidlunderSulese': pynames.generators.iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator(),
        'Dwarf': pynames.generators.iron_kingdoms.DwarfFullnameGenerator(),
         ' Gobber': pynames.generators.iron_kingdoms.GobberFullnameGenerator(),
         'IossanNyss': pynames.generators.iron_kingdoms.IossanNyssFullnameGenerator(),
         'Khadoran': pynames.generators.iron_kingdoms.KhadoranFullnameGenerator(),
         'Ogrun': pynames.generators.iron_kingdoms.OgrunFullnameGenerator(),
         'Ryn': pynames.generators.iron_kingdoms.RynFullnameGenerator(),
         'ThurianMorridane': pynames.generators.iron_kingdoms.ThurianMorridaneFullnameGenerator(),
         'Tordoran': pynames.generators.iron_kingdoms.TordoranFullnameGenerator(),
         'Trollkin': pynames.generators.iron_kingdoms.TrollkinFullnameGenerator()
         }
    }





class Cli(cmd.Cmd):

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.languages = ['RU', 'EN']
        self.genders = ['male', 'female']
        self.intro  = "Добро пожаловать\nДля справки наберите 'help'"
        self.doc_header ="Доступные команды (для справки по конкретной команде наберите 'help _команда_')"

    def do_generate(self, args):
        """hello - выводит 'hello world' на экран"""
        print("hello world")
    

    def complete_generate(self, text, line, start_index, end_index):
        if text:
            return [
                item for item in list(generators.keys())
                if item.startswith(text)
            ]
        else:
            return list(generators.keys())

    def do_info(self, args):
        """hello - выводит 'hello world' на экран"""
        print("hello world")

    def complete_info(self, text, line, start_index, end_index):
        # if text[:end_index] in list(generators.keys()):
        #     return [text[:end_index] + " male", text[:end_index] + " female"]
        # else: 
        
        line = line.replace("info ", "")
        if text:
            return [
                item for item in list(generators.keys())
                if item.startswith(text)
            ]
        else:
            return list(generators.keys())
        # return [
        # item.replace(line+" ", "") for item in list(generators.keys())
        # if item.startswith(line)
        # ]
        
    
    def do_language(self, args):
        """hello - выводит 'hello world' на экран"""
        print("hello world")

    def complete_language(self, text, line, start_index, end_index):
        if text:
            return [
                item for item in self.languages
                if item.startswith(text)
            ]
        else:
            return self.languages

    def do_send(self, line):
        pass    

    

    def default(self, line):
        print("Несуществующая команда")

if __name__ == "__main__":
    cli = Cli()
    print(generators.keys())
    
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("завершение сеанса...")