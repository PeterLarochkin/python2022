import cmd, pynames
from pynames import GENDER, LANGUAGE
from re import L



generators =  {
        'Scandinavian':pynames.generators.scandinavian.ScandinavianNamesGenerator(),
        'Russian':  pynames.generators.russian.PaganNamesGenerator(),
        'Mongolian': pynames.generators.mongolian.MongolianNamesGenerator(),
        'Korean':  pynames.generators.korean.KoreanNamesGenerator(),
        'Goblin': pynames.generators.goblin.GoblinGenerator(),
        'Orc': pynames.generators.orc.OrcNamesGenerator(),
        'elven' : {'DnD': pynames.generators.elven.DnDNamesGenerator()},
        'elven':  {'Warhammer': pynames.generators.elven.WarhammerNamesGenerator()},
        'iron_kingdoms': 
                        { 
                            'CaspianMidlunderSulese': pynames.generators.iron_kingdoms.CaspianMidlunderSuleseFullnameGenerator(),
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
        self.current_lan = "EN"

    def do_generate(self, args):
        """Генерация имени на экран"""
        # for arg in args:
        new_generators = generators
        sex = "male"
        for arg in args.split():
            if type(new_generators) == dict and arg in new_generators.keys():
                new_generators = new_generators[arg.replace("\n","")]
            else:
                if arg in self.genders:
                    sex = arg
        try:
            gender = GENDER.MALE if sex == "male" else GENDER.FEMALE if sex == "female" else None
            lang =  LANGUAGE.EN if self.current_lan == "EN" else LANGUAGE.RU
            print(new_generators.get_name_simple(gender, lang)) 

        except:
            print("troubles with args")         
        # print("hello world")
    

    def complete_generate(self, text, line, start_index, end_index):
        if line:
            new_generators = generators
            for word in line.split()[1:]:
                if type(new_generators) == dict and word in new_generators.keys():
                    new_generators = new_generators[word]
                else:
                    break
            return [
                item for item in list(new_generators.keys())
                if item.startswith(text)
            ]
        else:
            return list(generators.keys())

    def do_info(self, args):
        """Получение информации о именах"""
        print("hello world")

    def complete_info(self, text, line, start_index, end_index):
        # if text[:end_index] in list(generators.keys()):
        #     return [text[:end_index] + " male", text[:end_index] + " female"]
        # else: 
        
        
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
    # print(pynames.generators.korean.KoreanNamesGenerator().get_name("female"))
    
    try:
        cli.cmdloop()
    except KeyboardInterrupt:
        print("завершение сеанса...")